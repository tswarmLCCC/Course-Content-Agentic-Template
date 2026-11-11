# Implementation Plan: COSC 2060 Student Sandbox Template Repository & Builder's Guide

- **Spec Reference**: [`specs/008-student-sandbox-template-repo/spec.md`](file:///c:/dev/Course-Content-Agentic-Template/courses/cosc-2060-data-engineering/specs/008-student-sandbox-template-repo/spec.md)
- **Status**: Approved
- **Created**: 2026-11-11

---

## 1. Architectural Overview

We are building two tightly coupled deliverables inside `courses/cosc-2060-data-engineering/`:
1. **Builder's & Instructor Deployment Guide** (`courses/cosc-2060-data-engineering/STUDENT_SANDBOX_BUILDER_GUIDE.md`):
   - A comprehensive engineering & pedagogical playbook explaining how to construct, customize, publish, and maintain `tswarmLCCC/COSC-2060-Student-Sandbox` on GitHub.
   - Contrasts `CMAP-1815-Student-Sandbox` (2-container PostgreSQL 16 setup) with `COSC-2060-Student-Sandbox` (single-container Python 3.11 + CPU-only PyTorch + headless OpenCV + DuckDB/Polars + Docker-in-Docker).
   - Provides exact copy-paste `git` / `gh` CLI commands to initialize and push `student_sandbox_template/` to `https://github.com/tswarmLCCC/COSC-2060-Student-Sandbox`, enable **Template repository**, configure **GitHub Codespaces Prebuilds**, and embed the 1-Click badge in Canvas.
2. **Ready-to-Push Student Sandbox Template Repository** (`courses/cosc-2060-data-engineering/student_sandbox_template/`):
   - A complete, self-contained Git repository tree ready to push directly as the root of `tswarmLCCC/COSC-2060-Student-Sandbox`.

---

## 2. Target Directory Structure (`student_sandbox_template/`)

```text
student_sandbox_template/
├── .devcontainer/
│   ├── devcontainer.json          # Python 3.11 Bookworm + docker-in-docker feature + port 8000 forwarding
│   └── setup_sandbox.sh           # Automated pip install, dataset seeding, & MiniLM model pre-cache
├── .vscode/
│   ├── extensions.json            # Python, Jupyter, Ruff, Rainbow CSV, Parquet Viewer, Docker
│   └── settings.json              # Default interpreter, pytest enablement, terminal profile, ruler/formatting
├── datasets/
│   ├── seed_all_datasets.py       # Master seeding orchestrator called by setup_sandbox.sh & reset_sandbox.sh
│   ├── generate_fuel_data.py      # 1,000,000-row fuel fraud Parquet generator (outputs datasets/fuel_transactions.parquet)
│   └── README.md                  # Data dictionary for Apex Logistics tables, Parquet files, vision images, & logs
├── reset_sandbox.sh               # 1-command disaster recovery (re-runs seed_all_datasets.py & cleans output/ folders)
├── requirements.txt               # CPU-only PyTorch + headless OpenCV + DuckDB + Polars + FastAPI + Scikit-Learn
├── .gitignore                     # Ignores __pycache__, .venv, generated large parquets/models, output/ artifacts
├── README.md                      # Student-facing 1-Click Codespaces Quick Start, CLI/Notebook workflows, & Lab submission guide
└── units/
    ├── unit_01_relational_foundations/
    ├── unit_02_anomaly_detection_engines/
    ├── unit_03_visual_sensor_and_multimodal/
    ├── unit_04_unstructured_text_and_vector_rag/
    ├── unit_05_data_as_a_service_and_apis/
    ├── unit_06_agentic_interfaces_and_mcp/
    ├── unit_07_orchestration_and_automation/
    └── unit_08_capstone_defense_and_production/
```

### Per-Unit File Contract (`units/unit_0N_<slug>/`)
Every unit directory contains 7 standardized student-facing files (plus `Dockerfile` in Unit 8):
1. `ds_to_engine.ipynb` — Copied from `content/notebooks/unit_0N_ds_to_engine.ipynb`.
2. `coding_clinic.py` — Extracted and formatted from the "I Do" and "We Do" walkthrough code in `units/unit_0N_<slug>/lab_guide.md` so students can run and experiment with synchronous clinic demos directly from the terminal.
3. `lab{N}_starter.py` — Extracted from `units/unit_0N_<slug>/lab_guide.md` (or `content/labs/lab{N}_starter.py`), with dataset paths pre-aligned to work seamlessly from either the repository root or unit folder.
4. `lab_guide.md` — Adapted from `units/unit_0N_<slug>/lab_guide.md` with sandbox-specific execution tips.
5. `lab_rubric.md` — Extracted 100-point SpeedGrader evaluation rubric table from `lab_guide.md` (matching `CMAP-1815-Student-Sandbox` convention).
6. `study_guide.md` — Copied from `units/unit_0N_<slug>/reading.md` (with internal relative links cleaned for GitHub Markdown viewing).
7. `self_check_drills.md` — Copied from `units/unit_0N_<slug>/drills.md` (with expandable `<details><summary>` self-checks).
8. `Dockerfile` *(Unit 8 only)* — Multi-stage production container starter for the Unit 8 Capstone Defense.

---

## 3. Technical Design Decisions & Cross-References

- **ADR-001 (Accessibility)**: All markdown tables, code blocks, and callouts in `README.md`, `STUDENT_SANDBOX_BUILDER_GUIDE.md`, and unit files use semantic headers and descriptive links.
- **ADR-002 (Spec-Driven Development)**: All files trace directly to `REQ-01` through `REQ-10` in `spec.md`.
- **Path Resolution Resilience in `lab{N}_starter.py`**:
  - Students in Codespaces sometimes run `python units/unit_02_anomaly_detection_engines/lab2_starter.py` from the workspace root `/workspaces/COSC-2060-Student-Sandbox`, and sometimes `cd` into the unit folder first (`python lab2_starter.py`).
  - We will make dataset paths in `generate_fuel_data.py` and `lab2_starter.py` resilient to both working directories (checking `data/fuel_transactions.parquet` and `../../datasets/fuel_transactions.parquet` / `datasets/fuel_transactions.parquet`).
- **Strict Siloing**:
  - `teaching_notes.md` and `quiz.md` from `courses/cosc-2060-data-engineering/units/` are **strictly excluded** from `student_sandbox_template/` so students never see quiz answer keys or instructor solution scripts.

---

## 4. Verification Strategy
1. **Structural Completeness Check**: Automated script verifying all root files and all 8 unit folders (7 files per unit + `Dockerfile` in Unit 8 = 57 unit files + 10 root/config files = 67 files total).
2. **Python Syntax & AST Verification**: Run Python `py_compile` across all `.py` files (`datasets/seed_all_datasets.py`, `datasets/generate_fuel_data.py`, all 8 `coding_clinic.py`, and all 8 `labN_starter.py`).
3. **JSON Schema Validity**: Parse `.devcontainer/devcontainer.json`, `.vscode/extensions.json`, `.vscode/settings.json`, and all 8 `ds_to_engine.ipynb` files with `json.loads()` to guarantee zero JSON syntax errors.
4. **Leakage & Hygiene Audit**: Verify zero `teaching_notes.md`, `quiz.md`, or `file:///c:/` local paths exist anywhere inside `student_sandbox_template/`.

