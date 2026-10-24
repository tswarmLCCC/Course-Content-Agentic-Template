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
7. **Monorepo Course Sandboxing**: This repository holds multiple independent courses in `courses/<course-id>/`. The agent **must always check `CURRENT.md`** for the active course and strictly restrict search, read, and write operations to that specific course directory during course work.
8. **Living Documentation Maintenance**: Maintain the master [README.md](file:///c:/dev/Course-Content-Agentic-Template/README.md) as a living document. Whenever new workflows, conventions, prompt patterns, or courses are established or updated, immediately update `README.md` to reflect them.
9. **Idea Validation & Research Partner**: Actively research, stress-test, and validate architectural choices, technology selections, and curriculum sequencing before building. Do not merely construct what is proposed; evaluate pedagogical trade-offs (cognitive load on college sophomores, industry relevance, dependency ordering) and offer informed technical recommendations.
10. **Interactive Pop-up Modals for Choices**: When presenting multiple choices, trade-offs, or decisions to the user, always use the interactive `ask_question` tool so the user can easily click their choice directly in the UI.



---

## 2. Monorepo Structure & Course Sandboxing

```
Course-Content-Agentic-Template/
├── AGENTS.md                  # Master agent rules & lifecycle
├── CURRENT.md                 # Single source of truth: Active Course & Active Iteration
├── .agents/                   # Shared Antigravity Workspace Skills
│   └── skills/                # canvas-course-builder, slide-deck-generator, syllabus-docx-cloner, intake-scanner
├── docs/
│   ├── ADRs/                  # Shared standards (Accessibility, SDD)
│   └── playbooks/             # Pedagogical & production playbooks
├── specs/
│   └── _templates/            # Shared templates (spec, plan, tasks, rubrics, syllabi)
├── courses/                   # All individual courses live here
│   └── <course-id>/           # Dedicated silo for a course
│       ├── README.md          # Course overview, audience, competencies
│       ├── specs/             # Course-specific specs (001-xxx, 002-xxx)
│       └── content/           # Generated deliverables (HTML, Canvas pages, exercises)
└── ref/                       # Reference materials and raw source documents
```

### Sandboxing Rules for Agents:
- **Always read `CURRENT.md` first** to determine the `Active Course`.
- **Never cross course boundaries**: When working on `courses/course-A/`, never grep, read, or modify files in `courses/course-B/`.
- **Leverage Shared Skills Without Polluting Courses**: Use the workspace automation skills in [`.agents/skills/`](file:///c:/dev/Course-Content-Agentic-Template/.agents/skills/) (such as `canvas-course-builder` for QTI quizzes and DesignPLUS HTML formatting) across any course. Never copy build scripts or Python tools directly into course content directories.
- If the user asks for changes without specifying a course, prompt them to clarify which course or check `CURRENT.md`.

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
