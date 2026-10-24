---
name: canvas-course-builder
description: >-
  End-to-end workflow, architectural standard, and portable toolchain for generating
  production-grade, DesignPLUS-compliant Canvas Common Cartridge (.imscc) courses with native
  assignments, QTI 1.2 quizzes, markdown-to-HTML formatting, and institutional syllabus templates.
  Use this skill whenever authoring course content, converting quizzes to QTI, formatting Canvas
  pages with DesignPLUS styling, or packaging a complete course into a Canvas Common Cartridge.
---

# Canvas Course Cartridge Production Workflow

This skill defines the complete blueprint, structural rules, formatting standards, and automation scripts required to author, format, package, and deploy a complete college course into Canvas LMS via Common Cartridge (`.imscc`).

---

## 1. Portable Toolchain Architecture

This skill contains self-contained, zero-dependency Python tools and templates located within this directory:

- **Cartridge Compiler:** [`scripts/build_cartridge.py`](./scripts/build_cartridge.py)
- **QTI 1.2 Quiz Builder:** [`scripts/qti_builder.py`](./scripts/qti_builder.py)
- **DesignPLUS & Markdown Styler:** [`scripts/html_styler.py`](./scripts/html_styler.py)
- **Word Syllabus Generator:** [`scripts/docx_syllabus.py`](./scripts/docx_syllabus.py)
- **Course Config Template:** [`templates/course_config.example.json`](./templates/course_config.example.json)
- **Quiz Markdown Template:** [`templates/unit_quiz_template.md`](./templates/unit_quiz_template.md)
- **DesignPLUS CSS Guide:** [`references/designplus_guide.md`](./references/designplus_guide.md)
- **Common Cartridge XML Architecture:** [`references/canvas_cc_architecture.md`](./references/canvas_cc_architecture.md)
- **Deployment & Git Submodule Guide:** [`README.md`](./README.md)

---

## 2. Core Architecture & Module Taxonomy

Each weekly unit follows a strict, proven **8-Item Sequence** inside Canvas Modules:

| Sequence # | Item Title Convention | Type | Workflow State | Description |
| :--- | :--- | :--- | :--- | :--- |
| **1** | `Unit X Overview: [Topic]` | `WikiPage` | `active` (Published) | High-level roadmap, contact hour budget (150m study / 150m lab), learning objectives. Uses DesignPLUS banner ribbon. |
| **2** | `Unit X: Required Readings & Video Lectures` | `WikiPage` | `active` (Published) | Direct links to tutorials + responsive 16:9 embedded YouTube micro-video chapters with start timestamps. Clean standard layout. |
| **3** | `Unit X: Asynchronous Preparation & Drills` | `WikiPage` | `active` (Published) | Conceptual focus questions + formative self-check drills with interactive `<details>/<summary>` answer keys. |
| **4** | `Unit X: Applied Lab Guide` | `WikiPage` | `active` (Published) | Complete scenario instructions, in-class active learning challenges, and native HTML grading rubric table. |
| **5** | `Unit X Applied Lab Assignment` | `Assignment` | `active` (Published) | Native Canvas Assignment (50 pts) for SpeedGrader file upload (`.sql`, `.txt`, `.py`, `.pdf`) or text entry, linked to Labs group. |
| **6** | `Unit X: Learn with AI — Supplemental Practice Drill` | `WikiPage` | `active` (Published) | Socratic roleplay scenario, free tools guide, copy-paste master prompt, and weekly discussion debrief task. |
| **7** | `Unit X Knowledge Check: [Topic]` | `Quizzes::Quiz` | `active` (Published) | Native QTI 1.2 multiple-choice assessment (15 questions, 30 pts, 3 attempts, highest score kept). |
| **8** | `[Instructor Guide] Unit X Teaching Notes & Solutions` | `WikiPage` | `unpublished` | Hidden from students. Custom video production blueprint, synchronous class delivery agenda, and master solution key. |

---

## 3. Page Formatting & Visual Design Guidelines

### A. Selective Ribbon Policy
* **Apply DesignPLUS Banner Ribbon (`dp-header dp-basic-bar`) ONLY on:**
  - `home-page.html` (Front Page)
  - `start-here.html` (Course Orientation)
  - `unit-XX-overview.html` (Weekly Unit Overviews)
  - `course_settings/syllabus.html` (Native Syllabus Page)
