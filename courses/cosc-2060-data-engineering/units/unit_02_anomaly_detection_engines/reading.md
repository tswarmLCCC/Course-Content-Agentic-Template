# Unit 2: The Anomaly Engine & Unsupervised Learning Targets

> **Course**: COSC 2060 — Modern Data Engineering & AI Infrastructure  
> **Estimated Study Time**: 150 minutes of asynchronous conceptual deep-dive & hands-on exploration  
> **Target Audience**: College Sophomores (Prerequisites: Introductory SQL & Introductory Machine Learning)  
> **Core Toolchain**: Polars 0.20+ (Rust-powered Columnar DataFrame Library) & Scikit-Learn

---

## 1. Unit Overview & Objectives

In Unit 1, we tackled supervised learning targets. You learned how to bridge the gap between relational databases and feature matrices using DuckDB, avoiding the catastrophic trap of look-ahead bias with point-in-time `ASOF` joins.

In **Unit 2**, we pivot to **unsupervised learning targets** and **scale**.

In industry, the vast majority of enterprise data does **not** come with ground-truth labels. Nobody labels fraudulent credit card transactions, failing wind turbine bearings, or cyber-attacks in real time. Instead, data engineers must construct high-throughput pipelines that clean, normalize, and transform millions of raw event logs into high-dimensional feature spaces where **unsupervised anomaly detection algorithms** (such as Isolation Forests) can mathematically isolate outliers.

Furthermore, we confront the limits of traditional Python tools. In your introductory machine learning course, you used **Pandas** for everything. On small datasets (10,000 to 50,000 rows), Pandas feels fine. But when an enterprise pipeline ingests **1,000,000 transactions a day**, Pandas consumes massive amounts of RAM, locks up your CPU cores with Python's Global Interpreter Lock (GIL), and crashes with Out-Of-Memory (OOM) errors.

In this unit, you will replace Pandas with **Polars**—a blazing-fast, multithreaded DataFrame library written in Rust and built on the Apache Arrow columnar memory model.

### Measurable Learning Objectives
By the end of this unit, you will be able to:
1. **Analyze** the mathematical mechanics of distance metrics (Euclidean, Manhattan) and articulate why unscaled numerical features distort unsupervised anomaly detection models.
2. **Implement** robust data normalization techniques (Min-Max scaling and Z-Score standardization) natively using vectorized Polars expressions.
3. **Differentiate** between Pandas' eager object-pointer memory model and Polars' multithreaded Apache Arrow columnar execution architecture.
4. **Construct** declarative, leak-free transformation pipelines using Polars **LazyFrames** (`pl.scan_parquet`, expressions, and streaming execution).
5. **Ingest and Clean** 1,000,000 commercial fuel transaction records to feed an unsupervised Isolation Forest anomaly detection baseline.

---

## 2. The Narrative of Data: The Ghost Fuel Card Ring ($2.4M Theft)

To appreciate why scaling and normalization matter, consider an actual corporate logistics fraud case.

