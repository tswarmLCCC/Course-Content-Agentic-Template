# Feature Specification: Canvas Quizzes, Unit Overviews & 8-Item Sequence Completion

- **ID**: `courses/cosc-2060-data-engineering/specs/003-canvas-quizzes-and-sequence-completion`
- **Course**: `COSC 2060: Modern Data Engineering & AI Infrastructure`
- **Status**: Approved
- **Created**: 2026-10-24
- **Target Completion**: 45 minutes

---

## 1. Objective & Target Audience
- **Primary Persona**: College sophomore/junior students taking COSC 2060, and instructors deploying the course into Canvas LMS.
- **Problem Statement**: The course repository contains rich narrative readings, hands-on lab guides, and flipped classroom guides for all 8 units, but lacks the formal Knowledge Check quizzes, unit overview roadmaps, and course config required to compile a complete, production-grade Canvas Common Cartridge (`.imscc`).
- **One Job**: Author 8 unit quizzes (10 questions each, 80 total, with comprehensive concept rationales), 8 unit overview roadmaps, and the master `course_config.json` to complete the institutional 8-item Canvas module sequence.

---

## 2. Requirements (EARS Syntax)

- **Always (Ubiquitous)**:
  - `REQ-01`: The system **shall** author 8 distinct Unit Knowledge Check quiz files in Markdown conforming strictly to [unit_quiz_template.md](file:///c:/dev/Course-Content-Agentic-Template/.agents/skills/canvas-course-builder/templates/unit_quiz_template.md).
  - `REQ-02`: Each quiz **shall** contain exactly 10 questions with 4 distinct options (A, B, C, D) and a structured Markdown Answer Key table containing the correct option letter and conceptual rationale explaining why the answer is correct and common student misconceptions.
  - `REQ-03`: Each quiz **shall** be configured for Canvas LMS with 20 points possible (2 points per question), 3 allowed attempts, and the highest score retained.
  - `REQ-04`: The system **shall** author 8 Unit Overview markdown files (`overview.md`) detailing the weekly topic narrative, 300-minute contact hour budget (150m study / 150m lab), active learning objectives, and prerequisite checkpoints.
  - `REQ-05`: The system **shall** generate a `course_config.json` containing course metadata (COSC 2060), grading scale, learning outcomes, and weighted assignment groups (Hands-on Labs: 40%, Unit Quizzes: 20%, Preparation & Drills: 10%, Comprehensive Capstone: 30%).
- **When (Event-Driven)**:
  - `REQ-06`: **When** `build_course.py` is executed, the system **shall** convert all 8 markdown quizzes into standard Canvas QTI 1.2 XML assessment packages (`assessment_qti.xml` and `assessment_meta.xml`) with zero XML parsing errors.
  - `REQ-07`: **When** compiling the cartridge, the system **shall** package a complete, functional `.imscc` Common Cartridge containing all 8 units with native Canvas WikiPages, Assignments, and Quizzes.
- **While (State-Driven)**:
  - `REQ-08`: **While** generating quiz questions, questions **shall** test real data engineering scenarios, query syntax, memory models, vector math, API designs, and debugging edge cases covered in the unit readings and labs.
- **If-Then (Error/Unwanted Behavior)**:
  - `REQ-09`: **If** any quiz question has fewer than 4 choices or is missing from the Answer Key table, **then** `qti_builder.py` validation **shall** reject the build with a descriptive error.
- **Where (Optional Features / Sandboxing)**:
  - `REQ-10`: All deliverables **shall** reside strictly inside `courses/cosc-2060-data-engineering/` under modular unit directories (`units/unit_01_...` through `unit_08_...`), maintaining strict course sandboxing.

---

## 3. Deliberately Out of Scope
- Authoring high-stakes midterm or final proctored exams (quizzes are formative knowledge checks).
- Modifying the existing 8 readings or lab starter Python code.

---

## 4. Acceptance Criteria & Definition of Done
- [ ] 8 Unit Quiz Markdown files authored with 10 questions each (80 total questions) and complete Answer Keys with rationales.
- [ ] 8 Unit Overview Markdown files authored with contact hour budgets and objectives.
- [ ] `course_config.json` generated for COSC 2060.
- [ ] Units organized under `courses/cosc-2060-data-engineering/units/unit_01_...` through `unit_08_...`.
- [ ] Full `.imscc` Common Cartridge compiles cleanly with zero XML validation errors.
