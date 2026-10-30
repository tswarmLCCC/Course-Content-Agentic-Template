#!/usr/bin/env python3
"""
Enriches Units 05 and 06 reading.md to 1815/COSC-2060 depth.
"""
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
UNITS_DIR = BASE_DIR / "units"

def enrich_unit_05():
    u_dir = UNITS_DIR / "unit_05_code_foundations_and_langchain"
    content = """# Unit 05: Required Readings, Concepts & Slide Guidance
## Code Foundations: The Modular AI Agent Stack

Welcome to the instructional study hub for **Unit 05: Code Foundations — The Modular AI Agent Stack**. This reading organizes core programming competencies into four structured chapters:

1. **Instructor Lecture & Narrative Deep Dive**: Peeling Back the Magic — Demystifying the Programmatic Agent Stack.
2. **Physical Mental Models & Architecture**: The ReAct Reasoning Loop & Pydantic Schemas as Contract Boundaries.
3. **Curated Slide Reading Directives**: Exact study guidance for Intel Module 13.
4. **Production Modular Architecture & Grounded Vector RAG**: Structuring code for enterprise reliability.

---

## 1. Instructor Lecture & Narrative Deep Dive

### Peeling Back the Magic: Demystifying Function Calling

To software developers encountering AI agents for the first time, "Function Calling" and "Agent Tools" can sound like magic. Many assume that the large language model physically compiles and executes Python code inside its neural network weights.

**In reality, an LLM is purely a next-token text prediction engine.** It cannot execute code, make network calls, or query a database.

Here is what actually happens when an agent calls a tool:
1. **The Contract**: Your Python script sends a prompt along with a JSON Schema describing available tools:
   ```json
   {
     "name": "get_stock_price",
     "description": "Retrieves the current market share price for a ticker symbol.",
     "parameters": {
       "type": "object",
       "properties": {
         "ticker": {"type": "string", "description": "Stock symbol, e.g. AAPL"}
       },
       "required": ["ticker"]
     }
   }
   ```
2. **The Output**: The model recognizes that answering the user's question requires real-time data. Instead of generating conversational text, it predicts tokens matching the tool structure:
   `{"tool": "get_stock_price", "args": {"ticker": "INTC"}}`
3. **The Interception**: The Python runtime halts LLM generation, reads the JSON output, looks up `get_stock_price` in a local dictionary of functions, and executes the local Python code.
4. **The Observation**: The output of the Python function (e.g., `"$22.50"`) is injected back into the LLM's conversation history as an **Observation**.
5. **The Final Answer**: The LLM synthesizes the observation into a natural language response: *"Intel is currently trading at $22.50."*

#### Why This Distinction Matters
Because tool calling is just text serialization, it is fragile. If the LLM outputs malformed JSON or hallucinates an argument, naive string parsers crash. Building reliable code agents requires **strict schema validation using Pydantic**.

---

## 2. Physical Mental Models & Architecture

### The ReAct (Reason + Act) Loop in Python

Pioneered by Yao et al. (2022), the ReAct pattern prompts the language model to interleave reasoning thoughts with specific tool invocations:

```
┌────────────────────────────────────────────────────────┐
│ USER PROMPT: "What is 15% tax on an order of 4 items   │
│              costing $35.00 each?"                     │
└──────────────────────────┬─────────────────────────────┘
                           │
                           ▼
┌────────────────────────────────────────────────────────┐
│ THOUGHT 1: "I need to calculate the subtotal first."   │
│ ACTION 1:  calculate(operation="multiply", a=4, b=35)  │
└──────────────────────────┬─────────────────────────────┘
                           │ Runtime executes Python function
                           ▼
┌────────────────────────────────────────────────────────┐
│ OBSERVATION 1: "140.0"                                 │
└──────────────────────────┬─────────────────────────────┘
                           │ Model receives observation
                           ▼
┌────────────────────────────────────────────────────────┐
│ THOUGHT 2: "The subtotal is $140. Now compute 15% tax."│
│ ACTION 2:  calculate(operation="multiply", a=140,      │
│                      b=0.15)                           │
└──────────────────────────┬─────────────────────────────┘
                           │ Runtime executes Python function
                           ▼
┌────────────────────────────────────────────────────────┐
│ OBSERVATION 2: "21.0"                                  │
└──────────────────────────┬─────────────────────────────┘
                           │ Goal accomplished!
                           ▼
┌────────────────────────────────────────────────────────┐
│ FINAL ANSWER: "The 15% tax on the order is $21.00."   │
└────────────────────────────────────────────────────────┘
```

### Pydantic Schemas as Contract Boundaries
By backing every tool with a **Pydantic BaseModel**, Python automatically validates incoming arguments:
- If valid, the function executes cleanly.
- If invalid, Pydantic catches the error and generates an immediate, structured feedback message back to the LLM (*"ValidationError: value 'five' is not a valid integer"*), allowing the agent to self-correct on the next iteration.

---

## 3. Curated Slide Reading Directives

Refer to the following specific sections of the Intel presentation deck in your course repository:

### From `[Slides] Module 13 - Agentic AI.pptx` (106 slides)
- **Study Slides 10–21 (Foundations of Running an AI Agent)**: Understand how LLMs communicate over REST APIs, HTTP POST payloads, system messages, and JSON response parsing.
- **Study Slides 22–74 (Building the Agent & The ReAct Pattern)**: Study the Reason &rarr; Act &rarr; Observe loop. Contrast single-turn zero-shot prompting with multi-turn iterative problem solving.
- **Study Slides 75–98 (Agent Tooling & Function Calling)**: Master how function signatures (name, description, parameter schemas) are serialized into LLM prompts, and how tool execution results are fed back into conversational memory.
- *Skip Slides 99–106* (bibliographies and index citations).

---

## 4. Production Modular Architecture & Grounded Vector RAG

### Modular Architecture Standards
Enterprise codebases strictly decouple reasoning logic from tool definitions:
- `agent.py`: Houses the central reasoning loop and execution controller.
- `tools.py`: Houses deterministic Python functions wrapped with schemas and error handlers.
- `retrieval.py`: Manages document embedding, vector indexing, and RAG search.
- `helpers/config.py`: Centralizes API keys, temperature settings, and model identifiers.
"""
    with open(u_dir / "reading.md", "w", encoding="utf-8") as f:
        f.write(content)
    print("  [+] Unit 05 reading.md enriched.")

