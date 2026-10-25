# Task Checklist: Unit 01 — Agentic Foundations & Architectural Patterns

- **Spec Reference**: [`spec.md`](file:///c:/dev/Course-Content-Agentic-Template/modules/agentic-ai-introduction/specs/001-agentic-foundations-and-patterns/spec.md)
- **Plan Reference**: [`plan.md`](file:///c:/dev/Course-Content-Agentic-Template/modules/agentic-ai-introduction/specs/001-agentic-foundations-and-patterns/plan.md)

---

## Task Execution Sequence

- [x] **Task 1: Author Unit 01 Overview & Learn with AI Practice**
  - **Action**: Create `units/unit_01_agentic_foundations/overview.md` with contact hour budget, objectives, and roadmap, plus `learn_with_ai.md` with the Architecture Reviewer sparring prompt.
  - **Check**: Files exist on disk, contain zero broken links, and conform to DesignPLUS markdown guidelines. *(PASSED - verified files present and validated)*

- [x] **Task 2: Author 4-Chapter OER Reading Guide with Video Embed & Citations**
  - **Action**: Create `units/unit_01_agentic_foundations/reading.md` embedding Smitha Kolan's video, detailing the 3 patterns, the Yao et al. ReAct paper, the 5 Anthropic workflows, and Poka-Yoke tool design.
  - **Check**: File size > 15 KB, includes YouTube 16:9 iframe embed, academic citation for ReAct, and Anthropic research citation. *(PASSED - file size is 22.5 KB with full citations and responsive iframe)*

- [x] **Task 3: Author Asynchronous Preparation & Formative Drills**
  - **Action**: Create `units/unit_01_agentic_foundations/drills.md` with 4 conceptual focus questions and 3 ReAct state machine trace exercises.
  - **Check**: File contains at least 4 interactive `<details><summary>` expandable solution cards. *(PASSED - verified 7 interactive accordions)*

- [x] **Task 4: Author Applied Lab Guide, Starter Code, and Grading Rubric**
  - **Action**: Create `units/unit_01_agentic_foundations/lab_guide.md`, `rubric.md`, and executable `starter_blog_agents.py` implementing the Planner $\to$ Writer $\to$ Validator self-correcting loop.
  - **Check**: `python units/unit_01_agentic_foundations/starter_blog_agents.py` executes successfully in terminal with zero pip dependencies, demonstrating the auto-correcting loop. *(PASSED - exited with code 0, score 100/100, 2 iterations)*

- [x] **Task 5: Author 15-Question QTI 1.2 Knowledge Check Quiz**
  - **Action**: Create `units/unit_01_agentic_foundations/quiz.md` matching `templates/unit_quiz_template.md` with 15 questions covering video, ReAct, and Anthropic concepts with answer key.
  - **Check**: `python -c "import sys; sys.path.insert(0, '.agents/skills/canvas-course-builder/scripts'); import qti_builder; qs = qti_builder.parse_quiz_md('modules/agentic-ai-introduction/units/unit_01_agentic_foundations/quiz.md'); assert len(qs) == 15"` reports 15 parsed questions. *(PASSED - 15/15 questions parsed and compiled to QTI XML)*

- [x] **Task 6: Author Siloed Instructor Notes & Master Solutions**
  - **Action**: Create `units/unit_01_agentic_foundations/teaching_notes.md` with synchronous lecture breakdown, pacing, and master solution key.
  - **Check**: File exists and is tagged for unpublished workflow state. *(PASSED - verified 75-minute agenda, whiteboard exercises, and solution code)*

- [x] **Task 7: Compile Modular Cartridge (`_Modules_Import.imscc`) & Run XML Audit**
  - **Action**: Execute `python .agents/skills/canvas-course-builder/build_course.py --modular --config modules/agentic-ai-introduction/module_config.json --units-dir modules/agentic-ai-introduction/units --output modules/agentic-ai-introduction/Agentic_AI_Introduction_Modules_Import.imscc`.
  - **Check**: Cartridge builds cleanly with 0 XML errors, verifies all schema manifests, and excludes course homepage/syllabus. *(PASSED - 10 XML files verified with 0 errors, created 1.00 MB package)*

- [x] **Task 8: Content Hygiene Scan, EARS Audit & Clean Git Commit**
  - **Action**: Author/run audit script verifying zero dead `file:///` links, zero unrendered code blocks, and 100% compliance with EARS requirements.
  - **Check**: All 19 EARS requirements in `spec.md` verified PASS. *(PASSED - all HTML hygiene checks passed, dead links eliminated)*

---

## Definition of Done
- [x] Standalone cartridge `modules/agentic-ai-introduction/Agentic_AI_Introduction_Modules_Import.imscc` generated and verified.
- [x] Working tree clean in git.
