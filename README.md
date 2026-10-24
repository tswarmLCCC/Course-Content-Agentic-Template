# Course-Content-Agentic-Template

> **An Agentic Engineering Engine for Building Rigorous, Verifiable Course Content**  
> *Driven by Spec-Driven Development (SDD), EARS requirements syntax, and isolated monorepo course silos.*

---

## 1. What This Repository Is

This repository is **not just a folder of files**—it is a structured, AI-assisted curriculum authoring engine. 

Most people build courses with AI by chatting, getting a draft, and spending hours manually editing it ("vibe authoring"). This system uses **Spec-Driven Development (SDD)**:
1. **Write requirements first** before generating any curriculum, code, or exercises.
2. **AI interviews you (sparring)** one question at a time to surface edge cases, technical constraints, and out-of-scope items.
3. **Markdown files serve as the permanent memory**, ensuring work continues cleanly across sessions without context loss.
4. **Strict course sandboxing** allows multiple independent courses to live in the same repository without confusion.
5. **Idea validation and architectural research**: The AI functions as an active pedagogical research partner—analyzing cognitive load, prerequisite sequencing, and industry relevance before writing specs.


---

## 2. Repository Layout & Mental Model

```
Course-Content-Agentic-Template/
├── README.md                  # This living user manual & operational guide
├── AGENTS.md                  # Master rules governing AI agent behavior
├── CURRENT.md                 # Single source of truth: Active Course & Active Iteration
│
├── .agents/                   # Native Antigravity Workspace Skills (Zero Course Pollution)
│   └── skills/
│       ├── canvas-course-builder/  # QTI 1.2 quiz builder, DesignPLUS HTML styler, .imscc compiler
│       ├── slide-deck-generator/   # Programmatic 16:9 WCAG AAA PowerPoint (.pptx) engine
│       ├── syllabus-docx-cloner/   # Institutional Word (.docx) syllabus cloner
│       └── course-intake-scanner/  # Drop-zone scanner for raw curriculum intake
│
├── docs/
│   ├── ADRs/                  # Architectural Decision Records (Universal standards)
│   │   ├── ADR-001-accessibility.md           # WCAG 2.2 AA non-negotiable
│   │   ├── ADR-002-spec-driven-development.md # Mandatory SDD lifecycle
│   │   └── ADR-003-canvas-designplus-standards.md # Common Cartridge & DesignPLUS theme invariants
│   ├── playbooks/             # Pedagogical & Production Master Playbooks
│   │   ├── MASTER_COURSE_SETUP_AND_FORMATTING_GUIDE.md # Complete production blueprint
│   │   ├── COURSE_PRODUCTION_WORKFLOW.md      # End-to-end production pipeline
│   │   ├── SLIDE_DESIGN_PLAYBOOK.md           # Visual hierarchy & cognitive load rules
│   │   ├── WHY_WHAT_HOW_PEDAGOGY.md           # 3-phase scaffolding model
│   │   └── ZERO_COST_INFRASTRUCTURE.md        # Open-source lab standards
│   └── data_engineering_course_incoming_plan.md # Reference curriculum blueprints
│
├── prompts/                   # Living library of authoring prompts & skill blueprints
│   └── course_authoring_prompts.md # Prompts for high-rigor readings, labs, and sparring
│
├── specs/
│   └── _templates/            # Reusable templates for new units & modules
│       ├── spec_template.md   # EARS syntax requirements template
│       ├── plan_template.md   # Architectural & instructional design plan
│       ├── tasks_template.md  # Ordered task checklist with verification checks
│       ├── rubrics/           # Capstone defense, course audit, and peer review rubrics
│       ├── instructional/     # Competency maps, contingency runbooks, guides
│       ├── syllabi/           # Master Word syllabus template
│       └── code_labs/         # Standardized code lab template
│
├── courses/                   # Siloed Course Catalog
│   └── <course-id>/           # E.g. cosc-2060-data-engineering
│       ├── README.md          # Course overview, terminal competencies, schedule
│       ├── specs/             # Unit-specific specs (001-unit1-reading, etc.)
│       └── content/           # Generated deliverables (Markdown readings, Canvas HTML, labs)
│
└── ref/                       # Reference slide decks, PDFs, and gold-standard examples
```

