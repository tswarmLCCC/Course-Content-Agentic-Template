# CMAP 1815 & New Course Production Workflow Guide

This document captures the end-to-end design history, structural blueprints, formatting rules, and packaging workflow used to create the modern **CMAP 1815: Introduction to Modern SQL** course. Use this guide as the master reference when building new courses or updating existing curricula.

---

## Part 1: Where the "Learn with AI" Content is Located

The AI materials in CMAP 1815 are organized across multiple levels so they function as an active, Socratic pair-programming assistant rather than a passive shortcut:

### 1. In Course Orientation
- **Location:** Canvas Module: `Course Orientation & Database Setup` &rarr; Page: `Orientation: Learn with AI — Course Guidelines & Free Tools` (`wiki_content/orientation-learn-with-ai.html`).
- **Contents:**
  - **The AI Pair Programmer Philosophy:** Active Socratic learning, verification protocols, and anti-patterns to avoid.
  - **Zero-Cost Access:** Direct links to the Big 4 free chat platforms (ChatGPT Free, Claude Free, Google Gemini Free, Microsoft Copilot Free).
  - **The Verification Rule:** Every query generated or discussed with AI must be executed and verified against live PostgreSQL 16 in GitHub Codespaces.

### 2. In Every Weekly Unit (Item 6 of 8)
- **Location:** In every unit module, positioned between the Applied Lab Assignment and the Unit Knowledge Check Quiz.
- **Page Title:** `Unit X: Learn with AI — Supplemental Practice Drill` (`wiki_content/unit-XX-learn-with-ai.html`).
- **Contents per Unit:**
  - **Unit 1:** *Professor Codd (The Socratic SQL Master)* &mdash; Execution order (`FROM` before `SELECT`) & projection hazards (`SELECT *`).
  - **Unit 2:** *The Pedantic Database QA Lead* &mdash; ANSI Three-Valued Logic (`TRUE`, `FALSE`, `UNKNOWN`) & `NULL` traps.
  - **Unit 3:** *Stressed VP of Operations at OmniRetail* &mdash; Translating vague business requests into `INNER`, `LEFT`, and Anti-Joins.
  - **Unit 4:** *Chief Financial Officer (CFO)* &mdash; Matrix cross-tab pivoting (`CASE WHEN` inside `SUM`) & safe division (`NULLIF`).
  - **Unit 5:** *Chaos Database SRE* &mdash; Safe DML staging tables, atomic transactions (`BEGIN`/`COMMIT`/`ROLLBACK`), and `RETURNING` clauses.
  - **Unit 6:** *Staff Database Architect* &mdash; Refactoring unreadable nested subqueries into modular CTEs (`WITH`) & analytical window functions.
  - **Unit 7:** *Senior Enterprise Data Modeler* &mdash; 3NF normalization from messy spreadsheets & DDL constraints (`CHECK`, `FOREIGN KEY ON DELETE CASCADE`).
  - **Unit 8:** *Senior Performance DBA Panel* &mdash; Capstone technical defense, B-Tree index selectivity, write penalties, and `EXPLAIN ANALYZE` execution trees.
- **Graded Participation Task:** Students paste their prompt findings and insights to the weekly Canvas discussion board (part of the 10% Asynchronous Preparation & AI Participation gradebook category).

