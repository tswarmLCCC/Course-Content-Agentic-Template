# Unit 1: The Relational Foundation & Supervised Learning Targets

> **Course**: COSC 2060 — Modern Data Engineering & AI Infrastructure  
> **Estimated Study Time**: 150 minutes of asynchronous conceptual deep-dive & hands-on exploration  
> **Target Audience**: College Sophomores (Prerequisites: Introductory SQL & Introductory Machine Learning)  
> **Core Toolchain**: DuckDB 0.10+ (In-process Columnar OLAP Engine) & Python 3.10+

---

## 1. Unit Overview & Objectives

Welcome to **COSC 2060: Modern Data Engineering & AI Infrastructure**. 

In your introductory machine learning course, you learned how to train classification and regression algorithms. You split data into $X$ (features) and $y$ (target labels), called `model.fit(X_train, y_train)`, evaluated accuracy, and plotted ROC curves. But in that class, you were handed a gift that almost never exists in industry: **a clean, single-table, flat 2D CSV file** (like Iris, Titanic, or curated Kaggle datasets).

In your introductory SQL course, you learned how to query normalized databases. You wrote `SELECT`, `WHERE`, `ORDER BY`, and basic `INNER JOIN` statements to generate human-readable invoices and employee lists from relational tables.

**This unit is the bridge between those two worlds.**

In real production engineering, nobody hands you a clean CSV. Real enterprise data lives in multiple normalized relational tables that are constantly updated by operational transactions. If you naively join those tables using the SQL you learned in your introductory class, you will commit the cardinal sin of AI data engineering: **temporal data leakage** (also known as *look-ahead bias*). Your model will report 99% accuracy in your Jupyter Notebook, but will fail catastrophically the moment it is deployed to live production.

By the end of this unit, you will master the art of transforming raw transactional databases into leak-free machine learning feature matrices using modern columnar analytical SQL.

### Measurable Learning Objectives
By the end of this unit, you will be able to:
1. **Differentiate** between row-oriented OLTP database architectures (e.g., PostgreSQL) and columnar-oriented OLAP engines (e.g., DuckDB) in terms of disk I/O, cache efficiency, and analytical query performance.
2. **Identify and Diagnose** temporal data leakage and look-ahead bias in multi-table relational joins.
3. **Construct** point-in-time joins using DuckDB's native `ASOF JOIN` syntax to guarantee zero future data leaks into historical feature rows.
4. **Implement** defensive rolling window aggregations and lag features using SQL window functions (`PARTITION BY`, `ORDER BY`, `ROWS BETWEEN N PRECEDING AND 1 PRECEDING`).
5. **Generate** a production-ready, flat 2D feature matrix ($X, y$) from raw, messy relational logistics tables.

---

## 2. The Narrative of Data: Why the $10M Delivery Model Failed

To understand why data engineering is a distinct discipline from both software development and data science, consider an authentic industry failure.

A national freight logistics carrier employed hundreds of drivers moving freight between major distribution hubs. They wanted to predict whether a scheduled shipment would experience a severe delivery delay (`delivery_delay_mins > 30`) so dispatchers could reroute cargo proactively.

The company hired a brilliant machine learning graduate. The data scientist opened their notebook, connected to the company's PostgreSQL database, and wrote a standard SQL query:

```sql
-- NAIVE, CATASTROPHIC SQL QUERY (DO NOT USE IN PRODUCTION)
SELECT 
    r.route_id,
    r.driver_id,
    r.origin_city,
    r.dep_time::DATE AS route_date,
    r.distance_miles,
    w.precipitation_in,
    w.visibility_miles,
    w.road_condition,
    r.delivery_delay_mins AS target_delay
FROM routes r
LEFT JOIN weather_observations w
  ON r.origin_city = w.city
 AND r.dep_time::DATE = w.obs_time::DATE;
```

The scientist trained an XGBoost model on this dataset. The results were astounding: **99.4% ROC-AUC score**. The executive team was thrilled and deployed the model to live dispatch.

