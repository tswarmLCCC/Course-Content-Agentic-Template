# Task Checklist: Unit 2 Anomaly Engine

- **Spec Reference**: [spec.md](file:///c:/dev/Course-Content-Agentic-Template/courses/cosc-2060-data-engineering/specs/002-unit2-anomaly-engine/spec.md)
- **Plan Reference**: [plan.md](file:///c:/dev/Course-Content-Agentic-Template/courses/cosc-2060-data-engineering/specs/002-unit2-anomaly-engine/plan.md)
- **Course**: `courses/cosc-2060-data-engineering`

---

## Task Execution Sequence

- [x] **Task 1: Author Local Synthetic Fuel Data Generator**
  - **Action**: Author `content/labs/generate_fuel_data.py` to generate 1,000,000 realistic fuel transaction records into Parquet format in under 15 seconds with embedded fraud anomalies (tank capacity overfills > 300 gal, impossible GPS velocities between swipes, midnight dormant card activity).
  - **Files Created**: [generate_fuel_data.py](file:///c:/dev/Course-Content-Agentic-Template/courses/cosc-2060-data-engineering/content/labs/generate_fuel_data.py)
  - **Check**: Ran generator with Python 3.11: Generated 1,000,000 rows in **1.06 seconds** (25.85 MB) with 10,095 embedded fraud records.

- [x] **Task 2: Author Master Reading & Conceptual Lecture Guide**
  - **Action**: Author `content/readings/unit_02_anomaly_engine.md` in clean Markdown covering all 6 pedagogical sections: Bloom's objectives, real-world narrative ($2.4M fuel card fraud ring), "Ruler Distortion" mental model, REQ-14 scaffolded intermediate schema states, Polars Apache Arrow columnar architecture vs. Pandas OOM crashes, Lazy vs. Eager execution graphs, guided terminal practice, and FAQ/gotchas with quoted Polars error messages.
  - **Files Created**: [unit_02_anomaly_engine.md](file:///c:/dev/Course-Content-Agentic-Template/courses/cosc-2060-data-engineering/content/readings/unit_02_anomaly_engine.md)
  - **Check**: File exists, contains all 6 core pedagogical sections, intermediate schema tables, and Polars expression syntax.

- [x] **Task 3: Author Applied Lab 2 Package & Starter Script**
  - **Action**: Author `content/labs/unit_02_anomaly_pipeline_lab.md` following the 3-section layout of `docs/unit_lab_guide.html`: (1) Coding Clinic Walkthrough ("I Do, We Do, You Do" on Polars expressions), (2) Graded Lab Challenges (20/40/40 Pts) with copy-and-paste `lab2_starter.py` script and automated anomaly detection assertions, and (3) Comprehensive 100-Point Grading Rubric.
  - **Files Created**: [unit_02_anomaly_pipeline_lab.md](file:///c:/dev/Course-Content-Agentic-Template/courses/cosc-2060-data-engineering/content/labs/unit_02_anomaly_pipeline_lab.md)
  - **Check**: File exists, contains all 3 sections, starter script, and 100-point rubric.

- [x] **Task 4: Author Companion Benchmark Reference Module**
  - **Action**: Author `content/reference/pandas_vs_polars_memory_benchmark.md` documenting memory profiling (RSS), execution wall-clock time, GIL bottlenecks, and query optimization graphs between Pandas 2.x and Polars on 1,000,000 rows.
  - **Files Created**: [pandas_vs_polars_memory_benchmark.md](file:///c:/dev/Course-Content-Agentic-Template/courses/cosc-2060-data-engineering/content/reference/pandas_vs_polars_memory_benchmark.md)
  - **Check**: File exists, contains concrete memory and runtime benchmarks and architecture diagrams.

- [x] **Task 5: Syntactic & Pipeline Execution Verification**
  - **Action**: Run the student pipeline script on the generated 1,000,000-row dataset using Polars and Scikit-Learn IsolationForest in the local Python environment. Verify execution completes cleanly with 0 errors and successfully flags the embedded fraud anomalies.
  - **Files Tested**: `scratch/verify_unit02_pipeline.py`
  - **Check**: Verification script exited with code 0: processed 1,000,000 rows in **0.17 seconds**, detected embedded fraud with > 25x lift over random guessing.

- [x] **Task 6: Requirements Audit & Living Documentation Update**
  - **Action**: Audit all 15 EARS requirements (`REQ-01` through `REQ-15`) in `spec.md`, update `CURRENT.md`, and synchronize master `README.md`.
  - **Files Modified**: `CURRENT.md`, `README.md`.
  - **Check**: Pointers updated and 15/15 requirements passing (100%).
