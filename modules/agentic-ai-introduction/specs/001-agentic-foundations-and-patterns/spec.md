# Feature Specification: Unit 01 — Agentic Foundations & Architectural Patterns

- **Module**: `modules/agentic-ai-introduction`
- **ID**: `specs/001-agentic-foundations-and-patterns`
- **Status**: Draft (In Review)
- **Created**: 2026-10-25
- **Primary Sources**:
  1. Primary Video Lecture: Google Cloud Tech — *"AI agents explained: Build your first agent in 8 minutes"* hosted by Smitha Kolan ([YouTube](https://www.youtube.com/watch?v=Zqno_vux6d8)).
  2. Theoretical Foundation: Yao et al. (2022/2023) — *"ReAct: Synergizing Reasoning and Acting in Language Models"* ([arXiv:2210.03629](https://arxiv.org/abs/2210.03629)).
  3. Authoritative Industry Architecture: Anthropic Research (Dec 2024) — *"Building Effective Agents"* ([Anthropic Research](https://www.anthropic.com/research/building-effective-agents)).

---

## 1. Objective & Target Audience

- **Target Persona**: Undergraduate college students in Computer Science, Software Engineering, IT, or Data Science (2nd–3rd year).
- **Prerequisite Baseline**: Foundational Python proficiency (functions, loops, dictionaries, structured exceptions) and basic familiarity with interacting with LLM APIs or web chat interfaces.
- **The Core Cognitive Friction**: 
  - Students currently view LLMs as **single-turn text predictors** or passive chatbots ("vibe chatting").
  - They struggle to conceptualize how an LLM can function as a **stateful, goal-driven decision engine** that dynamically inspects its environment, chooses tools, interprets runtime observations, and self-corrects across multi-step execution loops.
- **One Job**:
  Demystify agentic systems by teaching students the spectrum between **deterministic workflows** and **autonomous agents**, grounding their understanding in the **ReAct (Reason + Act)** loop and the **Anthropic 5 Core Patterns**, culminating in an empirical, runnable self-correcting multi-agent blog generation pipeline.

---

## 2. Requirements (EARS Syntax)

### Deliverable A: Unit Overview (`units/unit_01_agentic_foundations/overview.md`)
- **Always (Ubiquitous)**:
  - `REQ-01`: The overview **shall** state the module's 4 core learning objectives, contact hour budget (150 min study / 150 min lab), and a 4-step sequential roadmap.
  - `REQ-02`: The overview **shall** be formatted for compilation into a native Canvas WikiPage with DesignPLUS accordion panels.

### Deliverable B: 4-Chapter OER Reading & Video Guide (`units/unit_01_agentic_foundations/reading.md`)
- **Always (Ubiquitous)**:
  - `REQ-03`: The reading guide **shall** embed the primary YouTube lecture ([`https://www.youtube.com/watch?v=Zqno_vux6d8`](https://www.youtube.com/watch?v=Zqno_vux6d8)) using a responsive 16:9 iframe container with start timestamps for key chapters.
  - `REQ-04`: The reading guide **shall** organize content into 4 distinct pedagogical chapters formatted with DesignPLUS accordion panels (`div.dp-panel-group`):
    - **Chapter 1: Agent Foundations & The Three Core Patterns** (Smitha Kolan primary source: Sequential, Reactive, Planning).
    - **Chapter 2: The ReAct Framework** (Yao et al., 2022: Thought $\to$ Action $\to$ Observation loops, synergizing verbal reasoning with environmental action).
    - **Chapter 3: Workflows vs. Autonomous Agents** (Anthropic 2024: Prompt Chaining with gates, Routing, Parallelization [Sectioning & Voting], Orchestrator-Workers, Evaluator-Optimizer).
    - **Chapter 4: Tool Design & Defensive ACI** (Agent-Computer Interfaces, Poka-Yoke error proofing, absolute paths, deterministic stopping conditions).
  - `REQ-05`: The text **shall** explicitly cite both the Anthropic research paper (*"Building Effective Agents"*, Dec 2024) and the original ReAct paper (*Yao et al., ICLR 2023*).
- **When (Event-Driven)**:
  - `REQ-06`: **When** presenting the ReAct loop, the guide **shall** provide an annotated ASCII/Mermaid execution trace contrasting pure reasoning (Chain-of-Thought) vs. pure acting vs. ReAct synergy.
- **If-Then (Defensive Design)**:
  - `REQ-07`: **If** an agent encounters an infinite tool recursion or malformed JSON tool response, **then** the text **shall** detail programmatic mitigation strategies (max iteration thresholds, structured schema validation, fallback routing).

### Deliverable C: Asynchronous Preparation & Drills (`units/unit_01_agentic_foundations/drills.md`)
- **Always (Ubiquitous)**:
  - `REQ-08`: The drills **shall** include 4 conceptual focus questions and 3 execution-tracing drills evaluating pattern selection (Workflow vs. Agent) and ReAct state machine transitions.
  - `REQ-09`: All drill solutions **shall** be formatted with interactive HTML `<details><summary>` expandable reveal cards for student self-checking.

### Deliverable D: Applied Lab Guide & Challenge (`units/unit_01_agentic_foundations/lab_guide.md`)
- **Always (Ubiquitous)**:
  - `REQ-10`: The lab guide **shall** follow the "I Do, We Do, You Do" gradual release framework:
    - **Part 1 ("I Do")**: Walking through a basic sequential prompt chain with a programmatic gate.
    - **Part 2 ("We Do")**: Implementing an Evaluator-Optimizer loop that critiques and refines draft text.
    - **Part 3 ("You Do")**: Building an autonomous, self-correcting 3-agent blog generation system (Planner Agent, Writer Agent, Validator/Checker Loop Agent) with a max-iteration stop condition.
  - `REQ-11`: The starter code **shall** operate using pure standard library Python 3 (with simulated/mock LLM execution or optional live API) so students with zero API credits can achieve 100% lab completion locally.
  - `REQ-12`: The lab guide **shall** embed a comprehensive 100-point rubric with concrete scoring tiers (Architecture 40 pts, Self-Correction & Loop Control 30 pts, Code Quality & Poka-Yoke Tools 20 pts, Test Verification 10 pts).

### Deliverable E: Native Canvas Assignment Descriptor
- **Always (Ubiquitous)**:
  - `REQ-13`: The assignment **shall** be configured for SpeedGrader file upload (`.py`, `.json`, `.txt`, `.pdf`) with 50 points possible.

### Deliverable F: Learn with AI Socratic Practice (`units/unit_01_agentic_foundations/learn_with_ai.md`)
- **Always (Ubiquitous)**:
  - `REQ-14`: The page **shall** provide a copy-paste master prompt assigning an AI chat model to roleplay as an "Architecture Reviewer" stress-testing student agent designs against prompt injection, infinite loops, and tool poisoning.

### Deliverable G: Native QTI 1.2 Knowledge Check Quiz (`units/unit_01_agentic_foundations/quiz.md`)
- **Always (Ubiquitous)**:
  - `REQ-15`: The quiz **shall** contain 15 multiple-choice questions assessing:
    - Kolan's 3 agent patterns (Sequential, Reactive, Planning).
    - Yao et al.'s ReAct loop mechanics (Thought, Action, Action Input, Observation).
    - Anthropic's 5 workflows (Prompt Chaining, Routing, Parallelization, Orchestrator-Workers, Evaluator-Optimizer).
    - Workflows vs. Agents architectural tradeoffs (latency, cost, determinism).
    - Tool engineering (ACI, Poka-Yoke, guardrails).
  - `REQ-16`: The quiz markdown **shall** include an `## Answer Key` table with detailed rationales for each option.

### Deliverable H: Unpublished Instructor Notes (`units/unit_01_agentic_foundations/teaching_notes.md`)
- **Always (Ubiquitous)**:
  - `REQ-17`: The instructor guide **shall** be compiled as an `unpublished` WikiPage containing class delivery timing, synchronous whiteboard prompts, common student misconceptions, and the complete master solution code.

### Deliverable I: Modular Cartridge Packaging & Verification
- **Always (Ubiquitous)**:
  - `REQ-18`: The compiler (`build_course.py --modular`) **shall** package Unit 01 into `modules/agentic-ai-introduction/Agentic_AI_Introduction_Modules_Import.imscc`.
  - `REQ-19`: The build **shall** validate 100% XML syntax across all generated manifests, module meta, assignment descriptors, and QTI 1.2 assessments with zero errors.

---

## 3. Deliberately Out of Scope

- Distributed multi-agent frameworks requiring heavyweight cloud infrastructure (e.g. AutoGen, CrewAI, LangGraph with Docker swarms) are excluded; the focus is pure architectural mechanics and Python implementations.
- Model fine-tuning or training is out of scope; all agent behavior is accomplished through prompt engineering, structured tool use, and stateful control loops.
- Proprietary paid APIs are not strictly mandated; full starter code must run out-of-the-box with deterministic mock providers or standard HTTP clients.

---

## 4. Acceptance Criteria & Definition of Done

- [ ] All 8 unit artifacts authored under `modules/agentic-ai-introduction/units/unit_01_agentic_foundations/`.
- [ ] Conforms to ADR-001 (WCAG 2.1/2.2 AA accessibility, clear contrast, semantic tables).
- [ ] Conforms to ADR-002 (Spec-driven lifecycle complete with plan and tasks).
- [ ] Conforms to ADR-003 (Pure DesignPLUS classes, hyphenated module titles, native `<head>` WikiPage metadata).
- [ ] Cartridge builds cleanly with `python .agents/skills/canvas-course-builder/build_course.py --modular` and passes automated XML parsing.