### The Catastrophic Deployment Failure
On day one of live operation, the model's accuracy collapsed to **51%**—no better than flipping a coin. Shipments were delayed across the country, warehouses were left unstaffed, and the company lost an estimated $10 million in contractual service level penalties.

What happened?

Look closely at the join condition:
```sql
ON r.origin_city = w.city AND r.dep_time::DATE = w.obs_time::DATE
```

Truck #104 departed Chicago at **7:15 AM** on a sunny morning. At **5:30 PM** that afternoon, a sudden severe blizzard struck Chicago, dumping 6 inches of snow. The weather monitoring station logged `precipitation_in = 6.0` and `road_condition = 'Snow/Ice'` at 6:00 PM.

Because the query joined purely on the **calendar date** (`dep_time::DATE = obs_time::DATE`), the evening blizzard data was attached to the morning truck's departure record. When the model was being trained, it looked at Truck #104 and saw "6 inches of snow at origin" and correctly learned that snow equals delays. 

In the real world at **7:15 AM**, that blizzard had not happened yet. The live model at departure time only had access to the 7:00 AM reading ("Clear skies, dry roads"). The model had been trained on the future.

```
REALITY TIMELINE:
06:00 AM ── Weather Observation: "Clear skies, dry roads"
07:15 AM ── Truck #104 Departs Chicago  <── MODEL MAKES PREDICTION HERE!
12:00 PM ── Truck #104 is 300 miles away
05:30 PM ── Severe Blizzard hits Chicago!
06:00 PM ── Weather Observation: "Blizzard, 6 inches snow, road closed"

WHAT NAIVE SQL JOIN DID:
Attached the 06:00 PM Blizzard to the 07:15 AM Departure! (LOOK-AHEAD BIAS)
```

This is **look-ahead bias** (temporal data leakage). A machine learning model will ruthlessly exploit any hint from the future if you feed it to it during training. As a data engineer, your primary responsibility is defensive: **you must construct data pipelines that mathematically prevent future knowledge from leaking into past events.**

---

## 3. The Mental Model: OLTP Row Filing vs. OLAP Columnar Straws

In your first SQL course, you used **PostgreSQL**. Why are we introducing a new engine, **DuckDB**, in this course?

To understand the difference, consider how data is stored physically on your computer's storage drive (SSD or hard disk).

```
TABLE: routes (route_id, driver_id, origin_city, distance_miles, delay_mins)

1. ROW-ORIENTED (OLTP - PostgreSQL):
[101, 44, 'Chicago', 450.2, 12] [102, 12, 'Denver', 612.0, 45] [103, 88, 'Dallas', 210.5, 0] ...
Bytes on disk are packed row after row.

2. COLUMN-ORIENTED (OLAP - DuckDB):
route_id:       [101, 102, 103, 104, 105, ...]
driver_id:      [44, 12, 88, 19, 44, ...]
origin_city:    ['Chicago', 'Denver', 'Dallas', 'Chicago', 'Denver', ...]
distance_miles: [450.2, 612.0, 210.5, 880.1, 312.4, ...]
delay_mins:     [12, 45, 0, 95, 4, ...]
Bytes on disk are packed column after column.
```

### The "Filing Cabinet" vs. "Drinking Straws" Metaphor

1. **OLTP (Online Transaction Processing — PostgreSQL)**:
   - Imagine a traditional office filing cabinet. Each folder holds all the papers for one single customer or route (the complete row).
   - If an ATM needs to update your bank balance, or an e-commerce store needs to insert one new order, PostgreSQL opens one folder, updates one number, and closes it. It is blazingly fast for single-row inserts, updates, and transactional safety (ACID compliance).
   - But what happens when an AI model wants the `AVG(distance_miles)` across 10 million rows? PostgreSQL must pull all 10 million folders out of the cabinet, read every piece of paper in every folder, just to look at the one line containing distance. Your disk and memory bus are choked with useless data.

