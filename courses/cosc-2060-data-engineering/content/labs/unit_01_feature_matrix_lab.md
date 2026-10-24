# Unit 1 Applied Lab: The Feature Matrix Builder

> **Course**: COSC 2060 — Modern Data Engineering & AI Infrastructure  
> **Unit**: Unit 1 — The Relational Foundation & Supervised Learning Targets  
> **Deliverable**: `lab1_yourlastname.py`  
> **Total Points**: 100 Points  
> **Toolchain**: Python 3.10+, DuckDB 0.10+

---

## 1. Lecture Walkthroughs & Coding Clinic (Gradual Release: "Try First, Then Watch")

These practice challenges follow the **Gradual Release of Responsibility** model ("I Do, We Do, You Do"). Before watching the instructor's video walkthrough, attempt each query in your interactive Python environment or DuckDB terminal. Then watch the recording to compare your query logic, examine execution plans, and review common beginner pitfalls!

```python
"""
====================================================================
COSC 2060 - Unit 1: Coding Clinic Practice
Gradual Release: "Try First, Then Watch"
====================================================================
Instructions:
1. Launch Python in your terminal and import duckdb.
2. Initialize an in-memory database with the clinic tables provided below.
3. Attempt each query challenge independently.
4. Compare your syntax against the instructor walkthrough video!
====================================================================
"""
import duckdb

con = duckdb.connect()

# Set up sample clinic tables
con.sql("""
CREATE TABLE clinic_drivers (
    driver_id INT, 
    driver_name VARCHAR, 
    safety_score DECIMAL(3,2)
);
CREATE TABLE clinic_routes (
    route_id INT, 
    driver_id INT, 
    city VARCHAR, 
    dep_time TIMESTAMP, 
    delay_mins INT
);
CREATE TABLE clinic_weather (
    city VARCHAR, 
    obs_time TIMESTAMP, 
    precip_in DECIMAL(4,2), 
    condition VARCHAR
);

INSERT INTO clinic_drivers VALUES 
    (101, 'Marcus Vance', 0.94),
    (102, 'Elena Rostova', 0.88);

INSERT INTO clinic_routes VALUES 
    (1, 101, 'Cheyenne', '2026-10-15 06:00:00', 10),
    (2, 101, 'Cheyenne', '2026-10-15 14:00:00', 25),
    (3, 102, 'Laramie',  '2026-10-15 09:30:00', 0);

INSERT INTO clinic_weather VALUES 
    ('Cheyenne', '2026-10-15 05:00:00', 0.00, 'Clear'),
    ('Cheyenne', '2026-10-15 12:00:00', 0.45, 'Thunderstorm'),
    ('Cheyenne', '2026-10-15 18:00:00', 1.20, 'Hail'),
    ('Laramie',  '2026-10-15 08:00:00', 0.05, 'Light Fog');
""")

# ==================================================================
# CHALLENGE 1: The Dimension Filter & Projection
# ==================================================================
# Write a query against 'clinic_drivers' that selects driver_name
# and safety_score for drivers with safety_score >= 0.90,
# sorted descending by score.
#
# [YOUR QUERY HERE]




# ==================================================================
# CHALLENGE 2: The First Leak-Free ASOF Join
# ==================================================================
# Write an ASOF JOIN between 'clinic_routes' and 'clinic_weather' on city
# that matches each route to the most recent weather observation 
# recorded strictly at or before route departure (dep_time >= obs_time).
# Select route_id, dep_time, obs_time, and condition.
#
# [YOUR QUERY HERE]




# ==================================================================
# CHALLENGE 3: The Rolling Lag (Zero Leakage)
# ==================================================================
# Calculate a rolling average delay for driver 101 across prior trips.
# Ensure that trip 2 (delay 25) DOES NOT include its own delay in its
# feature calculation! (Use ROWS BETWEEN 5 PRECEDING AND 1 PRECEDING).
#
# [YOUR QUERY HERE]
```

---

## 2. Applied Laboratory Challenges: The Feature Matrix Builder (100 Points)

### Scenario & Business Context
You have been hired as the lead data engineer for **Apex Logistics Inc.**, an interstate shipping company. The machine learning team is preparing to train a gradient-boosted decision tree (GBDT) model to predict delivery delays (`delivery_delay_mins`) before trucks depart their origin terminal.

