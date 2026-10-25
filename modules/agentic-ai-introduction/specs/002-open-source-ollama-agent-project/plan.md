# Technical & Architectural Plan: Open-Source Ollama Multi-Agent Blog Pipeline

- **Spec Reference**: [`spec.md`](file:///c:/dev/Course-Content-Agentic-Template/modules/agentic-ai-introduction/specs/002-open-source-ollama-agent-project/spec.md)
- **Status**: Draft (In Review / Ready for Sparring)
- **Primary Source**: Smitha Kolan, Google Cloud Tech ([YouTube](https://www.youtube.com/watch?v=Zqno_vux6d8))
- **Foundational Papers**: Yao et al. (ICLR 2023) ReAct; Anthropic (Dec 2024) *"Building Effective Agents"*

---

## 1. Executive Summary: Dual-Track Architecture (Google Cloud + Local Ollama)

In her Google Cloud Tech lecture, Smitha Kolan demonstrates a self-correcting multi-agent blog writer using Google's **Agent Development Kit (`google-adk`)**, **Gemini 1.5**, and the **ADK Web UI**.

Rather than discarding the Google Cloud implementation, this architecture establishes a **Unified Dual-Backend Ecosystem** that preserves and supports **both** paradigms:

1. **Google Cloud Track (Production & Cloud Lab)**: Direct integration with **Google Gemini 1.5** (Flash / Pro) via `google-genai` and Google ADK conventions, preserving 100% fidelity with the lecture video and Google Codelab.
2. **Local Open-Source Track (Zero-Cost & Private Lab)**: Direct integration with **Ollama** (`localhost:11434`) running open-weight models (`llama3.1:8b`, `qwen2.5:7b`, `llama3.2:3b`), enabling students and developers to run the exact same agent system locally without API keys, cloud bills, or network latency.
3. **Mock Simulation Track (Offline & CI Testing)**: A deterministic client running realistic agent traces for instant local testing without GPUs or network dependencies.

### Dual-Backend Comparative Architecture:

| Capability / Layer | Google Cloud Track (Smitha Kolan Video) | Local Open-Source Track (Ollama) |
| :--- | :--- | :--- |
| **Model Engine** | Google Gemini 1.5 Flash / Pro (`google-genai`) | Ollama (`llama3.1:8b`, `qwen2.5:7b`, `llama3.2:3b`) |
| **Provider Flag** | `--provider google` (requires `GEMINI_API_KEY`) | `--provider ollama` (connects to `localhost:11434`) |
| **Structured Output** | Gemini Pydantic Response Schema | Ollama Native Constrained Decoding (`format=Schema`) |
| **Tool Execution** | Google ADK / Gemini Function Calling | Ollama Python Function Calling (`tools=[...]`) |
| **Evaluation Loop** | Evaluator-Optimizer state machine (`google-adk`) | Evaluator-Optimizer state machine (Python coordinator) |
| **Observability** | Google ADK Web UI & Rich Terminal Trace | Standalone Local Web Dashboard & Rich Terminal Trace |
| **Deployment Use Case**| Enterprise cloud workflows & high-throughput labs | Local dev, privacy-sensitive data, offline learning |

Both backends share the **exact same Pydantic contracts**, the **exact same agent state machine**, and the **exact same UI layer**, allowing users to benchmark Google Gemini against open-source models side-by-side with a single flag switch!

---

## 2. High-Level System Architecture

```
                                  USER TOPIC
                                      │
                                      ▼
                        ┌───────────────────────────┐
                        │       PLANNER AGENT       │
                        │  (llama3.1 + Pydantic)    │
                        │   Produces: BlogPlan      │
                        └─────────────┬─────────────┘
                                      │
                                      ▼
                  ┌───────────────────────────────────────┐
                  │            WRITER AGENT               │◄───────────────────┐
                  │        (llama3.1 / qwen2.5)           │                    │
                  │   Produces: Markdown Draft            │                    │
                  └───────────────────┬───────────────────┘                    │
                                      │                                        │
                                      ▼                                        │
                        ┌───────────────────────────┐                          │
                        │      VALIDATOR AGENT      │                          │
                        │     (Rubric Evaluation)   │                          │
                        │ Produces: ValidationReport│                          │
                        └─────────────┬─────────────┘                          │
                                      │                                        │
                                      ▼                                        │
                              VALIDATION GATE                                  │
                                     / \                                       │
                                    /   \                                      │
                            Passed?       Failed?                              │
                             /             \                                   │
                            /               \                                  │
                          YES                NO                                │
                          /                   \                                │
                         ▼                     ▼                               │
             ┌─────────────────────┐   ┌────────────────────────┐              │
             │   FINAL ARTIFACT    │   │  RETRY HARNESS (LOOP)  │              │
             │   (Saved to Disk)   │   │ Iteration < Max (3)?   │              │
             └─────────────────────┘   └───────────┬────────────┘              │
                                                   │ YES: Feed critique diff ──┘
                                                   │ NO: Halt & Return Best
                                                   ▼
                                       ┌────────────────────────┐
                                       │ MAX RETRIES EXCEEDED   │
                                       │ (Surface Human Review) │
                                       └────────────────────────┘
```

---

## 3. Data Contracts & Pydantic Schemas (`schemas.py`)

To achieve the bulletproof reliability demonstrated in the video without relying on fragile string splitting, all agent boundaries are governed by strict Pydantic schemas enforced via Ollama's native constrained decoding.

```python
from pydantic import BaseModel, Field
from typing import List, Optional, Dict

class SectionPlan(BaseModel):
    heading: str = Field(description="Section title")
    key_points: List[str] = Field(description="2-4 bullet points to cover")
    target_words: int = Field(description="Target word count for this section (e.g. 100-150)")

class BlogPlan(BaseModel):
    title: str = Field(description="Compelling, publication-ready headline")
    target_audience: str = Field(description="Target reader persona and technical level")
    total_target_words: int = Field(description="Total word count goal (e.g. 500-800)")
    sections: List[SectionPlan] = Field(description="Ordered list of sections")

class ValidationReport(BaseModel):
    passed: bool = Field(description="True if draft passes all rubric gates, False otherwise")
    overall_score: int = Field(description="Quality score from 0 to 100")
    word_count_actual: int = Field(description="Measured word count of draft")
    missing_sections: List[str] = Field(description="Any section headings from the plan omitted in draft")
    critiques: List[str] = Field(description="Specific, objective defects identified")
    actionable_feedback: List[str] = Field(description="Concrete instructions for the Writer to fix on retry")

class AgentTrace(BaseModel):
    step_id: int
    agent_name: str
    phase: str
    prompt_tokens: int
    completion_tokens: int
    latency_ms: float
    output_summary: str
    tool_calls: Optional[List[Dict]] = None
```

---

## 4. Agent Nodes & Prompt Engineering

### 4.1 Planner Agent (`agents/planner.py`)
- **System Prompt**:
  > You are an elite Technical Editorial Director. Given a topic, you formulate a rigorous, logically sequenced blog post outline. You specify explicit section titles, key technical arguments, and realistic word budgets.
- **Execution Call**:
  ```python
  response = ollama.chat(
      model=selected_model,
      messages=[{"role": "system", "content": PLANNER_SYSTEM_PROMPT}, {"role": "user", "content": f"Topic: {topic}"}],
      format=BlogPlan.model_json_schema(),
      options={"temperature": 0.2}
  )
  plan = BlogPlan.model_validate_json(response.message.content)
  ```

### 4.2 Writer Agent (`agents/writer.py`)
- **System Prompt**:
  > You are a senior technical writer. You author clear, engaging, highly accurate markdown blog posts following an approved outline. 
  > If previous validator critique is provided, you MUST explicitly address every single item of feedback to correct the draft.
- **Inputs**: `BlogPlan` + (Optional) `previous_draft` + (Optional) `critique_feedback`.
- **Execution Call**: Generates complete markdown text. Supports streaming for live UI rendering.

### 4.3 Validator Agent (`agents/validator.py`)
- **System Prompt**:
  > You are a meticulous technical copy editor and grading evaluator. Inspect the provided blog draft against the initial plan and strict quality rubric:
  > 1. Word Count Gate: Must be within +/- 15% of the target.
  > 2. Structural Gate: All sections from the plan must be present.
  > 3. Quality Gate: No fluff, no repetitive boilerplate, concrete technical depth.
  > Output a strict JSON ValidationReport. Be rigorous: if it misses criteria, mark passed=False.
- **Execution Call**:
  ```python
  response = ollama.chat(
      model=selected_model,
      messages=[
          {"role": "system", "content": VALIDATOR_SYSTEM_PROMPT},
          {"role": "user", "content": f"Plan: {plan.model_dump_json()}\n\nDraft:\n{draft}"}
      ],
      format=ValidationReport.model_json_schema(),
      options={"temperature": 0.0}
  )
  report = ValidationReport.model_validate_json(response.message.content)
  ```

---

## 5. ReAct Tool Calling Integration (`tools.py`)

In the video, agents access tools to ground reasoning. In our open-source version, Ollama's native tool-calling protocol exposes local Python functions:

```python
def calculate_reading_metrics(text: str) -> dict:
    """Computes word count, character count, and Flesch-Kincaid reading ease grade level."""
    words = text.split()
    word_count = len(words)
    # Lightweight syllable estimation
    return {"word_count": word_count, "reading_ease": "Grade 10 (Technical Professional)"}

def local_vector_search(query: str) -> str:
    """Searches local markdown knowledge base or ChromaDB for grounding technical snippets."""
    # Queries local vector collection or text files
    return f"Retrieved 2 grounding technical citations for: {query}"

available_tools = [calculate_reading_metrics, local_vector_search]
```

When Ollama returns `tool_calls`, the runtime executes the matching function locally and injects the output with `role: "tool"`, completing the ReAct `Thought -> Action -> Observation` cycle.

---

## 6. Observability: The Open-Source "ADK Web UI" Alternative

The standout feature in Smitha Kolan's tutorial is the visual execution trace in Google's ADK Web UI. We implement a dual-mode open-source counterpart:

### Mode A: Rich Terminal Console
- Uses Python `rich` (`Live`, `Tree`, `Panel`, `Syntax`):
  - Renders a colored multi-agent DAG.
  - Displays streaming tokens with real-time latency and token/sec counters.
  - Formats validator reports as clean colored scorecards (Green `[PASSED]`, Red `[RETRY]`).
  - Shows git-style diffs between Draft 1 and Draft 2 so students see exactly what the auto-correcting loop fixed.

### Mode B: Standalone Local Web Dashboard
- Built with **FastAPI** + **Vanilla HTML/CSS/JS** (or Python **FastHTML**):
  - Zero external npm/build steps; runs via `python -m app.web`.
  - **Live Graph Viewer**: Visual nodes (Planner $\to$ Writer $\to$ Validator) lighting up as execution moves through the state machine.
  - **Live Streaming SSE**: Streams agent thoughts and drafts in real time.
  - **Interactive Revision Diff Viewer**: Toggle between Iteration 1 and Iteration 2 side-by-side with additions highlighted in green and deletions in red.
  - **Model & Parameter Controls**: Dropdown to select installed Ollama models (`llama3.1:8b`, `qwen2.5:7b`, etc.) and adjust `max_iterations` and temperature sliders.

---

## 7. Hardware Adaptation & Model Benchmark Matrix

To ensure this project runs smoothly for college students and developers with varying machine specs:

| Hardware Tier | Recommended Model | Quantization | VRAM / RAM Required | Expected Generation Speed |
| :--- | :--- | :---: | :---: | :---: |
| **Tier 1: Entry / Ultrabook** (M1/M2 8GB, Intel i5/i7 16GB RAM, No GPU) | `llama3.2:3b` or `qwen2.5:3b` | `Q4_K_M` | ~2.2 GB | 25–40 tokens/sec |
| **Tier 2: Mid / Developer** (RTX 3060/4060 8GB VRAM, M-series 16GB/24GB) | **`llama3.1:8b`** *(Recommended)* | `Q4_K_M` | ~4.8 GB | 20–35 tokens/sec |
| **Tier 3: High-Reasoning Workstation** (RTX 3090/4090 24GB, M-series 32GB+) | **`qwen2.5:14b`** or `mistral-small:22b` | `Q4_K_M` | ~9.5 GB | 18–28 tokens/sec |

*Built-in Simulation Mode*: If the user does not have Ollama installed or has zero GPU acceleration, running `python main.py --mock` invokes a deterministic `MockOllamaClient` that executes the full multi-agent loop with realistic simulated delays and traces.

---

## 8. Directory & Package Structure

```
ollama-multiagent-blog/
├── README.md                  # Project overview, setup guide, and CLI commands
├── pyproject.toml             # Dependencies (ollama, pydantic, rich, fastapi, uvicorn)
├── app/
│   ├── __init__.py
│   ├── config.py              # Model selection, provider flag, Ollama endpoint, API keys
│   ├── schemas.py             # Pydantic data contracts (BlogPlan, ValidationReport)
│   ├── providers/
│   │   ├── __init__.py
│   │   ├── base.py            # BaseLLMProvider abstract interface
│   │   ├── google_provider.py # Google Gemini 1.5 Flash/Pro provider (google-genai / google-adk)
│   │   ├── ollama_provider.py # Ollama local provider (llama3.1, qwen2.5, llama3.2)
│   │   └── mock_provider.py   # Deterministic simulation provider for offline/CI
│   ├── tools.py               # ReAct tool definitions (word count, reading level, search)
│   ├── agents/
│   │   ├── __init__.py
│   │   ├── planner.py         # Planner agent (topic -> BlogPlan)
│   │   ├── writer.py          # Writer agent (plan + critique -> markdown draft)
│   │   └── validator.py       # Validator agent (draft -> ValidationReport)
│   ├── coordinator.py         # Evaluator-Optimizer state machine & runaway loop guards
│   ├── ui/
│   │   ├── terminal.py        # Rich terminal live dashboard & diff renderer
│   │   └── web/               # Standalone ADK-style local web dashboard
│   │       ├── server.py      # FastAPI server with SSE streaming
│   │       └── static/        # Vanilla HTML, modern CSS, and JS graph viewer
│   └── main.py                # Unified CLI entry point
└── tests/
    ├── test_schemas.py        # Validates Pydantic schema serialization
    ├── test_mock_pipeline.py  # Tests state machine loop with MockOllamaClient
    └── test_live_ollama.py    # Integration test against live Ollama server
```

---

## 9. Implementation Roadmap & Phased Execution

```
[Phase 1: Foundation] ──> [Phase 2: Agent Nodes] ──> [Phase 3: State Machine] ──> [Phase 4: Observability]
  - Pydantic schemas        - Planner Agent            - Evaluator-Optimizer      - Rich terminal UI
  - Ollama client wrapper   - Writer Agent             - Max iteration cap        - Local web dashboard
  - Mock client             - Validator Agent          - Tool calling             - Side-by-side diff
```

### Phase 1: Foundation & Client Harness
1. Scaffold package layout and `pyproject.toml`.
2. Define Pydantic models in `schemas.py`.
3. Build `client.py` with automatic Ollama health check and `MockOllamaClient` fallback.

### Phase 2: Agent Nodes
1. Implement `PlannerAgent` with structured `BlogPlan` output.
2. Implement `WriterAgent` supporting both initial drafting and critique-directed revision.
3. Implement `ValidatorAgent` with multi-tier scoring (word count, structural coverage, technical depth).

### Phase 3: Evaluator-Optimizer Coordinator
1. Build `coordinator.py` state machine orchestrating Planner $\to$ Writer $\to$ Validator $\to$ Retry.
2. Enforce hard `max_iterations = 3` cap to prevent runaway execution.
3. Integrate `tools.py` for ReAct environmental grounding.

### Phase 4: Observability & Web Dashboard
1. Implement Rich terminal renderer (`terminal.py`) with colored badges, scorecards, and live diffs.
2. Build lightweight local web dashboard (`ui/web/`) mimicking Google's ADK Web UI with live streaming SSE.

### Phase 5: Verification & Course Integration
1. Author automated test suite (`tests/`).
2. Package runnable project as a featured Capstone / Extension Project in the `modules/agentic-ai-introduction` curriculum.

---

## 10. Risk Analysis & Mitigations

| Risk | Impact | Mitigation |
| :--- | :--- | :--- |
| **Ollama Not Installed / Offline** | Student cannot run project | Built-in `MockOllamaClient` automatically activates when `--mock` flag is passed or when `localhost:11434` is unreachable. |
| **Model Hallucinates Invalid JSON** | Parser crash in agent loop | Use Ollama native constrained decoding (`format=Schema.model_json_schema()`), which enforces grammar constraints at token sampling time. |
| **Runaway Revision Loop** | Infinite token generation | Coordinator enforces a strict `max_iterations` counter (default: 3) and exits gracefully if score doesn't pass. |
| **Hardware Latency on 8GB Laptops** | Slow generation (> 2 min/turn) | Config presets automatically select `llama3.2:3b` on low-resource machines and reduce outline section counts. |