2. **OLAP (Online Analytical Processing — DuckDB)**:
   - Imagine that instead of folders, every column is stored in its own dedicated drinking straw. One straw holds all 10 million route IDs; another straw holds all 10 million distances.
   - When DuckDB calculates `AVG(distance_miles)`, it only opens the `distance_miles` straw! It never touches, reads, or loads driver names, addresses, or cities into memory. 
   - Furthermore, because all the numbers in that straw are identical data types (`FLOAT`), modern CPU vector registers (SIMD — Single Instruction, Multiple Data) can crunch 8 to 16 numbers in a single clock cycle.

### Why DuckDB for Data Engineering?
DuckDB is an **in-process analytical database** (often called "the SQLite for Analytics"). 
- It requires **no server setup, no background daemon, no open ports, and no administrative passwords**.
- It installs cleanly into any Python environment with `pip install duckdb`.
- It can directly query raw CSV files, Parquet files, and Python dictionaries without needing `CREATE TABLE` or `COPY FROM` boilerplate.

---

## 4. Technical Deep Dive: Evolving SQL to Feature Engineering

Now let's examine the step-by-step cognitive progression from raw normalized relational tables to a clean 2D feature matrix.

### Step 1: The Raw Input Tables
Our logistics enterprise has three messy normalized tables:

```
Table 1: drivers (Dimension)
+-----------+---------------+------------+--------------+---------------+
| driver_id | driver_name   | hire_date  | safety_score | vehicle_type  |
+-----------+---------------+------------+--------------+---------------+
| 401       | Alice Vance   | 2023-03-15 | 0.96         | Semi-Trailer  |
| 402       | Bob Sterling  | 2021-08-01 | 0.88         | Box Truck     |
+-----------+---------------+------------+--------------+---------------+

Table 2: routes (Fact / Events)
+----------+-----------+-------------+-----------+---------------------+---------------------+------------------+
| route_id | driver_id | origin_city | dest_city | dep_time            | sched_arrival       | delay_mins (y)   |
+----------+-----------+-------------+-----------+---------------------+---------------------+------------------+
| 9001     | 401       | Cheyenne    | Denver    | 2026-10-12 06:15:00 | 2026-10-12 08:30:00 | 45               |
| 9002     | 402       | Salt Lake   | Boise     | 2026-10-12 07:00:00 | 2026-10-12 12:45:00 | 0                |
+----------+-----------+-------------+-----------+---------------------+---------------------+------------------+

Table 3: weather_observations (Continuous Sensor Stream)
+------------+-----------+---------------------+------------------+------------------+----------------+
| station_id | city      | obs_time            | precipitation_in | visibility_miles | road_condition |
+------------+-----------+---------------------+------------------+------------------+----------------+
| W-CHY-01   | Cheyenne  | 2026-10-12 05:00:00 | 0.00             | 10.0             | Dry            |
| W-CHY-01   | Cheyenne  | 2026-10-12 06:00:00 | 0.15             | 4.5              | Wet            |
| W-CHY-01   | Cheyenne  | 2026-10-12 07:00:00 | 0.80             | 1.0              | Snow/Ice       |
| W-SLC-02   | Salt Lake | 2026-10-12 06:30:00 | 0.00             | 10.0             | Dry            |
+------------+-----------+---------------------+------------------+------------------+----------------+
```

Notice the engineering challenge:
- Truck `9001` departed Cheyenne at `06:15:00`.
- What was the weather? 
  - At `05:00:00`, it was dry.
  - At `06:00:00`, it was wet with 0.15 inches of rain.
  - At `07:00:00`, it began snowing heavily.
- The truck departed at **06:15**. The most recent weather observation available to dispatch was the **06:00:00** reading. 
- If our query attaches the `07:00:00` reading, we leak future snow into a truck that had already left 45 minutes earlier!

---

### Step 2: The Point-in-Time Join with DuckDB `ASOF JOIN`

DuckDB provides native syntax specifically engineered for time-series and financial/logistics alignment: the **`ASOF JOIN`** (*As-Of Join*).