### 3. In the Source Repository
- [`shared_assets/ai_guidance/AI_PAIR_PROGRAMMING_GUIDELINES.md`](file:///c:/dev/CMAP_1815_Autogen/shared_assets/ai_guidance/AI_PAIR_PROGRAMMING_GUIDELINES.md)
- In `scripts/build_canvas_cartridge.py` under the `LEARN_WITH_AI_DATA` dictionary.

---

## Part 2: Master Course Layout & Architecture

Each weekly unit follows a standardized 8-item sequence that guides students from concept discovery to hands-on mastery:

```
Unit Module Architecture:
├── 1. Unit Overview: [Topic] (DesignPLUS Ribbon Banner + Accordions)
├── 2. Required Readings & Video Lectures (Tutorial Links + Embedded YouTube Chapters)
├── 3. Asynchronous Preparation & Drills (Focus Questions + Expandable Self-Check Drills)
├── 4. Applied SQL Lab Guide (Scenario Specs + Active Challenges + HTML Rubric Table)
├── 5. [Unit X] Applied SQL Lab Assignment (Canvas SpeedGrader .sql Turn-in, 50 pts)
├── 6. Learn with AI — Supplemental Practice Drill (Roleplay Persona + Discussion Task)
├── 7. Unit Knowledge Check: [Topic] (Native Canvas QTI Quiz, 15 Qs, 30 pts)
└── 8. [Instructor Guide] Teaching Notes & Solutions (Unpublished: Video Blueprints & Solution SQL)
```

---

## Part 3: Page Layout & Visual Styling Guidelines

### 1. Selective Header Ribbon Policy
- **Banner Ribbons (`dp-header dp-basic-bar`):** Used exclusively on high-level navigation and overview pages:
  - Home Page (`home-page.html`)
  - Course Orientation / Start Here (`start-here.html`)
  - Unit Overviews (`unit-XX-overview.html`)
  - Syllabus Page (`course_settings/syllabus.html`)
- **Clean Standard Layout (`render_standard_page_html`):** Used on all inner content pages (Reading pages, Lab Guides, Async Drills, AI Practice, Instructor Notes) to prevent visual fatigue.
  - Header: `<h1 style="color: #1e3a8a; margin-top: 0; margin-bottom: 1.25rem;">`
  - Lead Callout Box: `<div style="background: #f8fafc; border-left: 4px solid #1e3a8a; padding: 1rem 1.25rem; margin-bottom: 1.75rem; border-radius: 0 4px 4px 0; font-size: 1.05em; line-height: 1.5; color: #334155;">`
  - Section Divs: `<h2 style="color: #1e3a8a; border-bottom: 2px solid #e2e8f0; padding-bottom: 0.4rem; margin-top: 1.75rem; margin-bottom: 1rem;">`

### 2. Markdown Translation Standards
- **Rubric Tables:** Parsed into clean HTML `<table>` elements with `#1e3a8a` navy headers, white header text, `#f8fafc` zebra striping, and `#cbd5e1` borders.
- **SQL / Code Blocks:** Encapsulated in dark `#0f172a` containers with `#f8fafc` text, padding, and monospace fonts.
- **Interactive Self-Check Drills:** Parsed into styled `<details style="background: #f8fafc; border: 1px solid #cbd5e1; border-radius: 6px; padding: 0.75rem 1.25rem; margin: 1rem 0;">` with `<summary style="cursor: pointer; font-weight: 600; color: #1e3a8a;">` for interactive answer reveals.

---

## Part 4: Syllabus Standardization & Template Workflow

To generate an institutional Word syllabus that matches college branding:
1. **Extract Existing .docx Template:** Extract `word/document.xml` from an existing approved course export.
2. **Transform Course Content:** Update course code, course title, prerequisites, credit hours, catalog description, module outline, and grading criteria while preserving XML paragraph styles, table borders, fonts, and headers.
3. **Package in Cartridge:** Save the `.docx` file into `web_resources/syllabi/` and declare it in `imsmanifest.xml`.
4. **Canvas Integration:** Reference the file in `course_settings/syllabus.html` using Canvas filebase links (`$IMS-CC-FILEBASE$/syllabi/...`).

---

## Part 5: Assessment & Gradebook Weighting Standards

Configure `course_settings/assignment_groups.xml` with four standard weighted categories:

```xml
<assignmentGroups>
  <assignmentGroup>
    <title>Hands-on SQL Labs</title>
    <position>1</position>
    <group_weight>40.0</group_weight>
  </assignmentGroup>
  <assignmentGroup>
    <title>Unit Knowledge Checks &amp; Quizzes</title>
    <position>2</position>
    <group_weight>20.0</group_weight>
  </assignmentGroup>
  <assignmentGroup>
    <title>Asynchronous Preparation &amp; Drills</title>
    <position>3</position>
    <group_weight>10.0</group_weight>
  </assignmentGroup>
  <assignmentGroup>
    <title>Comprehensive Course Capstone</title>
    <position>4</position>
    <group_weight>30.0</group_weight>
  </assignmentGroup>
</assignmentGroups>
```

---

## Part 6: Automated Cartridge Builder Execution

To compile new course content into a production-ready Canvas package:

```bash
# Run the automated build script
python scripts/build_canvas_cartridge.py
```

### Build Pipeline Steps:
1. Provisions directories (`wiki_content`, `course_settings`, `web_resources/syllabi`, `non_cc_assessments`, assignment and quiz folders).
2. Converts raw markdown (rubrics, guides, drills) to rich HTML.
3. Writes native Canvas assignment descriptors (`assignment_settings.xml`) and SpeedGrader HTML files.
4. Generates standard QTI 1.2 XML quiz packages.
5. Synchronizes `module_meta.xml` and `imsmanifest.xml` with shared deterministic MD5 IDs.
6. Validates all XML files for schema well-formedness.
7. Archives the build directory into `CMAP_1815_Complete.imscc`.

### Canvas Import:
1. Open Canvas &rarr; **Settings** &rarr; **Import Course Content**.
2. Select **Content Type:** **Common Cartridge 1.x Package**.
3. Choose `CMAP_1815_Complete.imscc`, select **All content**, and click **Import**.
