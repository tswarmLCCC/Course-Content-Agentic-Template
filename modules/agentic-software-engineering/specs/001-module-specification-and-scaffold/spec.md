# Feature Specification: Agentic Software Engineering 3-Unit Modular Bundle

- **ID**: `specs/001-module-specification-and-scaffold`
- **Status**: Draft — In Review
- **Created**: 2026-10-26
- **Target Completion**: 30 minutes
- **Active Silo**: `modules/agentic-software-engineering/`

---

## 1. Objective & Target Audience

- **Primary Persona**: Undergraduate students in Computer Science, Software Engineering, DevOps, or Applied AI; and higher-ed instructors seeking an enterprise-aligned curriculum on AI-augmented software engineering.
- **Problem Statement**: Generative AI tools (ChatGPT, Claude, Copilot) encourage students to adopt "vibe coding"—casual, unstructured natural language prompting where generated code is accepted without verification. This practice creates severe technical debt ("the 80% trap"), context degradation, and hallucinations in production environments. Students lack understanding of how professional engineering teams govern autonomous agents using harnesses, specification-driven development (SDD), context engineering, and automated verification loops.
- **One Job**: Author and compile a complete, production-grade 3-unit standalone Canvas Common Cartridge (`Agentic_Software_Engineering_Modules_Import.imscc`) grounded in Google's landmark whitepaper (*The New SDLC With Vibe Coding*), featuring the 10/90 Harness Rule, repository governance (`AGENTS.md`), FastMCP open protocols, and closed-loop test-driven self-healing agent pipelines.

---

## 2. Requirements (EARS Syntax)

### Always (Ubiquitous Requirements)
- `REQ-01`: The module package **shall** provide 3 complete, sequentially scaffolded units:
  - **Unit 01**: *Vibe Coding vs. Agentic SDLC & The 10/90 Harness Rule*
  - **Unit 02**: *Harness Architecture, Context Engineering & Rule Governance*
  - **Unit 03**: *Open Protocols (FastMCP) & Multi-Agent CI/CD Test-Driven Verification*
- `REQ-02`: Each unit **shall** strictly adhere to the standardized 8-item Canvas LMS sequence:
  1. `Unit X Overview` (`WikiPage`)
  2. `Unit X Required Readings, Concepts & Video Lectures` (`WikiPage`)
  3. `Unit X Asynchronous Preparation & Drills` (`WikiPage`)
  4. `Unit X Applied Lab Guide` (`WikiPage`)
  5. `Unit X Applied Lab Assignment` (`Assignment`)
  6. `Unit X Learn with AI — Supplemental Practice Drill` (`WikiPage`)
  7. `Unit X Knowledge Check` (`Quizzes::Quiz`)
  8. `[Instructor Guide] Unit X Teaching Notes & Solutions` (`WikiPage`, Unpublished)
- `REQ-03`: All WikiPages **shall** conform to ADR-001 (WCAG 2.2 AA accessibility) and ADR-003 (native Canvas DesignPLUS styling without clashing inline styles).
- `REQ-04`: Every applied lab assignment **shall** support a dual-backend hybrid runtime: Google Gemini API (cloud free-tier) and local Ollama (`qwen2.5-coder:7b` / `14b`), ensuring zero-cost, 100% offline student reproducibility.

### When (Event-Driven Requirements)
- `REQ-05`: **When** a student completes the asynchronous reading guide in Unit 01, the system **shall** present an interactive analysis contrasting the CapEx/OpEx economics of vibe coding versus the 10/90 Harness Rule.
- `REQ-06`: **When** the applied lab starter script in Unit 01 executes, the agent harness **shall** read an EARS specification document, construct an implementation plan, generate code, and verify all unit tests pass before outputting a finished artifact.
- `REQ-07`: **When** Unit 02 is loaded, the context engine **shall** demonstrate progressive disclosure by selectively injecting domain skill files (`.agents/skills/`) rather than bloating the system prompt.
- `REQ-08`: **When** Unit 03's FastMCP tool server executes, it **shall** expose standardized JSON-RPC endpoints that allow both local (Ollama) and cloud (Gemini) agents to inspect code, run linters, and trigger automated test suites.

### While (State-Driven Requirements)
- `REQ-09`: **While** an autonomous agent in Unit 03 executes a self-healing refactoring loop, it **shall** capture unit test tracebacks, analyze syntax/logic errors, apply non-destructive diff patches, and re-execute tests up to a configurable maximum retry limit.
- `REQ-10`: **While** in Canvas Modular Import Mode, the build compiler **shall** output a self-contained `.imscc` cartridge without altering the host course's front page, syllabus, or navigation settings.

### If-Then (Error & Unwanted Behavior)
- `REQ-11`: **If** no cloud API key is supplied by a student, **then** the lab harnesses **shall** automatically detect and fall back to the local Ollama instance without raising unhandled authentication exceptions.
- `REQ-12`: **If** an agent attempts a full-file overwrite during code modification, **then** the harness tools **shall** reject the action and require targeted, diff-based chunk replacement.
- `REQ-13`: **If** an agent enters an infinite self-healing loop during test verification, **then** the execution harness **shall** terminate safely after exhausting the step budget and return a structured failure diagnosis.

### Where (Optional / Modality Features)
- `REQ-14`: **Where** students have GPU-equipped machines, the lab environment **shall** allow switching model weights from `qwen2.5-coder:7b` to `qwen2.5-coder:14b` via a single environment variable (`OLLAMA_MODEL`).

---

## 3. Deliberately Out of Scope

- **Full Course Shell Packaging**: No institutional syllabus `.docx` or homepage `home-page.html` (this is a standalone modular package, not a 16-week full course).
- **Proprietary Vendor Lock-in**: No mandatory paid API keys (OpenAI o1/o3 or Anthropic Claude API) required to achieve 100% lab grade.
- **Complex Multi-Host Distributed Systems**: No Kubernetes or multi-node cluster orchestration; all multi-agent labs execute within a single student development environment (VS Code / terminal).
- **Subjective "Vibe" Evaluation**: No ungrounded LLM self-evaluation without deterministic pytest assertions.

---

## 4. Acceptance Criteria & Definition of Done

- [ ] All 14 EARS requirements (`REQ-01` through `REQ-14`) verified and passing.
- [ ] Conforms to **ADR-001** (WCAG 2.2 AA compliant contrast, alt tags, semantic HTML).
- [ ] Conforms to **ADR-002** (Full SDD lifecycle: `spec.md`, `plan.md`, `tasks.md`, verified evidence).
- [ ] Conforms to **ADR-003** (DesignPLUS classes, hyphenated module titles, bundled banner, valid `<head>` WikiPage metadata).
- [ ] Standalone cartridge `Agentic_Software_Engineering_Modules_Import.imscc` compiles cleanly via `build_course.py --modular` with 0 validation errors.
- [ ] Automated pytest verification scripts validate all starter code, labs, and dual-backend fallbacks.
