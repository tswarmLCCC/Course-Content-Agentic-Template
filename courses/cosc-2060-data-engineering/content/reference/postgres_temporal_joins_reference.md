# Reference Module: Point-in-Time Joins in Pure PostgreSQL

> **Course**: COSC 2060 — Modern Data Engineering & AI Infrastructure  
> **Target Audience**: Instructors, Advanced Students, and Systems Engineers  
> **Topic**: Implementing As-Of / Temporal Alignment in PostgreSQL 16 without DuckDB

---

## 1. Overview: The PostgreSQL As-Of Challenge

In Unit 1, we leveraged **DuckDB's native `ASOF JOIN`** to merge time-series weather observations with truck departures. DuckDB is designed for analytics (OLAP), so it includes specialized temporal join algorithms natively.

However, in many enterprise architectures, your operational data lives in **PostgreSQL**. PostgreSQL is a world-class relational database (OLTP), but standard SQL has no native `ASOF` keyword. If you must engineer features directly inside PostgreSQL without exporting to DuckDB, you have two primary architectural patterns:

1. **The `LATERAL` Subquery Pattern** (Recommended for performance with proper indexing).
2. **The CTE + Window Function (`ROW_NUMBER`) Pattern** (Standard SQL portable across Oracle, SQL Server, and MySQL 8+).

---

## 2. Pattern 1: The `LEFT JOIN LATERAL` Technique

A `LATERAL` join acts like a correlated subquery in the `FROM` clause: for each row in the outer table (`routes`), PostgreSQL evaluates the inner subquery, passing values from the outer row.

```sql
-- PURE POSTGRESQL 16: POINT-IN-TIME AS-OF JOIN
SELECT 
    r.route_id,
    r.driver_id,
    r.origin_city,
    r.dep_time,
    w.obs_time AS weather_recorded_at,
    w.precipitation_in,
    w.visibility_miles,
    w.road_condition,
    r.delivery_delay_mins AS target_delay
FROM routes r
LEFT JOIN LATERAL (
    SELECT 
        w.obs_time,
        w.precipitation_in,
        w.visibility_miles,
        w.road_condition
    FROM weather_observations w
    WHERE w.city = r.origin_city
      AND w.obs_time <= r.dep_time
    ORDER BY w.obs_time DESC
    LIMIT 1
) w ON true
ORDER BY r.dep_time ASC;
```

### How PostgreSQL Executes This:
1. PostgreSQL scans the `routes` table.
2. For each route, it evaluates the `LATERAL` block, substituting `r.origin_city` and `r.dep_time`.
3. It filters the weather observations matching the city where `obs_time <= dep_time`.
4. It sorts by `obs_time DESC` and takes the top record (`LIMIT 1`).
5. Because of `LEFT JOIN ... ON true`, if a route departed before the earliest weather observation, the weather columns return `NULL` instead of dropping the route.

### Mandatory Performance Index:
Without an index, this query performs an **$O(N \times M)$ Nested Loop Sequential Scan**, which will lock up your database on large tables! To make this fast, create a **composite B-Tree index**:

```sql
CREATE INDEX idx_weather_city_time 
ON weather_observations (city, obs_time DESC);
```
With this composite index, PostgreSQL converts the subquery from a full table scan into an instant **Index Scan (Backward)**, finding the exact single row in logarithmic time $O(N \log M)$.

---

## 3. Pattern 2: Window Function (`ROW_NUMBER()`) Fallback

If your database does not support `LATERAL` joins, you can use a Common Table Expression (CTE) with `ROW_NUMBER()`:

```sql
WITH ranked_weather AS (
    SELECT 
        r.route_id,
        w.obs_time,
        w.precipitation_in,
        w.visibility_miles,
        w.road_condition,
        ROW_NUMBER() OVER (
            PARTITION BY r.route_id 
            ORDER BY w.obs_time DESC
        ) AS rank_order
    FROM routes r
    JOIN weather_observations w
      ON r.origin_city = w.city
     AND w.obs_time <= r.dep_time
)
SELECT 
    r.route_id,
    r.driver_id,
    r.dep_time,
    rw.obs_time AS weather_recorded_at,
    rw.precipitation_in,
    rw.visibility_miles,
    rw.road_condition,
    r.delivery_delay_mins AS target_delay
FROM routes r
LEFT JOIN ranked_weather rw
  ON r.route_id = rw.route_id
 AND rw.rank_order = 1
ORDER BY r.dep_time ASC;
```

### Trade-Offs:
- **Pros**: 100% ANSI-SQL compliant; works across nearly every modern SQL engine.
- **Cons**: Substantially higher memory overhead. The inner join produces an intermediate Cartesian product of *all* historical weather observations prior to departure, which must then be sorted in memory before filtering `WHERE rank_order = 1`.

---

## 4. Execution Plan Comparison: PostgreSQL vs. DuckDB

| Metric | **PostgreSQL 16 (`LATERAL`)** | **DuckDB 0.10+ (`ASOF JOIN`)** |
|---|---|---|
| **Join Mechanism** | Nested Loop with Index Scan | Vectorized Sort-Merge / Binary Search As-Of |
| **Index Requirement** | Mandatory composite index `(city, obs_time DESC)` | No index required; sorts in-memory in columnar batches |
| **Execution Model** | Row-at-a-time (tuple iterator) | Block-at-a-time (SIMD vectorized vector chucks) |
| **Best Used When** | Real-time, single-route inference API (e.g. querying weather for 1 newly dispatched truck) | Offline batch feature matrix generation (e.g. processing 10 million historical trips for model training) |

---

## 5. Architectural Recommendation for Engineering Teams

- **Use PostgreSQL (with `LATERAL`)** when your application is a live web service (like an operations dashboard or FastAPI backend in Unit 5) that needs to look up the latest sensor observation for **one single transaction at a time**.
- **Use DuckDB** when you need to assemble training datasets, historical feature stores, and analytical benchmarks across millions of rows, taking advantage of local memory, zero server configuration, and native `ASOF` performance.
