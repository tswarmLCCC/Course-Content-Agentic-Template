# Implementation Plan: Unit 2 Review Remediation, Hybrid Notebook Architecture & Course-Wide Sophomore Polish

- **Spec**: [spec.md](spec.md)
- **ADRs**: ADR-001 (WCAG 2.1/2.2 AA), ADR-002 (Spec-Driven Development), ADR-003 (Canvas/DesignPLUS Invariants)

---

## 1. Architecture & Technical Decisions

### 1.1 Rendering & Escaping Hygiene (`REQ-02`, `REQ-08`)
- Fix `.agents/skills/canvas-course-builder/scripts/html_styler.py` line 54 so fenced code blocks with leading list indentation (`^[ \t]*```...`) are matched, dedented, and replaced cleanly without leaving `__CODE_BLOCK_*__` tokens.
- Audit and clean stray `\$` escapes and raw LaTeX expressions across `courses/cosc-2060-data-engineering/content/` and `units/unit_01..08/` (e.g., replacing raw `$1920 \times 1080 \to 640 \times 640$` and `mathcal{O(N)}` with clean HTML/Unicode/code spans) so both Canvas HTML and WeasyPrint/PDF (`COSC_2060_Course_Book.pdf`) render cleanly.

### 1.2 GitHub-Only Assignment Submission Workflow (`REQ-01`)
- Update `content/getting_started_lab.md` (Orientation A) Section 5 to replace "Download... and upload to Canvas" with a clean GitHub workflow: `git add -A && git commit -m "..." && git push`, then paste the personal repository URL + list of changed files into the Canvas assignment text box.
- Update all `units/unit_01..08/lab_guide.md` and `student_sandbox_template/units/unit_01..08/lab_guide.md` submission sections to match.

### 1.3 Orientation B Consistency (`REQ-03`)
- Audit `content/ai_data_shapes_guide.html` against the 8 units of COSC 2060 (`syllabus.md` Section 2) and replace untaught/drifted sections (such as NER Alignment and Graph Data) with the actual shapes taught in Units 1–8 (Supervised Tabular Matrices, Scaled/Encoded Anomaly Matrices, Image Tensors & YOLO Bounding Boxes, Chunked Text & Vector Stores for RAG, FastAPI JSON REST Schemas, MCP Agent Tool Interfaces, Dagster Asset DAGs, and Containerized Pipelines).

### 1.4 LCCC Syllabus Template Compliance (`REQ-04`)
- Extract all mandatory institutional sections from `specs/_templates/syllabi/LCCC_Master_Syllabus_Template.docx` and merge any missing sections (Attendance & Drop for Non-Attendance, Incomplete Grades, Academic Integrity Admin Procedures 3.15P/3.16P, Artificial Intelligence policy, Behavior in the Classroom, Student Rights & Responsibilities, OSA Accommodations, Learning Commons/NetTutor Tutoring) into `courses/cosc-2060-data-engineering/syllabus.md` while keeping COSC 2060 course details intact.

### 1.5 Hybrid `.ipynb` Walkthroughs & `.py` Graded Labs (`REQ-05`)
- For Units 1–8 in `student_sandbox_template/units/`, ensure interactive walkthroughs & Coding Clinics (including Unit 2's Driver 42 row-by-row inspection) are executable cell-by-cell in `.ipynb` notebooks (`coding_clinic.ipynb` / `ds_to_engine.ipynb`), and update `units/unit_XX/reading.md` & `study_guide.md` directions so students run cells interactively rather than executing a whole `.py` file at once.
- Add `# %%` VS Code interactive cell markers and step-by-step checkpoint prints to `labN_starter.py` files (Units 1–8) while keeping them clean `.py` files for GitHub diffs.

### 1.6 Sophomore Readability & Pedagogical Polish Loop (`REQ-06`)
- Review Orientation A/B and Units 1–8 (`reading.md`, `lab_guide.md`, `drills.md`) with a "college sophomore new to data engineering" lens: verify every term/operator is introduced before use, transitions are smooth, and AI-cliché headers are avoided.

### 1.7 Build & Verification (`REQ-07`)
- Regenerate `COSC_2060_Complete.imscc` and `COSC_2060_Course_Book.pdf`, verify zero `__CODE_BLOCK_*__`, stray `\$`, or raw LaTeX leaks, and update `README.md`.

---

## 2. Explicit Out-of-Scope Boundaries
- No changes to other courses (`courses/*` other than `cosc-2060-data-engineering/`) or `modules/`.
- No changes to the 8-unit curriculum sequence or grading weights.