Your mission is to write a defensive data pipeline script (`lab1_feature_builder.py`) that ingests three messy, unjoined operational tables and outputs a clean, leak-free 2D feature matrix saved as `feature_matrix.parquet` (and `.csv`).

### Database Schemas
Your pipeline will create and populate three tables:

1. **`drivers`**:
   - `driver_id` (INTEGER, Primary Key)
   - `driver_name` (VARCHAR)
   - `hire_date` (DATE)
   - `safety_score` (DECIMAL(3,2))
   - `vehicle_type` (VARCHAR)

2. **`routes`**:
   - `route_id` (INTEGER, Primary Key)
   - `driver_id` (INTEGER, Foreign Key)
   - `origin_city` (VARCHAR)
   - `dest_city` (VARCHAR)
   - `dep_time` (TIMESTAMP)
   - `sched_arrival` (TIMESTAMP)
   - `act_arrival` (TIMESTAMP)
   - `distance_miles` (DECIMAL(6,1))
   - `delivery_delay_mins` (INTEGER, Target Variable)

3. **`weather_observations`**:
   - `station_id` (VARCHAR)
   - `city` (VARCHAR)
   - `obs_time` (TIMESTAMP)
   - `precipitation_in` (DECIMAL(4,2))
   - `visibility_miles` (DECIMAL(4,1))
   - `wind_speed_mph` (INTEGER)
   - `road_condition` (VARCHAR)

---

### Submission Instructions
1. Save your Python script as `lab1_yourlastname.py`.
2. Ensure your script runs standalone from the command line (`python lab1_yourlastname.py`) without errors.
3. Your script must generate `output/feature_matrix.parquet` and print summary diagnostics.
4. Upload `lab1_yourlastname.py` to the Canvas assignment portal.

---

### Graded Challenges

#### Part 1: DuckDB Environment & Schema Introspection (20 Points)
1. **Engine Verification**: Write DuckDB SQL to inspect the active version and verify in-memory execution.
2. **Schema Ingestion**: Programmatically create the three relational tables and populate them with the provided mock logistics dataset (10 drivers, 30 routes, 50 weather observations).
3. **Integrity Audit**: Write a validation query verifying that no route has `act_arrival < dep_time` (sanity checking the raw operational logs).

#### Part 2: Temporal Point-in-Time Alignment (40 Points)
1. **The As-Of Join**: Construct a clean `ASOF JOIN` that matches each route's `dep_time` with the closest historical weather observation where `obs_time <= dep_time` and `origin_city = city`.
2. **Zero-Leakage Assertion**: Write an automated defensive assertion test that checks every row in the result set. If any row has `weather_obs_time > dep_time`, your script must raise a `RuntimeError("CRITICAL: Temporal data leakage detected!")`.
3. **Missing Weather Fallback**: Use `COALESCE` to handle routes that departed before the first weather station recording of the day, setting default baseline values (`precipitation_in = 0.0`, `visibility_miles = 10.0`, `road_condition = 'Normal'`).

#### Part 3: Feature Engineering & Matrix Export (40 Points)
1. **Rolling Driver Experience Features**:
   - Compute `driver_prior_avg_delay`: Average delay over the driver's prior 5 routes using `ROWS BETWEEN 5 PRECEDING AND 1 PRECEDING`. (Must evaluate to `0.0` for a driver's first trip).
   - Compute `driver_lifetime_trips`: Count of all routes completed prior to the current departure timestamp.
2. **Temporal Extraction**:
   - Extract `dep_hour` (0–23) and `dep_day_of_week` (0–6).
3. **Final 2D Matrix Export**:
   - Select the final feature matrix columns:
     - Entity IDs: `route_id`, `driver_id`
     - Features ($X$): `dep_hour`, `dep_day_of_week`, `distance_miles`, `safety_score`, `vehicle_type`, `driver_prior_avg_delay`, `driver_lifetime_trips`, `precipitation_in`, `visibility_miles`, `wind_speed_mph`, `road_condition`
     - Target Label ($y$): `target_delay_mins`
   - Export the result directly to Parquet format using DuckDB's `COPY ... TO 'output/feature_matrix.parquet' (FORMAT PARQUET)`.

