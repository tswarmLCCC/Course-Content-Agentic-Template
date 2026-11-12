# Spec 009: Bottom-Up Pedagogical Scaffolding, Syllabus Alignment & Lab Onboarding

- **Course**: `COSC 2060: Modern Data Engineering & AI Infrastructure`
- **Target Silo**: `courses/cosc-2060-data-engineering/`
- **Iteration**: `009-pedagogical-scaffolding-and-syllabus-alignment`
- **Stage**: Stage 1 — Specify
- **Date**: 2026-11-12

---

## 1. Problem Statement & Pedagogical Context

Following a comprehensive instructor review of `COSC 2060` (`revewNotes.txt`) with a beginner student learner mindset (students entering from **CMAP 1815: Relational Databases** and introductory Python, *without* prior machine learning coursework), five critical pedagogical and structural gaps were identified:

1. **Syllabus Location, Formatting & Institutional `.docx` Fidelity**:
   - The Canvas Syllabus page (`course_settings/syllabus.html` and `course-orientation-and-syllabus.html`) does not match the `CMAP 1815` DesignPLUS multi-panel layout and navigation structure.
   - The downloadable Word syllabus (`COSC_2060_Master_Syllabus.docx`) was generated as a minimal stripped XML document rather than cloned from the institutional `specs/_templates/syllabi/LCCC_Master_Syllabus_Template.docx` using the `syllabus-docx-cloner` workflow.
2. **Missing "Getting Started with the Lab" & "The Shapes of AI Data" Onboarding Pages**:
   - Now that the `COSC-2060-Student-Sandbox` template repository (`https://github.com/tswarmLCCC/COSC-2060-Student-Sandbox`) is live, students need a dedicated **"Getting Started with the Lab Environment (GitHub Codespaces Sandbox)"** page in the Orientation Module (and linked in Unit 1) walking them step-by-step from clicking *"Use this template"* to running their first query and notebook cell.
   - The visual reference guide **"The Shapes of AI Data: A Companion Guide for Data Engineers"** (`docs/data_engineering_page_ai_data_shapes_guide.html`) needs to be integrated into the **Getting Started - Course Orientation** module so students understand the target data structures across all 8 units from Day 1.
3. **Unit 1 Reading Jumps into the Middle & Contains LaTeX/Assumed-Knowledge Typos**:
   - Unit 1's reading currently assumes prior ML coursework (*"In your introductory machine learning coursework, you were provided a clean, static, single-table flat CSV file..."*) and contains unrendered raw LaTeX tokens (`$X$`, `$y$`, `$\mu$`, `$\sigma$`) that display as literal dollar signs in Canvas HTML.
   - While the narrative and `ASOF JOIN` sections in Unit 1 are strong and must be preserved, the reading jumps straight from the opening paragraph into **temporal data leakage** before ever teaching students:
     - What **Target Data Shape** we are building and why downstream systems require it.
     - What **Source Systems** produce the raw operational data.
     - What **Feature Engineering** is and how to build basic features from SQL (`SELECT`, arithmetic ratios, `CASE WHEN` flags, `JOIN`s, `GROUP BY` aggregations) from the ground up.
     - What **Supervised Learning** (`X` input features predicting a target `y`) is, *before* introducing how temporal joins can leak future information and how `ASOF JOIN` solves it.
4. **Course-Wide Target Output Format & Source Systems Grounding (Units 1–8)**:
   - Every unit (Units 1–8) must open its conceptual deep dive by explicitly defining:
     1. **The Target Output Format & Why We Use It** (with a concrete visual schema/sample table showing the exact shape being built).
     2. **The Operational Source Systems** (where the raw data originates in the real world and why it cannot be fed directly to downstream consumers).