* **Use Clean Standard Layout (`render_standard_page_html`) on all Inner Pages:**
  - Standard typography (`-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif`)
  - Navy blue section headers (`<h2 style="color: #1e3a8a; border-bottom: 2px solid #e2e8f0; ...">`)
  - Lead card callouts (`<div style="background: #f8fafc; border-left: 4px solid #1e3a8a; ...">`)
  - Avoid heavy, repetitive banner ribbons on subpages.

### B. Markdown-to-HTML Translation Rules
Never dump raw markdown or large `<pre><code>` blocks on student-facing pages:
1. **Rubrics & Tables:** Convert `| Col 1 | Col 2 |` into styled `<table style="width: 100%; border-collapse: collapse; border: 1px solid #cbd5e1;">` with navy blue headers (`#1e3a8a`), cell borders, and alternating zebra rows (`#f8fafc`).
2. **Code Blocks:** Wrap in styled dark syntax boxes: `<div style="background: #0f172a; color: #f8fafc; padding: 1rem 1.25rem; border-radius: 6px; font-family: Consolas, Monaco, monospace;"><pre><code>...</code></pre></div>`.
3. **Interactive Drills:** Convert `<details><summary>` into styled accordion cards with borders and hover cursor.
4. **Inline Syntax:** Convert `` `code` `` into `<code style="background: #f1f5f9; color: #0369a1; padding: 0.15rem 0.35rem; border-radius: 3px; font-weight: 600;">`.

---

## 4. Native QTI 1.2 Quizzes

To produce Canvas-compliant quizzes:
1. Author markdown quiz files matching [`templates/unit_quiz_template.md`](./templates/unit_quiz_template.md) with `### Question X`, options `* A) ... * D)`, and an `## Answer Key` table with rationales.
2. Use [`scripts/qti_builder.py`](./scripts/qti_builder.py) to compile into:
   - `[quiz_id]/assessment_qti.xml`: QTI 1.2 single/multiple response elements.
   - `[quiz_id]/assessment_meta.xml`: Canvas quiz settings (`allowed_attempts="3"`, `scoring_policy="keep_highest"`, `points_possible="30.0"`).
   - `non_cc_assessments/[quiz_id].xml.qti`: Duplicate QTI XML payload required by Canvas import engine.

---

## 5. Institutional Syllabus Standardization

1. Generate the master Word syllabus using [`scripts/docx_syllabus.py`](./scripts/docx_syllabus.py) to produce a zero-dependency OpenXML `.docx` file.
2. Place the resulting file into `web_resources/syllabi/` and declare it as a `webcontent` resource in `imsmanifest.xml`.
3. Embed the download link into `course_settings/syllabus.html`:
   ```html
   <a class="instructure_file_link instructure_scribd_file inline_disabled" 
      title="Master Syllabus.docx" 
      href="$IMS-CC-FILEBASE$/syllabi/Master%20Syllabus.docx?canvas_=1&amp;canvas_qs_wrap=1" 
      target="_blank">Download Master Syllabus (Word .docx)</a>
   ```

---

## 6. Canvas Gradebook & Assessment Configuration

### Weighted Assignment Groups (`course_settings/assignment_groups.xml`)
Enforce institutional 100% weighted distribution:
- **Hands-on Applied Labs / Projects:** 40.0%
- **Comprehensive Capstone:** 30.0%
- **Unit Knowledge Checks (Quizzes):** 20.0%
- **Asynchronous Preparation & AI Participation:** 10.0%

### Native Assignment Descriptors (`assignment_settings.xml`)
Every lab assignment directory (`[assign_id]/`) must include:
1. `assignment_settings.xml`: Sets `submission_types` (`online_text_entry,online_upload`), `allowed_extensions` (`sql,txt,pdf`), `points_possible` (50.0), and `assignment_group_identifierref`.
2. `[assign_id].html`: Clean assignment description with clear submission steps and the full grading rubric table.

---

## 7. Packaging & Deployment Protocol

1. Compile the cartridge and validate XML integrity:
   - Ensure all 32-character hexadecimal MD5 IDs match across `imsmanifest.xml` and `module_meta.xml`.
   - Validate XML parsing with `xml.etree.ElementTree.parse()`.
   - Compress the directory into `.imscc` via standard ZIP DEFLATE.
2. In Canvas:
   - Navigate to **Settings** &rarr; **Import Course Content**.
   - Select **Common Cartridge 1.x Package**.
   - Select the generated `.imscc` file, choose **All content**, and click **Import**.
