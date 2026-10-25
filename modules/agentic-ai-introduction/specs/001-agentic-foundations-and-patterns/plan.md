# Technical & Architectural Plan: Unit 01 — Agentic Foundations & Architectural Patterns

- **Spec Reference**: [`spec.md`](file:///c:/dev/Course-Content-Agentic-Template/modules/agentic-ai-introduction/specs/001-agentic-foundations-and-patterns/spec.md)
- **Status**: Draft (In Review)
- **Target Unit Directory**: `modules/agentic-ai-introduction/units/unit_01_agentic_foundations/`

---

## 1. Pedagogical & Technical Architecture

### A. The 8-Item Standardized Module Sequence
Following the battle-tested COSC 2060 Canvas taxonomy, the unit bundle consists of:
1. `overview.md` $\to$ Canvas Item 1 (`WikiPage`): Overview, measurable objectives, contact hour budget (150m study / 150m lab), and 4-step roadmap.
2. `reading.md` $\to$ Canvas Item 2 (`WikiPage`): 4-chapter OER guide with responsive YouTube video embed and DesignPLUS accordion panels.
3. `drills.md` $\to$ Canvas Item 3 (`WikiPage`): 4 concept checks + 3 trace exercises with `<details><summary>` reveals.
4. `lab_guide.md` $\to$ Canvas Item 4 (`WikiPage`): "I Do, We Do, You Do" lab clinic, starter specifications, and rubric table.
5. Canvas Assignment $\to$ Canvas Item 5 (`Assignment`): Native Canvas SpeedGrader submission (50 pts, `.py`/`.json`/`.txt`/`.pdf`).
6. `learn_with_ai.md` $\to$ Canvas Item 6 (`WikiPage`): Socratic roleplay prompt & ethical co-pilot guardrails.
7. `quiz.md` $\to$ Canvas Item 7 (`Quizzes::Quiz`): 15-question QTI 1.2 multiple choice quiz with complete answer rationales.
8. `teaching_notes.md` $\to$ Canvas Item 8 (`WikiPage` - Unpublished): Hidden instructor script, whiteboard prompts, and solution key.

### B. Core Theoretical Synthesis
- **Primary Source (Video)**: Smitha Kolan (Google Cloud Tech) — Sequential pipelines, Reactive feedback, and Planning agents.
- **Foundational Paper**: Yao et al. (ICLR 2023) ReAct — Thought $\to$ Action $\to$ Action Input $\to$ Observation cycle.
- **Industry Architecture**: Anthropic (Dec 2024) — Augmented LLM, Prompt Chaining (with gates), Routing, Parallelization (Sectioning/Voting), Orchestrator-Workers, Evaluator-Optimizer, Autonomous Agents, and Poka-Yoke ACI.

### C. Applied Lab Architecture ("You Do"): The Auto-Correcting Multi-Agent Pipeline
- Standard library Python 3 (no pip dependencies required, 100% portable).
- Simulated/Mock LLM engine with optional pluggable API client (OpenAI/Anthropic/Gemini compatible).
- **Agent Roles**:
  1. *Planner Agent*: Decomposes a target topic into a 3-part structured outline.
  2. *Writer Agent*: Generates draft sections based on outline and style constraints.
  3. *Validation/Critic Loop Agent*: Evaluates word count, tone, hallucination heuristics, and formatting rules. Returns PASS or structured critique.
  4. *Coordinator*: Executes loop with a strict `max_iterations=3` stopping condition to prevent infinite token burn.

---

## 2. ADR Conformance & Invariants

- **ADR-001 (Accessibility)**: 
  - All embedded YouTube videos use accessible captions, `title` attributes, and 16:9 responsive wrappers.
  - Interactive drills use native semantic `<details>` and `<summary>` tags with clear contrast.
  - Rubrics use semantic HTML tables with navy headers (`#1e3a8a`) and high-contrast text.
- **ADR-002 (Spec-Driven Development)**: 
  - Complete traceability from `spec.md` to `plan.md` to `tasks.md` to verified deliverables.
- **ADR-003 (Canvas Cartridge & DesignPLUS Theme Invariants)**:
  - Clean DesignPLUS classes (`dp-header`, `dp-panels-wrapper`, `dp-panel-group`) without clashing inline styles.
  - Hyphenated module title: `Unit 01 - Agentic Foundations & Architectural Patterns` (zero colons).
  - Mandatory `<head>` metadata contract with `editor_type="rce"` for all WikiPages.

---

## 3. Dependency Graph & Verification Strategy

- **Build Toolchain**: `.agents/skills/canvas-course-builder/build_course.py --modular`
- **Output Target**: `modules/agentic-ai-introduction/Agentic_AI_Introduction_Modules_Import.imscc`
- **Verification Suite**:
  1. Automated ElementTree XML parsing of all QTI and manifest files.
  2. Content hygiene scan (0 broken links, 0 unrendered markdown blocks, well-formed HTML).
  3. Python starter script automated test run verifying the self-correcting agent loop.
