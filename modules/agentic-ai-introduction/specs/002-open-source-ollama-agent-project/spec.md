# Feature Specification: Open-Source Multi-Agent Blog Pipeline with Ollama & Python

- **Module**: `modules/agentic-ai-introduction`
- **ID**: `specs/002-open-source-ollama-agent-project`
- **Status**: Draft (In Review / Ready for Sparring)
- **Created**: 2026-10-25
- **Primary Influences**:
  1. Google Cloud Tech Lecture: *"AI agents explained: Build your first agent in 8 minutes"* by Smitha Kolan ([YouTube](https://www.youtube.com/watch?v=Zqno_vux6d8)).
  2. Theoretical Foundation: Yao et al. (ICLR 2023) ReAct Framework ([arXiv:2210.03629](https://arxiv.org/abs/2210.03629)).
  3. Industry Architectural Reference: Anthropic Engineering (Dec 2024) *"Building Effective Agents"* ([Anthropic Research](https://www.anthropic.com/research/building-effective-agents)).

---

## 1. Objective & Target Audience

### Primary Persona
- Undergraduate CS/IT/Data Science students and open-source developers seeking to build production-grade agentic architectures locally without proprietary cloud vendor lock-in (Google Cloud, OpenAI, Anthropic), API fees, or external cloud latency.

### Problem Statement
- In her tutorial, Smitha Kolan demonstrates an elegant multi-agent architecture (Planner $\to$ Writer $\to$ Validator self-correcting loop with visual tracing). However, the original project relies on Google's proprietary **Agent Development Kit (`google-adk`)**, **Gemini API keys**, and **Vertex AI / Cloud Run** infrastructure.
- Students and developers lack a **100% open-source, local-first equivalent** that runs completely on their own machines using **Python** and **Ollama**, featuring:
  1. Transparent multi-agent coordination.
  2. Native structured outputs via Pydantic JSON schemas.
  3. True ReAct tool execution (function calling).
  4. An open-source local visual trace interface equivalent to the ADK Web UI.

### One Job
- Deliver a comprehensive, reproducible, open-source Python project plan and codebase that runs the self-correcting multi-agent blog writer entirely on local Ollama models (`llama3.1:8b`, `qwen2.5:7b`, or `llama3.2:3b`), complete with terminal trace visualization, an interactive local web dashboard, and defensive runaway loop guards.

---

## 2. Requirements (EARS Syntax)

### Component 1: Local Model Runtime & Hardware Adaptation
- **Always (Ubiquitous)**:
  - `REQ-01`: The system **shall** interface with local models via the official `ollama` Python library communicating with `http://localhost:11434`.
  - `REQ-02`: The system **shall** support model selection with verified parameter profiles for:
    - `llama3.1:8b` (Recommended default: robust instruction-following & tool calling).
    - `qwen2.5:7b` / `qwen2.5:14b` (High-reasoning alternative: exceptional structured JSON adherence).
    - `llama3.2:3b` / `qwen2.5:3b` (Low-resource tier: runs on 8GB RAM laptops).
- **If-Then (Graceful Offline Fallback)**:
  - `REQ-03`: **If** an active Ollama instance is not detected on `localhost:11434`, **then** the system **shall** surface a clear diagnostic error with startup instructions (`ollama run llama3.1`) and provide an optional simulated/mock mode (`--mock`) for offline testing.

### Component 2: Agent Architecture & Structured Contracts
- **Always (Ubiquitous)**:
  - `REQ-04`: The **Planner Agent** **shall** receive a topic and return a strictly validated `BlogPlan` Pydantic object containing:
    - `title: str`
    - `target_audience: str`
    - `estimated_word_count: int`
    - `sections: list[SectionPlan]` (each with `heading`, `key_points`, and `target_words`).
  - `REQ-05`: The **Writer Agent** **shall** ingest the `BlogPlan` (and any validator critique feedback from prior iterations) and generate a cohesive, markdown-formatted blog article.
  - `REQ-06`: The **Validator Agent** **shall** critique the draft against an objective rubric and return a strictly validated `ValidationReport` Pydantic object containing:
    - `passed: bool`
    - `overall_score: int` (0–100)
    - `word_count_check: dict` (actual vs target range)
    - `missing_sections: list[str]`
    - `critiques: list[str]`
    - `actionable_feedback: list[str]`
  - `REQ-07`: All agent structured outputs **shall** use Ollama's native constrained decoding (`format=Schema.model_json_schema()`) to guarantee 100% syntactically valid JSON responses.

### Component 3: Evaluator-Optimizer Feedback Loop & Loop Controls
- **Always (Ubiquitous)**:
  - `REQ-08`: The **Coordinator State Machine** **shall** orchestrate the Evaluator-Optimizer loop:
    - Step 1: Planner generates plan.
    - Step 2: Writer drafts article based on plan.
    - Step 3: Validator inspects draft.
    - Step 4a: If `passed == True`, state machine marks status `COMPLETED` and emits final article.
    - Step 4b: If `passed == False`, state machine packages `actionable_feedback` into a revision prompt, increments `iteration_count`, and re-invokes the Writer Agent.
- **If-Then (Defensive Runaway Guard)**:
  - `REQ-09`: **If** the loop reaches `max_iterations` (default: 3) without achieving a passing score, **then** the state machine **shall** halt, flag status `MAX_RETRIES_EXCEEDED`, and return the highest-scoring draft along with an unaddressed defect summary.

### Component 4: ReAct Tool Calling Integration
- **Where (Optional Tool-Augmented Mode)**:
  - `REQ-10`: **Where** the ReAct tool-calling mode is enabled, the system **shall** equip the agent with local Python tools using Ollama's native `tools=[...]` function-calling protocol:
    - `calculate_reading_level(text: str) -> dict`: Computes Flesch-Kincaid grade level and syllable statistics.
    - `lookup_fact_or_stat(query: str) -> str`: Queries a local OER vector store or DuckDuckGo API for grounding evidence.
    - `verify_code_syntax(snippet: str, language: str) -> dict`: Runs syntax/ast verification on code blocks.
  - `REQ-11`: The agent **shall** log explicit `Thought`, `Action`, `Action Input`, and `Observation` transitions into its execution trace.

### Component 5: Observability, Trace UI & Visual Dashboard
- **Always (Ubiquitous)**:
  - `REQ-12`: The system **shall** provide a **Rich Terminal Interface** displaying live colored status panels, agent thought bubbles, tool execution badges, and retry diffs.
  - `REQ-13`: The system **shall** provide a **Lightweight Local Web Dashboard** (equivalent to Google's ADK Web UI) that:
    - Visualizes the interactive agent graph (Planner $\to$ Writer $\to$ Validator $\to$ Loop).
    - Displays step-by-step agent thought traces and token/latency metrics.
    - Renders side-by-side markdown revision diffs showing what the Writer fixed based on Validator feedback.
    - Offers an input form to kick off new runs with customizable topics, word counts, and Ollama model selectors.

---

## 3. Deliberately Out of Scope

- **Cloud API Mandates**: No requirements for OpenAI, Anthropic, or Google Cloud API keys; the entire architecture must run on local weights.
- **Heavyweight Framework Lock-in**: AutoGen, LangGraph, CrewAI, or semantic-kernel abstractions are excluded from the core layer; the architecture will use pure Python, Pydantic, and the official `ollama` SDK to ensure 100% pedagogical transparency.
- **Distributed Multi-Node Clusters**: Single-machine execution (developer workstation or laptop with 8GB–32GB RAM).

---

## 4. Acceptance Criteria & Definition of Done

- [ ] Detailed implementation plan authored in `plan.md` cross-referenced with this spec.
- [ ] Conforms to ADR-001 (Accessible UI color contrasts, semantic HTML in web dashboard).
- [ ] Conforms to ADR-002 (Spec-driven lifecycle).
- [ ] State machine data structures, Pydantic schemas, and prompts fully specified.
- [ ] Plan committed to repository git history.
