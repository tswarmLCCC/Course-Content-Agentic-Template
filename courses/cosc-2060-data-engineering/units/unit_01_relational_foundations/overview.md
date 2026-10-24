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

## Weekly Milestones & Deliverables
- [ ] Read [Unit 01 Required Readings & Concepts](reading.md).
- [ ] Complete [Unit 01 Asynchronous Preparation & Drills](drills.md).
- [ ] Implement and test [Unit 01 Applied Lab Assignment](lab_guide.md).
- [ ] Complete [Unit 01 Knowledge Check](quiz.md) (10 questions, 3 attempts).
