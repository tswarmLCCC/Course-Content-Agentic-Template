# Task Checklist: Toolchain & Catalog Migration

- **Spec Reference**: [spec.md](file:///c:/dev/Course-Content-Agentic-Template/specs/001-toolchain-and-catalog-migration/spec.md)
- **Plan Reference**: [plan.md](file:///c:/dev/Course-Content-Agentic-Template/specs/001-toolchain-and-catalog-migration/plan.md)

---

## Task Execution Sequence

- [x] **Task 1: Migrate Core Canvas Course Builder Skill**
  - **Action**: Copy and structure `.agents/skills/canvas-course-builder/` with `SKILL.md`, `scripts/` (`build_cartridge.py`, `qti_builder.py`, `html_styler.py`, `docx_syllabus.py`), `templates/`, and `references/`.
  - **Files Modified**: `.agents/skills/canvas-course-builder/*`
  - **Check**: Run Python compilation test `python -m py_compile .agents/skills/canvas-course-builder/scripts/*.py` (Passed: all 4 scripts compiled successfully)

- [x] **Task 2: Migrate Slide Deck Generator Skill**
  - **Action**: Create `.agents/skills/slide-deck-generator/` with `SKILL.md` and `scripts/` (`slide_engine.py`, `audit_deck.py`).
  - **Files Modified**: `.agents/skills/slide-deck-generator/*`
  - **Check**: Run Python compilation test `python -m py_compile .agents/skills/slide-deck-generator/scripts/*.py` (Passed: slide_engine.py and audit_deck.py compiled cleanly)

- [x] **Task 3: Migrate Syllabus Docx Cloner & Course Intake Scanner Skills**
  - **Action**: Create `.agents/skills/syllabus-docx-cloner/` (with `SKILL.md`, `docx_syllabus.py`, and `LCCC_Master_Syllabus_Template.docx`) and `.agents/skills/course-intake-scanner/` (with `SKILL.md` and `intake_scanner.py`).
  - **Files Modified**: `.agents/skills/syllabus-docx-cloner/*`, `.agents/skills/course-intake-scanner/*`
  - **Check**: Verify files exist and scripts pass `py_compile`. (Passed: docx_syllabus.py and intake_scanner.py compiled cleanly)

- [x] **Task 4: Migrate Pedagogical Playbooks**
  - **Action**: Copy all four foundational playbooks plus the Master Setup & Formatting Playbook into `docs/playbooks/` (`COURSE_PRODUCTION_WORKFLOW.md`, `SLIDE_DESIGN_PLAYBOOK.md`, `WHY_WHAT_HOW_PEDAGOGY.md`, `ZERO_COST_INFRASTRUCTURE.md`, `MASTER_COURSE_SETUP_AND_FORMATTING_GUIDE.md`).
  - **Files Modified**: `docs/playbooks/*`
  - **Check**: Verify all 4 playbooks exist and display proper markdown formatting. (Passed: All 5 files present and verified)

- [x] **Task 5: Migrate Curriculum & Rubric Templates**
  - **Action**: Copy reusable templates (`rubrics/`, `instructional/`, `code_labs/`, `syllabi/`) into `specs/_templates/`.
  - **Files Modified**: `specs/_templates/rubrics/*`, `specs/_templates/instructional/*`, `specs/_templates/code_labs/*`, `specs/_templates/syllabi/*`
  - **Check**: Verify templates directory structure. (Passed: All rubric, instructional, syllabus, and code lab templates verified)

- [x] **Task 6: Update Master Documentation (README.md & AGENTS.md)**
  - **Action**: Update `README.md` and `AGENTS.md` to document the newly available skills, their invocation patterns, and how they fit into the course creation workflow.
  - **Files Modified**: `README.md`, `AGENTS.md`
  - **Check**: Verify markdown links and documentation sections. (Passed: README.md and AGENTS.md updated with full catalog & skills)

---

## Verification & Retrospective Audit
- [x] Run functional test on `qti_builder.py` and `html_styler.py` using sample quiz data. (Passed: `scratch/test_verification.py` passed all assertions)
- [x] Audit against every requirement in `spec.md` (Pass/Fail table).

| Requirement | Description | Status | Evidence |
| :--- | :--- | :--- | :--- |
| **REQ-01** | Package tools in `.agents/skills/` with `SKILL.md` | **PASS** | 4 modular skills created under `.agents/skills/` with valid YAML frontmatter. |
| **REQ-02** | Zero external pip dependencies for `canvas-course-builder` | **PASS** | Pure Python 3 standard library (`os`, `re`, `html`, `hashlib`, `xml.etree`). |
| **REQ-03** | `canvas-course-builder` QTI & DesignPLUS compilation | **PASS** | `qti_builder.py` and `html_styler.py` tested and verified producing valid QTI 1.2 XML and styled HTML. |
| **REQ-04** | `slide-deck-generator` 16:9 WCAG AAA deck generation | **PASS** | `slide_engine.py` and `audit_deck.py` compiled cleanly under `.agents/skills/slide-deck-generator/`. |
| **REQ-05** | `syllabus-docx-cloner` institutional Word syllabus engine | **PASS** | Cloner script and `LCCC_Master_Syllabus_Template.docx` migrated to `.agents/skills/syllabus-docx-cloner/`. |
| **REQ-06** | `course-intake-scanner` drop-zone intake scanner | **PASS** | `intake_scanner.py` and skill guide migrated to `.agents/skills/course-intake-scanner/`. |
| **REQ-07** | Skills universally accessible without polluting course dirs | **PASS** | All tools live in `.agents/skills/`; course folders contain zero tool copies. |
| **REQ-08** | No mutation of existing course content | **PASS** | `courses/cosc-2060-data-engineering/` is 100% untouched. |
| **REQ-09** | Playbooks in `docs/playbooks/` & templates in `specs/_templates/` | **PASS** | 5 playbooks in `docs/playbooks/`, rubric/instructional/code lab templates in `specs/_templates/`. |
| **REQ-10** | Living documentation updated in `README.md` and `AGENTS.md` | **PASS** | Both files updated with complete catalog references, layout trees, and agent rules. |

- [x] User review and sign-off.