---

### Copy-and-Paste Starter Template (`lab1_starter.py`)

Copy the code below into a file named `lab1_starter.py` to begin your lab:

```python
"""
====================================================================
COSC 2060: Modern Data Engineering & AI Infrastructure
Unit 1 Applied Lab: The Feature Matrix Builder
Starter Template File (100 Points Total)
====================================================================
Student Name : [YOUR NAME HERE]
Submission   : lab1_yourlastname.py
Due Date     : Friday at 11:59 PM (Midnight MT)
====================================================================
"""
import os
import duckdb

def initialize_database():
    """Initializes in-memory DuckDB and loads raw operational tables."""
    con = duckdb.connect()
    
    print("Loading raw operational logistics data...")
    
    # 1. Drivers Dimension Table
    con.sql("""
    CREATE TABLE drivers (
        driver_id INT PRIMARY KEY,
        driver_name VARCHAR,
        hire_date DATE,
        safety_score DECIMAL(3,2),
        vehicle_type VARCHAR
    );
    INSERT INTO drivers VALUES
        (101, 'Sarah Chen',    '2022-01-15', 0.98, 'Semi-Trailer'),
        (102, 'David Miller',  '2021-06-10', 0.85, 'Box Truck'),
        (103, 'Amina Yusuf',   '2023-04-20', 0.92, 'Semi-Trailer'),
        (104, 'Carlos Gomez',  '2020-11-05', 0.79, 'Flatbed');
    """)
    
    # 2. Routes Transactional Fact Table
    con.sql("""
    CREATE TABLE routes (
        route_id INT PRIMARY KEY,
        driver_id INT,
        origin_city VARCHAR,
        dest_city VARCHAR,
        dep_time TIMESTAMP,
        sched_arrival TIMESTAMP,
        act_arrival TIMESTAMP,
        distance_miles DECIMAL(6,1),
        delivery_delay_mins INT
    );
    INSERT INTO routes VALUES
        (1, 101, 'Cheyenne', 'Denver',   '2026-10-12 06:00:00', '2026-10-12 08:00:00', '2026-10-12 08:15:00', 102.5, 15),
        (2, 101, 'Denver',   'Cheyenne', '2026-10-12 14:00:00', '2026-10-12 16:00:00', '2026-10-12 16:45:00', 102.5, 45),
        (3, 102, 'Salt Lake','Boise',    '2026-10-12 07:30:00', '2026-10-12 13:30:00', '2026-10-12 13:30:00', 345.0, 0),
        (4, 103, 'Cheyenne', 'Casper',   '2026-10-12 09:00:00', '2026-10-12 12:00:00', '2026-10-12 12:20:00', 178.0, 20),
        (5, 101, 'Cheyenne', 'Denver',   '2026-10-13 06:30:00', '2026-10-13 08:30:00', '2026-10-13 08:35:00', 102.5, 5);
    """)
    
    # 3. Weather Observations Asynchronous Sensor Stream
    con.sql("""
    CREATE TABLE weather_observations (
        station_id VARCHAR,
        city VARCHAR,
        obs_time TIMESTAMP,
        precipitation_in DECIMAL(4,2),
        visibility_miles DECIMAL(4,1),
        wind_speed_mph INT,
        road_condition VARCHAR
    );
    INSERT INTO weather_observations VALUES
        ('CHY-1', 'Cheyenne', '2026-10-12 05:00:00', 0.00, 10.0, 12, 'Dry'),
        ('CHY-1', 'Cheyenne', '2026-10-12 08:00:00', 0.25,  4.0, 28, 'Wet'),
        ('CHY-1', 'Cheyenne', '2026-10-12 12:00:00', 0.90,  1.2, 45, 'Snow/Ice'),
        ('DEN-1', 'Denver',   '2026-10-12 06:00:00', 0.00, 10.0,  8, 'Dry'),
        ('DEN-1', 'Denver',   '2026-10-12 13:00:00', 0.10,  6.0, 15, 'Wet'),
        ('SLC-1', 'Salt Lake','2026-10-12 06:30:00', 0.00, 10.0,  5, 'Dry');
    """)
    
    return con


def build_feature_matrix(con):
    """
    Constructs the leak-free feature matrix query and returns the DuckDB relation.
    
    TODO: Complete the SQL statement below adhering to all unit requirements:
    1. ASOF JOIN routes with weather_observations on city and dep_time >= obs_time
    2. Rolling window lag with ROWS BETWEEN 5 PRECEDING AND 1 PRECEDING
    3. Proper COALESCE defaults for early morning departures
    """
    query = """
    -- [YOUR PIPELINE SQL HERE]
    SELECT 
        r.route_id,
        r.driver_id,
        EXTRACT(HOUR FROM r.dep_time) AS dep_hour,
        r.distance_miles,
        d.safety_score,
        r.delivery_delay_mins AS target_delay_mins
    FROM routes r
    JOIN drivers d ON r.driver_id = d.driver_id
    """
    return con.sql(query)


def verify_no_leakage(con):
    """
    Automated Defensive Audit: Verifies that no weather observation attached
    to a route was recorded AFTER the departure time.
    """
    leakage_check = con.sql("""
    SELECT count(*) AS leak_count
    FROM routes r
    ASOF JOIN weather_observations w
      ON r.origin_city = w.city
     AND r.dep_time >= w.obs_time
    WHERE w.obs_time > r.dep_time;
    """).fetchone()[0]
    
    assert leakage_check == 0, f"LEAKAGE DETECTED: {leakage_check} rows have future weather data!"
    print("PASS: Zero temporal leakage verified. Pipeline is defensive.")


def main():
    print("=" * 60)
    print("Apex Logistics Data Pipeline: Feature Matrix Generator")
    print("=" * 60)
    
    con = initialize_database()
    
    # Run defensive verification
    verify_no_leakage(con)
    
    # Build and preview matrix
    matrix = build_feature_matrix(con)
    print("\nFeature Matrix Sample Preview:")
    matrix.show()
    
    # Export to Parquet
    os.makedirs("output", exist_ok=True)
    matrix.write_parquet("output/feature_matrix.parquet")
    print("Successfully exported feature matrix to output/feature_matrix.parquet")



if __name__ == "__main__":
    main()
```

