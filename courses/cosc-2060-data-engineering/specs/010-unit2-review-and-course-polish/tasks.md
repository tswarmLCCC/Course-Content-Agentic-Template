# Task List: 010-unit2-review-and-course-polish

- [x] **Task 1: Fix `html_styler.py` code-fence regex & clean stray `\$` / raw LaTeX leaks across course markdown** (`REQ-02`, `REQ-08`)
  - *Check*: Run a Python verification script over all `content/*.md` and `units/*/*.md` rendered through `html_styler.py` confirming zero `__CODE_BLOCK_` tokens, zero `\$` currency leaks, and zero raw LaTeX (`\times`, `\to`, `mathcal{O`).
- [x] **Task 2: Update Orientation A (`getting_started_lab.md`) and all 8 `lab_guide.md` files for GitHub-only submissions** (`REQ-01`)
  - *Check*: `Select-String` across `content/getting_started_lab.md`, `units/*/lab_guide.md`, and `student_sandbox_template/units/*/lab_guide.md` shows zero "Download..." or "upload to Canvas" `.py` file-upload instructions, and all specify GitHub repo URL + changed files list.
- [x] **Task 3: Audit & update Orientation B (`content/ai_data_shapes_guide.html`) for 8-unit consistency** (`REQ-03`)
  - *Check*: Inspect headings and unit mappings in `content/ai_data_shapes_guide.html` and confirm 1:1 alignment with Units 1–8 in `syllabus.md` with DesignPLUS-compliant HTML.
- [x] **Task 4: Align `syllabus.md` with `LCCC_Master_Syllabus_Template.docx`** (`REQ-04`)
  - *Check*: Diff sections of `syllabus.md` against `LCCC_Master_Syllabus_Template.docx` confirming all mandatory LCCC institutional policies, dates, OSA, and tutoring sections are present.
- [x] **Task 5: Implement Hybrid `.ipynb` Coding Clinics & `# %%` Lab Checkpoints (Units 1–8)** (`REQ-05`)
  - *Check*: Verify `coding_clinic.ipynb` (or `.ipynb` clinic cells) and `# %%` markers in `labN_starter.py` across `student_sandbox_template/units/unit_01..08/`, and verify `reading.md` / `study_guide.md` directions point to cell-by-cell execution (e.g., Unit 2 Driver 42).
- [x] **Task 6: Sophomore Readability & Pedagogical Polish Loop across Orientation & Units 1–8** (`REQ-06`)
  - *Check*: Document per-unit readability pass findings and verify zero unexplained jargon jumps or AI-cliché headers across `units/unit_01..08/`.
- [x] **Task 7: Rebuild `COSC_2060_Complete.imscc` and `COSC_2060_Course_Book.pdf`, verify outputs, and update `README.md`** (`REQ-07`)
  - *Check*: Run cartridge build + `build_course_book.py`, confirm exit code 0, and verify rendered PDF pages (especially previously failing pages) are clean.
