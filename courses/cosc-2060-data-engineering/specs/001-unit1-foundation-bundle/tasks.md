# Task Checklist: Unit 1 Foundation Bundle

- **Spec Reference**: [spec.md](file:///c:/dev/Course-Content-Agentic-Template/courses/cosc-2060-data-engineering/specs/001-unit1-foundation-bundle/spec.md)
- **Plan Reference**: [plan.md](file:///c:/dev/Course-Content-Agentic-Template/courses/cosc-2060-data-engineering/specs/001-unit1-foundation-bundle/plan.md)
- **Course**: `courses/cosc-2060-data-engineering`

---

## Task Execution Sequence

- [x] **Task 1: Author Master Reading & Conceptual Lecture Guide**
  - **Action**: Author `content/readings/unit_01_relational_foundation.md` in clean, human-readable Markdown matching the depth of `ref/unit_reading_example.html`. Cover Bloom's objectives, the narrative of look-ahead bias, OLTP vs. OLAP mental model, REQ-14 step-by-step intermediate schemas, DuckDB `ASOF JOIN`, rolling lags, terminal practice, and FAQ/gotchas with quoted error messages.
  - **Files Created**: [unit_01_relational_foundation.md](file:///c:/dev/Course-Content-Agentic-Template/courses/cosc-2060-data-engineering/content/readings/unit_01_relational_foundation.md)
  - **Check**: File exists, contains all 6 core pedagogical sections and REQ-14 intermediate data state diagrams.

- [x] **Task 2: Author Applied Lab 1 Package & Starter Script**
  - **Action**: Author `content/labs/unit_01_feature_matrix_lab.md` following the 3-section structure of `docs/unit_lab_guide.html`: (1) Gradual Release Coding Clinic ("I Do, We Do, You Do"), (2) Graded Lab Challenges across `drivers`, `routes`, `weather_observations` with copy-and-paste `lab1_starter.py` script, and (3) Comprehensive 100-Point Grading Rubric.
  - **Files Created**: [unit_01_feature_matrix_lab.md](file:///c:/dev/Course-Content-Agentic-Template/courses/cosc-2060-data-engineering/content/labs/unit_01_feature_matrix_lab.md)
  - **Check**: File exists, contains all 3 sections, complete table schemas, starter code, and 100-point rubric.

- [x] **Task 3: Author PostgreSQL Alternative Reference Module**
  - **Action**: Author `content/reference/postgres_temporal_joins_reference.md` demonstrating point-in-time joins in pure PostgreSQL using `LEFT JOIN LATERAL (...)`, composite indexing, and execution plan comparisons with DuckDB.
  - **Files Created**: [postgres_temporal_joins_reference.md](file:///c:/dev/Course-Content-Agentic-Template/courses/cosc-2060-data-engineering/content/reference/postgres_temporal_joins_reference.md)
  - **Check**: File exists, contains runnable PostgreSQL SQL queries and execution plan explanations.

- [x] **Task 4: Syntactic Verification of Code & Queries**
  - **Action**: Run a Python validation script in the local environment using DuckDB to verify that all SQL queries and transformation snippets in the reading and lab execute without error.
  - **Files Tested**: `scratch/verify_unit01_queries.py`
  - **Check**: Verification script exited with code 0; all queries executed and exported Parquet cleanly.

- [x] **Task 5: Requirements Audit & Verification**
  - **Action**: Conduct a strict Pass/Fail audit against every EARS requirement (`REQ-01` through `REQ-14`) in `spec.md`.
  - **Check**: Pass/fail table published: 14/14 requirements passing (100%).

- [x] **Task 6: Update State & Documentation**
  - **Action**: Update `CURRENT.md` and master `README.md` to record Unit 1 completion.
  - **Files Modified**: `CURRENT.md`, `README.md`.
  - **Check**: Pointers updated and synchronized.
