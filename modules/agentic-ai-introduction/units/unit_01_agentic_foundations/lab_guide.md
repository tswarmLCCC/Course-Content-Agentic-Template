# Unit 01 Applied Lab: The Auto-Correcting Multi-Agent Blog Pipeline

> **Course**: Agentic AI — Autonomous Agents & Tool Use  
> **Unit**: Unit 01 — Agentic Foundations & Architectural Patterns  
> **Deliverable**: `agent_blog_pipeline.py`  
> **Total Points**: 100 Points (50 Points in Canvas Gradebook)  
> **Toolchain**: Python 3.10+ (Standard Library Only — Zero pip packages required)

---

## 1. Scenario & Objective

In modern content engineering, producing enterprise-grade technical documentation or articles requires multiple specialized roles: an architect who outlines the structure, a technical writer who drafts the prose, and an editorial critic who validates accuracy, word count, and brand guidelines.

When developers attempt to accomplish this in a single monolithic prompt, the LLM frequently loses track of constraints—skipping sections, drifting off-topic, or generating superficial content.

**Your Mission**: Construct an autonomous, self-correcting 3-agent content generation pipeline inspired by Smitha Kolan's Google Cloud Tech architecture and Anthropic's Evaluator-Optimizer pattern. Your system will coordinate a **Planner Agent**, a **Writer Agent**, and a **Validator Agent** in an iterative feedback loop that catches errors, enforces constraints, and terminates deterministically.

---

## 2. Coding Clinic: "I Do, We Do, You Do"

### "I Do" — Instructor Demonstration: Prompt Chaining with a Programmatic Gate
Before deploying autonomous loops, understand how to chain prompts sequentially and place **hard programmatic code gates** between LLM calls to prevent bad state propagation:

```python
import json

def step1_generate_outline(topic: str) -> dict:
    """Prompt 1: Generate high-level outline."""
    # Simulated LLM Call 1
    return {
        "title": f"Guide to {topic}",
        "sections": ["Concepts", "Architecture", "Conclusion"]
    }

def programmatic_gate(outline: dict) -> bool:
    """Deterministic Code Gate: Verify outline before burning tokens on drafting."""
    if len(outline.get("sections", [])) < 3:
        raise ValueError("Gate Check Failed: Outline must have at least 3 sections!")
    return True

def step2_draft_section(title: str, section_name: str) -> str:
    """Prompt 2: Draft individual section."""
    # Simulated LLM Call 2
    return f"### {section_name}\nThis section explains {section_name.lower()} in detail."

# Execution
outline = step1_generate_outline("Vector Search")
if programmatic_gate(outline):
    draft = step2_draft_section(outline["title"], outline["sections"][0])
    print(draft)
```

---

### "We Do" — Guided Practice: The Evaluator-Optimizer Critique Loop
In an Evaluator-Optimizer workflow, the output of a generator is critiqued by an evaluator model against explicit rubric criteria, and the critique is injected back into the generator prompt:

```python
def evaluator_optimizer_loop(draft_func, evaluate_func, max_turns=3):
    current_draft = draft_func(feedback=None)
    
    for turn in range(1, max_turns + 1):
        critique = evaluate_func(current_draft)
        print(f"Turn {turn}: Score = {critique['score']}/100, Passed = {critique['passed']}")
        
        if critique["passed"]:
            return current_draft, turn
            
        # Re-draft with feedback
        current_draft = draft_func(feedback=critique["issues"])
        
    return current_draft, max_turns
```

---

### "You Do" — Applied Challenge: The 3-Agent Auto-Correcting Blog Writer

You will implement the complete multi-agent pipeline adhering to the following structural requirements:

1. **Role 1 — Planner Agent**:
   - Takes a `topic: str`.
   - Returns a structured dictionary containing `title`, `target_words`, and a list of at least 3 mandatory `sections`.
2. **Role 2 — Writer Agent**:
   - Takes `plan: dict` and an optional `critique: dict`.
   - On the initial call, drafts the complete blog post.
   - On retry calls, inspects `critique["issues"]`, expands explanations, and restores any missing sections.
3. **Role 3 — Validator Agent**:
   - Inspects the draft text against 3 strict validation gates:
     1. Word count must be between 120 and 250 words.
     2. All sections from the Planner's outline must be present as Markdown `## Headings`.
     3. Must contain zero forbidden filler words (e.g., "delve", "tapestry", "in conclusion").
   - Returns JSON: `{"passed": bool, "score": int, "word_count": int, "issues": list[str]}`.
4. **Role 4 — Agent Coordinator (Loop Harness)**:
   - Enforces a hard `max_iterations = 3` cap.
   - Records an `execution_trace` logging every Thought, Action, and Observation.
   - Halts and returns the published blog post as soon as `passed == True`.

---

## 3. Starter Code & Extension Project Instructions

### Core Lab Starter Script (Zero Dependencies)
A self-contained starter script has been provided in your repository at:  
`starter_blog_agents.py` (located in this unit's lab starter folder).

To verify the starter script in your terminal:
```bash
python units/unit_01_agentic_foundations/starter_blog_agents.py
```

### Advanced Extension: Dual-Backend Project (Google Gemini + Local Ollama + Web Dashboard)
For students and developers wanting to run the multi-agent pipeline with live LLM backends and an interactive visual UI (the open-source equivalent to the Google ADK Web UI):
- Explore the complete codebase under: `projects/dual-agentic-blog/`
- **Run with Local Ollama (100% Free & Private)**:
  ```bash
  python -m app.main --provider ollama --model llama3.1:8b --topic "Modern Vector Search & RAG"
  ```
- **Run with Google Gemini (Cloud Track)**:
  ```bash
  set GEMINI_API_KEY="your-api-key"
  python -m app.main --provider google --model gemini-1.5-flash --topic "Modern Vector Search & RAG"
  ```
- **Launch Local Web Dashboard**:
  ```bash
  python -m app.main --web --port 8000
  ```
  Open `http://localhost:8000` to inspect live agent thought traces, visual DAG execution nodes, and side-by-side revision diffs!

---

## 4. Evaluation Rubric & Scoring Criteria (100 Points Total)

| Criteria | Points | Unsatisfactory (0–59%) | Competent (60–84%) | Exemplary (85–100%) |
| :--- | :---: | :--- | :--- | :--- |
| **Agent Separation of Concerns** | 25 | Agents share state or execute monolithic prompts without distinct roles. | Planner, Writer, and Validator are distinct classes, but prompts blur responsibilities. | Clean encapsulation: Planner, Writer, and Validator have strict, isolated system prompts and interfaces. |
| **Self-Correcting Feedback Loop** | 30 | Pipeline fails or terminates after 1 rejection without re-drafting. | Pipeline re-drafts, but ignores specific validator feedback or thrash-repeats errors. | Flawless Evaluator-Optimizer loop: Writer explicitly addresses validator critique and passes on iteration 2. |
| **Defensive Loop Controls** | 25 | Unbounded `while True` loop with potential for infinite recursion. | Has iteration counter, but missing structured error logging or state history. | Strict `max_iterations` enforcement, state tracking, and deterministic termination safeguards. |
| **Poka-Yoke Tool Design & Validation** | 20 | Unstructured string parsing; crashes on malformed output. | Basic JSON parsing with minimal exception handling. | Robust schema validation, structured error diagnostics, and clean terminal tracing. |