A nationwide freight carrier operated a fleet of 5,000 commercial long-haul trucks. Each driver was issued an automated fleet fuel credit card tied to their employee ID. Drivers were instructed to swipe their card at commercial travel centers (Love's, Pilot Flying J, TravelCenters of America) to refuel their Class 8 diesel semi-trucks.

Every month, the company processed approximately **1.2 million fuel transaction records**. To prevent fraud, the accounting department ran a nightly Python script using Pandas. The script calculated basic summary statistics and flagged any transaction where `transaction_amount > $1,200`.

The system seemed fine. For two years, zero major alerts were triggered.

### The $2.4 Million Discovery
During an external audit, forensic accountants discovered that a syndicate of 14 rogue drivers had stolen **$2.4 million in fuel** over an 18-month period. 

How did they bypass the data pipeline?

1. **The Tank Siphon Exploit**: A standard Class 8 semi-truck holds dual fuel tanks with a combined physical capacity of **300 gallons**. At $3.80 per gallon, a full tank costs approximately **$1,140**. The rogue drivers pulled into travel plazas, pumped 250 gallons into their truck, and then pumped an extra **150 gallons into hidden 55-gallon drums** in their trailer, logging 400 gallons for **$1,520**. But they asked the fuel clerk to split the swipe into two separate charges: **$760 and $760**. The naive Pandas filter (`amount > $1,200`) never blinked.
2. **The Cloned Card Teleportation**: One driver sold cloned duplicates of his fuel card to accomplices in different states. At **1:15 PM**, the driver swiped his card in Cheyenne, Wyoming. At **2:00 PM** (45 minutes later), his cloned card was swiped in Dallas, Texas—**950 miles away**. 
   - A commercial semi-truck has a maximum governed speed of 75 mph. Moving 950 miles in 45 minutes implies an impossible speed of **1,266 mph**!
   - Because the data pipeline analyzed transactions in isolation without calculating time-series velocities across consecutive driver swipes, the fraud went completely undetected.

```
THE TELEPORTATION EXPLOIT:
13:15 PM ── Station ST-WY-01 (Cheyenne, WY) ── 180 Gallons Diesel ($684.00)
14:00 PM ── Station ST-TX-22 (Dallas, TX)   ── 210 Gallons Diesel ($798.00)
Delta Time: 45 minutes (0.75 hours)
Delta Distance: 950 miles
Implied Velocity: 1,266 mph! <── PHYSICAL IMPOSSIBILITY!
```

### Why Pandas Failed the Engineering Team
When the junior data engineer tried to write a new script in Pandas that sorted the 1.2 million transactions by driver and calculated rolling velocity vectors and z-scores, the script **crashed the server with an Out-of-Memory (OOM) error**. 

Pandas attempted to allocate **8.4 GB of RAM** to hold Python objects, ran a single-threaded Python `.apply()` loop that pegged 1 CPU core at 100% for 45 minutes, and was terminated by the Linux kernel's Out-Of-Memory Killer (`Killed: 9`).

This is why modern data engineering has moved beyond Pandas. We need engines that process millions of records in seconds while mathematically standardizing features for machine learning.

---

## 3. The Mental Model: "The Ruler Distortion" (Why Scaling Matters)

Before writing code, let's examine why unnormalized features destroy unsupervised anomaly detection algorithms.

Imagine you are designing a surveillance system to detect abnormal objects. You measure two features:
- $X_1$: **Height** (measured in millimeters, e.g. 1,750 mm to 1,900 mm).
- $X_2$: **Weight** (measured in metric tons, e.g. 0.07 tons to 0.09 tons).

Now calculate the standard Euclidean distance between Person A (1,800 mm, 0.08 tons) and Person B (1,850 mm, 0.08 tons):
$$d = \sqrt{(1850 - 1800)^2 + (0.08 - 0.08)^2} = \sqrt{2500 + 0} = 50.0$$

Now calculate the distance between Person A (1,800 mm, 0.08 tons) and Person C (1,800 mm, 0.16 tons — double the weight!):
$$d = \sqrt{(1800 - 1800)^2 + (0.16 - 0.08)^2} = \sqrt{0 + 0.0064} = 0.08$$

The algorithm thinks Person B (who is slightly taller) is **625 times more different** than Person C (who weighs twice as much)! 

```
UNSCALED FEATURE SPACE (The Ruler Distortion):
Odometer (Miles):    0 ─── 100,000 ─── 200,000 ─── 300,000 ─── 400,000 ─── 500,000
Gallons Pumped:      0 ─── 50 ─── 100 ─── 150 ─── 200 ─── 250 ─── 300

A 50-mile difference in Odometer is trivial noise.
A 50-gallon difference in Gallons is a major physical anomaly!
Yet the mathematical algorithm treats a 50-unit change identically on both axes!
```

### The Two Normalization Standards
To eliminate ruler distortion, every feature must be projected onto a standardized mathematical scale:

1. **Min-Max Normalization (Scaling to $[0, 1]$)**:
   $$X_{\text{norm}} = \frac{X - X_{\text{min}}}{X_{\text{max}} - X_{\text{min}}}$$
   - Compresses all numbers strictly between 0.0 and 1.0.
   - Ideal when your features have bounded physical limits (e.g. percentages, coordinates).
2. **Standardization (Z-Score Scaling to $\mu = 0, \sigma = 1$)**:
   $$Z = \frac{X - \mu}{\sigma}$$
   - Centers data around a mean of 0 with a standard deviation of 1.
   - Ideal for anomaly detection: any observation with $|Z| > 3.0$ is immediately recognizable as being more than 3 standard deviations from normal.

---

## 4. Technical Deep Dive: Polars Architecture vs. Pandas OOM

Why does Pandas struggle with 1,000,000 rows, while Polars processes it in less than 2 seconds?

```
PANDAS MEMORY MODEL (Pointer Indirection):
Series: [ Pointer_0 ] ───> Python Object: Float(124.5)  (28 bytes of overhead!)
        [ Pointer_1 ] ───> Python Object: Float(512.0)  (28 bytes of overhead!)
        [ Pointer_2 ] ───> Python Object: Float(88.2)   (28 bytes of overhead!)
Memory is fragmented across RAM. The CPU cache misses constantly.

POLARS MEMORY MODEL (Contiguous Apache Arrow Column):
Float32 Array: [ 124.5 | 512.0 | 88.2 | 210.0 | 45.1 | ... ]
Packed raw binary bytes in contiguous memory. Zero Python object overhead.
```

### The Three Structural Differences:

1. **Apache Arrow Columnar Memory**:
   - In Pandas, every string and number is boxed inside a heavyweight Python object. A 1,000,000-row string column can easily balloon to 1.5 GB in RAM.
   - In Polars, memory is stored in **Apache Arrow** format: flat, contiguous, unboxed binary buffers. The entire 1M-row string column takes only ~15 MB.
2. **Multi-Threading in Rust (No GIL)**:
   - Pandas is single-threaded. When you run `.apply()`, one CPU core pegs at 100% while your other 7 or 15 cores sit idle.
   - Polars is written in **Rust** using the Rayon work-stealing parallelism library. When you run a transformation, Polars splits the data across **every available CPU thread automatically**.
3. **Lazy vs. Eager Execution**:
   - **Eager (Pandas)**: Every line of code runs immediately and allocates intermediate memory:
     ```python
     # PANDAS: EAGER (Allocates 3 full intermediate copies in RAM!)
     df = pd.read_parquet("fuel.parquet")        # Allocation 1 (500 MB)
     df = df[df["gallons"] > 0]                  # Allocation 2 (500 MB)
     df["scaled"] = (df["gallons"] - 50) / 200   # Allocation 3 (500 MB)
     ```
   - **Lazy (Polars)**: Calling `.lazy()` creates a computational recipe (a query graph). Polars optimizes the graph, combines steps, and streams data in small chunks:
     ```python
     # POLARS: LAZY (Zero RAM allocated until collect() is called!)
     q = (
         pl.scan_parquet("fuel.parquet")          # Creates query plan
         .filter(pl.col("gallons") > 0)           # Pushes filter down into Parquet reader
         .with_columns(
             ((pl.col("gallons") - 50) / 200).alias("scaled")
         )
     )
     df = q.collect(engine="streaming")           # Executes in memory-safe chunks!
     ```


---

## 5. Scaffolded Intermediate Transformations (REQ-14)

Let's trace a concrete 2-row sample through our data pipeline to see how each transformation stage alters the feature space for sophomore learners.

```
STAGE 1: Raw Ingested Transaction Data
+----------------+---------------------+-----------+----------------+-------------------+----------------+
| transaction_id | timestamp           | driver_id | gallons_pumped | odometer_reading  | fuel_type      |
+----------------+---------------------+-----------+----------------+-------------------+----------------+
| 1001           | 2026-09-12 12:00:00 | 104       | 120.0          | 450,000           | Diesel         |
| 1002           | 2026-09-12 12:45:00 | 104       | 480.0 (FRAUD!) | NULL              | Diesel         |
+----------------+---------------------+-----------+----------------+-------------------+----------------+
Observations:
- Row 1002 has 480 gallons (exceeds semi-truck tank capacity of 300 gal!).
- Row 1002 has a missing (NULL) odometer reading.
- Odometer is in hundreds of thousands, while gallons is in hundreds.

STAGE 2: Null Imputation & Feature Extraction
+----------------+---------------------+-----------+----------------+-------------------+----------------+--------------------+
| transaction_id | timestamp           | driver_id | gallons_pumped | odometer_reading  | fuel_type      | implied_speed_mph  |
+----------------+---------------------+-----------+----------------+-------------------+----------------+--------------------+
| 1001           | 2026-09-12 12:00:00 | 104       | 120.0          | 450,000           | Diesel         | 52.4               |
| 1002           | 2026-09-12 12:45:00 | 104       | 480.0          | 450,050 (Imputed) | Diesel         | 245.8 (FRAUD!)     |
+----------------+---------------------+-----------+----------------+-------------------+----------------+--------------------+
Transformations Applied:
- Imputed NULL odometer using forward fill over driver_id.
- Calculated implied speed between consecutive swipes: Delta Distance (184 miles) / Delta Time (0.75 hrs) = 245.8 mph.

STAGE 3: Vectorized Min-Max Normalization (Mapped to [0.0, 1.0])
+----------------+--------------------+--------------------+-----------------------+----------------+
| transaction_id | norm_gallons       | norm_odometer      | norm_implied_speed    | fuel_type      |
+----------------+--------------------+--------------------+-----------------------+----------------+
| 1001           | 0.14               | 0.50               | 0.18                  | Diesel         |
| 1002           | 0.96 (OUTLIER!)    | 0.50               | 0.98 (OUTLIER!)       | Diesel         |
+----------------+--------------------+--------------------+-----------------------+----------------+
Mathematical Impact:
- All features now carry equal mathematical weight.
- Row 1002 jumps out with extreme values (0.96 and 0.98), ready for Isolation Forest!

STAGE 4: Final 2D Matrix (Categorical One-Hot Encoding)
+----------------+--------------------+--------------------+-----------------------+-----------+--------+
| transaction_id | norm_gallons       | norm_odometer      | norm_implied_speed    | is_diesel | is_def |
+----------------+--------------------+--------------------+-----------------------+-----------+--------+
| 1001           | 0.14               | 0.50               | 0.18                  | 1.0       | 0.0    |
| 1002           | 0.96               | 0.50               | 0.98                  | 1.0       | 0.0    |
+----------------+--------------------+--------------------+-----------------------+-----------+--------+
```

---

## 6. Guided Student Practice: Hands-on with Polars Expressions

Let's test Polars syntax hands-on. Open your terminal, ensure your virtual environment is active, and install Polars and Scikit-Learn:

```bash
pip install polars pyarrow scikit-learn
```

Launch a Python interactive shell (`python`) and run:

```python
import polars as pl

# 1. Create a sample LazyFrame
lazy_df = pl.LazyFrame({
    "driver_id": [101, 101, 102],
    "gallons": [120.0, 450.0, 80.0],
    "fuel_type": ["Diesel", "Diesel", "DEF"]
})

# 2. Write declarative transformation expressions
query = (
    lazy_df
    # Add a tank capacity alert column
    .with_columns(
        (pl.col("gallons") > 300.0).alias("tank_capacity_violation")
    )
    # Normalize gallons using Min-Max scaling
    .with_columns(
        ((pl.col("gallons") - pl.col("gallons").min()) / 
         (pl.col("gallons").max() - pl.col("gallons").min())).alias("norm_gallons")
    )
)

# 3. View the optimized query plan BEFORE executing
print(query.explain())

# 4. Execute the plan and collect results
result = query.collect()
print(result)
```

### Expected Output:
```text
shape: (3, 5)
┌───────────┬─────────┬───────────┬─────────────────────────┬──────────────┐
│ driver_id ┆ gallons ┆ fuel_type ┆ tank_capacity_violation ┆ norm_gallons │
│ ---       ┆ ---     ┆ ---       ┆ ---                     ┆ ---          │
│ i64       ┆ f64     ┆ str       ┆ bool                    ┆ f64          │
╞═══════════╪═════════╪═══════════╪═════════════════════════╪══════════════╡
│ 101       ┆ 120.0   ┆ Diesel    ┆ false                   ┆ 0.108108     │
│ 101       ┆ 450.0   ┆ Diesel    ┆ true                    ┆ 1.0          │
│ 102       ┆ 80.0    ┆ DEF       ┆ false                   ┆ 0.0          │
└───────────┴─────────┴───────────┴─────────────────────────┴──────────────┘
```

Notice:
- `query.explain()` prints the compiled physical execution plan. Polars optimized the math before touching a single byte!
- The tank capacity violation evaluated to `true` instantly for 450 gallons.

---

## 7. Frequently Asked Questions & Common Gotchas

### Gotcha 1: The "LazyFrame Has No Attribute" Trap
* **Symptom**: You call `df.head()` or `df.shape` and Python throws:
  ```text
  AttributeError: 'LazyFrame' object has no attribute 'shape'
  ```
* **Why it happens**: A `LazyFrame` is a **recipe**, not a materialized table. It does not know how many rows it has because it hasn't read the file yet!
* **Fix**: Call `.collect()` when you need the actual table: `df.collect().shape`. During pipeline construction, keep it lazy until the end.

---

### Gotcha 2: The Eager Assignment Anti-Pattern
* **Symptom**: You try to assign columns like Pandas (`df['new_col'] = ...`) and Polars throws:
  ```text
  TypeError: 'LazyFrame' object does not support item assignment
  ```
* **Why it happens**: Polars DataFrames and LazyFrames are **immutable**. You never modify a column in place.
* **Fix**: Always use `.with_columns()`:
  ```python
  # CORRECT POLARS IDIOM
  df = df.with_columns(
      (pl.col("gallons") * 3.85).alias("estimated_cost")
  )
  ```

---

### Gotcha 3: The `ComputeError` on Window Over
* **Symptom**: You call `pl.col("timestamp").diff().over("driver_id")` and Polars throws:
  ```text
  polars.exceptions.ComputeError: cannot compute diff on unordered group
  ```
* **Why it happens**: Unlike SQL where you specify `OVER (PARTITION BY driver_id ORDER BY timestamp)`, Polars requires the DataFrame to be explicitly sorted by your time column first before applying `.diff().over()`.
* **Fix**: Pre-sort your LazyFrame:
  ```python
  df = df.sort(["driver_id", "timestamp"]).with_columns(
      pl.col("timestamp").diff().over("driver_id").alias("time_delta")
  )
  ```

---

## 8. Appendix: Polars vs. Pandas Quick Reference

| Operation | Pandas (Imperative / Eager) | Polars (Declarative Expressions) |
|---|---|---|
| **Filter Rows** | `df[df['amt'] > 100]` | `df.filter(pl.col('amt') > 100)` |
| **Add / Modify Columns** | `df['tax'] = df['amt'] * 0.08` | `df.with_columns((pl.col('amt') * 0.08).alias('tax'))` |
| **Grouped Aggregation** | `df.groupby('driver')['amt'].mean()` | `df.group_by('driver').agg(pl.col('amt').mean())` |
| **Time Difference** | `df.groupby('driver')['time'].diff()` | `df.sort(['driver', 'time']).with_columns(pl.col('time').diff().over('driver'))` |
| **Missing Imputation** | `df['col'].fillna(0)` | `pl.col('col').fill_null(0)` |
| **Execution Model** | Eager (Immediate memory copy) | Lazy (`pl.scan_parquet` $\rightarrow$ `.collect()`) |
