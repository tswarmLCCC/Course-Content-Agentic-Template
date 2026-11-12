# COSC 2060 Student Sandbox — Builder's & Instructor Deployment Guide

> **Target Repository**: `https://github.com/tswarmLCCC/COSC-2060-Student-Sandbox`  
> **Reference Architecture**: Modeled after [`tswarmLCCC/CMAP-1815-Student-Sandbox`](https://github.com/tswarmLCCC/CMAP-1815-Student-Sandbox)  
> **Assembled Template Path**: [`courses/cosc-2060-data-engineering/student_sandbox_template/`](file:///c:/dev/Course-Content-Agentic-Template/courses/cosc-2060-data-engineering/student_sandbox_template/README.md)

---

## 1. Executive Summary & Architectural Evolution (`CMAP 1815` vs. `COSC 2060`)

In **CMAP 1815 (Introduction to Modern SQL)**, the student sandbox provides a 1-click cloud PostgreSQL 16 server so beginners can write relational queries without installing database daemons locally.

In **COSC 2060 (Modern Data Engineering & AI Infrastructure)**, students progress across an 8-unit multimodal pipeline stack: **DuckDB** (in-process OLAP), **Polars** (1M-row vectorized LazyFrames), **Scikit-Learn** (Isolation Forest), **OpenCV** (letterbox image tensors), **Sentence-Transformers** (384-d dense embeddings), **FastAPI & Pydantic v2** (Data as a Service), **MCP** (Model Context Protocol tool guardrails), **Asset DAGs** (exponential backoff & DLQ), and **Multi-Stage Dockerfiles**.

| Architectural Dimension | `CMAP-1815-Student-Sandbox` (SQL) | `COSC-2060-Student-Sandbox` (Data Eng & AI) | Engineering Rationale for COSC 2060 |
| :--- | :--- | :--- | :--- |
| **Container Topology** | 2-Container `docker-compose.yml` (`workspace` + `postgres:16`) | Single-Container `devcontainer.json` (`mcr.microsoft.com/devcontainers/python:1-3.11-bookworm`) | DuckDB, Polars, and FastAPI `TestClient` run **in-process**. Using the pre-cached official Python 3.11 image with zero custom `features` or `onCreateCommand` blocks guarantees instant spin-up and prevents GitHub Codespaces from ever falling back to the `base:alpine` recovery container. |
| **Database & Storage** | Client-Server `postgres:16` over port `5432` | In-Process `DuckDB` (`apex_logistics.duckdb`) + `Apache Parquet` (`fuel_transactions.parquet`) | Zero network socket overhead; operates directly on Arrow/Parquet memory buffers. |
| **PyTorch / Embedding Footprint** | N/A | CPU-Only PyTorch (`--extra-index-url https://download.pytorch.org/whl/cpu`) | Default `pip install sentence-transformers` on Linux pulls **2.5 GB of NVIDIA CUDA** libraries on CPU-only Codespaces. CPU-only index shrinks the container by ~2 GB and speeds up installation 4x. |
| **Computer Vision Runtime** | N/A | `opencv-python-headless` | Standard `opencv-python` crashes inside headless Linux containers with `ImportError: libGL.so.1: cannot open shared object file`. |
| **Capstone Container Support** | N/A | `ghcr.io/devcontainers/features/docker-in-docker:2` | Allows students to run `docker build` and `docker run` inside their Codespace during the **Unit 8 Capstone Defense**. |
| **Disaster Recovery** | `./reset_database.sh` (runs `psql -f setup_chap1.sql`) | `./reset_sandbox.sh` (runs `python datasets/seed_all_datasets.py` & cleans `output/`) | Regenerates `apex_logistics.duckdb`, 1M fuel rows, synthetic inspection images, and maintenance logs while leaving student `.py` and `.ipynb` files untouched. |
| **Unit Folder Contents** | `.sql` starter, `.sql` lecture code, `.md` guides | `ds_to_engine.ipynb` + `coding_clinic.py` + `labN_starter.py` + `.md` guides | Supports both interactive Jupyter visual transitions ("DS Prototype -> DE Engine") and standalone terminal pipeline execution. |

---

## 2. Complete Sandbox Directory Blueprint

The complete, ready-to-push repository has already been assembled for you at [`courses/cosc-2060-data-engineering/student_sandbox_template/`](file:///c:/dev/Course-Content-Agentic-Template/courses/cosc-2060-data-engineering/student_sandbox_template/).

```text
COSC-2060-Student-Sandbox/
├── .devcontainer/
│   ├── devcontainer.json          # Python 3.11 Bookworm + docker-in-docker + VS Code extensions
│   └── setup_sandbox.sh           # Runs pip install, seeds datasets, & pre-warms MiniLM-L6-v2
├── .github/
│   └── workflows/
│       └── personalize_template.yml # Auto-rewrites README Codespaces badge for student template copies
├── .vscode/
│   ├── extensions.json            # Python, Pylance, Jupyter, Ruff, Rainbow CSV, Parquet Viewer, Docker
│   └── settings.json              # Pre-wires /usr/local/bin/python interpreter & pytest
├── datasets/
│   ├── README.md                  # Student data dictionary for all 4 core datasets
│   ├── seed_all_datasets.py       # Master seeding orchestrator (DuckDB, Parquet, Vision, Logs)
│   └── generate_fuel_data.py      # Vectorized DuckDB generator for 1,000,000 fuel rows (< 5 sec)
├── .gitattributes                 # Enforces LF line endings on *.sh and Dockerfile across Windows/Linux
├── .gitignore                     # Excludes generated *.parquet, *.duckdb, and output/ from git status
├── requirements.txt               # CPU-optimized PyTorch + headless OpenCV + DuckDB/Polars/FastAPI
├── reset_sandbox.sh               # 1-command disaster recovery script
├── README.md                      # Student-facing 1-Click Codespaces badge & workflow guide
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

### Standard 7-File Contract Inside Every `units/unit_0N_.../` Folder
1. **`ds_to_engine.ipynb`**: Interactive Jupyter Notebook demonstrating the architectural shift from a fragile Data Science script to a production Data Engineering engine.
2. **`coding_clinic.py`**: Standalone runnable Python script containing the synchronous class "I Do" and "We Do" demonstrations.
3. **`lab{N}_starter.py`**: Pre-scaffolded Python starter template with built-in mock data and `assert` verification tests.
4. **`lab_guide.md`**: Complete business scenario, technical specifications, and submission instructions.
5. **`lab_rubric.md`**: Extracted 100-point grading rubric matching Canvas SpeedGrader.
6. **`study_guide.md`**: Full OER reading chapter and architectural reference.
7. **`self_check_drills.md`**: Formative diagnostic questions and code execution traces with expandable `<details>` answer keys.
8. **`Dockerfile`** *(Unit 8 only)*: Multi-stage container starter for the Capstone Defense.

> [!IMPORTANT]
> **Strict Student Siloing**: Instructor-only files (`teaching_notes.md` and `quiz.md`) are **never** copied into `student_sandbox_template/`.

---

## 3. Step-by-Step Guide: Publishing to `tswarmLCCC/COSC-2060-Student-Sandbox`

Follow these steps to publish the assembled template folder as a standalone GitHub Template Repository.

### Step 1: Create the Empty Repository on GitHub
1. Navigate to [https://github.com/new](https://github.com/new) (signed into your `tswarmLCCC` account).
2. Set **Repository name** to: `COSC-2060-Student-Sandbox`
3. Set **Description** to: `COSC 2060: Modern Data Engineering & AI Infrastructure — 1-Click GitHub Codespaces Student Lab Sandbox (DuckDB, Polars, OpenCV, RAG, FastAPI, MCP)`
4. Select **Public** (required for free student Codespaces launch badges and LCCC classroom access).
5. Leave **Add a README file**, **.gitignore**, and **license** **UNCHECKED** (our template folder already includes all of them).
6. Click **Create repository**.

### Step 2: Initialize and Push `student_sandbox_template/`
Open PowerShell on your workstation and run the following commands to push the assembled sandbox directory to your new GitHub repository:

```powershell
# 1. Navigate into the assembled sandbox directory
cd "c:\dev\Course-Content-Agentic-Template\courses\cosc-2060-data-engineering\student_sandbox_template"

# 2. Initialize a fresh Git repository on branch 'main'
git init -b main

# 3. Stage all 67 sandbox files (respecting .gitattributes LF line endings)
git add .

# 4. Create the initial commit
git commit -m "Initial release: COSC 2060 Student Lab Sandbox (Units 1-8, Devcontainer, Datasets)"

# 5. Connect to your GitHub remote and push
git remote add origin https://github.com/tswarmLCCC/COSC-2060-Student-Sandbox.git
git push -u origin main
```

*(Note: After pushing, you can remove the nested `.git` folder inside `student_sandbox_template` via `Remove-Item -Recurse -Force .git` so the parent monorepo continues tracking the template files cleanly.)*

### Step 3: Enable "Template Repository" Mode on GitHub
Just like `CMAP-1815-Student-Sandbox`, marking the repository as a **Template** allows students to click **"Use this template"** or launch a clean personal Codespace:
1. Go to `https://github.com/tswarmLCCC/COSC-2060-Student-Sandbox/settings`.
2. Under the **General** tab, right below the repository name, check the box labeled **☑️ Template repository**.

---

## 4. Configuring GitHub Codespaces Prebuilds (Highly Recommended)

Because COSC 2060 installs `duckdb`, `polars`, `scikit-learn`, `opencv-python-headless`, `torch` (CPU), `sentence-transformers`, `fastapi`, and seeds 1,000,000 Parquet rows + caches the `all-MiniLM-L6-v2` model, a cold build takes ~90–120 seconds.

By enabling **Codespaces Prebuilds**, GitHub runs `.devcontainer/setup_sandbox.sh` ahead of time whenever you push to `main`, snapshot-caching the container so **student Codespaces boot in under 15 seconds**:

1. Open `https://github.com/tswarmLCCC/COSC-2060-Student-Sandbox/settings/codespaces`.
2. Under **Prebuild configuration**, click **Set up prebuild**.
3. Select branch: **`main`**.
4. Select region: **US West** (or leave as all regions).
5. Click **Create**.

---

## 5. How the Template Repo & Auto-Personalizing Badge Work in Canvas

### Why Hardcoded Codespaces Badges Fail on Template Repositories
If a student creates their own repository (`<student-username>/COSC-2060-Student-Sandbox`) from a template repository, a static badge pointing to `https://codespaces.new/tswarmLCCC/COSC-2060-Student-Sandbox` would launch a Codespace attached to **your upstream instructor repo** instead of the student's new repository.

### Our 2-Part Solution Built into `student_sandbox_template/`
1. **2-Step Student Onboarding in `README.md`**:
   - **Step 1** provides a 1-Click **"Create Your Personal Sandbox Repo"** button pointing to GitHub's template instantiation endpoint:
     ```markdown
     [![Use This Template](https://img.shields.io/badge/Step_1-Create_Your_Personal_Sandbox_Repo-2ea44f?style=for-the-badge&logo=github)](https://github.com/new?template_owner=tswarmLCCC&template_name=COSC-2060-Student-Sandbox&owner=%40me&name=COSC-2060-Student-Sandbox&description=My+COSC+2060+Data+Engineering+Sandbox&visibility=private)
     ```
   - **Step 2** shows students both how to launch via the green **`<> Code` -> `Codespaces` -> `Create codespace on main`** button on their new repo AND via their auto-personalized badge.
2. **Automated Badge Rewrite Action (`.github/workflows/personalize_template.yml`)**:
   - The moment a student creates their repository from your template, GitHub Actions runs `.github/workflows/personalize_template.yml` (guarded by `if: github.repository != 'tswarmLCCC/COSC-2060-Student-Sandbox'` so it **never** alters your upstream template).
   - Within ~15 seconds, the Action replaces `tswarmLCCC/COSC-2060-Student-Sandbox` with `${GITHUB_REPOSITORY}` (`<student-username>/COSC-2060-Student-Sandbox`) inside the student's `README.md` and adds a green confirmation banner (`✅ Personal Sandbox Initialized for <student-username>/COSC-2060-Student-Sandbox!`).

### What Link to Put in Canvas LMS
In your **Canvas Course Orientation** page, embed the **Step 1 Template Generator Link** (or link directly to `https://github.com/tswarmLCCC/COSC-2060-Student-Sandbox` where students follow Step 1 & Step 2):
```markdown
[![Create Your COSC 2060 Sandbox Repo](https://img.shields.io/badge/Step_1-Create_Your_COSC_2060_Sandbox_Repo-2ea44f?style=for-the-badge&logo=github)](https://github.com/new?template_owner=tswarmLCCC&template_name=COSC-2060-Student-Sandbox&owner=%40me&name=COSC-2060-Student-Sandbox&description=My+COSC+2060+Data+Engineering+Sandbox&visibility=private)
```

### 3. Student Submission Workflow
Because each student works inside their own repository (`<student-username>/COSC-2060-Student-Sandbox`), they have full write permissions to `git commit` and `git push` their work, and can also download `lab{N}_{lastname}.py` from the VS Code Explorer sidebar (**Right-click -> Download...**) to upload directly to Canvas SpeedGrader.

---

## 6. Instructor Maintenance & Troubleshooting Playbook

### Updating a Lab Starter or Dataset Mid-Semester
If you update any course file inside `courses/cosc-2060-data-engineering/units/`, you can re-synchronize the `student_sandbox_template/` folder at any time and push the update to `tswarmLCCC/COSC-2060-Student-Sandbox`. Students who already launched a Codespace can pull updates via:
```bash
git pull origin main
./reset_sandbox.sh
```

### Common Troubleshooting Checks
1. **`./reset_sandbox.sh: /bin/bash^M: bad interpreter`**:
   - **Cause**: Windows Git converted `.sh` files from `LF` to `CRLF` on checkout.
   - **Prevention Built-In**: We included [`.gitattributes`](file:///c:/dev/Course-Content-Agentic-Template/courses/cosc-2060-data-engineering/student_sandbox_template/.gitattributes) with `*.sh text eol=lf`, ensuring Git always stores and checks out `.sh` files with Unix `LF` line endings.
2. **`FileNotFoundError: Missing data/fuel_transactions.parquet` in Unit 2**:
   - **Prevention Built-In**: Both `datasets/seed_all_datasets.py` and `units/unit_02_anomaly_detection_engines/lab2_starter.py` automatically resolve `fuel_transactions.parquet` whether the student runs the script from the workspace root (`/workspaces/COSC-2060-Student-Sandbox`) or after running `cd units/unit_02_anomaly_detection_engines`.
3. **Why We Avoid `features` (`docker-in-docker`) and `onCreateCommand` (`apt-get update`) in `devcontainer.json`**:
   - In GitHub Codespaces, if any Devcontainer Feature (like `docker-in-docker`) or blocking `onCreateCommand` exits with a non-zero status code during container creation, Codespaces aborts the build and drops the user into **`mcr.microsoft.com/devcontainers/base:alpine` (Recovery Mode)** — which lacks `apt-get`, `pip`, and `/usr/local/python`.
   - Keeping `.devcontainer/devcontainer.json` strictly on the pre-cached `mcr.microsoft.com/devcontainers/python:1-3.11-bookworm` image with `postCreateCommand: "bash .devcontainer/setup_sandbox.sh"` guarantees 100% reliable container startup. For Unit 8, `lab8_starter.py` validates the multi-stage `Dockerfile` and executes the blind evaluation batch directly in Python.