---

## 3. Grading Rubric & Scoring Criteria (100 Points Total)

| Criteria | Exemplary (Full Points) | Competent (Partial Points) | Developing (Needs Revision) | Points |
|---|---|---|---|---|
| **1. Temporal Leakage Prevention (ASOF Join)** | The `ASOF JOIN` is constructed correctly with `dep_time >= obs_time`. Automated assertions pass with zero future timestamp contamination. | Join executes, but inequality is inverted or calendar dates are used instead of timestamps, causing minor leakage. | Standard `LEFT JOIN` used without time boundaries, introducing catastrophic look-ahead bias. | **30** |
| **2. Rolling Window Isolation (Lag Features)** | Rolling driver statistics strictly utilize `ROWS BETWEEN N PRECEDING AND 1 PRECEDING`. Current row is never included in input feature computation. | Window function partitions correctly, but uses `CURRENT ROW` for feature calculation, causing label leakage. | Window functions omitted or syntax produces runtime errors. | **25** |
| **3. Pipeline Execution & Output Format** | Standalone script executes cleanly without human intervention; outputs valid `output/feature_matrix.parquet` with correct schema. | Script runs, but requires manual file path tweaks or exports only flat uncompressed CSV. | Script fails to execute due to unhandled Python or DuckDB syntax errors. | **20** |
| **4. Defensive Null & Edge Case Handling** | Uses `COALESCE` to provide sensible physical defaults for routes with no prior weather history or first-time drivers. | Leaves unexpected `NULL` values across continuous feature columns. | Script crashes on missing values or unhandled joins. | **15** |
| **5. Code Quality & Standards** | Professional Python/SQL formatting: uppercase SQL keywords, descriptive column aliases, clear docstrings, and modular design. | Minor style violations (mixed case keywords, cryptic column names, missing comments). | Unformatted monolithic script; no documentation or explanatory comments. | **10** |
| **Total** | | | | **100** |