```sql
SELECT 
    r.route_id,
    r.driver_id,
    r.dep_time,
    r.origin_city,
    w.obs_time AS weather_obs_time,
    w.precipitation_in,
    w.visibility_miles,
    w.road_condition
FROM routes r
ASOF JOIN weather_observations w
  ON r.origin_city = w.city
 AND r.dep_time >= w.obs_time;
```

#### How DuckDB Evaluates This Query:
1. It matches `origin_city` with `city` (exact match).
2. For each route, it scans backward through time and picks the single weather record with the **largest `obs_time` that is still $\le$ `dep_time`**.
3. For Route `9001` (dep: `06:15:00`), it evaluates:
   - `07:00:00 <= 06:15:00` $\rightarrow$ **FALSE** (Discarded!)
   - `06:00:00 <= 06:15:00` $\rightarrow$ **TRUE** (Selected!)
   - `05:00:00 <= 06:15:00` $\rightarrow$ TRUE, but `06:00:00` is more recent.

```
INTERMEDIATE SCHEMA 1: After Leak-Free ASOF Join
+----------+-----------+---------------------+-------------+---------------------+------------------+------------------+
| route_id | driver_id | dep_time            | origin_city | weather_obs_time    | precipitation_in | road_condition   |
+----------+-----------+---------------------+-------------+---------------------+------------------+------------------+
| 9001     | 401       | 2026-10-12 06:15:00 | Cheyenne    | 2026-10-12 06:00:00 | 0.15             | Wet              |
| 9002     | 402       | 2026-10-12 07:00:00 | Salt Lake   | 2026-10-12 06:30:00 | 0.00             | Dry              |
+----------+-----------+---------------------+-------------+---------------------+------------------+------------------+
Notice: Zero look-ahead bias! The 07:00:00 snow reading was safely excluded.
```

---

### Step 3: Rolling Window Features (Defensive Lagging)

Machine learning models love historical aggregate features. For example: *"What is this driver's average delay over their past 5 trips?"*

In SQL, we calculate rolling statistics using **Window Functions**. But here lies another lethal trap for beginners:

```sql
-- WRONG: ACCIDENTAL LABEL LEAKAGE!
AVG(r.delivery_delay_mins) OVER (
    PARTITION BY r.driver_id 
    ORDER BY r.dep_time 
    ROWS BETWEEN 5 PRECEDING AND CURRENT ROW -- DANGER!
) AS driver_rolling_avg_delay
```

**Why is `CURRENT ROW` fatal?**  
`CURRENT ROW` includes the delay of the *current trip* inside the feature used to predict that very same trip's delay! If a truck is 45 minutes late today, that 45 minutes is factored into its own input feature.

The correct, defensive formulation uses `1 PRECEDING`:
```sql
-- DEFENSIVE: STOPS AT THE PREVIOUS COMPLETED TRIP
AVG(r.delivery_delay_mins) OVER (
    PARTITION BY r.driver_id 
    ORDER BY r.dep_time 
    ROWS BETWEEN 5 PRECEDING AND 1 PRECEDING
) AS driver_historical_avg_delay
```

```
INTERMEDIATE SCHEMA 2: Rolling Window Isolation
Driver 401 Trips:
Trip 1 (Oct 1): Delay = 10 mins  --> Prior Avg: NULL (First trip)
Trip 2 (Oct 4): Delay = 20 mins  --> Prior Avg: 10.0 mins (Uses Trip 1 only)
Trip 3 (Oct 8): Delay = 0 mins   --> Prior Avg: 15.0 mins (Uses Trips 1 & 2)
Trip 4 (Oct 12): [CURRENT TRIP]  --> Prior Avg: 10.0 mins (Uses Trips 1, 2, 3)
```

---

### Step 4: The Final 2D Machine Learning Feature Matrix

Combining the driver dimension table, the point-in-time weather join, and the lagged historical rolling statistics yields our final, production-ready feature matrix:

