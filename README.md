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
├── docs/
│   ├── ADRs/                  # Architectural Decision Records (Universal standards)
│   │   ├── ADR-001-accessibility.md           # WCAG 2.2 AA non-negotiable
│   │   └── ADR-002-spec-driven-development.md # Mandatory SDD lifecycle
│   └── data_engineering_course_incoming_plan.md # Reference curriculum blueprints
│
├── prompts/                   # Living library of authoring prompts & skill blueprints
│   └── course_authoring_prompts.md # Prompts for high-rigor readings, labs, and sparring
│
├── specs/
│   └── _templates/            # Reusable templates for new units & modules
│       ├── spec_template.md   # EARS syntax requirements template
│       ├── plan_template.md   # Architectural & instructional design plan
│       └── tasks_template.md  # Ordered task checklist with verification checks
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

## 5. Active Courses in this Workspace

| Course ID | Course Code & Title | Units | Active Stage | Directory |
|---|---|---|---|---|
| `cosc-2060-data-engineering` | COSC 2060: Modern Data Engineering & AI Infrastructure | 8 Units (16 Wks) | **Complete 8-Unit Preview Generated** (Readings, Labs, Code Deliverables) | [courses/cosc-2060-data-engineering/](file:///c:/dev/Course-Content-Agentic-Template/courses/cosc-2060-data-engineering/README.md) |


---

## 6. Living Maintenance Protocol

As we work together and discover new patterns, optimizations, or rules:
- Any new architectural decision is recorded in `docs/ADRs/`.
- Any reusable authoring prompt is added to `prompts/`.
- This `README.md` is updated to reflect changes to the engine, workflows, and catalog.
