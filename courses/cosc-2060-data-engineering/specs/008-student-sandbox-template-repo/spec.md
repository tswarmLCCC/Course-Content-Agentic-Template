# Feature Specification: COSC 2060 Student Sandbox Template Repository & Builder's Guide

- **ID**: `specs/008-student-sandbox-template-repo`
- **Status**: Approved
- **Created**: 2026-11-11
- **Target Completion**: 60 minutes

---

## 1. Objective & Target Audience
- **Primary Persona**:
  1. **College Sophomores** enrolled in *COSC 2060: Modern Data Engineering & AI Infrastructure* who need a zero-friction, 1-click GitHub Codespaces (or local VS Code Devcontainer) environment with pre-seeded multimodal datasets, pre-installed Python/AI libraries, interactive notebooks, and weekly lab starters.
  2. **Course Instructors / Authors** who need a comprehensive, repeatable Builder's & Deployment Guide (`STUDENT_SANDBOX_BUILDER_GUIDE.md`) to publish, maintain, and update `tswarmLCCC/COSC-2060-Student-Sandbox` as a GitHub Template Repository.
- **Problem Statement**:
  - While `CMAP-1815-Student-Sandbox` provides a 1-click PostgreSQL 16 sandbox for introductory SQL students, `COSC 2060` requires a modern multimodal Python data & AI infrastructure stack (DuckDB, Polars, Scikit-Learn, OpenCV, Sentence-Transformers, FastAPI, Pydantic v2, MCP, DAG orchestration, and Docker-in-Docker).
  - Without a pre-configured Codespaces sandbox and CPU-optimized dependencies, students face local environment drift, 2.5 GB CUDA PyTorch bloat on CPU-only Codespaces, missing `libGL` OpenCV crashes, HuggingFace download stalls, and manual copy-pasting of starter scripts from Canvas pages.
- **One Job**: Author a complete **Student Sandbox Builder's & Deployment Guide** (`courses/cosc-2060-data-engineering/STUDENT_SANDBOX_BUILDER_GUIDE.md`) AND assemble the complete, ready-to-push **`COSC-2060-Student-Sandbox`** template repository inside `courses/cosc-2060-data-engineering/student_sandbox_template/` mirroring the proven UX of `CMAP-1815-Student-Sandbox`.

---

## 2. Requirements (EARS Syntax)

### A. Builder's & Deployment Guide (`STUDENT_SANDBOX_BUILDER_GUIDE.md`)
- `REQ-01`: **Always**: The repository **shall** include a comprehensive markdown guide at `courses/cosc-2060-data-engineering/STUDENT_SANDBOX_BUILDER_GUIDE.md` documenting:
  1. Architectural comparison between `CMAP-1815-Student-Sandbox` (client-server RDBMS) and `COSC-2060-Student-Sandbox` (in-process Python OLAP + AI + Docker-in-Docker).
  2. Complete directory blueprint and file-by-file responsibilities.
  3. Step-by-step instructions for initializing, pushing, enabling **GitHub Template Repository** mode, configuring **GitHub Codespaces Prebuilds**, and embedding the 1-Click Codespaces badge into Canvas.
  4. Instructor maintenance & troubleshooting playbook (updating datasets, verifying CPU-only PyTorch memory bounds, testing Unit 8 Docker-in-Docker).

### B. Devcontainer & VS Code Environment (`.devcontainer/` & `.vscode/`)
- `REQ-02`: **Always**: The sandbox `.devcontainer/devcontainer.json` **shall** use the official `mcr.microsoft.com/devcontainers/python:1-3.11-bookworm` base image and include the `ghcr.io/devcontainers/features/docker-in-docker:2` feature so students can build and verify their Unit 8 Capstone `Dockerfile` directly inside GitHub Codespaces.
- `REQ-03`: **Always**: The sandbox `requirements.txt` **shall** configure CPU-only PyTorch (`--extra-index-url https://download.pytorch.org/whl/cpu`) and `opencv-python-headless` alongside `duckdb`, `pyarrow`, `polars`, `scikit-learn`, `numpy`, `Pillow`, `sentence-transformers`, `fastapi`, `uvicorn`, `pydantic>=2.0`, `httpx`, and `pytest` so the container installs rapidly and stays within GitHub Codespaces free-tier disk and RAM limits.
- `REQ-04`: **When** the Codespace container finishes creation (`postCreateCommand`), the system **shall** execute `.devcontainer/setup_sandbox.sh` to install dependencies, generate/seed all starter datasets in `datasets/`, pre-cache the `all-MiniLM-L6-v2` embedding model (with graceful offline fallback), and print a clear readiness banner.
- `REQ-05`: **Always**: The `.vscode/extensions.json` and `.vscode/settings.json` files **shall** pre-configure Python, Jupyter, Ruff, Rainbow CSV, Parquet Viewer, and Docker extensions with clean default interpreter and pytest settings.

