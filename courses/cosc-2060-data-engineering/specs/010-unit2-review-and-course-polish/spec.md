# Feature Specification: Unit 2 Review Remediation, Hybrid Notebook Architecture & Course-Wide Sophomore Polish

- **ID**: `specs/010-unit2-review-and-course-polish`
- **Status**: Completed
- **Created**: 2026-11-13
- **Target Completion**: Iterative multi-unit pass

---

## 1. Objective & Target Audience
- **Primary Persona**: College sophomores enrolled in COSC 2060 (Modern Data Engineering & AI Infrastructure) with introductory SQL (`CMAP 1815`) and introductory Python backgrounds, plus the course instructor reviewing student work via GitHub.
- **Problem Statement**: Review of Unit 2 and the generated `COSC_2060_Course_Book.pdf` surfaced six friction points: (1) Canvas assignment directions still ask for `.py` file uploads instead of GitHub-only submissions; (2) indented bash/Python code blocks and inline `$`/LaTeX leak raw `__CODE_BLOCK_*__` placeholders and `\$` escapes into HTML/PDF; (3) Orientation B (*Shapes of AI Data*) drifted from what Units 1–8 actually teach; (4) `syllabus.md` needs full alignment with LCCC's institutional syllabus template; (5) Unit 2's row-by-row code walkthroughs (e.g., Driver 42) are awkward when students are told to run an entire `.py` file at once instead of stepping through `.ipynb` cells; and (6) the course needs a bottom-up sophomore readability pass.
- **One Job**: Align COSC 2060's submission workflow, LCCC syllabus, Orientation A/B accuracy, rendering hygiene, hybrid `.ipynb`/`.py` lab experience, and sophomore-level readability across the course, cartridge, course book PDF, and student sandbox template.

---

## 2. Requirements (EARS Syntax)

### Always (Ubiquitous)
- `REQ-01` (**GitHub-Only Assignment Submission**): Orientation A (`getting_started_lab.md`), all unit `lab_guide.md` files, and Canvas assignment instructions **shall** instruct students to commit and push all work to their single personal GitHub repository (`COSC-2060-Student-Sandbox-yourname`) used throughout the semester, and to submit only the GitHub repository URL plus a list of changed files in Canvas (with zero `.py` file-download/upload instructions).
- `REQ-02` (**Rendering & Escaping Hygiene**): `.agents/skills/canvas-course-builder/scripts/html_styler.py` and all course markdown sources **shall** render fenced code blocks (including indented code blocks inside lists), currency values (`$`), and inline math/symbols cleanly with zero leaked `__CODE_BLOCK_*__` placeholders, stray `\$` escapes, or unrendered LaTeX in both `COSC_2060_Complete.imscc` and `COSC_2060_Course_Book.pdf`.
- `REQ-03` (**Orientation B Consistency**): `content/ai_data_shapes_guide.html` (*The Shapes of AI Data*) **shall** accurately reflect the exact data shapes, tools, and architectures taught across Units 1–8 of COSC 2060 (tabular feature matrices, scaled/encoded matrices, image tensors & YOLO labels, RAG vector stores, FastAPI JSON schemas, MCP tool interfaces, Dagster DAGs, and containerized pipelines), removing inconsistent or untaught topics.
- `REQ-04` (**LCCC Syllabus Template Compliance**): `syllabus.md` (and any generated Canvas syllabus page / `.docx` export) **shall** include all mandatory Laramie County Community College (LCCC) institutional sections and boilerplate from `specs/_templates/syllabi/LCCC_Master_Syllabus_Template.docx` (Attendance & Drop for Non-Attendance, Incomplete Grades, Academic Integrity Procedures 3.15P/3.16P, Artificial Intelligence policy, Behavior in the Classroom, Student Rights & Responsibilities, OSA Accommodations, and Learning Commons/NetTutor Tutoring).
- `REQ-05` (**Hybrid `.ipynb` Walkthroughs & `.py` Graded Labs**): Interactive code walkthroughs and Coding Clinics (such as Driver 42 row-by-row inspection in Unit 2 and corresponding clinics across Units 1–8) **shall** be provided as cell-by-cell Jupyter Notebooks (`.ipynb`) in `student_sandbox_template/` with matching step-by-step instructions in `reading.md`, while graded labs (`labN_starter.py`) **shall** remain clean `.py` scripts enhanced with `# %%` VS Code interactive cell markers and step-by-step check prints for incremental execution and clean GitHub diffs.
- `REQ-06` (**Sophomore Readability & Pedagogical Polish**): Every unit's `reading.md`, `lab_guide.md`, `drills.md`, and Orientation pages **shall** pass a sophomore-readability review ensuring technical terms are introduced before use, code walkthroughs progress bottom-up without unexplained leaps, and prose avoids AI-cliché headers/phrasing.

### When (Event-Driven)
- `REQ-07` (**Build & Verification**): **When** content, template, and script updates are complete, the build pipeline **shall** regenerate `COSC_2060_Complete.imscc` and `COSC_2060_Course_Book.pdf` with zero build errors and verified clean rendering on previously failing pages.

### If-Then (Error/Unwanted Behavior)
- `REQ-08` (**Code Block Fallback**): **If** a markdown file contains an indented fenced code block inside a numbered or bulleted list, **then** `html_styler.py` **shall** strip the common indentation and render it as a styled `<pre><code>` block rather than leaving raw `__CODE_BLOCK_*__` tokens.

---

## 3. Deliberately Out of Scope
- Changing the 8-unit curriculum sequence, core datasets, or grading weights in COSC 2060.
- Converting Unit 5–8 server/orchestration/container deliverables (FastAPI, MCP, Dagster, Docker) into `.ipynb` notebooks.
- Modifying any course or module outside `courses/cosc-2060-data-engineering/` (except the shared `html_styler.py` parser bug fix under `.agents/skills/canvas-course-builder/scripts/`).

---

## 4. Acceptance Criteria & Definition of Done
- [ ] Every requirement `REQ-01` through `REQ-08` is verified and passing.
- [ ] `COSC_2060_Complete.imscc` compiles cleanly and passes cartridge validation.
- [ ] `COSC_2060_Course_Book.pdf` rebuilds cleanly with zero `__CODE_BLOCK_*__`, stray `\$`, or unrendered LaTeX leaks.
- [ ] Conforms to ADR-001 (WCAG 2.1/2.2 AA), ADR-002 (Spec-Driven Development), and ADR-003 (Canvas/DesignPLUS invariants).
- [ ] Deliverables reviewed and accepted by the user.

