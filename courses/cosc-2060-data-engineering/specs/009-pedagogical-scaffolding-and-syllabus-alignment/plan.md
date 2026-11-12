# Implementation Plan 009: Bottom-Up Pedagogical Scaffolding, Syllabus Alignment & Lab Onboarding

- **Course**: `COSC 2060: Modern Data Engineering & AI Infrastructure`
- **Target Silo**: `courses/cosc-2060-data-engineering/`
- **Spec Reference**: [`spec.md`](file:///c:/dev/Course-Content-Agentic-Template/courses/cosc-2060-data-engineering/specs/009-pedagogical-scaffolding-and-syllabus-alignment/spec.md)
- **Stage**: Stage 2 — Plan
- **Date**: 2026-11-12

---

## 1. Architectural Alignment & ADR Cross-Reference

- **ADR-001 (Accessibility)**: All new and refactored HTML/Markdown pages (`syllabus.html`, `getting-started-lab-sandbox.html`, `ai-data-shapes-guide.html`, and Unit 1–8 readings/labs) use semantic headings, accessible zebra-striped HTML tables with high-contrast `#1e3a8a` headers, and clean HTML math notation (`<i>X</i>`, `<i>y</i>`, `<sub>`, `&mu;`, `&sigma;`) instead of raw unrendered LaTeX `$X$`.
- **ADR-002 (Spec-Driven Development)**: Every file change maps 1-to-1 to `REQ-001` through `REQ-011` (including `REQ-006B` eliminating AI-speak and two-part colon headers).
- **ADR-003 (Canvas Cartridge & DesignPLUS Theme Invariants)**:
  - All native WikiPages include the mandatory `<head>` metadata contract (`identifier`, `editing_roles`, `workflow_state`, `editor_type="rce"`).
  - Module titles remain strictly hyphenated (`Unit 01 - Relational Foundations`).
  - Selective ribbon policy: DesignPLUS banner ribbons (`render_designplus_html`) on Front Page, Orientation pages, Syllabus, and Unit Overviews/Readings (4-panel layout matching `ref/unit_reading_example.html`).

---

## 2. Component Design & File Layout

### 2.1 Institutional Syllabus Cloning & DesignPLUS Syllabus Page (`REQ-001`, `REQ-002`)
1. **LCCC Master Word Syllabus Cloner (`scripts/docx_syllabus.py` / `build_course.py`)**:
   - Enhance `.agents/skills/canvas-course-builder/scripts/docx_syllabus.py` so that when `specs/_templates/syllabi/LCCC_Master_Syllabus_Template.docx` exists, it clones the official LCCC `.docx` archive (preserving all Word styles, customXml, headers/footers, and institutional policy tables) and injects the `COSC 2060` course metadata, description, outcomes, grading weights, and 16-week schedule into `word/document.xml`.
2. **DesignPLUS Syllabus Page (`course_settings/syllabus.html` & `wiki_content/course-orientation-and-syllabus.html`)**:
   - Update `courses/cosc-2060-data-engineering/syllabus.md` with comprehensive, human-written LCCC syllabus sections.
   - Update `build_course.py` so both `course_settings/syllabus.html` and `course-orientation-and-syllabus.html` render the complete `syllabus.md` sections inside clean DesignPLUS panels alongside the prominent `.docx` download link.

### 2.2 New Orientation Pages (`REQ-003`, `REQ-004`, `REQ-005`)
1. **`Getting Started with the Lab Environment` (`getting-started-lab-sandbox.html`)**:
   - Added as Item 2 in `Getting Started - Course Orientation` module (and linked at the top of `Unit 01 Overview` and `Unit 01: Applied Lab Guide`).
   - Contains 5 clear, human-written sections:
     1. *Creating Your Personal Sandbox Repository on GitHub* (2-step *"Use this template"* guide for `https://github.com/tswarmLCCC/COSC-2060-Student-Sandbox`)
     2. *Launching Your Cloud Workstation in GitHub Codespaces*
     3. *Finding Your Files in VS Code* (`datasets/`, `units/unit_01_...` through `unit_08_...`)
     4. *How Each Unit Works* (`study_guide.md`, `ds_to_engine.ipynb`, `coding_clinic.py`, and `labN_starter.py`)
     5. *Running Code, Submitting Labs, and Resetting Your Sandbox* (`bash reset_sandbox.sh`)
2. **`Common AI Data Shapes` (`ai-data-shapes-guide.html`)**:
   - Added to `Getting Started - Course Orientation` module.
   - Adapted from `docs/data_engineering_page_ai_data_shapes_guide.html` with:
     - All raw LaTeX (`\[x_{\text{scaled}} = \frac{x - \mu}{\sigma}\]`, `\( \dots \)`) converted to clean HTML math.
     - All AI-cliché two-part colon headings converted to natural human headers (e.g., *"Common AI Data Shapes"*, *"1. Tabular Feature Matrices for Supervised Learning"*, *"2. Scaled Feature Tables for Unsupervised Clustering"*, etc.).

### 2.3 Anti-AI-Speak & Natural Human Headers (`REQ-006`, `REQ-006B`)
- Audit all headings and prose across Units 1–8 (`overview.md`, `reading.md`, `study_guide.md`, `lab_guide.md`, `learn_with_ai.md`, `teaching_notes.md`) and replace formulaic `Hook: Subtitle` headers and AI buzzwords (*"cardinal sin"*, *"ruthlessly exploit"*, *"catastrophic"*, *"delve"*, *"unsleeping pipeline"*, *"death of the CSV"*) with direct, clear instructor headings and grounded explanations.
- Eradicate all raw `$X$`, `$y$`, `$\mu$`, `$\sigma$` tokens across all markdown and notebook files.

### 2.4 Unit 1 Bottom-Up Reading Refactor (`REQ-007`, `REQ-008`)
Refactor `units/unit_01_relational_foundations/reading.md`, `content/readings/unit_01_relational_foundation.md`, and `student_sandbox_template/units/unit_01_relational_foundations/study_guide.md` so Chapter 1 follows this 8-part bottom-up progression:
1. **Moving from Database Reports to AI Datasets**: Bridging from `CMAP 1815` SQL reports to analytical feature tables (zero assumed ML coursework).
2. **What Our Output Table Looks Like and Where the Data Comes From**: Concrete 6-row example of the flat feature table we are building (`route_id`, `distance_miles`, `driver_years_exp`, `rolling_3_route_delay`, `temp_f`, `precip_in`, and target `is_delayed`), why downstream models need one flat table instead of normalized tables, and the three operational source systems (`drivers` HR table, `routes` dispatch table, `weather` NOAA sensor log).
3. **Building Features in SQL from the Ground Up**: Step-by-step SQL tutorial starting with basic `SELECT` arithmetic (`delay_per_mile`), `CASE WHEN` indicator flags (`is_long_haul`, `is_delayed`), `LEFT JOIN` to combine `routes` and `drivers`, and basic `GROUP BY` / `OVER (PARTITION BY driver_id)` historical averages.
4. **How Supervised Learning Uses Features and Targets**: Plain-English introduction to input features (`X`) and target labels (`y`), explaining how a model learns from past trips and why every feature must only use information available *before* the truck leaves.
5. **How Future Data Leaks into Training Tables**: The Chicago blizzard story (7:15 AM departure vs. 5:30 PM blizzard) showing how a standard date join (`dep_time::DATE = obs_time::DATE`) accidentally leaks the future into historical rows.
6. **How Row and Column Databases Store Data**: Preserving the PostgreSQL filing cabinet vs. DuckDB drinking straw comparison.
7. **Working with DuckDB, Rolling Windows, and ASOF JOIN**: Step-by-step code ramp-up from `import duckdb` and querying Parquet files to lagged window frames (`ROWS BETWEEN 3 PRECEDING AND 1 PRECEDING`) and DuckDB's `ASOF JOIN`.
8. **Practice Exercises and Common Questions**: Hands-on sandbox tasks and beginner FAQ matching `CMAP 1815` (`ref/unit_reading_example.html`).

### 2.5 Course-Wide Bottom-Up Reading & Code Ramp-Up (`Units 2–8`, `REQ-009`, `REQ-010`)
1. **Units 2–8 Readings (`units/unit_02..08/reading.md`, `content/readings/unit_02..08.md`, `student_sandbox_template/units/unit_02..08/study_guide.md`)**:
   - Add **What Our Output Looks Like and Where the Data Comes From** (target format + sample output + source systems) at the start of Chapter 1 in every unit.
   - Add **Step-by-Step Code Ramp-Up** in Chapter 1 teaching the unit's library from line 1 (e.g., Polars `pl.read_parquet` & `.select()` in Unit 2; OpenCV `cv2.imread` & image shapes in Unit 3; token chunking & ChromaDB basics in Unit 4; `@app.get` & `BaseModel` in Unit 5; Python tool functions & `@mcp.tool()` in Unit 6; `@asset` functions in Unit 7; `Dockerfile` instructions in Unit 8).
   - Add **Practice Exercises and Common Questions** at the end of Chapter 1 in every unit.
2. **Units 1–8 Lab Guides, Coding Clinics & Starters (`REQ-010`)**:
   - Add **Part 0: Basics Warm-Up** to `lab_guide.md`, `coding_clinic.py`, and `labN_starter.py` across Units 1–8 so every lab starts with a simple, confidence-building warm-up before the main engineering tasks.

---

## 3. Verification Strategy

1. **Automated Content & Anti-Pattern Audit**:
   - Verify zero occurrences of raw `$X$`, `$y$`, `$\mu$`, `$\sigma$`, or `introductory machine learning coursework` across all files.
   - Verify all 8 unit readings contain the bottom-up sections (Target Format & Source Systems, Foundational Code Ramp-Up, Practice Exercises & FAQ).
   - Verify all 8 `lab_guide.md`, `coding_clinic.py`, and `labN_starter.py` files include `Part 0: Basics Warm-Up` and pass `python -m py_compile`.
2. **Cartridge & Sandbox Sync**:
   - Push all updated files in `student_sandbox_template/` to `https://github.com/tswarmLCCC/COSC-2060-Student-Sandbox.git`.
   - Run `build_course.py` and verify `COSC_2060_Complete.imscc` compiles with zero XML errors, includes the cloned `COSC_2060_Master_Syllabus.docx`, `getting-started-lab-sandbox.html`, and `ai-data-shapes-guide.html`, and passes 100% link verification.