### C. Datasets & 1-Click Disaster Recovery (`datasets/` & `reset_sandbox.sh`)
- `REQ-06`: **Always**: The `datasets/` directory **shall** contain a master seeding script (`datasets/seed_all_datasets.py`) plus unit-specific generators (including the 1,000,000-row `generate_fuel_data.py` Parquet generator, Apex Logistics DuckDB database `apex_logistics.duckdb`, synthetic multi-resolution fleet inspection images for Unit 3, and maintenance logs for Unit 4).
- `REQ-07`: **When** a student executes `./reset_sandbox.sh`, the system **shall** rebuild `datasets/` and clean generated `output/` artifacts to their pristine initial state while strictly preserving all student code files (`*.py`, `*.ipynb`, `Dockerfile`) inside `units/`.

### D. Weekly Unit Packages (`units/unit_01_...` through `units/unit_08_...`)
- `REQ-08`: **Always**: The sandbox `units/` directory **shall** contain 8 structured unit folders matching the COSC 2060 progression:
  - `unit_01_relational_foundations`
  - `unit_02_anomaly_detection_engines`
  - `unit_03_visual_sensor_and_multimodal`
  - `unit_04_unstructured_text_and_vector_rag`
  - `unit_05_data_as_a_service_and_apis`
  - `unit_06_agentic_interfaces_and_mcp`
  - `unit_07_orchestration_and_automation`
  - `unit_08_capstone_defense_and_production`
- `REQ-09`: **Always**: Each of the 8 unit folders in `student_sandbox_template/units/` **shall** include:
  1. `ds_to_engine.ipynb`: The interactive Data Science Prototype → Data Engineering Engine Jupyter Notebook.
  2. `coding_clinic.py`: Standalone runnable Python script containing the "I Do, We Do, You Do" synchronous/walkthrough coding challenges.
  3. `lab{N}_starter.py`: Complete, syntactically valid Python starter script with mock data initialization and defensive assertion tests.
  4. `lab_guide.md`: Applied lab instructions, business scenario, and submission instructions tailored to the sandbox.
  5. `lab_rubric.md`: Standalone 100-point grading rubric table extracted for rapid student self-audit.
  6. `study_guide.md`: Asynchronous reading and architectural study guide.
  7. `self_check_drills.md`: Formative self-assessment questions and syntax traces before class.
  *(Plus a starter `Dockerfile` in `unit_08_capstone_defense_and_production/`).*

### E. Student-Facing Root `README.md`
- `REQ-010`: **Always**: The sandbox root `README.md` **shall** mirror the clarity of `CMAP-1815-Student-Sandbox/README.md`, featuring a 1-Click GitHub Codespaces launch badge (`https://codespaces.new/tswarmLCCC/COSC-2060-Student-Sandbox?quickstart=1`), terminal vs. Jupyter Notebook execution guides, `./reset_sandbox.sh` disaster recovery instructions, full repository tree map, and weekly Canvas submission workflow.

---

## 3. Deliberately Out of Scope
- Modifying the existing compiled Canvas Common Cartridge (`COSC_2060_Complete.imscc`) or altering existing files in `courses/cosc-2060-data-engineering/units/` and `content/` (we will read from them to populate `student_sandbox_template/` without mutating source course files).
- Pushing directly to a remote GitHub repository (we will prepare the complete standalone folder and provide the exact `git` / `gh` commands in the Builder's Guide for the user to push to `tswarmLCCC/COSC-2060-Student-Sandbox`).
- Include instructor-only `teaching_notes.md` or quiz keys inside the student sandbox repository (must remain strictly student-facing).

---

## 4. Acceptance Criteria & Definition of Done
- [x] `courses/cosc-2060-data-engineering/STUDENT_SANDBOX_BUILDER_GUIDE.md` authored with full architecture, setup, Codespaces Prebuild, and GitHub publication instructions.
- [x] `courses/cosc-2060-data-engineering/student_sandbox_template/` populated with `.devcontainer/`, `.vscode/`, `datasets/`, `reset_sandbox.sh`, `requirements.txt`, `.gitignore`, `README.md`, and all 8 `units/` directories.
- [x] Every `units/unit_0N_.../` directory verified to contain all 7 required artifacts (`ds_to_engine.ipynb`, `coding_clinic.py`, `labN_starter.py`, `lab_guide.md`, `lab_rubric.md`, `study_guide.md`, `self_check_drills.md`, plus `Dockerfile` in Unit 8).
- [x] All Python scripts (`coding_clinic.py`, `labN_starter.py`, `datasets/seed_all_datasets.py`) verified for 100% valid Python AST syntax (`py_compile`).
- [x] Zero instructor-only solution keys or `teaching_notes.md` leaked into `student_sandbox_template/`.