5. **Bottom-Up Code & Syntax Ramp-Up (Readings, Coding Clinics, Notebooks & Labs across Units 1–8)**:
   - Currently, code examples in the readings and labs start at an intermediate/advanced level without first teaching the foundational library calls and syntax patterns from scratch.
   - Every unit must include a **"Foundational Syntax & Code Ramp-Up"** section in Chapter 1 of the Reading (modeled after `CMAP 1815`'s Section 4 *Implementation* and Section 5 *Student Exercises: Live Practice*) AND a **"Part 0: Basics Warm-Up"** in the unit's Lab Guide, `coding_clinic.py`, and `labN_starter.py` so students build confidence step-by-step before tackling the core defensive engineering challenge.
6. **Eliminating "AI-Speak" & Cliché Two-Part Colon Headings**:
   - Throughout the readings, companion guides, overviews, and lab guides, headings and prose currently overuse the formulaic AI cliché of dramatic two-part titles separated by a colon (e.g., *"The Shapes of AI Data: A Companion Guide for Data Engineers"*, *"Asking Questions of Temporal Data: Relational Foundations for AI"*, *"The Narrative of Data: Why the $10M Delivery Model Failed"*, *"The Physical Mental Model: Row Filing vs. Columnar Straws"*), alongside melodramatic AI buzzwords (*"cardinal sin"*, *"ruthlessly exploit"*, *"catastrophic"*, *"paradigm shift"*, *"delve"*).
   - All headings and prose across the course must be rewritten in natural, direct, human-instructor language without the repetitive `Title: Dramatic Subtitle` pattern.

---

## 2. Target Audience

- **Primary Learners**: Community college sophomores (`LCCC`) who have completed introductory SQL (`CMAP 1815`) and introductory Python, with **zero prior Machine Learning, DuckDB, Polars, OpenCV, ChromaDB, FastAPI, MCP, Dagster, or Docker experience**.
- **Instructors**: Faculty importing `COSC_2060_Complete.imscc` into Canvas LMS and using `COSC-2060-Student-Sandbox` in GitHub Codespaces.

---

## 3. EARS Requirements

### 3.1 Syllabus Formatting, Placement & Institutional `.docx` Cloning (`CMAP 1815` Alignment)
- **REQ-001 (Ubiquitous — Always)**: The course build pipeline shall generate `COSC_2060_Master_Syllabus.docx` by cloning `specs/_templates/syllabi/LCCC_Master_Syllabus_Template.docx` (preserving 100% of LCCC institutional XML styles, customXml, table borders, and college policy sections) and populating it with `COSC 2060` metadata, outcomes, grading breakdown, and 16-week schedule.
- **REQ-002 (Ubiquitous — Always)**: Both `course_settings/syllabus.html` (the native Canvas Syllabus tab linked from the Home Page *"Syllabus & Policies"* button) and `wiki_content/course-orientation-and-syllabus.html` (in the Orientation module) shall render the complete `syllabus.md` content formatted in `CMAP 1815` DesignPLUS style (banner ribbon, prominent `.docx` download callout box, and full structured sections for Course Info, Zero-Cost Stack, Learning Outcomes, Weighted Grading Table, 16-Week Schedule Table, and Institutional Policies).

### 3.2 Orientation Module: "Getting Started with the Lab" & "The Shapes of AI Data"
- **REQ-003 (Ubiquitous — Always)**: The `Getting Started - Course Orientation` module shall include a dedicated native WikiPage titled **`Getting Started with the Lab Environment`** (`getting-started-lab-sandbox.html`) that provides beginner-friendly, step-by-step instructions for:
  1. Creating a private personal repository from `https://github.com/tswarmLCCC/COSC-2060-Student-Sandbox` via *"Use this template"*.
  2. Launching GitHub Codespaces and verifying the pre-built Python 3.11 + DuckDB + Polars environment.
  3. Navigating the workspace directory (`datasets/`, `units/unit_01_...` through `unit_08_...`).
  4. Using the 4 learning files in every unit (`study_guide.md`, `ds_to_engine.ipynb`, `coding_clinic.py`, and `labN_starter.py`), executing code in both the VS Code terminal and Jupyter Notebook UI, and using `bash reset_sandbox.sh`.
- **REQ-004 (Ubiquitous — Always)**: The `Getting Started - Course Orientation` module shall include a native WikiPage titled **`Common AI Data Shapes`** (`ai-data-shapes-guide.html`) adapted from `docs/data_engineering_page_ai_data_shapes_guide.html` (with all raw LaTeX notation converted to clean HTML tags and all two-part colon AI headers replaced with natural human headings).
- **REQ-005 (When — Event)**: When a student views `Unit 01 Overview` or `Unit 01: Applied Lab Guide`, the page shall include a direct callout and link to the `Getting Started with the Lab Environment` orientation guide.

### 3.3 Unit 1 Reading Refactoring, Anti-AI-Speak & LaTeX/Typo Eradication
- **REQ-006 (Ubiquitous — Always)**: All reading, study guide, drill, and lab files across Units 1–8 (`units/`, `content/`, and `student_sandbox_template/`) shall contain **zero** raw LaTeX dollar-sign math tokens (e.g., `$X$`, `$y$`, `$\mu$`, `$\sigma$`, `$10M` collisions) that fail to render in Canvas WikiPages; all mathematical variables and formulas shall use clean semantic HTML (`<i>X</i>`, `<i>y</i>`, `<sub>`, `&mu;`, `&sigma;`, `&times;`).
- **REQ-006B (Ubiquitous — Always)**: All headings, subheadings, and prose across Units 1–8, Orientation pages, and `student_sandbox_template/` shall eliminate AI-cliché phrasing and the formulaic two-part colon header pattern (`"Dramatic Hook: Technical Subtitle"`), using direct, conversational, human-instructor headings instead (e.g., *"What Our Output Table Looks Like"*, *"Where the Raw Data Comes From"*, *"Building Features in SQL"*, *"How a Bad Join Ruined a Delivery Model"*, *"Row Databases vs. Columnar Databases"*, *"Writing Queries in DuckDB"*).
- **REQ-007 (Ubiquitous — Always)**: Unit 1's reading (`units/unit_01_relational_foundations/reading.md`, `content/readings/unit_01_relational_foundation.md`, and `student_sandbox_template/units/unit_01_relational_foundations/study_guide.md`) shall remove any assumption of prior machine learning coursework and instead explicitly bridge from students' `CMAP 1815` SQL & introductory Python background.
- **REQ-008 (Ubiquitous — Always)**: Unit 1's Chapter 1 (`1. Instructor Lecture & Conceptual Deep Dive`) shall be structured from the bottom up in the following sequence using natural, human-written section headers before introducing data leakage and `ASOF JOIN`, while preserving all existing high-value content (the delivery delay failure story, the Filing Cabinet vs. Drinking Straw OLTP/OLAP mental model, and `ASOF JOIN` progression):
  1. **Moving from Database Reports to AI Datasets**: How operational SQL (`CMAP 1815`) differs from building datasets for analytics and machine learning.
  2. **The Target Data Shape and Source Systems**: What a flat feature matrix looks like (concrete table of `routes` + `drivers` + `weather` features mapped to a target column `is_delayed`), why downstream models need one flat table instead of separate normalized tables, and what source systems generate this data.
  3. **Building Features in SQL from the Ground Up**: Step-by-step guide showing what a "feature" is and how to build features using familiar SQL (`SELECT` math expressions, `CASE WHEN` flags, `LEFT JOIN` across tables, and basic `GROUP BY` / window aggregations).
  4. **How Supervised Learning Uses Features and Targets**: Plain-English explanation of how a model uses input columns (`X`) to predict a target column (`y`), setting up the delivery model failure story.
  5. **How Future Data Leaks into Training Tables**: Preserving the Chicago blizzard timeline and showing why joining on calendar dates (`dep_time::DATE = obs_time::DATE`) accidentally leaks evening weather into morning departures.
  6. **Row Databases vs. Columnar Databases**: Preserving the PostgreSQL filing cabinet vs. DuckDB drinking straw comparison.
  7. **Working with DuckDB, Rolling Windows, and ASOF JOIN**: Step-by-step code walkthrough starting from `import duckdb` and basic queries, then rolling lookback windows (`1 PRECEDING`), and finally `ASOF JOIN`.
  8. **Practice Exercises and Common Questions**: Hands-on sandbox tasks and beginner Q&A modeled after `CMAP 1815`.

### 3.4 Course-Wide Bottom-Up Scaffolding (Units 1–8 Readings, Labs, Clinics & Notebooks)
- **REQ-009 (Ubiquitous — Always)**: Every unit's reading (`Units 1–8`) shall include:
  - A **Target Output Format & Source Systems** section at the beginning of Chapter 1 showing the exact data structure being built in that unit, why that format is used, and what real-world source systems feed it.
  - A **Foundational Syntax & Code Ramp-Up** section in Chapter 1 that introduces every library function, SQL clause, or Python API used in that unit from the ground up with simple, annotated, minimal examples before combining them into full pipelines.
  - A **Live Sandbox Practice & Common Pitfalls (FAQ)** section at the end of Chapter 1 matching the `CMAP 1815` reading pattern.
- **REQ-010 (Ubiquitous — Always)**: Every unit's `lab_guide.md`, `coding_clinic.py`, and `labN_starter.py` (in both `courses/cosc-2060-data-engineering/` and `student_sandbox_template/`) shall begin with a beginner-friendly **"Part 0 / Step 0: Basics Warm-Up"** task that verifies the student can connect to the unit's tool/dataset, inspect the schema/sample records, and execute a single foundational operation before progressing to Part 1 ("I Do" / Guided), Part 2 ("We Do" / Defensive), and Part 3 ("You Do" / Production Deliverable).
- **REQ-011 (When — Event)**: When all updates are completed across `courses/cosc-2060-data-engineering/` and `student_sandbox_template/`, the build pipeline shall push the updated sandbox files to `https://github.com/tswarmLCCC/COSC-2060-Student-Sandbox.git` and recompile `COSC_2060_Complete.imscc` with zero XML errors and zero broken links.

---

## 4. Out of Scope

- Changing the 8 unit topics, gradebook category weights (Labs 40%, Quizzes 20%, Drills 10%, Capstone 30%), or replacing the core open-source technology stack (DuckDB, Polars, OpenCV, ChromaDB, FastAPI, MCP, Dagster, Docker).
- Modifying any files outside `courses/cosc-2060-data-engineering/`, `.agents/skills/canvas-course-builder/`, `CURRENT.md`, and `README.md`.