```sql
-- FINAL PRODUCTION FEATURE MATRIX PIPELINE
WITH driver_history AS (
    SELECT 
        route_id,
        driver_id,
        dep_time,
        origin_city,
        dest_city,
        distance_miles,
        delivery_delay_mins,
        -- Rolling 5-trip average delay (strictly prior trips)
        AVG(delivery_delay_mins) OVER (
            PARTITION BY driver_id 
            ORDER BY dep_time 
            ROWS BETWEEN 5 PRECEDING AND 1 PRECEDING
        ) AS driver_prior_avg_delay,
        -- Total trips completed prior to this route
        COUNT(route_id) OVER (
            PARTITION BY driver_id 
            ORDER BY dep_time 
            ROWS BETWEEN UNBOUNDED PRECEDING AND 1 PRECEDING
        ) AS driver_completed_trips
    FROM routes
)
SELECT 
    -- 1. Entity Identifiers (Metadata)
    h.route_id,
    h.driver_id,
    
    -- 2. Temporal & Route Features
    EXTRACT(HOUR FROM h.dep_time) AS dep_hour_of_day,
    EXTRACT(DOW FROM h.dep_time) AS dep_day_of_week,
    h.distance_miles,
    
    -- 3. Driver Dimension Features
    d.safety_score,
    d.vehicle_type,
    COALESCE(h.driver_prior_avg_delay, 0.0) AS driver_prior_avg_delay,
    h.driver_completed_trips,
    
    -- 4. Point-in-Time Weather Features (No Leakage)
    w.precipitation_in,
    w.visibility_miles,
    w.road_condition,
    
    -- 5. TARGET LABEL (y)
    h.delivery_delay_mins AS target_delay_mins

FROM driver_history h
JOIN drivers d
  ON h.driver_id = d.driver_id
ASOF JOIN weather_observations w
  ON h.origin_city = w.city
 AND h.dep_time >= w.obs_time
ORDER BY h.dep_time ASC;
```

```
FINAL 2D MATRIX (Ready for Pandas / Scikit-Learn):
+----------+-----------+----------+-------------+--------------+------------------+----------------+-------------------+
| route_id | dep_hour  | distance | safety_score| prior_avg_del| precipitation_in | road_condition | target_delay_mins |
+----------+-----------+----------+-------------+--------------+------------------+----------------+-------------------+
| 9001     | 6         | 112.5    | 0.96        | 10.0         | 0.15             | Wet            | 45                |
| 9002     | 7         | 340.0    | 0.88        | 0.0          | 0.00             | Dry            | 0                 |
+----------+-----------+----------+-------------+--------------+------------------+----------------+-------------------+
```
This is a mathematically sound, leak-free feature matrix. Every single column represents information that was **physically available in the real world at departure time**.

---

## 5. Guided Student Practice: Hands-On in DuckDB

Let's test these queries hands-on. You can execute this either directly in Python or using the standalone DuckDB CLI.

### Option A: Running Inside a Python Virtual Environment
Open your terminal, create your lab directory, and launch Python:

```bash
# 1. Create a workspace folder
mkdir -p ~/cosc2060/unit01
cd ~/cosc2060/unit01

# 2. Create and activate a clean virtual environment
python -m venv .venv
source .venv/bin/activate  # On Windows PowerShell: .venv\Scripts\Activate.ps1

# 3. Install DuckDB
pip install duckdb
```

Launch a Python interactive shell (`python`) and run:
```python
import duckdb

# Connect to an in-memory database
con = duckdb.connect()

# Create sample routes and weather
con.sql("""
CREATE TABLE routes (route_id INT, city VARCHAR, dep_time TIMESTAMP);
CREATE TABLE weather (city VARCHAR, obs_time TIMESTAMP, condition VARCHAR);

INSERT INTO routes VALUES (1, 'Cheyenne', '2026-10-12 06:15:00');
INSERT INTO weather VALUES 
    ('Cheyenne', '2026-10-12 05:00:00', 'Clear'),
    ('Cheyenne', '2026-10-12 06:00:00', 'Rain'),
    ('Cheyenne', '2026-10-12 07:00:00', 'Blizzard');
""")

# Run the ASOF JOIN
result = con.sql("""
SELECT r.route_id, r.dep_time, w.obs_time AS weather_time, w.condition
FROM routes r
ASOF JOIN weather w
  ON r.city = w.city
 AND r.dep_time >= w.obs_time;
""")

result.show()
```

