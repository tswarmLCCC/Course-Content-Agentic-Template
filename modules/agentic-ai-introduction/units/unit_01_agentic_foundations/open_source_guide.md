# Unit 01: Open-Source Lab — Local Multi-Agent Pipeline with Ollama & Python

Welcome to the **Open-Source Local Track** for Unit 01. In this hands-on lab extension, you will run the complete multi-agent self-correcting blog writer entirely on your local machine using **Ollama**, **open-weight models**, and **Python**—with **zero API keys, zero cloud costs, and 100% data privacy**.

This project provides the open-source equivalent to Google's Agent Development Kit (ADK) and includes both a **Rich Terminal Console** and a **Standalone Local Web Dashboard**.

---

## 1. Open-Source vs. Cloud Architecture (The Dual-Track Ecosystem)

While the primary video lecture demonstrates the multi-agent pattern using Google Cloud Vertex AI and Gemini, this open-source architecture implements the exact same state machine locally:

```
                                  USER TOPIC
                                      │
                                      ▼
                        ┌───────────────────────────┐
                        │       PLANNER AGENT       │
                        │  (llama3.1:8b + Pydantic) │
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
                            Passed?       Failed?                              │
                             /             \                                   │
                          YES                NO                                │
                          /                   \                                │
                         ▼                     ▼                               │
             ┌─────────────────────┐   ┌────────────────────────┐              │
             │   FINAL ARTIFACT    │   │  RETRY HARNESS (LOOP)  │              │
             │   (Saved to Disk)   │   │ Iteration < Max (3)?   │              │
             └─────────────────────┘   └───────────┬────────────┘              │
                                                   │ YES: Feed critique diff ──┘
                                                   ▼
                                       ┌────────────────────────┐
                                       │ MAX RETRIES EXCEEDED   │
                                       │ (Surface Human Review) │
                                       └────────────────────────┘
```

### Comparative Stack:

| Component | Google Cloud Track (Smitha Kolan Video) | Open-Source Local Track (Ollama) |
| :--- | :--- | :--- |
| **Model Runtime** | Google Vertex AI / Gemini 1.5 Flash | **Ollama** (`localhost:11434`) running `llama3.1:8b` |
| **Provider Flag** | `--provider google` (requires `GEMINI_API_KEY`) | `--provider ollama` (no keys required) |
| **Structured Output** | Gemini Schema Definition | **Ollama Native Constrained Decoding** (`format=Schema`) |
| **Tool Execution** | Google ADK / Gemini Function Calling | **Ollama Native Tool Calling** (`tools=[callable_fns]`) |
| **Visual Dashboard** | Google ADK Web UI | **FastAPI Standalone Web Dashboard (`localhost:8000`)** |
| **Cost & Latency** | Cloud metering, external network transit | **$0.00 cost, zero data egress, offline capable** |

---

## 2. Local Environment Setup & Ollama Model Profiles

### Step 1: Install & Launch Ollama
1. Download Ollama from [ollama.com](https://ollama.com/) (available for macOS, Windows, and Linux).
2. Start the Ollama background daemon:
   ```bash
   ollama serve
   ```

### Step 2: Pull an Open-Weight Model
Select the model that matches your computer's RAM and GPU capacity:

- **Recommended Default (16GB RAM or GPU with 8GB VRAM)**:
  ```bash
  ollama run llama3.1:8b
  ```
- **High-Reasoning & Structured Output Alternative**:
  ```bash
  ollama run qwen2.5:7b
  ```
- **Low-Resource Laptop Profile (8GB RAM)**:
  ```bash
  ollama run llama3.2:3b
  ```

---

## 3. Project Architecture & Code Tour

The open-source project is located in the repository under:  
`modules/agentic-ai-introduction/projects/dual-agentic-blog/`

### Key Architectural Modules:
- **`app/schemas.py`**: Strict Pydantic models (`BlogPlan`, `ValidationReport`, `AgentTraceStep`). Ollama enforces these schemas directly at the token generation level via constrained decoding (`format=Schema.model_json_schema()`), preventing hallucinated formatting or markdown wrapper syntax.
- **`app/providers/`**: The pluggable provider strategy layer:
  - `ollama_provider.py`: Communicates with `localhost:11434` via the official `ollama` Python library.
  - `google_provider.py`: Communicates with Google Gemini 1.5 via `google-genai` (for side-by-side benchmarking).
  - `mock_provider.py`: Deterministic simulation engine allowing offline testing with zero keys and zero GPUs.
- **`app/tools.py`**: Environmental ReAct tools:
  - `calculate_reading_metrics`: Flesch-Kincaid readability scoring and word counts.
  - `verify_code_syntax`: AST parsing of embedded code blocks.
  - `local_grounding_search`: Factual citation lookup.
- **`app/coordinator.py`**: The Evaluator-Optimizer state machine enforcing state transitions and a hard `max_iterations = 3` runaway guard.

---

## 4. Running the Pipeline: CLI & Terminal Traces

### Running with Local Ollama:
```bash
python -m app.main --provider ollama --model llama3.1:8b --topic "Modern Vector Search & RAG"
```

### Running with Google Gemini (Cloud Track):
```bash
set GEMINI_API_KEY="your-api-key"
python -m app.main --provider google --model gemini-1.5-flash --topic "Modern Vector Search & RAG"
```

### Running Offline Simulation Mode:
```bash
python -m app.main --provider mock --topic "Modern Vector Search & RAG"
```

### Terminal Output Highlights:
When running in terminal mode, Python `rich` displays:
1. **Strategic Blueprint Tree**: Section headings and word budgets from the Planner Agent.
2. **Validator Scorecard**: Colored badges (`[PASSED]` vs. `[RETRY REQUIRED]`) with bulleted defect critiques.
3. **Live Git-Style Diff**: Shows exactly what lines the Writer Agent modified between Iteration 1 and Iteration 2 to resolve the Validator's critique!

---

## 5. Launching the Local Web Dashboard (Google ADK Web UI Equivalent)

To launch the visual web dashboard mimicking Google's ADK Web UI:

```bash
python -m app.main --web --port 8000
```

Open **`http://localhost:8000`** in your web browser.

### Features of the Web Dashboard:
- **Interactive Agent Graph**: Visual SVG/CSS nodes (`Planner -> Writer -> Validator -> Loop -> Published`) that dynamically highlight and pulse as execution progresses through the state machine.
- **Real-Time Trace Feed**: Inspect agent thought traces, phase transitions, and latency metrics in milliseconds.
- **Side-by-Side Revision Diff Viewer**: Toggle between Iteration 1 and Iteration 2 to see the exact edits made by the self-correcting loop.
- **Multi-Backend Selector**: Switch between Local Ollama, Google Gemini, and Mock Simulation directly from the UI dropdown.

---

## 6. Hands-On Exploration Exercises

To solidify your understanding of agentic architectures, try these three experiments:

1. **The Iteration Budget Stress-Test**: Run the pipeline with `--max-iterations 1`. Observe what happens when the initial draft fails the validator: does the system crash, or does it cleanly return the best-effort draft with an unaddressed issues summary?
2. **Model Comparison Benchmark**: Run the identical topic through `--provider ollama --model llama3.1:8b` and `--provider google --model gemini-1.5-flash`. Compare:
   - Latency per iteration.
   - Number of retries needed to satisfy the validator.
   - Word count accuracy against the Planner's outline.
3. **Custom Tool Expansion**: Open `app/tools.py` and implement a custom tool (e.g. checking for passive voice or querying a local SQLite database). Pass it to the Writer Agent and verify that the model calls your tool in its execution trace!
