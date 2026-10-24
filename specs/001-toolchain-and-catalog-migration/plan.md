# Technical & Architectural Plan: Toolchain & Catalog Migration

- **Spec Reference**: [spec.md](file:///c:/dev/Course-Content-Agentic-Template/specs/001-toolchain-and-catalog-migration/spec.md)
- **Status**: Approved
- **Created**: 2026-10-24

---

## 1. Technical Architecture & Approach

### Component Layout
1. **Workspace Skills (`.agents/skills/`)**:
   - `.agents/skills/canvas-course-builder/`:
     - `SKILL.md`: Activation trigger, 8-item Canvas module taxonomy, page formatting rules.
     - `scripts/build_cartridge.py`: Pure Python `.imscc` compiler.
     - `scripts/qti_builder.py`: Markdown quiz to QTI 1.2 XML converter.
     - `scripts/html_styler.py`: DesignPLUS CSS and markdown-to-HTML formatter.
     - `scripts/docx_syllabus.py`: Institutional Word syllabus updater.
     - `templates/course_config.example.json`: Sample course configuration for Common Cartridge build.
     - `templates/unit_quiz_template.md`: Standard markdown quiz format with answer key & rationales.
     - `references/designplus_guide.md`: DesignPLUS CSS class cheat sheet.
     - `references/canvas_cc_architecture.md`: IMS Common Cartridge XML specification mapping.
   - `.agents/skills/slide-deck-generator/`:
     - `SKILL.md`: 5 slide archetypes, WCAG AAA palette, speaker note rules.
     - `scripts/slide_engine.py`: Programmatic `python-pptx` widescreen deck builder.
     - `scripts/audit_deck.py`: Contrast and accessibility audit script.
   - `.agents/skills/syllabus-docx-cloner/`:
     - `SKILL.md`: Institutional Word XML cloning and syllabus transformation guide.
     - `scripts/docx_syllabus.py`: Script to extract and modify Word XML without style loss.
     - `templates/LCCC_Master_Syllabus_Template.docx`: Gold-standard Word document template.
   - `.agents/skills/course-intake-scanner/`:
     - `SKILL.md`: Workflow for cataloging raw syllabi, transcripts, and decks.
     - `scripts/intake_scanner.py`: Scanner script generating `scaffolded_course_plan.md`.

2. **Pedagogical Playbooks (`docs/playbooks/`)**:
   - `COURSE_PRODUCTION_WORKFLOW.md`: Master end-to-end course production standard.
   - `SLIDE_DESIGN_PLAYBOOK.md`: Visual hierarchy and cognitive load design rules.
   - `WHY_WHAT_HOW_PEDAGOGY.md`: 3-phase pedagogical scaffolding architecture.
   - `ZERO_COST_INFRASTRUCTURE.md`: Open-source and institutional resource guidelines.

3. **Curriculum & Rubric Templates (`specs/_templates/`)**:
   - `instructional/`: Instructional guide, competency map, demo contingency runbooks.
   - `rubrics/`: Capstone defense rubric, course audit rubric, peer review rubric.
   - `code_labs/`: Code lab template.

---

## 2. ADR Conformance & Constraints

- **Accessibility Check (ADR-001)**:
  - Slide engine enforces minimum 7:1 contrast ratio (WCAG 2.1 AAA) across all 5 archetypes.
  - HTML styler uses semantic HTML5 elements (`<details>`, `<summary>`, styled `<table>` with headers and `aria-label`).
- **Platform Constraints**:
  - `canvas-course-builder` tools rely purely on standard library `os`, `re`, `html`, `hashlib`, `xml.etree.ElementTree`, and `zipfile`—guaranteeing portability across any instructor machine.
  - Skill scripts must be executable directly from their directory or via standard python invocation.
- **Privacy & Sandboxing**:
  - All tools operate strictly on input/output directories supplied via arguments or configurations.
  - No course files in `courses/cosc-2060-data-engineering/` are touched.

---

## 3. Dependency Graph & Risk Mitigation

- **Prerequisites**: Source files in `..\CMAP_1815_Autogen` accessible via filesystem.
- **Known Risks**:
  - Path differences when scripts run from different working directories:
    * *Mitigation*: Ensure script relative path lookups use `__file__` directory resolution where applicable.
  - Missing `python-pptx` on student/instructor machines for slide generator:
    * *Mitigation*: Clearly document optional pip requirements in `slide-deck-generator/SKILL.md`. Core Canvas tools remain 100% zero-dependency.