### Expected Output:
```
┌──────────┬─────────────────────┬─────────────────────┬───────────┐
│ route_id │      dep_time       │    weather_time     │ condition │
│  int32   │      timestamp      │      timestamp      │  varchar  │
├──────────┼─────────────────────┼─────────────────────┼───────────┤
│        1 │ 2026-10-12 06:15:00 │ 2026-10-12 06:00:00 │ Rain      │
└──────────┴─────────────────────┴─────────────────────┴───────────┘
```
Observe that even though the blizzard reading was in the table, DuckDB precisely selected `06:00:00 Rain` because it was the latest observation prior to `06:15:00`.

---

## 6. Frequently Asked Questions & Common Gotchas

### Gotcha 1: The DuckDB Trailing Comma Trap
* **Symptom**: You write a query and DuckDB throws:
  ```text
  Parser Error: syntax error at or near "FROM"
  LINE 4: FROM routes;
          ^
  ```
* **Why it happens**: You left a trailing comma after the last column in your `SELECT` clause (e.g. `SELECT id, name, FROM routes;`). The SQL grammar expects another column identifier after every comma.
* **Fix**: Check the character right before `FROM` and delete the dangling comma.

---

### Gotcha 2: Ordering Requirement in `ASOF JOIN`
* **Symptom**: DuckDB throws:
  ```text
  Binder Error: ASOF join condition must be of the form: table1.col >= table2.col
  ```
* **Why it happens**: You wrote `AND w.obs_time <= r.dep_time` instead of putting the left table on the left side of the comparison, or you used the wrong inequality.
* **Fix**: In DuckDB, the left table column (`r.dep_time`) must appear on the left side of the inequality: `r.dep_time >= w.obs_time`.

---

### Gotcha 3: The `CURRENT ROW` Leak Trap
* **Symptom**: Your feature matrix has an extraordinarily high correlation (e.g. $r = 0.98$) with the target label, but new predictions fail in validation.
* **Why it happens**: In your window calculation, you wrote `ROWS BETWEEN 5 PRECEDING AND CURRENT ROW`.
* **Fix**: Always specify `1 PRECEDING` as the upper bound for any rolling feature calculated over a target variable. If a driver is currently on Trip #10, their prior performance can only be evaluated across Trips 1 through 9.

---

### Gotcha 4: Timestamp Precision Mismatches
* **Symptom**: Your `ASOF JOIN` returns `NULL` for weather columns across all rows.
* **Why it happens**: `routes.dep_time` was stored with timezone information (`TIMESTAMPTZ`), but `weather.obs_time` was stored as naive local time (`TIMESTAMP`), or one was formatted as a string (`VARCHAR`). DuckDB requires both time columns to share comparable temporal types.
* **Fix**: Explicitly cast timestamps using `::TIMESTAMP` (e.g. `r.dep_time::TIMESTAMP >= w.obs_time::TIMESTAMP`).

---

## 7. Appendix: Technical Reference & Environment Summary

| Feature | PostgreSQL 16 (OLTP) | DuckDB 0.10+ (OLAP) |
|---|---|---|
| **Architecture** | Client-Server Daemon | In-Process Embedded Library |
| **Storage Model** | Row-Oriented (Heap files) | Columnar (Vectorized) |
| **Point-in-Time Join** | `LEFT JOIN LATERAL (...)` | Native `ASOF JOIN` |
| **Local Installation** | Service daemon / Docker container | `pip install duckdb` |
| **Primary Use Case** | Web applications, live transactions, ACID updates | Analytical feature stores, ML pipelines, large file transformations |
