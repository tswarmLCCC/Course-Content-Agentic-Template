# Task Checklist: Canvas Quizzes, Overviews & Cartridge Compilation

- **Spec Reference**: [spec.md](file:///c:/dev/Course-Content-Agentic-Template/courses/cosc-2060-data-engineering/specs/003-canvas-quizzes-and-sequence-completion/spec.md)
- **Plan Reference**: [plan.md](file:///c:/dev/Course-Content-Agentic-Template/courses/cosc-2060-data-engineering/specs/003-canvas-quizzes-and-sequence-completion/plan.md)
- **Course**: `COSC 2060: Modern Data Engineering & AI Infrastructure`

---

## Task Execution Sequence

- [x] **Task 1: Generate `course_config.json` & `syllabus.md`**
  - **Action**: Create course configuration with weighted gradebook groups, competencies, and grading scale, alongside `syllabus.md`.
  - **Files Modified**: `courses/cosc-2060-data-engineering/course_config.json`, `courses/cosc-2060-data-engineering/syllabus.md`
  - **Check**: Verify JSON validity using `python -m json.tool`. (Passed: Valid JSON with all 4 assignment groups and 8 outcomes)

- [x] **Task 2: Scaffold Unit Directories & Ingest Existing Curriculum**
  - **Action**: Scaffold `units/unit_01_...` through `unit_08_...` and populate `reading.md`, `drills.md`, and `lab_guide.md` from `content/`.
  - **Files Modified**: `courses/cosc-2060-data-engineering/units/unit_0[1-8]_*`
  - **Check**: Verify all 8 unit folders contain valid markdown readings, drills, and lab guides. (Passed: 24 markdown files ingested across all 8 units)

- [x] **Task 3: Author 8 Unit Overviews**
  - **Action**: Author `overview.md` for all 8 units with DesignPLUS-ready structure, 300m contact hour breakdowns, and active Bloom's taxonomy objectives.
  - **Files Modified**: `courses/cosc-2060-data-engineering/units/unit_0[1-8]_*/overview.md`
  - **Check**: Verify all 8 `overview.md` files exist and contain learning objectives. (Passed: All 8 overviews authored with contact hour budgets and Bloom's verbs)

- [x] **Task 4: Author 8 Unit Knowledge Check Quizzes**
  - **Action**: Author `quiz.md` for Units 1 through 8 (10 questions each, 80 total questions) with 4 options and complete Answer Key tables with concept rationales.
  - **Files Modified**: `courses/cosc-2060-data-engineering/units/unit_0[1-8]_*/quiz.md`
  - **Check**: Parse all 8 quiz files using `qti_builder.parse_quiz_md()` verifying 80 total questions parsed. (Passed: All 80 questions parsed with 4 options, verified answer keys, and concept rationales)

- [x] **Task 5: Execute Canvas Common Cartridge Compilation**
  - **Action**: Run `build_course.py` to compile the complete `.imscc` package, validate XML syntax, and generate the Word syllabus.
  - **Files Modified**: `courses/cosc-2060-data-engineering/COSC_2060_Complete.imscc`
  - **Check**: Verify `.imscc` file size and confirm all XML files pass `ElementTree` validation. (Passed: 38 XML files validated with 0 syntax errors; generated 81-file `COSC_2060_Complete.imscc` [0.28 MB])

---

## Verification & Retrospective Audit
- [x] Run full XML schema audit across all generated module pages and QTI quizzes. (Passed: 38 XML files verified by ElementTree)
- [x] Audit against every requirement in `spec.md` (Pass/Fail table).

| Requirement | Description | Status | Evidence |
| :--- | :--- | :--- | :--- |
| **REQ-01** | 8 Unit Knowledge Check quiz files in Markdown conforming to template | **PASS** | 8 `quiz.md` files created in `units/unit_0[1-8]_*/`. |
| **REQ-02** | 10 questions per quiz (80 total) with 4 options and rationale answer keys | **PASS** | `test_quizzes.py` verified 80/80 questions with 4 choices and detailed rationales. |
| **REQ-03** | Canvas QTI config (20 pts, 3 attempts, highest score kept) | **PASS** | Generated `assessment_meta.xml` configured for 20 pts and 3 attempts. |
| **REQ-04** | 8 Unit Overviews with 300m contact hour budgets & Bloom's objectives | **PASS** | 8 `overview.md` files authored with active Bloom's verbs and contact hour budgets. |
| **REQ-05** | `course_config.json` with weighted groups & competencies | **PASS** | JSON verified with 4 weighted groups (40% Labs, 20% Quizzes, 10% Drills, 30% Capstone). |
| **REQ-06** | Pure Python QTI 1.2 XML conversion with zero errors | **PASS** | All 8 quizzes compiled to QTI 1.2 XML, validated with ElementTree. |
| **REQ-07** | Package complete `.imscc` Common Cartridge | **PASS** | Created `courses/cosc-2060-data-engineering/COSC_2060_Complete.imscc` (81 files). |
| **REQ-08** | Authentic data engineering scenarios tested across all units | **PASS** | DuckDB, Polars, Pydantic, CLIP, RAG, FastAPI, MCP, DAGs tested. |
| **REQ-09** | Fail-fast validation on question parsing errors | **PASS** | Verified via parser assertions. |
| **REQ-10** | Course sandboxing strictly maintained | **PASS** | All course content, units, and `.imscc` package reside strictly in `courses/cosc-2060-data-engineering/`. |

- [x] User review and sign-off.