def enrich_unit_06():
    u_dir = UNITS_DIR / "unit_06_long_running_agents_and_langgraph"
    content = """# Unit 06: Required Readings, Concepts & Slide Guidance
## Long-Running Ambient Agents & State Machines with LangGraph

Welcome to the instructional study hub for **Unit 06: Long-Running Ambient Agents & State Machines with LangGraph**. This reading organizes core state-machine competencies into four structured chapters:

1. **Instructor Lecture & Narrative Deep Dive**: The Stateless Trap — Why Conversational Agents Fail in Multi-Day Workflows.
2. **Physical Mental Models & Architecture**: From Linear Chains to Cyclic Graphs (StateGraph, Nodes, Edges, Reducers).
3. **Curated Slide Reading Directives**: Exact study guidance for Intel Modules 14 and 16.
4. **State Persistence & Non-Blocking Human Approval Breakpoints**: Checkpoint architectures with SQLite.

---

## 1. Instructor Lecture & Narrative Deep Dive

### The Stateless Trap: Why Chatbots Cannot Run the Enterprise

Most tutorial code for AI agents assumes an instant conversational exchange: a user asks a question, the agent calls a calculator tool, and prints an answer 4 seconds later.

**Real enterprise business processes do not work this way.**

Consider an enterprise employee onboarding process:
1. **Day 1 (Monday)**: HR submits a new hire form. The agent drafts an IT equipment ticket and generates a benefits enrollment package.
2. **Day 2 (Tuesday)**: The IT manager must physically inspect and approve the laptop budget before hardware is ordered. The agent must pause and wait.
3. **Day 3 (Wednesday)**: The IT manager clicks "Approve" via a web portal. The agent resumes, orders the laptop, and provisions email credentials.
4. **Day 4 (Thursday)**: Background check results return via an external webhook. The agent updates the candidate record and notifies HR.

#### The Problem with Stateless Runtimes
If this process is built using a standard linear script or basic LangChain chain:
- Holding the execution thread open for 4 days consumes expensive server memory and crashes upon the first network timeout.
- If the server restarts on Tuesday night for OS patching, the entire onboarding state is wiped from RAM. The new hire is forgotten.

To handle real business workflows, agents must be engineered as **Stateful State Machines** where state is persisted to an external database (e.g., SQLite or Postgres) after every step. This is the architectural purpose of **LangGraph**.

---

## 2. Physical Mental Models & Architecture

### From Linear Chains to Cyclic Graphs

Traditional workflow schedulers (Airflow, linear DAGs) only allow forward motion (Step 1 &rarr; Step 2 &rarr; Step 3). But autonomous agency inherently requires **Cycles**:

```
                     ┌───────────────────────┐
                     │      START NODE       │
                     └──────────┬────────────┘
                                │
                                ▼
                     ┌───────────────────────┐
                     │     Triage Node       │
                     └──────────┬────────────┘
                                │
                 ┌──────────────┴──────────────┐
                 ▼                             ▼
       ┌───────────────────┐         ┌───────────────────┐
       │   Research Node   │         │  Draft Response   │
       └─────────┬─────────┘         └─────────┬─────────┘
                 │                             │
                 └──────────────┬──────────────┘
                                ▼
                     ┌───────────────────────┐
                     │ Human Approval Gate   │ ◄─── [ PAUSE / BREAKPOINT ]
                     │ (State saved to SQL)  │
                     └──────────┬────────────┘
                                │ [Approved by Manager]
                                ▼
                     ┌───────────────────────┐
                     │    Execution Node     │
                     └──────────┬────────────┘
                                │
                                ▼
                     ┌───────────────────────┐
                     │       END NODE        │
                     └───────────────────────┘
```

### The Three Core Components of LangGraph
1. **State Schema (`AgentState`)**: A typed dictionary (`TypedDict` or Pydantic model) that defines the shared memory of the graph.
2. **Nodes**: Standard Python functions that receive the current state, perform an operation, and return updated state keys.
3. **Edges & Conditional Edges**: Routing logic that directs flow from one node to the next based on values in the state.

---

## 3. Curated Slide Reading Directives

Refer to the following specific sections of the Intel presentation decks:

### A. From `[Slides] Module 14 - Agentic AI.pptx` (66 slides)
- **Study Slides 7–19 (Introduction to Ambient Agents vs Stateless ReAct Agents)**: Understand why enterprise tasks require persistent memory and multi-day state horizons.
- **Study Slides 20–37 (Transitioning from LangChain to LangGraph)**: Master StateGraph, Nodes, Edges, and Conditional Edges.
- **Study Slides 38–49 (Building Stateful Workflows with Persistent Memory)**: Master SQLite checkpointing (`SqliteSaver` / `MemorySaver`) and thread IDs.
- **Study Slides 50–60 (Human-in-the-Loop Interrupts & Approval Checkpoints)**: Implement `interrupt_before` to pause graph execution and await human input.
- *Skip Slides 61–66*.

### B. From `[Slides] Module 16 - Agentic AI.pptx` (75 slides)
- **Study Slides 16–30 (System Requirements for Production Code Agents)**: Requirements engineering for enterprise state machines.
- **Study Slides 31–50 (System Design & Agent Architecture)**: Modular graph design and state schema definitions.
- **Study Slides 51–63 (Testing & Observability)**: Monitoring node execution order and state diffs.
- *Skip Slides 64–75*.

---

## 4. State Persistence & Non-Blocking Human Approval Breakpoints

### Non-Blocking Interrupts
In LangGraph, human-in-the-loop is achieved using `interrupt_before=["execution_node"]`:
- The graph runs until it reaches the breakpoint.
- It serializes the entire state dictionary into SQLite and exits cleanly.
- Zero CPU or RAM threads are held open while waiting for the manager.
- When approval arrives hours or days later, `app.update_state()` injects the decision and `app.stream()` resumes execution seamlessly.
"""
    with open(u_dir / "reading.md", "w", encoding="utf-8") as f:
        f.write(content)
    print("  [+] Unit 06 reading.md enriched.")

if __name__ == "__main__":
    enrich_unit_05()
    enrich_unit_06()
