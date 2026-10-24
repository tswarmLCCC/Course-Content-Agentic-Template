# Unit 01 Overview: Relational Foundations & Vectorized Ingestion

Welcome to Unit 01 of **COSC 2060: Modern Data Engineering & AI Infrastructure**. This week establishes the bedrock of analytical data engineering: understanding why row-oriented databases crawl under analytical workloads and how vectorized columnar execution engines (DuckDB and Polars) achieve sub-second query performance on gigabyte-scale datasets without cluster overhead.

---

## Weekly Contact Hour Budget (300 Minutes Total)
- **Conceptual Study & Readings (150 min)**: Review the core reading on columnar memory, DuckDB vectorization, and SQL query plans.
- **Asynchronous Preparation & Drills (60 min)**: Complete the self-check diagnostic exercises and execution order drills.
- **Hands-on Engineering Lab (90 min)**: Implement the Fleet Telemetry Feature Matrix Lab using DuckDB CLI and Python starter code.

---

## Measurable Learning Objectives
By the end of this unit, you will be able to:
1. **Differentiate** columnar memory layouts (Apache Arrow/Parquet) from row-oriented storage (B-Tree heap pages) in terms of I/O efficiency and CPU cache utilization.
2. **Execute** high-throughput analytical transformations on multi-gigabyte CSV and Parquet files using in-process DuckDB queries.
3. **Analyze** query execution plans using `EXPLAIN ANALYZE` to identify scan bottlenecks and predicate pushdown opportunities.
4. **Construct** a verified vehicle telemetry feature matrix aggregating fuel consumption, speed variance, and runtime anomalies.

---

## Weekly Learning Roadmap & Deliverables

Follow the sequential module workflow in Canvas to complete this unit:

1. **Step 1: Required Readings & Reference Architecture**  
   Study the conceptual architecture, columnar execution models, and benchmark case studies in the module reading.
2. **Step 2: Diagnostic Drills & Syntax Checks**  
   Complete the asynchronous concept checks, query trace evaluations, and defensive gotcha drills before tackling the lab.
3. **Step 3: Applied Engineering Lab & Starter Code**  
   Build and test your local data pipeline implementation (`lab1_starter.py`) adhering to the 100-point rubric, then submit your script to the assignment dropbox.
4. **Step 4: Knowledge Check & Concept Verification**  
   Take the untimed 10-question formative assessment in Canvas (up to 3 attempts, highest score kept) to lock in key terminology and mental models.