---

## 3. How to Use This System (Instructor Workflow)

### A. Starting or Switching an Active Course
To prevent the AI from confusing different subjects, all work is sandboxed through **[CURRENT.md](file:///c:/dev/Course-Content-Agentic-Template/CURRENT.md)**:
1. Open `CURRENT.md`.
2. Set `Active Course: courses/<course-id>`.
3. Set `Active Iteration: specs/<NNN-feature-name>`.
4. When you interact with the agent, it will strictly read and write inside that course directory.

### B. The 4-Stage Authoring Cycle

Every unit of curriculum (a reading guide, a lab assignment, a quiz bank, an interactive demo) goes through four explicit stages:

```
[1. Specify] ──> [2. Plan] ──> [3. Tasks] ──> [4. Implement & Verify]
```

1. **Stage 1: Specify (`specs/<NNN>/spec.md`)**
   - The agent interviews you (**one question at a time**) about target learners, prerequisites, learning friction, and out-of-scope boundaries.
   - The agent drafts the spec using **EARS** (*Easy Approach to Requirements Syntax*):
     - *Always:* Ubiquitous requirements.
     - *When:* Event-driven requirements.
     - *While:* State-driven requirements.
     - *If-Then:* Unwanted behavior and error handling.
     - *Where:* Optional configurations.
   - **Review checkpoint:** You review and approve the spec before anything is drafted.

2. **Stage 2: Plan (`specs/<NNN>/plan.md`)**
   - The spec is translated into instructional architecture, code dependencies, dataset schemas, and pedagogical metaphors.
   - Cross-checked against **ADR-001 (Accessibility)** and **ADR-002 (SDD)**.
   - **Review checkpoint:** You verify the plan and technical constraints.

3. **Stage 3: Tasks (`specs/<NNN>/tasks.md`)**
   - Work is decomposed into 15–30 minute increments ordered strictly by dependency.
   - Every single task contains an explicit `Check:` verification step.

4. **Stage 4: Implement & Verify (`content/`)**
   - The agent authors the content or code directly from the spec, executing the verification check for each task.
   - When complete, the agent conducts a **Pass/Fail Audit** against every single EARS requirement in `spec.md`.

---

## 4. Quality Standards & Golden Rules

- **Rigor Benchmark**: All course readings must match the pedagogical depth modeled in [ref/unit_reading_example.html](file:///c:/dev/Course-Content-Agentic-Template/ref/unit_reading_example.html). This means:
  - Deep narrative framing of real-world industry friction (why naive approaches fail).
  - Concrete mental models and conceptual metaphors.
  - Complete, syntactically verified code snippets with line-by-line annotations.
  - Guided student hands-on terminal/CLI practice.
  - Frequently Asked Questions and exact quoted error messages with explanations.
- **Human-Review First**: Initial drafts are generated in clean, semantic Markdown. Visual styling or complex HTML formatting is deferred until the pedagogical content is verified.
- **Accessibility by Default**: Under **[ADR-001](file:///c:/dev/Course-Content-Agentic-Template/docs/ADRs/ADR-001-accessibility.md)**, everything created must target WCAG 2.2 AA (minimum WCAG 2.1 AA).
- **Prompt Curation**: High-performing prompts used during authoring are refined and permanently stored in **[prompts/course_authoring_prompts.md](file:///c:/dev/Course-Content-Agentic-Template/prompts/course_authoring_prompts.md)** so they can be reused or converted into Antigravity IDE skills.

---

## 5. Agent Tools & Automation Skills Catalog

This repository includes a portable, modular automation toolchain located under `.agents/skills/`. Because these tools live in `.agents/skills/`, they are automatically discoverable by AI agents working across any course in the workspace without duplicating code into course folders.

| Skill / Tool | Path | Dependencies | Core Capabilities |
| :--- | :--- | :--- | :--- |
| **Canvas Course Builder** | [`.agents/skills/canvas-course-builder/`](file:///c:/dev/Course-Content-Agentic-Template/.agents/skills/canvas-course-builder/SKILL.md) | **Zero** (Pure Python 3 standard library) | • Enforces mandatory Canvas WikiPage `<head>` metadata (`identifier`, `editing_roles`, `workflow_state`, `editor_type`) to eliminate sandboxed `<iframe>` attachments and "Download HTML" headers.<br>• Generates native Canvas Front Page (`home-page.html`) with `<meta name="front_page" content="true"/>` and interactive DesignPLUS Module Accordions (`dp-quick-links-panels-accordion-plus`).<br>• Renders DesignPLUS ribbon headers and collapsible accordion panels (`dp-panels-wrapper dp-accordion-plus`) for Unit Overviews.<br>• Compiles QTI 1.2 XML quizzes with comprehensive rationales and packages complete `.imscc` Common Cartridges. |
| **Slide Deck Generator** | [`.agents/skills/slide-deck-generator/`](file:///c:/dev/Course-Content-Agentic-Template/.agents/skills/slide-deck-generator/SKILL.md) | `python-pptx` | • Programmatically generates 16:9 widescreen PowerPoint (`.pptx`) decks.<br>• Enforces WCAG 2.1 AAA contrast ratios across 5 proven slide archetypes.<br>• Automates 100% speaker notes coverage and contrast audits. |
| **Syllabus Word Cloner** | [`.agents/skills/syllabus-docx-cloner/`](file:///c:/dev/Course-Content-Agentic-Template/.agents/skills/syllabus-docx-cloner/SKILL.md) | Standard Library (`zipfile`, `re`) | • Clones and updates institutional Word (`.docx`) syllabi preserving 100% style fidelity and Word XML schemas.<br>• Updates course codes, schedules, grading policies, and accreditation text. |
| **Course Intake Scanner** | [`.agents/skills/course-intake-scanner/`](file:///c:/dev/Course-Content-Agentic-Template/.agents/skills/course-intake-scanner/SKILL.md) | Standard Library | • Scans unstructured assets across drop zones (`raw_syllabi/`, `legacy_decks/`, `transcripts/`).<br>• Scaffolds competency maps and unit outlines. |

### The 8-Item Standard Canvas Module Sequence
Every weekly unit produced by `canvas-course-builder` follows a battle-tested sequence inside Canvas LMS:
1. `Unit X Overview: [Topic]` (`WikiPage` - Published) — DesignPLUS banner ribbon, interactive accordions for Objectives, Roadmap, and Contact Hours.
2. `Unit X: Required Readings & Video Lectures` (`WikiPage` - Published) — Clean standard layout or DesignPLUS multi-ribbon chapters.
3. `Unit X: Asynchronous Preparation & Drills` (`WikiPage` - Published) — Conceptual focus questions with interactive `<details>/<summary>` self-check answer keys.
4. `Unit X: Applied Lab Guide` (`WikiPage` - Published) — Scenario instructions, defensive engineering edge cases, and native HTML rubric tables.
5. `Unit X Applied Lab Assignment` (`Assignment` - Published) — Native 50-pt Canvas Assignment for SpeedGrader file upload or text entry.
6. `Unit X: Learn with AI — Supplemental Practice Drill` (`WikiPage` - Published) — Socratic AI roleplay scenario, free tool guides, and reflection prompts.
7. `Unit X Knowledge Check: [Topic]` (`Quizzes::Quiz` - Published) — Native Canvas QTI 1.2 quiz (multiple-choice with full rationales, 3 attempts).
8. `[Instructor Guide] Unit X Teaching Notes & Solutions` (`WikiPage` - Unpublished) — Hidden from students; contains synchronous agendas and master solution keys.

### The 4-Slot Flipped Classroom Model & DS-to-DE Transition Notebook Pattern
Every 2-week instructional unit balances asynchronous conceptual preparation with rigorous in-class live coding clinics:
- **Slot 1 (Out-of-Class 1, 75m)**: Asynchronous conceptual preparation — high-rigor reading guide, mental model videos, OER references, and self-check drills with `<details>/<summary>` answer keys.
- **Slot 2 (In-Class 1, 75m)**: Live Coding Clinic ("I Do, We Do") — real-world incident retrospective, architecture whiteboard sparring, and hands-on execution of the **DS-to-DE Transition Notebook**.
- **Slot 3 (Out-of-Class 2, 75m)**: Asynchronous lab onboarding — applied scenario briefing, environment setup, and walkthrough video.
- **Slot 4 (In-Class 2, 75m)**: Active Lab Hacking ("You Do") — live student coding, 1-on-1 bug triage, and terminal-based defensive test harness verification.

#### The 8-Cell Transition Notebook Pattern
To bridge the cognitive gap between data science prototypes and production data engineering engines, units feature interactive Jupyter notebooks following an 8-cell pedagogical progression:
1. **Scenario & Persona Framing**: Contextualized as inheriting a naive prototype from a junior data scientist.
2. **Naive Python Prototype**: Baseline using familiar single-threaded tools (Pandas, Scikit-learn, PIL, unvalidated Pickle).
3. **The Scaling Ceiling / Bottleneck**: Profiling execution time, peak memory usage, or safety vulnerabilities on realistic workloads.
4. **The Modern Data Engineering Engine**: Production refactoring utilizing high-performance, memory-mapped, or vectorized engines (DuckDB `ASOF LEFT JOIN`, Polars Lazy Expressions, OpenCV C-contiguous tensors, ChromaDB vector indexing, FastAPI + Pydantic v2 async validation, MCP JSON-RPC 2.0 servers, Asset DAGs, and Dockerized Pytest quality gates).
5. **Head-to-Head Profiling & Benchmark**: Direct speedup and memory footprint visualization.
6. **Line-by-Line Architectural Teardown**: Pedagogical breakdown of internal mechanics (vectorization, SIMD, lazy evaluation, zero-copy memory).
7. **Deterministic Output & Parity Verification**: Strict test assertions verifying mathematical and business logic parity between the naive prototype and engine output.
8. **Defensive Engineering & Take-Home Challenge**: Edge case injection (dirty schemas, missing keys, high concurrency) challenging students to harden the pipeline.

### Command & Tool Invocation Cheatsheet
All tools are executable directly via standard Python 3:

```bash
# 1. Compile Full Course into Canvas Common Cartridge (.imscc)
python .agents/skills/canvas-course-builder/build_course.py --config courses/cosc-2060-data-engineering/course_config.json --units-dir courses/cosc-2060-data-engineering/units --output courses/cosc-2060-data-engineering/COSC_2060_Complete.imscc

# 2. Compile Markdown Quiz into Canvas QTI 1.2 XML
python -c "import sys; sys.path.insert(0, '.agents/skills/canvas-course-builder/scripts'); import qti_builder; qs = qti_builder.parse_quiz_md('path/to/quiz.md'); xml = qti_builder.build_qti_xml('quiz_01', 'Unit 1 Quiz', qs); open('output/quiz.xml', 'w').write(xml)"

# 3. Generate 16:9 Widescreen PowerPoint Presentation (.pptx)
python -c "import sys; sys.path.insert(0, '.agents/skills/slide-deck-generator/scripts'); from slide_engine import SlideEngine; prs = SlideEngine.create_presentation(); SlideEngine.add_title_slide(prs, 'LCCC', 'COSC 2060', 'Unit 01', 'Intro to Modern Data Eng', 'Instructor'); prs.save('unit_01.pptx')"

# 4. Clone and Transform Institutional Word (.docx) Syllabus
python -c "import sys; sys.path.insert(0, '.agents/skills/syllabus-docx-cloner/scripts'); import docx_syllabus; docx_syllabus.update_syllabus('.agents/skills/syllabus-docx-cloner/templates/LCCC_Master_Syllabus_Template.docx', 'COSC 2060: Modern Data Engineering', 'output/syllabus.docx')"

# 5. Scan Drop Zones for Curriculum Intake
python .agents/skills/course-intake-scanner/scripts/intake_scanner.py
```

### Master Pedagogical Playbooks
Located in [`docs/playbooks/`](file:///c:/dev/Course-Content-Agentic-Template/docs/playbooks/):
- **[Master Course Setup & Formatting Playbook](file:///c:/dev/Course-Content-Agentic-Template/docs/playbooks/MASTER_COURSE_SETUP_AND_FORMATTING_GUIDE.md)**: Comprehensive reference for DesignPLUS styling, color palettes, and LMS best practices.
- **[Course Production Workflow](file:///c:/dev/Course-Content-Agentic-Template/docs/playbooks/COURSE_PRODUCTION_WORKFLOW.md)**: End-to-end production pipeline from intake to Canvas deployment.
- **[Slide Design Playbook](file:///c:/dev/Course-Content-Agentic-Template/docs/playbooks/SLIDE_DESIGN_PLAYBOOK.md)**: Visual hierarchy, contrast, and cognitive load management.
- **[Why/What/How Pedagogy](file:///c:/dev/Course-Content-Agentic-Template/docs/playbooks/WHY_WHAT_HOW_PEDAGOGY.md)**: 3-phase pedagogical scaffolding architecture.
- **[Zero-Cost Infrastructure](file:///c:/dev/Course-Content-Agentic-Template/docs/playbooks/ZERO_COST_INFRASTRUCTURE.md)**: Standards for open-source tools and zero-cost student labs.

### Shared Instructional & Rubric Templates
Located in [`specs/_templates/`](file:///c:/dev/Course-Content-Agentic-Template/specs/_templates/):
- **Instructional (`specs/_templates/instructional/`)**: [competency_map_template.md](file:///c:/dev/Course-Content-Agentic-Template/specs/_templates/instructional/competency_map_template.md), [instructional_guide_template.md](file:///c:/dev/Course-Content-Agentic-Template/specs/_templates/instructional/instructional_guide_template.md), [demo_contingency_runbook_template.md](file:///c:/dev/Course-Content-Agentic-Template/specs/_templates/instructional/demo_contingency_runbook_template.md)
- **Rubrics (`specs/_templates/rubrics/`)**: [capstone_defense_rubric_template.md](file:///c:/dev/Course-Content-Agentic-Template/specs/_templates/rubrics/capstone_defense_rubric_template.md), [course_audit_rubric.md](file:///c:/dev/Course-Content-Agentic-Template/specs/_templates/rubrics/course_audit_rubric.md), [peer_review_rubric_template.md](file:///c:/dev/Course-Content-Agentic-Template/specs/_templates/rubrics/peer_review_rubric_template.md)
- **Code Labs (`specs/_templates/code_labs/`)**: [code_lab_template.py](file:///c:/dev/Course-Content-Agentic-Template/specs/_templates/code_labs/code_lab_template.py)
- **Syllabi (`specs/_templates/syllabi/`)**: [LCCC_Master_Syllabus_Template.docx](file:///c:/dev/Course-Content-Agentic-Template/specs/_templates/syllabi/LCCC_Master_Syllabus_Template.docx)

---

## 6. Active Courses in this Workspace

| Course ID | Course Code & Title | Units | Active Stage | Directory |
|---|---|---|---|---|
| `cosc-2060-data-engineering` | COSC 2060: Modern Data Engineering & AI Infrastructure | 8 Units (16 Wks) | **Production Canvas Cartridge (.imscc) Compiled** (Readings, Labs, 80 QTI Quizzes, 8 DS-to-DE Transition Notebooks, 8 Coding Clinic PPTX Decks & Word Syllabus) | [courses/cosc-2060-data-engineering/](file:///c:/dev/Course-Content-Agentic-Template/courses/cosc-2060-data-engineering/README.md) |


---

## 7. Living Maintenance Protocol

As we work together and discover new patterns, optimizations, or rules:
- Any new architectural decision is recorded in `docs/ADRs/`.
- Any reusable authoring prompt is added to `prompts/`.
- Any workspace-wide automation skill is added to `.agents/skills/`.
- This `README.md` is updated to reflect changes to the engine, workflows, and catalog.

