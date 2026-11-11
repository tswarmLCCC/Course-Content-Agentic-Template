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
| **Container Topology** | 2-Container `docker-compose.yml` (`workspace` + `postgres:16`) | Single-Container `devcontainer.json` (`python:1-3.11-bookworm` + `docker-in-docker`) | DuckDB, Polars, and FastAPI `TestClient` run **in-process**. Eliminating the second container saves ~400 MB RAM for 1M-row Polars & embedding models and halves Codespace boot time. |
| **Database & Storage** | Client-Server `postgres:16` over port `5432` | In-Process `DuckDB` (`apex_logistics.duckdb`) + `Apache Parquet` (`fuel_transactions.parquet`) | Zero network socket overhead; operates directly on Arrow/Parquet memory buffers. |
| **PyTorch / Embedding Footprint** | N/A | CPU-Only PyTorch (`--extra-index-url https://download.pytorch.org/whl/cpu`) | Default `pip install sentence-transformers` on Linux pulls **2.5 GB of NVIDIA CUDA** libraries on CPU-only Codespaces. CPU-only index shrinks the container by ~2 GB and speeds up installation 4x. |
| **Computer Vision Runtime** | N/A | `opencv-python-headless` | Standard `opencv-python` crashes inside headless Linux containers with `ImportError: libGL.so.1: cannot open shared object file`. |
| **Capstone Container Support** | N/A | `ghcr.io/devcontainers/features/docker-in-docker:2` | Allows students to run `docker build` and `docker run` inside their Codespace during the **Unit 8 Capstone Defense**. |
| **Disaster Recovery** | `./reset_database.sh` (runs `psql -f setup_chap1.sql`) | `./reset_sandbox.sh` (runs `python datasets/seed_all_datasets.py` & cleans `output/`) | Regenerates `apex_logistics.duckdb`, 1M fuel rows, synthetic inspection images, and maintenance logs while leaving student `.py` and `.ipynb` files untouched. |
| **Unit Folder Contents** | `.sql` starter, `.sql` lecture code, `.md` guides | `ds_to_engine.ipynb` + `coding_clinic.py` + `labN_starter.py` + `.md` guides | Supports both interactive Jupyter visual transitions ("DS Prototype $\rightarrow$ DE Engine") and standalone terminal pipeline execution. |

---

## 2. Complete Sandbox Directory Blueprint

The complete, ready-to-push repository has already been assembled for you at [`courses/cosc-2060-data-engineering/student_sandbox_template/`](file:///c:/dev/Course-Content-Agentic-Template/courses/cosc-2060-data-engineering/student_sandbox_template/).

```text
COSC-2060-Student-Sandbox/
├── .devcontainer/
│   ├── devcontainer.json          # Python 3.11 Bookworm + docker-in-docker + VS Code extensions
│   └── setup_sandbox.sh           # Runs pip install, seeds datasets, & pre-warms MiniLM-L6-v2
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

## 5. Embedding the Sandbox in Canvas LMS

### 1. The 1-Click Launch URL
Use this exact URL in your Canvas Course Orientation page and weekly Lab Assignment descriptions:
```markdown
[![Open in GitHub Codespaces](https://github.com/codespaces/badge.svg)](https://codespaces.new/tswarmLCCC/COSC-2060-Student-Sandbox?quickstart=1)
```
* Note the `?quickstart=1` query parameter: it allows students to resume an existing Codespace in 1 click if they already launched one in an earlier week, preventing duplicate container sprawl!

### 2. Student Submission Workflow
Students never need to configure `git push` credentials or SSH keys to submit their work:
1. They edit `units/unit_0N_.../lab{N}_starter.py` directly in their browser Codespace.
2. They run `python lab{N}_starter.py` in the integrated terminal until all defensive `assert` checks print `PASS`.
3. They rename or save a copy as `lab{N}_{lastname}.py`, right-click the file in the VS Code Explorer sidebar, click **Download...**, and upload the `.py` file to Canvas SpeedGrader.

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
3. **Testing Unit 8 `Dockerfile` Inside Codespaces**:
   - Because `.devcontainer/devcontainer.json` includes `"ghcr.io/devcontainers/features/docker-in-docker:2"`, the `docker` daemon runs automatically inside the student's Codespace. Students can verify their Unit 8 Capstone container via:
     ```bash
     cd units/unit_08_capstone_defense_and_production
     docker build -t apex-capstone:v1 .
     docker run --rm apex-capstone:v1
     ```

