# Task Checklist: AIML 2050 Scaffold & Curriculum Intake

- **Spec Reference**: [`spec.md`](file:///c:/dev/Course-Content-Agentic-Template/courses/aiml-2050-ai-in-the-workforce/specs/001-course-scaffold-and-intake/spec.md)
- **Plan Reference**: [`plan.md`](file:///c:/dev/Course-Content-Agentic-Template/courses/aiml-2050-ai-in-the-workforce/specs/001-course-scaffold-and-intake/plan.md)
- **Course**: AIML 2050: AI in the Workforce

---

## Task Execution Sequence

- [x] **Task 1: Workspace Silo & Mode Setup**
  - **Action**: Switch `CURRENT.md` to `courses/aiml-2050-ai-in-the-workforce`, update root `README.md`, and generate `course_config.json`, master `README.md`, and `syllabus.md`.
  - **Files Modified**: `CURRENT.md`, `README.md`, `courses/aiml-2050-ai-in-the-workforce/*`
  - **Check**: Verified `CURRENT.md` active target points to `courses/aiml-2050-ai-in-the-workforce`.

- [x] **Task 2: Intake Staging & Scaffold Directories**
  - **Action**: Create `intake/` dropzone instructions, configure `local_config.json` resolver, and scaffold `units/unit-01` through `units/unit-08` directories.
  - **Files Modified**: `courses/aiml-2050-ai-in-the-workforce/intake/*`, `local_config.json`, `units/`
  - **Check**: Verified 20 Intel modules detected across filesystem at configured path.

- [ ] **Task 3: Ingest Intel Curriculum & Synthesize 20 &rarr; 8 Matrix with Reading Lists**
  - **Action**: Ingest Intel Table of Contents, parse 20 modules & 5 projects, pair units, align contact hours to 6.0 hrs/week, and define exact slide reading ranges and open-source guides.
  - **Files Modified**: `courses/aiml-2050-ai-in-the-workforce/intake/synthesis_matrix.md`, `course_config.json`, `syllabus.md`
  - **Check**: Formal alignment matrix and reading lists reviewed and approved by user.

- [ ] **Task 4: Define Backward Design Outcomes & Weekly Projects**
  - **Action**: For each of the 8 weeks, establish 2–3 measurable Learning Outcomes and a concrete applied workplace project with grading criteria.
  - **Files Modified**: `courses/aiml-2050-ai-in-the-workforce/syllabus.md`, `course_config.json`, `plan.md`
  - **Check**: 8 distinct project definitions and 9 course-level CLOs validated in `syllabus.md` and `course_config.json`.

- [ ] **Task 5: Author Unit Deliverables (8-Item Sequence)**
  - **Action**: Incrementally author units 01 through 08 (Overviews, Readings, Drills, Labs, SpeedGrader Assignments, AI Drills, QTI Quizzes).
  - **Files Modified**: `units/unit-01/` through `units/unit-08/`
  - **Check**: Python XML validators and QTI parser pass with 0 errors.

- [ ] **Task 6: Final Common Cartridge Compilation**
  - **Action**: Build and verify `AIML_2050_Complete.imscc`.
  - **Files Modified**: `courses/aiml-2050-ai-in-the-workforce/AIML_2050_Complete.imscc`
  - **Check**: Successful zip compression and Canvas import verification.
