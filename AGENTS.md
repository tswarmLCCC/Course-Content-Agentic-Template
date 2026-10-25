# AGENTS.md — Spec-Driven Iteration Guidelines

Instructions for any AI agent or assistant working in this repository. Read this file before doing anything else.

---

## 1. Core Operating Principles

1. **No Spec, No Build**: Never jump straight into code, curriculum, or asset generation from a casual prompt. All work begins with written requirements in a spec document.
2. **Implementation Plan Before Execution**: For every task and iteration step, maintain an implementation plan detailing objectives, architecture/design decisions, step-by-step actions, and verification strategy.
3. **One Question at a Time (Sparring)**: When interviewing or clarifying with the user, ask one focused question at a time (or use structured multiple choice for distinct trade-offs). Stress-test ideas by identifying edge cases and ambiguities early.
4. **Project Memory in Markdown**: The repository's markdown files are the project's permanent memory. Do not rely on ephemeral LLM chat history. Any requirement change, architectural decision, or plan update must be recorded directly in the project files.
5. **Strict Scope Boundaries**: Honor the "Out of Scope" section in the spec and plan. If something seems missing or useful, ask the user first—never silently add unrequested features.
6. **Check Before Checking Off**: Every task in `tasks.md` must have a verifiable check. Never mark a task complete without executing and demonstrating its verification.
7. **Monorepo Sandboxing (Courses & Modules)**: This repository holds both full semester courses in `courses/<course-id>/` and standalone modular imports in `modules/<module-id>/`. The agent **must always check `CURRENT.md`** for the active target and strictly restrict search, read, and write operations to that specific silo directory during authoring.
8. **Living Documentation Maintenance**: Maintain the master [README.md](file:///c:/dev/Course-Content-Agentic-Template/README.md) as a living document. Whenever new workflows, conventions, prompt patterns, courses, or modules are established or updated, immediately update `README.md` to reflect them.
9. **Idea Validation & Research Partner**: Actively research, stress-test, and validate architectural choices, technology selections, and curriculum sequencing before building. Do not merely construct what is proposed; evaluate pedagogical trade-offs (cognitive load on college sophomores, industry relevance, dependency ordering) and offer informed technical recommendations.
10. **Interactive Pop-up Modals for Choices**: When presenting multiple choices, trade-offs, or decisions to the user, always use the interactive `ask_question` tool so the user can easily click their choice directly in the UI.



---

## 2. Monorepo Structure & Sandboxing

```
Course-Content-Agentic-Template/
├── AGENTS.md                  # Master agent rules & lifecycle
├── CURRENT.md                 # Single source of truth: Active Target & Active Iteration
├── .agents/                   # Shared Antigravity Workspace Skills
│   └── skills/                # canvas-course-builder, slide-deck-generator, syllabus-docx-cloner, intake-scanner
├── docs/
│   ├── ADRs/                  # Shared standards (Accessibility, SDD)
│   └── playbooks/             # Pedagogical & production playbooks
├── specs/
│   └── _templates/            # Shared templates (spec, plan, tasks, rubrics, syllabi)
├── courses/                   # Full Semester Course Silos
│   └── <course-id>/           # E.g. cosc-2060-data-engineering
│       ├── README.md          # Course overview, audience, competencies
│       ├── specs/             # Course-specific specs (001-xxx, 002-xxx)
│       ├── units/             # Weekly unit packages (readings, labs, quizzes)
│       └── <code_Complete.imscc> # Full course export
├── modules/                   # Standalone Module Bundles & Modular Imports
│   └── <module-id>/           # E.g. agentic-ai-introduction
│       ├── README.md          # Module overview, audience, target competencies
│       ├── specs/             # Module-specific specs (001-xxx, etc.)
│       ├── units/             # 1-3 modular unit packages
│       └── <name_Modules_Import.imscc> # Modular cartridge for dropping into any host course
└── ref/                       # Reference materials and raw source documents
```

### Sandboxing & Target Modes:
1. **Full Course Mode (`courses/<course-id>/`)**:
   - Compiles a complete Canvas course shell including Front Page (`home-page.html`), Course Orientation module, Institutional Syllabus (`syllabus.html` & `.docx`), and all weekly units.
   - Output: `<Course_Code>_Complete.imscc` placed in the course directory.
2. **Modular Import Mode (`modules/<module-id>/`)**:
   - Compiles standalone 1–3 module packages intended to drop cleanly into any existing course without altering the host course's front page, syllabus, or orientation settings.
   - Cartridge naming standard: Must include a descriptive name with `_Modules_Import.imscc` or `_Standalone_Module.imscc`.
   - Output: Placed directly in the module directory (`modules/<module-id>/`).
3. **Sandboxing Invariant**:
   - **Always read `CURRENT.md` first** to determine the `Active Target`.
   - **Never cross boundaries**: When working on `courses/course-A/` or `modules/module-B/`, never grep, read, or modify files outside that silo.
   - Use shared skills in [`.agents/skills/`](file:///c:/dev/Course-Content-Agentic-Template/.agents/skills/) without copying scripts into course or module folders.

---

## 3. The 4-Stage Iteration Lifecycle

Every unit of work within an active course follows this cycle:

```
[1. Specify] ──> [2. Plan] ──> [3. Tasks] ──> [4. Implement & Verify]
```

### Stage 1: Specify (`courses/<course-id>/specs/<NNN-feature>/spec.md`)
- Conduct a sparring interview: ask who it is for, what problem it solves, what it must do, and what is out of scope.
- Write requirements using **EARS** (*Easy Approach to Requirements Syntax*):
  - **Always**: *The module shall...* (ubiquitous requirement)
  - **When (Event)**: *When [trigger], the system shall...*
  - **While (State)**: *While [in state], the system shall...*
  - **If (Error/Unwanted)**: *If [condition], then the system shall...*
  - **Where (Option)**: *Where [feature/option enabled], the system shall...*
- Stop for user review and confirmation before planning.

### Stage 2: Plan (`courses/<course-id>/specs/<NNN-feature>/plan.md`)
- Translate the spec into architecture, data structures, instructional design, or file layouts.
- Cross-reference with existing Architectural Decision Records (`docs/ADRs/`).
- Define explicit technical constraints, dependencies, and out-of-scope boundaries.
- Stop for user review before task decomposition.

### Stage 3: Tasks (`courses/<course-id>/specs/<NNN-feature>/tasks.md`)
- Decompose the plan into bite-sized, ordered tasks (15–30 minute increments).
- Order tasks strictly by dependency.
- Include a concrete `Check:` step for each task (a test command, visual verification, or acceptance criteria).

### Stage 4: Implement & Verify
- Implement one task at a time, strictly following the specification.
- Run the task's `Check:` step and present evidence of completion.
- When all tasks are complete, perform a full pass/fail audit against every EARS requirement in `spec.md`.

---

## 4. Architectural Decisions (ADRs)

Non-negotiables that apply across all courses:
- **ADR-001 (Accessibility)**: All output (web content, documents, media) must target WCAG 2.2 AA (minimum WCAG 2.1 AA).
- **ADR-002 (Spec-Driven Development)**: All work must be traceable to an approved spec in `courses/<course-id>/specs/`.
- **ADR-003 (Canvas Cartridge & DesignPLUS Theme Invariants)**: All Common Cartridge packages must strictly enforce native WikiPage `<head>` metadata, hyphenated module titles (no colons), pure DesignPLUS theme classes (zero clashing inline CSS), and bundled 1100x220 course banners.
