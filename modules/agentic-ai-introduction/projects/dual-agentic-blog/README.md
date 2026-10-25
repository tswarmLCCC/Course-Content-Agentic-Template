# Dual-Backend Multi-Agent Self-Correcting Blog Writer

An enterprise-grade, dual-track implementation of the multi-agent blog writer demonstrated by Smitha Kolan in Google Cloud Tech's *"AI agents explained: Build your first agent in 8 minutes"*, featuring the ReAct loop (Yao et al., 2023) and Anthropic's Evaluator-Optimizer pattern.

## Overview & Dual-Backend Architecture

This project supports **both Google Cloud (Gemini) and Local Open-Source (Ollama)** under a unified contract:

```
                                  USER TOPIC
                                      │
                                      ▼
                        ┌───────────────────────────┐
                        │       PLANNER AGENT       │
                        │  (Gemini or Local Ollama) │
                        │   Produces: BlogPlan      │
                        └─────────────┬─────────────┘
                                      │
                                      ▼
                  ┌───────────────────────────────────────┐
                  │            WRITER AGENT               │◄───────────────────┐
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

## Quickstart

### 1. Installation
```bash
pip install -e .
```

### 2. Running with Local Ollama (100% Free & Private)
```bash
# Ensure Ollama is running (e.g. ollama run llama3.1)
python -m app.main --provider ollama --model llama3.1:8b --topic "Modern Vector Search & RAG"
```

### 3. Running with Google Gemini (Cloud Track)
```bash
set GEMINI_API_KEY="your-api-key"
python -m app.main --provider google --model gemini-1.5-flash --topic "Modern Vector Search & RAG"
```

### 4. Running Offline Simulation Mode (No Keys, No GPU)
```bash
python -m app.main --provider mock --topic "Modern Vector Search & RAG"
```

### 5. Launching the Local Web Dashboard (ADK Web UI Equivalent)
```bash
python -m app.main --web --port 8000
```
Open `http://localhost:8000` to interactively view live agent thoughts, tool execution, and side-by-side revision diffs!
