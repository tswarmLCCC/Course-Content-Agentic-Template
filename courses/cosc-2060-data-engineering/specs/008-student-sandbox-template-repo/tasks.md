# Task Breakdown: COSC 2060 Student Sandbox Template Repository & Builder's Guide

- **Spec Reference**: [`specs/008-student-sandbox-template-repo/spec.md`](file:///c:/dev/Course-Content-Agentic-Template/courses/cosc-2060-data-engineering/specs/008-student-sandbox-template-repo/spec.md)
- **Plan Reference**: [`specs/008-student-sandbox-template-repo/plan.md`](file:///c:/dev/Course-Content-Agentic-Template/courses/cosc-2060-data-engineering/specs/008-student-sandbox-template-repo/plan.md)
- **Status**: Completed & Verified (100% PASS)

---

## Ordered Implementation Tasks

### Task 1: Scaffold Devcontainer, VS Code Config, & Root Infrastructure (`REQ-02`–`REQ-05`, `REQ-07`, `REQ-10`)
- **Action**: Create `courses/cosc-2060-data-engineering/student_sandbox_template/` with:
  - `.devcontainer/devcontainer.json` (Python 3.11 Bookworm + `docker-in-docker:2` + port 8000 forwarding + VS Code extensions)
  - `.devcontainer/setup_sandbox.sh` (pip install, dataset seed execution, MiniLM model cache pre-warming, readiness banner)
  - `.vscode/extensions.json` & `.vscode/settings.json`
  - `requirements.txt` (CPU-only PyTorch index + headless OpenCV + DuckDB, Polars, Scikit-Learn, Sentence-Transformers, FastAPI, Pydantic v2, HTTPX, Pytest, Ruff)
  - `.gitignore`
  - `reset_sandbox.sh` (1-click dataset re-seeding & output cleanup preserving student `.py`/`.ipynb` files)
  - `README.md` (Student-facing Codespaces launch guide modeled after `CMAP-1815-Student-Sandbox/README.md`)
- **Check**: Verify all JSON config files parse cleanly via `python -c "import json..."` and bash scripts have clean LF line endings (`\n`).

### Task 2: Build Datasets Directory & Automated Seeding Engine (`REQ-06`)
- **Action**: Create `student_sandbox_template/datasets/` containing:
  - `generate_fuel_data.py` (1,000,000-row fuel fraud Parquet generator outputting to `datasets/fuel_transactions.parquet` and `data/fuel_transactions.parquet`)
  - `seed_all_datasets.py` (Master dataset generator seeding `datasets/apex_logistics.duckdb`, `datasets/fuel_transactions.parquet`, `datasets/raw_fleet_images/` multi-aspect inspection images with `annotations.json`, and `datasets/maintenance_logs.txt`)
  - `datasets/README.md` (Schema & data dictionary for students)
- **Check**: Compile and execute `py_compile` on `seed_all_datasets.py` and `generate_fuel_data.py`.

### Task 3: Populate All 8 Unit Directories in `student_sandbox_template/units/` (`REQ-08`, `REQ-09`)
- **Action**: Assemble `unit_01_relational_foundations` through `unit_08_capstone_defense_and_production` inside `student_sandbox_template/units/`, populating each with:
  1. `ds_to_engine.ipynb` (from `content/notebooks/unit_0N_ds_to_engine.ipynb`)
  2. `coding_clinic.py` (runnable "I Do, We Do, You Do" synchronous clinic scripts)
  3. `lab{N}_starter.py` (runnable starter templates with resilient dataset path lookup)
  4. `lab_guide.md` (cleaned applied lab guide)
  5. `lab_rubric.md` (standalone 100-point rubric table)
  6. `study_guide.md` (from `units/unit_0N_.../reading.md`)
  7. `self_check_drills.md` (from `units/unit_0N_.../drills.md`)
  8. `Dockerfile` in `unit_08_capstone_defense_and_production/`
- **Check**: Run automated verification confirming all 8 unit folders contain all required files and every `.py` script passes `py_compile`.

### Task 4: Author Comprehensive Builder's & Deployment Guide (`REQ-01`)
- **Action**: Write `courses/cosc-2060-data-engineering/STUDENT_SANDBOX_BUILDER_GUIDE.md` detailing:
  1. Executive Summary & Architectural Evolution (`CMAP-1815` PostgreSQL vs. `COSC-2060` Multimodal AI/DE Stack)
  2. Complete Repository Blueprint & File Contract
  3. Engineering Deep-Dive: Why Single-Container + CPU-Only Torch + Headless OpenCV + Docker-in-Docker
  4. Step-by-Step GitHub Template Repository Publication (`git init`, `gh repo create`, Template checkbox, branch protection)
  5. Configuring GitHub Codespaces Prebuilds (eliminating student wait time)
  6. Embedding the 1-Click Launch Badge & Reset Workflow into Canvas LMS
  7. Semester Maintenance & Troubleshooting Playbook
- **Check**: Verify `STUDENT_SANDBOX_BUILDER_GUIDE.md` exists, links resolve, and all sections required by `REQ-01` are complete.

### Task 5: End-to-End Audit & Living Documentation Update (`REQ-01`–`REQ-10`)
- **Action**:
  - Run comprehensive verification script checking all EARS requirements (`REQ-01` to `REQ-10`), AST syntax of all 18 Python scripts, JSON validity of all 11 JSON/Notebook files, LF line endings on `.sh` scripts, and zero leaked instructor keys.
  - Update `courses/cosc-2060-data-engineering/README.md`, master `README.md`, and `CURRENT.md`.
- **Check**: Present complete verification audit output to user.
