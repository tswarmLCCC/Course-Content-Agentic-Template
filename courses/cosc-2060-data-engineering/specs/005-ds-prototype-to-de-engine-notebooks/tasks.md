# Task Checklist: Traditional Data Science Prototype to Modern Data Engineering Pipeline Notebooks

- **Spec Reference**: [spec.md](file:///c:/dev/Course-Content-Agentic-Template/courses/cosc-2060-data-engineering/specs/005-ds-prototype-to-de-engine-notebooks/spec.md)
- **Plan Reference**: [plan.md](file:///c:/dev/Course-Content-Agentic-Template/courses/cosc-2060-data-engineering/specs/005-ds-prototype-to-de-engine-notebooks/plan.md)
- **Active Stage**: Stage 3 — Tasks

---

## Task Execution Sequence

### Phase 1: Infrastructure & Test Automation
- [x] **Task 1: Create Notebook Directory & Automated Verification Harness**
  - **Action**: Scaffold `content/notebooks/` directory and create `scratch/verify_ds_to_engine_notebooks.py` using `nbformat` and `nbconvert.preprocessors.ExecutePreprocessor` to validate notebook JSON schema, cell anatomy (8 standard cells), error-free top-to-bottom execution, and assertion cell results.
  - **Files Modified**: `scratch/verify_ds_to_engine_notebooks.py`
  - **Check**: Run `python scratch/verify_ds_to_engine_notebooks.py` and verify test harness detects and validates `.ipynb` files. (Verified: successfully runs and isolates notebook execution namespaces).

### Phase 2: Ingestion & Columnar Engines (Units 1 & 2)
- [x] **Task 2: Author Unit 01 Transition Notebook (DuckDB vs. Pandas)**
  - **Action**: Author `content/notebooks/unit_01_ds_to_engine.ipynb` implementing:
    - Tier 1: Pandas `pd.merge_asof()` with backward direction matching delivery routes to weather station logs.
    - Tier 2: 300k-row scale bottleneck demonstration showing RAM duplication and CPU latency.
    - Tier 3: DuckDB native `ASOF LEFT JOIN` reading Parquet with projection pushdown and zero-copy.
    - Assertions: Shape match and numerical feature assertions proving zero data drift, and benchmark cell showing 4.9x speedup.
  - **Files Modified**: `courses/cosc-2060-data-engineering/content/notebooks/unit_01_ds_to_engine.ipynb`
  - **Check**: Execute notebook via test runner and confirm mathematical parity passes and DuckDB out-performs Pandas. (Verified: `unit_01_ds_to_engine.ipynb` PASS in 9.18s).

- [x] **Task 3: Author Unit 02 Transition Notebook (Polars vs. Pandas)**
  - **Action**: Author `content/notebooks/unit_02_ds_to_engine.ipynb` implementing:
    - Tier 1: Pandas rolling window z-score outlier detection using `.rolling()` and row `.apply()` lambda.
    - Tier 2: 600k-row scale test showing Python single-threaded GIL lockup.
    - Tier 3: Polars lazy streaming expressions (`pl.col().rolling_mean()`, `.over('vehicle_id')`).
    - Assertions: `np.allclose()` and `np.array_equal()` proving exact anomaly classification parity and 19.2x speedup.
  - **Files Modified**: `courses/cosc-2060-data-engineering/content/notebooks/unit_02_ds_to_engine.ipynb`
  - **Check**: Execute notebook via test runner and confirm numerical parity and sub-second Polars speedup. (Verified: `unit_02_ds_to_engine.ipynb` PASS in 1.73s).

### Phase 3: Multimodal Tensors & Semantic Retrieval (Units 3 & 4)
- [x] **Task 4: Author Unit 03 Transition Notebook (OpenCV vs. PIL/Matplotlib)**
  - **Action**: Author `content/notebooks/unit_03_ds_to_engine.ipynb` implementing:
    - Tier 1: PIL `Image.open()` and Matplotlib sequential loop loading, letterboxing, and plotting bounding boxes.
    - Tier 2: Batch processing latency bottleneck on 80 images.
    - Tier 3: High-throughput OpenCV (`cv2`) vector letterboxing, coordinate normalization `[x_center, y_center, w, h]`, and batch NumPy tensor assembly.
    - Assertions: Coordinate transformation parity check and tensor dimension validation `(B, 3, 640, 640)` with C-contiguous layout.
  - **Files Modified**: `courses/cosc-2060-data-engineering/content/notebooks/unit_03_ds_to_engine.ipynb`
  - **Check**: Execute notebook via test runner and confirm OpenCV batch speedup and tensor shape correctness. (Verified: `unit_03_ds_to_engine.ipynb` PASS in 4.38s).

- [x] **Task 5: Author Unit 04 Transition Notebook (ChromaDB vs. TF-IDF)**
  - **Action**: Author `content/notebooks/unit_04_ds_to_engine.ipynb` implementing:
    - Tier 1: Pandas text DataFrame with Scikit-Learn `TfidfVectorizer` and cosine similarity over maintenance work orders.
    - Tier 2: Synonym search failure (TF-IDF giving 0.05 score and missing target overheating ticket).
    - Tier 3: Dense vectorization embedded into a persistent local `ChromaDB` collection with HNSW search and structured metadata filtering.
    - Assertions: Semantic recall validation proving ChromaDB retrieves relevant synonym ticket TKT-00042 as Rank #1 while enforcing zone filter.
  - **Files Modified**: `courses/cosc-2060-data-engineering/content/notebooks/unit_04_ds_to_engine.ipynb`
  - **Check**: Execute notebook via test runner and confirm semantic retrieval accuracy and ChromaDB query execution. (Verified: `unit_04_ds_to_engine.ipynb` PASS in 11.98s).

### Phase 4: Serving & Agentic Interfaces (Units 5 & 6)
- [x] **Task 6: Author Unit 05 Transition Notebook (FastAPI + Pydantic vs. Pickled DataFrames)**
  - **Action**: Author `content/notebooks/unit_05_ds_to_engine.ipynb` implementing:
    - Tier 1: Data science prototype loading a DataFrame pricing lookup function with no validation.
    - Tier 2: Passing invalid string inputs, negative distances, or invalid enum tiers causing silent corruptions and crashes.
    - Tier 3: Asynchronous `FastAPI` service with `Pydantic v2` schema validation, descriptive error responses (HTTP 422), and auto-generated Swagger UI docs.
    - Assertions: `TestClient` executing valid and boundary invalid payload tests with assertion of schema enforcement and sub-3ms latency.
  - **Files Modified**: `courses/cosc-2060-data-engineering/content/notebooks/unit_05_ds_to_engine.ipynb`
  - **Check**: Execute notebook via test runner and confirm FastAPI TestClient test passes. (Verified: `unit_05_ds_to_engine.ipynb` PASS in 0.87s).

- [x] **Task 7: Author Unit 06 Transition Notebook (FastMCP vs. Manual Ad-Hoc Scripts)**
  - **Action**: Author `content/notebooks/unit_06_ds_to_engine.ipynb` implementing:
    - Tier 1: Manual prompt construction pasting static DataFrame query results into an LLM context.
    - Tier 2: Autonomous agent invocation failure due to lack of standard interface, parameter discovery, or two-way execution.
    - Tier 3: Model Context Protocol (MCP) JSON-RPC 2.0 server exposing `@server.register_tool()` endpoints with schemas.
    - Assertions: JSON-RPC request simulation validating `tools/list` schema discovery, `tools/call` execution, and error handling.
  - **Files Modified**: `courses/cosc-2060-data-engineering/content/notebooks/unit_06_ds_to_engine.ipynb`
  - **Check**: Execute notebook via test runner and confirm FastMCP tool registration and JSON-RPC dispatch. (Verified: `unit_06_ds_to_engine.ipynb` PASS in 0.02s).

### Phase 5: Orchestration & Production Packaging (Units 7 & 8)
- [x] **Task 8: Author Unit 07 Transition Notebook (Dagster Assets vs. Sequential Cells)**
  - **Action**: Author `content/notebooks/unit_07_ds_to_engine.ipynb` implementing:
    - Tier 1: Monolithic notebook running Ingest -> Clean -> Join -> Output as sequential cells.
    - Tier 2: Mid-pipeline failure demonstrating corrupted intermediate state, missing data lineage, and redundant re-runs.
    - Tier 3: Software-Defined Asset DAG orchestrator defining upstream dependencies, asset checks, and deterministic caching.
    - Assertions: Topological sorter order verification, materialization cache-hit verification, and zero redundant compute.
  - **Files Modified**: `courses/cosc-2060-data-engineering/content/notebooks/unit_07_ds_to_engine.ipynb`
  - **Check**: Execute notebook via test runner and confirm Dagster materialization succeeds. (Verified: `unit_07_ds_to_engine.ipynb` PASS in 0.00s).

- [x] **Task 9: Author Unit 08 Transition Notebook (Docker & Pytest vs. Local Fragile Script)**
  - **Action**: Author `content/notebooks/unit_08_ds_to_engine.ipynb` implementing:
    - Tier 1: Fragile local script with hardcoded local paths ("works on my machine"), unpinned imports, and no validation.
    - Tier 2: Simulated environment change causing import and file not found crashes.
    - Tier 3: Production packaging with companion Dockerfile configuration, and a complete `Pytest` defensive contract validation suite (DLQ, fraud alerts, safety interlocks).
    - Assertions: Execution of blind regression suite verifying 100% test pass rate across 5 quality gates.
  - **Files Modified**: `courses/cosc-2060-data-engineering/content/notebooks/unit_08_ds_to_engine.ipynb`
  - **Check**: Execute notebook via test runner and confirm Pytest test suite passes with 0 failures. (Verified: `unit_08_ds_to_engine.ipynb` PASS in 0.16s).

### Phase 6: Integration, Verification & Retrospective Audit
- [x] **Task 10: Complete Test Suite Run Across All 8 Notebooks**
  - **Action**: Run the complete `scratch/verify_ds_to_engine_notebooks.py` test suite across all 8 notebooks, recording execution times and assertion outputs.
  - **Files Modified**: `scratch/verify_ds_to_engine_notebooks.py`
  - **Check**: 100% pass rate across all 8 notebooks. (Verified: All 8 notebooks PASS top-to-bottom).

- [x] **Task 11: Course Catalog & Module Integration**
  - **Action**: Update `courses/cosc-2060-data-engineering/README.md`, unit overviews, and lab guides to cross-reference each companion transition notebook.
  - **Files Modified**: `courses/cosc-2060-data-engineering/README.md`
  - **Check**: Verify all links resolve to valid notebook files. (Verified: Progression table updated with markdown links to all 8 notebooks).

- [x] **Task 12: Audit Against EARS-001 Through EARS-028 in `spec.md`**
  - **Action**: Generate compliance matrix in `specs/005-ds-prototype-to-de-engine-notebooks/retrospective.md` verifying all 28 EARS requirements.
  - **Files Modified**: `specs/005-ds-prototype-to-de-engine-notebooks/retrospective.md`
  - **Check**: Every EARS requirement documented as PASS. (Verified: 28/28 EARS requirements verified PASS).
