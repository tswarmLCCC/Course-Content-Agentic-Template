# Feature Specification: Toolchain & Catalog Migration from CMAP 1815 Autogen

- **ID**: `specs/001-toolchain-and-catalog-migration`
- **Status**: Approved
- **Created**: 2026-10-24
- **Target Completion**: 30 minutes

---

## 1. Objective & Target Audience
- **Primary Persona**: Curriculum Author & Agentic AI Assistant working across independent courses in `courses/<course-id>/`.
- **Problem Statement**: The legacy `CMAP_1815_Autogen` workspace contained powerful automation engines (Canvas Common Cartridge compiler, QTI 1.2 quiz builder, DesignPLUS HTML styler, 16:9 slide generator, and Word syllabus cloner), but became cumbersome due to code duplication across 4 different folders and tight coupling with course content.
- **One Job**: Migrate the complete automation toolchain, Antigravity skills, pedagogical playbooks, and institutional templates into modular, sandboxed locations (`.agents/skills/`, `docs/playbooks/`, `specs/_templates/`) without polluting individual course directories.

---

## 2. Requirements (EARS Syntax)

- **Always (Ubiquitous)**:
  - `REQ-01`: The system **shall** package all agent-executable automation tools under `.agents/skills/<skill-name>/` with valid Antigravity `SKILL.md` frontmatter and self-contained scripts.
  - `REQ-02`: The system **shall** ensure all core tools in `canvas-course-builder` (`qti_builder.py`, `html_styler.py`, `build_cartridge.py`) operate using pure Python 3 standard library with zero external pip dependencies.
- **When (Event-Driven)**:
  - `REQ-03`: **When** an agent invokes `canvas-course-builder`, the system **shall** provide executable scripts to parse Markdown quizzes into Canvas QTI 1.2 XML with rationales, apply DesignPLUS CSS styling to Markdown/HTML, and package complete `.imscc` cartridges.
  - `REQ-04`: **When** an agent invokes `slide-deck-generator`, the system **shall** provide an executable Python engine to generate 16:9 widescreen PowerPoint (`.pptx`) decks conforming to WCAG 2.1 AAA contrast and the 5 standard slide archetypes.
  - `REQ-05`: **When** an agent invokes `syllabus-docx-cloner`, the system **shall** provide an automated workflow to clone and update institutional Word `.docx` syllabi with full style and XML schema fidelity.
  - `REQ-06`: **When** an agent invokes `course-intake-scanner`, the system **shall** provide a drop-zone scanner script to inventory unstructured assets into a competency map.
- **While (State-Driven)**:
  - `REQ-07`: **While** operating in any course directory under `courses/<course-id>/`, the migrated skills and tools **shall** remain decoupled and universally accessible without copying tool scripts into course folders.
- **If-Then (Error/Unwanted Behavior)**:
  - `REQ-08`: **If** any migrated tool is executed, it **shall not** modify files outside its target course or output directory, and **shall not** mutate existing course content in `courses/cosc-2060-data-engineering/`.
- **Where (Optional Features / Living Docs)**:
  - `REQ-09`: The system **shall** store pedagogical playbooks in `docs/playbooks/` and institutional rubric/instructional templates in `specs/_templates/`.
  - `REQ-10`: The system **shall** update master documentation in `README.md` and `AGENTS.md` to document the available skills and their invocation patterns.

---

## 3. Deliberately Out of Scope
- Migrating CMAP 1815-specific unit files, lecture notes, or SQLite/Postgres dataset SQL files (`units/`, `sql/`, `shared_assets/datasets/`).
- Modifying or altering existing COSC 2060 course curriculum in `courses/cosc-2060-data-engineering/`.
- Introducing third-party web frameworks or heavy Node.js dependencies for Canvas packaging.

---

## 4. Acceptance Criteria & Definition of Done
- [ ] `.agents/skills/canvas-course-builder/` contains `SKILL.md`, `scripts/`, `templates/`, and `references/`.
- [ ] `.agents/skills/slide-deck-generator/` contains `SKILL.md` and `scripts/`.
- [ ] `.agents/skills/syllabus-docx-cloner/` contains `SKILL.md` and `scripts/` (with master syllabus template).
- [ ] `.agents/skills/course-intake-scanner/` contains `SKILL.md` and `scripts/`.
- [ ] `docs/playbooks/` contains all 4 pedagogical and production playbooks.
- [ ] `specs/_templates/` contains instructional and rubric templates.
- [ ] Pure Python tools (`qti_builder.py`, `html_styler.py`, `build_cartridge.py`) execute without syntax or import errors.
- [ ] `README.md` and `AGENTS.md` updated with the new skills catalog.
