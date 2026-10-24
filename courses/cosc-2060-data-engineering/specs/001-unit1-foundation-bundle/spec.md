# Feature Specification: Unit 1 Foundation Bundle

- **Course**: `courses/cosc-2060-data-engineering`
- **ID**: `specs/001-unit1-foundation-bundle`
- **Status**: In Review
- **Created**: 2026-10-23
- **Target Deliverables**:
  1. Unit 1 Master Reading & Lecture Guide (`content/readings/unit_01_relational_foundation.md`)
  2. Applied Lab 1 Package & Starter Script (`content/labs/unit_01_feature_matrix_lab.md`)
  3. PostgreSQL Alternative Reference Guide (`content/reference/postgres_temporal_joins_reference.md`)

---

## 1. Objective & Target Audience
- **Primary Persona**: **College Sophomores (2nd-year undergraduates)**.
  - **Prior Background**: Completed an introductory SQL class (basic SELECT, single-table queries, basic joins) and an introductory Machine Learning class (familiar with supervised learning concepts: features $X$, target labels $y$, train/test splits, overfitting, and evaluation metrics).
  - **The Critical Cognitive Gap**: In ML class, students were handed clean, pre-packaged CSV datasets (e.g. Iris, Titanic, or Kaggle files). In SQL class, they queried static operational rows for human reports. They have **never engineered a feature matrix from scratch** out of raw, messy relational databases, nor have they wrestled with real-world time-series alignment.
- **Pedagogical Stance & Scaffolding**: 
  - Materials must be **carefully and deliberately scaffolded** using the "I Do, We Do, You Do" gradual release model.
  - Complex transformations (such as `ASOF JOIN` and rolling window lags) must be broken down visually into intermediate data states before presenting the final unified query.
  - Connect concepts directly to their ML intuition: show how bad SQL engineering creates artificial 99% training accuracy that immediately collapses upon deployment due to temporal leakage.
- **One Job**: Bridge the gap between relational databases and machine learning by teaching students how to transform raw, messy transactional logistics tables into a leak-free 2D feature matrix ready for model consumption.


---

## 2. Requirements (EARS Syntax)

### Deliverable A: Master Reading & Conceptual Lecture Guide
- **Always (Ubiquitous)**:
  - `REQ-01`: The reading guide **shall** include the 6 core pedagogical sections: Unit Overview & Measurable Objectives, Narrative of Real-World Friction, Conceptual Metaphor, Technical Deep Dive, Guided Hands-on Practice, and FAQs/Gotchas with exact quoted error messages.
  - `REQ-02`: The reading guide **shall** use clean, semantic Markdown formatted for easy human review without raw visual HTML classes.
  - `REQ-03`: The reading guide **shall** explicitly contrast row-oriented OLTP (PostgreSQL) against columnar-oriented OLAP (DuckDB) in terms of memory layout, disk I/O, and analytical query performance.
- **When (Event-Driven)**:
  - `REQ-04`: **When** presenting temporal data leakage, the text **shall** illustrate the exact real-world mechanism of look-ahead bias with a concrete timeline diagram showing why a standard SQL `LEFT JOIN` on dates contaminates route departure features with post-departure weather events.
  - `REQ-05`: **When** introducing As-Of joins, the text **shall** provide complete, runnable DuckDB SQL queries utilizing `ASOF JOIN` with explicit inequality constraints (`routes.dep_time >= weather.obs_time`).
  - `REQ-14`: The instructional reading and coding clinics **shall** include intermediate ASCII/Markdown table schemas illustrating data states step-by-step (Raw Normalized $\to$ Point-in-Time Joined $\to$ Window Aggregated $\to$ Final 2D Feature Matrix) to ensure sophomore students never experience cognitive overload.
- **If-Then (Error & Defensive Mitigation)**:
  - `REQ-06`: **If** a query contains trailing commas, mismatched timestamps, or missing aliases, **then** the FAQ section **shall** quote the exact DuckDB parser error messages and provide step-by-step resolution explanations.

---

### Deliverable B: Applied Lab 1 Package & Starter Script
- **Always (Ubiquitous)**:
  - `REQ-07`: The lab guide **shall** follow the 3-part layout from `docs/unit_lab_guide.html`:
    1. Lecture Walkthrough & Coding Clinic (Gradual Release: "I Do, We Do, You Do").
    2. Applied Lab Challenges with 3 progressive parts and a copy-and-paste starter script (`lab1_starter.py` / `lab1_starter.sql`).
    3. Comprehensive 100-Point Evaluation Rubric.
  - `REQ-08`: The lab scenario **shall** provide 3 realistic, messy logistics tables:
    - `drivers`: ID, name, hire date, safety rating, vehicle type.
    - `routes`: Route ID, driver ID, departure time, scheduled arrival, actual arrival, distance miles, historical delivery delay (target label).
    - `weather_observations`: Station ID, observation timestamp, precipitation inches, visibility miles, road surface condition.
- **When (Event-Driven)**:
  - `REQ-09`: **When** building the final feature matrix, students **shall** execute an `ASOF JOIN` that attaches only the latest weather observation recorded *strictly before or at* the route departure timestamp.
- **While (State-Driven)**:
  - `REQ-10`: **While** computing rolling feature metrics (e.g. driver average delay over their past 5 trips), the query **shall** use window functions with `ROWS BETWEEN ... PRECEDING` that strictly exclude current or future rows.
- **If-Then (Defensive Engineering Check)**:
  - `REQ-11`: **If** future weather records (timestamp > departure time) appear in the feature matrix, **then** the automated self-check test **shall** flag the record as a catastrophic temporal leak and fail the submission.

---

### Deliverable C: PostgreSQL Alternative Reference Module
- **Always (Ubiquitous)**:
  - `REQ-12`: The reference guide **shall** provide complete, production-grade PostgreSQL 16 SQL code implementing the identical point-in-time join using `LEFT JOIN LATERAL (...) ON true` and window functions (`ROW_NUMBER() OVER (...)`).
  - `REQ-13`: The guide **shall** contrast the `EXPLAIN ANALYZE` query execution plans between PostgreSQL's nested loops and DuckDB's vectorized columnar scan.

---

## 3. Deliberately Out of Scope
- Training machine learning models (e.g. Scikit-learn, XGBoost) is deferred to later units; Unit 1 focuses 100% on data engineering and pipeline generation.
- Production cloud deployment (AWS, Snowflake, BigQuery) is out of scope; all work is local-first.
- Automated API serving is out of scope; deferred to Unit 5 (FastAPI).

---

## 4. Acceptance Criteria & Definition of Done
- [ ] Every requirement from REQ-01 through REQ-13 verified in written deliverables.
- [ ] Conforms to ADR-001 (WCAG 2.1/2.2 AA compliant markdown structure, clear contrast, semantic tables).
- [ ] Conforms to ADR-002 (Spec, plan, tasks, and deliverables fully linked in project memory).
- [ ] User review and approval received on `spec.md` before planning phase.
