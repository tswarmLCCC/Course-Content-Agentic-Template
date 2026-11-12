# Tasks 009: Bottom-Up Pedagogical Scaffolding, Syllabus Alignment & Lab Onboarding

- **Course**: `COSC 2060: Modern Data Engineering & AI Infrastructure`
- **Target Silo**: `courses/cosc-2060-data-engineering/`
- **Spec Reference**: [`spec.md`](file:///c:/dev/Course-Content-Agentic-Template/courses/cosc-2060-data-engineering/specs/009-pedagogical-scaffolding-and-syllabus-alignment/spec.md)
- **Plan Reference**: [`plan.md`](file:///c:/dev/Course-Content-Agentic-Template/courses/cosc-2060-data-engineering/specs/009-pedagogical-scaffolding-and-syllabus-alignment/plan.md)
- **Stage**: Stage 3 — Tasks
- **Date**: 2026-11-12

---

## Ordered Task Checklist

- [x] **Task 1: Institutional `.docx` Syllabus Cloner & DesignPLUS Syllabus Page (`REQ-001`, `REQ-002`)**
  - **Action**:
    1. Inspect `specs/_templates/syllabi/LCCC_Master_Syllabus_Template.docx` and update `.agents/skills/canvas-course-builder/scripts/docx_syllabus.py` to clone the official LCCC Word template (preserving all Word XML styles, customXml, headers/footers, and institutional policy tables) while populating `COSC 2060` metadata, description, outcomes, grading breakdown, and 16-week schedule.
    2. Expand `courses/cosc-2060-data-engineering/syllabus.md` with natural human headings, complete course details, zero-cost software stack, grading tables, 16-week unit schedule, and LCCC institutional policies.
    3. Update `.agents/skills/canvas-course-builder/build_course.py` so both `course_settings/syllabus.html` and `wiki_content/course-orientation-and-syllabus.html` render the full `syllabus.md` sections inside DesignPLUS panels alongside the prominent `.docx` download banner.
  - **Check**: Run a Python test verifying `COSC_2060_Master_Syllabus.docx` is a valid ZIP/OpenXML archive containing the LCCC `customXml` and `word/styles.xml` payloads and `COSC 2060` text, and verify `syllabus.html` contains all 7 syllabus panels.

- [x] **Task 2: Orientation Pages — `Getting Started with the Lab Environment` & `Common AI Data Shapes` (`REQ-003`, `REQ-004`, `REQ-005`)**
  - **Action**:
    1. Author `courses/cosc-2060-data-engineering/content/getting_started_lab.md` with clear, natural human headings covering: (1) Creating your personal sandbox repo from `https://github.com/tswarmLCCC/COSC-2060-Student-Sandbox`, (2) Launching GitHub Codespaces, (3) Navigating the workspace folders, (4) Using `study_guide.md`, `ds_to_engine.ipynb`, `coding_clinic.py`, and `labN_starter.py`, and (5) Running scripts, submitting to Canvas, and resetting with `bash reset_sandbox.sh`.
    2. Clean and adapt `docs/data_engineering_page_ai_data_shapes_guide.html` into `courses/cosc-2060-data-engineering/content/ai_data_shapes_guide.html` with natural human headings (removing two-part colon AI headers) and clean HTML math (zero raw `\[...\]` or `$...$` LaTeX).
    3. Update `build_course.py` so `Getting Started - Course Orientation` includes both `Getting Started with the Lab Environment` (`getting-started-lab-sandbox.html`) and `Common AI Data Shapes` (`ai-data-shapes-guide.html`), and link `getting-started-lab-sandbox.html` at the top of `Unit 01 Overview` and `Unit 01: Applied Lab Guide`.
  - **Check**: Verify `getting-started-lab-sandbox.html` and `ai-data-shapes-guide.html` are registered in `module_meta.xml` and `imsmanifest.xml` with valid `<head>` metadata and zero raw LaTeX tokens.

- [x] **Task 3: Unit 1 Bottom-Up Reading Refactor & Anti-AI-Speak Rewrite (`REQ-006`, `REQ-006B`, `REQ-007`, `REQ-008`)**
  - **Action**:
    1. Rewrite `courses/cosc-2060-data-engineering/units/unit_01_relational_foundations/reading.md` (and sync to `content/readings/unit_01_relational_foundation.md` and `student_sandbox_template/units/unit_01_relational_foundations/study_guide.md`) with natural human headers and an 8-part bottom-up structure:
       - *Moving from Database Reports to AI Datasets* (bridging from `CMAP 1815` SQL & Python, zero assumed ML coursework)
       - *What Our Output Table Looks Like and Where the Data Comes From* (concrete 6-row feature matrix table, why downstream models need one flat table, and the 3 operational source systems: HR `drivers`, Dispatch `routes`, NOAA `weather`)
       - *Building Features in SQL from the Ground Up* (teaching what a feature is and building basic SQL features step-by-step: arithmetic ratios, `CASE WHEN` flags, `LEFT JOIN`s, and basic `GROUP BY` / window averages)
       - *How Supervised Learning Uses Features and Targets* (plain-English explanation of input features `X` and target column `y` using HTML `<i>X</i>` and `<i>y</i>`)
       - *How Future Data Leaks into Training Tables* (preserving the Chicago blizzard delivery failure story and naive date join analysis)
       - *How Row and Column Databases Store Data* (preserving the PostgreSQL filing cabinet vs. DuckDB drinking straw mental model)
       - *Working with DuckDB, Rolling Windows, and ASOF JOIN* (bottom-up code ramp from `import duckdb` and basic Parquet queries to `ROWS BETWEEN 3 PRECEDING AND 1 PRECEDING` and `ASOF JOIN`)
       - *Practice Exercises and Common Questions* (live sandbox exercises and beginner FAQ modeled after `CMAP 1815`)
  - **Check**: Verify `units/unit_01_relational_foundations/reading.md` has zero `$X$` / `$y$` tokens, zero references to *"introductory machine learning coursework"*, natural human headers, and all 8 bottom-up sections.

- [x] **Task 4: Units 2–8 Bottom-Up Reading & Anti-AI-Speak Refactor (`REQ-006`, `REQ-006B`, `REQ-009`)**
  - **Action**:
    1. Refactor `reading.md` across Units 2–8 (and sync to `content/readings/unit_02..08.md` and `student_sandbox_template/units/unit_02..08/study_guide.md`) to:
       - Replace formulaic two-part colon AI headers and melodramatic buzzwords with natural, direct human instructor headings and tone.
       - Remove all raw LaTeX dollar-sign math tokens (`$\mu$`, `$\sigma$`, `$X$`, etc.) in favor of clean HTML (`&mu;`, `&sigma;`, `<i>X</i>`).
       - Open Chapter 1 of every unit with **What Our Output Looks Like and Where the Data Comes From** (explicitly showing the target data format/schema, why downstream consumers require it, and the real-world source systems).
       - Add a **Step-by-Step Code Ramp-Up** section teaching every library and syntax construct from line 1 before the complex pipeline code.
       - Close Chapter 1 of every unit with **Practice Exercises and Common Questions** (live sandbox practice + beginner FAQ).
  - **Check**: Run an audit script across all 8 unit readings and study guides verifying zero raw LaTeX `$` math tokens, presence of Target Output/Source Systems + Code Ramp-Up + Practice/FAQ sections, and natural headings.

- [x] **Task 5: Bottom-Up Code Ramp-Up in Lab Guides, Coding Clinics, Starters & Notebooks (`REQ-010`)**
  - **Action**:
    1. Update `overview.md`, `lab_guide.md`, `coding_clinic.py`, `labN_starter.py`, and `ds_to_engine.ipynb` across Units 1–8 (in both `courses/cosc-2060-data-engineering/` and `student_sandbox_template/`) to:
       - Remove raw LaTeX tokens and AI-cliché headers.
       - Add **Part 0: Basics Warm-Up** at the beginning of each `lab_guide.md`, `coding_clinic.py`, and `labN_starter.py` so students first verify basic connection, schema inspection, and a single foundational operation before tackling Parts 1–3.
  - **Check**: Run `python -m py_compile` on all 16 `.py` files (`coding_clinic.py` and `labN_starter.py` across Units 1–8) and verify `Part 0` is present in all 8 units.

- [x] **Task 6: Push Updated Sandbox Template, Rebuild `COSC_2060_Complete.imscc` & Full Audit (`REQ-011`)**
  - **Action**:
    1. Commit and push all updated files in `courses/cosc-2060-data-engineering/student_sandbox_template/` to `https://github.com/tswarmLCCC/COSC-2060-Student-Sandbox.git`.
    2. Compile `courses/cosc-2060-data-engineering/COSC_2060_Complete.imscc` using `build_course.py`.
    3. Run full XML validation, link verification, and EARS requirement pass/fail audit.
    4. Update `CURRENT.md` and `README.md`.
  - **Check**: Verify `git push` succeeds, `build_course.py` reports 0 XML errors, and all EARS requirements (`REQ-001` through `REQ-011`) pass verification.
