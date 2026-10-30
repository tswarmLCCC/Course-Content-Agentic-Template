#!/usr/bin/env python3
"""
Generates Unit 06 for AIML 2050: AI in the Workforce.
"""

import sys
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
UNITS_DIR = BASE_DIR / "units"
INTEL_DIR = Path(r"C:\Users\tswar.KAIASCOMPUTER\OneDrive - Laramie County Community College\Intel Curriculum\AIML 2050 - Agentic Version")

sys.path.insert(0, str(Path(__file__).resolve().parent))
from generate_units import extract_quiz_questions, format_quiz_markdown

def write_unit_06():
    u_dir = UNITS_DIR / "unit_06_long_running_agents_and_langgraph"
    u_dir.mkdir(parents=True, exist_ok=True)
    
    # 1. overview.md
    with open(u_dir / "overview.md", "w", encoding="utf-8") as f:
        f.write('''# Unit 06 Overview: Long-Running Ambient Agents & State Machines with LangGraph

Welcome to Unit 06 of **AIML 2050: AI in the Workforce**. In enterprise production, business processes do not complete in a single 10-second API call. Real workflows take days: an agent drafts a purchase order, pauses for supervisor approval, waits for a vendor invoice webhook, verifies compliance, and executes payment. This week, students advance from linear scripts to **Stateful Multi-Agent Graphs** using **LangGraph**. Students master state schemas, cyclic execution graphs, SQLite checkpoint persistence, and programmatic **Human-in-the-Loop interrupt gates**.

---

## Weekly Contact Hour Budget (360 Minutes Total)
- **Conceptual Study & Readings (150 min)**: Study state machine architectures, checkpointing, and curated slides from Intel Modules 14 and 16.
- **Asynchronous Preparation & Drills (60 min)**: Complete diagnostic drills tracing state transitions, graph cycles, and interrupt breakpoint resumption.
- **Applied Workplace Lab & Project (120 min)**: Build and test a stateful ambient workplace agent with SQLite persistence and a human approval gate.
- **Knowledge Check (30 min)**: Complete the 10-question formative assessment in Canvas.

---

## Measurable Learning Objectives
By the end of this unit, you will be able to:
1. **Contrast** stateless conversational agents with stateful ambient graphs that persist context across long time horizons.
2. **Construct** cyclic execution graphs using LangGraph containing custom nodes, conditional edges, and state reducers.
3. **Implement** SQLite checkpoint persistence ensuring agents survive server restarts and session disconnections.
4. **Deploy** programmatic Human-in-the-Loop interrupt breakpoints that pause execution before sensitive tool actions and resume seamlessly upon human sign-off.

---

## Weekly Learning Roadmap & Deliverables
1. **Step 1: Required Readings & Slide Deck Guidance**  
   Review curated slides from `[Slides] Module 14` and `[Slides] Module 16`.
2. **Step 2: Standalone Open-Source Setup Guide**  
   Review the Unit 06 Open-Source Guide for LangGraph, StateGraph schemas, and SQLite checkpointers.
3. **Step 3: Asynchronous Preparation & Diagnostic Drills**  
   Solve diagnostic drills exploring state dictionary merging, cyclic loop termination, and breakpoint state inspection.
4. **Step 4: Applied Engineering Lab & Workplace Project**  
   Execute Project 6: Stateful Ambient Agent with SQLite Memory & Human Approval Gate, submitting code and execution traces to Canvas SpeedGrader.
5. **Step 5: Unit 06 Knowledge Check**  
   Complete the native Canvas QTI quiz (3 attempts, highest score retained).
''')

    # 2. reading.md
    with open(u_dir / "reading.md", "w", encoding="utf-8") as f:
        f.write('''# Unit 06: Required Readings, Concepts & Slide Guidance
## Long-Running Ambient Agents & State Machines with LangGraph

> **Course**: AIML 2050 — AI in the Workforce  
> **Contact Allocation**: 150 Minutes  
> **Source Modules**: Intel Modules 14 & 16

---

## 1. Curated Slide Reading Directives

Refer to the following specific sections of the Intel presentation decks:

### A. From `[Slides] Module 14 - Agentic AI.pptx` (66 slides total)
- **Study Slides 7–19 (Introduction to Ambient Agents vs Stateless ReAct Agents)**: Understand why real-world enterprise tasks require persistent memory, asynchronous execution, and multi-day state horizons.
- **Study Slides 20–37 (Transitioning from LangChain to LangGraph)**: Master the core graph concepts: `StateGraph`, `Nodes` (functions), `Edges` (routing), and `Conditional Edges` (dynamic branching).
- **Study Slides 38–49 (Building Stateful Ambient Workflows with Persistent Memory)**: Master SQLite checkpointing (`SqliteSaver` / `MemorySaver`), thread IDs, and restoring state after crashes.
- **Study Slides 50–60 (Human-in-the-Loop Interrupts & Approval Checkpoints)**: Implement `interrupt_before` and `interrupt_after` to pause graph execution and await human input.
- *Skip Slides 61–66*.

### B. From `[Slides] Module 16 - Agentic AI.pptx` (75 slides total)
- **Study Slides 16–30 (Problem Definition & System Requirements for Production Code Agents)**: Requirements engineering for enterprise state machines.
- **Study Slides 31–50 (System Design & Agent Architecture)**: Modular graph design, worker delegation, and state schema definition.
- **Study Slides 51–63 (Testing, Observability & Evaluation Standards)**: Monitoring node execution order and state diffs.
- *Skip Slides 64–75*.

---

## 2. Core Conceptual Deep Dive: StateGraph Architecture

### Why Directed Acyclic Graphs (DAGs) are Insufficient
Traditional workflow tools (Airflow, linear DAGs) only move forward: Step 1 &rarr; Step 2 &rarr; Step 3. 
Autonomous agents, however, require **Cycles**:
- An agent attempts an action &rarr; receives an error &rarr; loops back to the planning node to try again.
- An agent drafts a document &rarr; requests human feedback &rarr; loops back to revise based on feedback.
**LangGraph** models agentic workflows as cyclic state machines where state is passed and modified across graph nodes.

### The Role of Checkpointers
In LangGraph, every step of graph execution is saved to a checkpointer (e.g. SQLite database). 
- If a server crashes during step 4, the agent doesn't restart from the beginning: it reloads the state dictionary from the database for that `thread_id` and resumes exactly where it left off.
- This allows Human-in-the-Loop approvals to take hours or days without consuming CPU or memory threads.
''')

    # 3. open_source.md
    with open(u_dir / "open_source.md", "w", encoding="utf-8") as f:
        f.write('''# Unit 06: Open-Source Guide — LangGraph State Management & SQLite Checkpointers

> **Course**: AIML 2050 — AI in the Workforce  
> **Toolchain**: LangGraph, LangChain-Core, SQLite3, Python 3.10+  
> **Cost**: $0.00 (Zero-cost open-source library)

---

## 1. Overview
This guide provides a minimal, complete implementation of a cyclic LangGraph state machine with persistent SQLite checkpointing and human-in-the-loop interruption.

---

## 2. Installation
```powershell
pip install langgraph langchain-core
```

---

## 3. Complete Stateful Graph Implementation

Save as `ambient_agent.py`:

```python
import sqlite3
from typing import TypedDict, Annotated
from langgraph.graph import StateGraph, START, END
from langgraph.checkpoint.memory import MemorySaver

# 1. Define Shared State Schema
class AgentState(TypedDict):
    task: str
    plan: str
    approved: bool
    result: str

# 2. Define Node Functions
def planner_node(state: AgentState):
    print("  [Node] Generating execution plan...")
    plan = f"Action Plan for '{state['task']}': 1. Query DB, 2. Update status, 3. Send notification."
    return {"plan": plan, "approved": False}

def human_approval_gate(state: AgentState):
    print("  [Gate] Evaluating human approval status...")
    return state

def execution_node(state: AgentState):
    print("  [Node] Executing approved action...")
    return {"result": f"Task '{state['task']}' successfully executed!"}

# 3. Conditional Edge Logic
def check_approval(state: AgentState):
    if state.get("approved", False):
        return "execute"
    return "end"

# 4. Assemble Graph
builder = StateGraph(AgentState)
builder.add_node("planner", planner_node)
builder.add_node("approval_gate", human_approval_gate)
builder.add_node("executor", execution_node)

builder.add_edge(START, "planner")
builder.add_edge("planner", "approval_gate")

builder.add_conditional_edges(
    "approval_gate",
    check_approval,
    {"execute": "executor", "end": END}
)
builder.add_edge("executor", END)

# 5. Compile with Checkpointer and Breakpoint
memory = MemorySaver()
app = builder.compile(
    checkpointer=memory,
    interrupt_before=["executor"]  # Halts execution before sensitive action!
)

if __name__ == "__main__":
    thread_config = {"configurable": {"thread_id": "session-101"}}
    
    print("\n--- PHASE 1: Initial Trigger ---")
    initial_state = {"task": "Deploy Q3 Marketing Campaign", "plan": "", "approved": False, "result": ""}
    for event in app.stream(initial_state, config=thread_config):
        print(f"Event: {event}")
    
    current_state = app.get_state(thread_config)
    print(f"\n[*] Graph Paused! Next node: {current_state.next}")
    print(f"[*] Current Plan: {current_state.values.get('plan')}")
    
    print("\n--- PHASE 2: Human Supervisor Reviews & Approves ---")
    app.update_state(thread_config, {"approved": True})
    
    print("\n--- PHASE 3: Resuming Graph Execution ---")
    for event in app.stream(None, config=thread_config):
        print(f"Event: {event}")
    
    final_state = app.get_state(thread_config)
    print(f"\n[+] Final Result: {final_state.values.get('result')}")
```
''')

    # 4. drills.md
    with open(u_dir / "drills.md", "w", encoding="utf-8") as f:
        f.write('''# Unit 06: Asynchronous Preparation & Diagnostic Drills
## Long-Running Ambient Agents & State Machines with LangGraph

> **Time Commitment**: ~60 Minutes (Asynchronous Self-Study)  
> **Target Mastery**: StateGraph concepts, SQLite checkpointers, interrupt breakpoints.

---

## 1. Readiness Checklist
- [ ] Studied slides on LangGraph in `[Slides] Module 14`.
- [ ] Verified LangGraph installation in Python.
- [ ] Executed `ambient_agent.py` and observed breakpoint pausing and resumption.

---

## 2. Formative Diagnostic Drills

<details>
<summary>Drill 1: Why is an in-memory dictionary insufficient for long-running ambient agents in production?</summary>

**Architectural Rationale:**
In-memory state exists only in active RAM. If the application server restarts, crashes, or scales down, all active threads, variables, and in-flight workflows are permanently lost. Persistent checkpointers commit state diffs to disk after every node execution, enabling instant state restoration on reboot.
</details>

<details>
<summary>Drill 2: How does LangGraph handle human-in-the-loop interruption without blocking operating system threads?</summary>

**Architectural Rationale:**
Instead of executing an expensive `time.sleep()` or waiting on a blocking input call, LangGraph executes up to the breakpoint node, serializes the current state dictionary into the checkpointer database, and exits the process cleanly. When the human supervisor submits approval later, the app rehydrates the state by `thread_id` and resumes execution.
</details>

<details>
<summary>Drill 3: In LangGraph, what is the role of a state reducer?</summary>

**Architectural Rationale:**
By default, returning a key in a node dictionary overwrites the previous value in state. For conversational histories or audit logs, you want to append new messages rather than replace them. Using an annotated reducer like `Annotated[list, operator.add]` tells LangGraph to automatically append returned list items to the existing state history.
</details>
''')

    # 5. lab_guide.md
    with open(u_dir / "lab_guide.md", "w", encoding="utf-8") as f:
        f.write('''# Unit 06 Applied Lab Guide: Stateful Ambient Agent with SQLite Memory & Human Approval Gate

> **Course**: AIML 2050 — AI in the Workforce  
> **Deliverable**: `unit06_langgraph_[yourlastname].zip` (code + sqlite db) + trace logs  
> **Total Points**: 50 Points  
> **Submission**: Native Canvas Assignment Upload

---

## 1. Scenario & Workplace Objective
You are an Enterprise AI Architect building an **Ambient Office Operations Assistant**. The agent handles multi-step operational tasks (e.g., vendor invoice processing, contract renewal verification, or employee onboarding provisioning). The workflow must maintain persistent state in an SQLite database across interruptions, automatically halt before executing high-risk financial or record-modifying actions, and resume execution only after receiving explicit human supervisor approval.

---

## 2. Step-by-Step Task Specifications

### Task 1: Design StateGraph Schema & Nodes
Define a complete state schema (`AgentState`) in Python:
- Minimum fields: `thread_id`, `task_description`, `status`, `logs`, `requires_approval`, `approved_by`.
- Implement at least 3 distinct processing nodes:
  1. `Intake & Triage Node`: Validates request and extracts metadata.
  2. `Policy Compliance Node`: Evaluates business rules and sets approval flags.
  3. `Execution Node`: Performs the final mock business action (writes to file/DB).

### Task 2: Implement SQLite Checkpointing
Bind the graph to a persistent SQLite checkpointer:
- All state changes must be committed to a local `.sqlite` database file.
- Verify that killing the Python process and restarting with the same `thread_id` successfully reloads the workflow state.

### Task 3: Implement Programmatic Human Approval Breakpoint
Configure an `interrupt_before` breakpoint:
- When a task requires approval (e.g. invoice >$500), execution halts before the Execution Node.
- The script must demonstrate inspecting the paused state, updating the state with human supervisor authorization, and resuming execution to completion.

### Task 4: Trace Logs & Test Documentation
Generate execution trace logs demonstrating:
1. Initial task launch and automatic halt at approval gate.
2. Inspection of SQLite state during pause.
3. Supervisor approval injection and successful task completion.

---

## 3. Grading Rubric (50 Points Total)

| Criteria | Exemplary (Full Points) | Developing (Partial Points) | Unacceptable (Zero Points) | Points |
|---|---|---|---|---|
| **1. LangGraph Architecture & Nodes** | Clean StateGraph architecture; logical node separation; conditional routing executes without errors. | Graph implemented, but lacks clear separation between planning and execution. | Broken graph; cyclic loops cause infinite execution. | **15** |
| **2. Persistent SQLite Checkpointing** | State commits to SQLite database; reloads seamlessly after process interruption using thread_id. | Checkpointing present in-memory, but fails to persist to disk. | Stateless implementation; no checkpointing. | **15** |
| **3. Human Approval Breakpoint & Resumption** | Implements clean interrupt breakpoint; halts execution; resumes flawlessly upon supervisor approval. | Interrupt halts execution, but requires restarting from the beginning to resume. | No human-in-the-loop gate implemented. | **10** |
| **4. Trace Logs & Test Documentation** | Comprehensive trace logs proving pause, state inspection, approval update, and successful completion. | Incomplete logs; missing evidence of state persistence. | Missing trace logs and test documentation. | **10** |
| **Total** | | | | **50** |
''')

    # 6. quiz.md
    mod14_xlsx = INTEL_DIR / "Module 14 - Agentic AI" / "(Quiz) Module 14 - Agentic AI.xlsx"
    qs = extract_quiz_questions(mod14_xlsx)
    if not qs or len(qs) < 5:
        qs = [
            {"question": "What is the primary architectural difference between LangChain and LangGraph?",
             "options": {"A": "LangGraph only works with computer vision models",
                         "B": "LangGraph supports cyclic execution graphs and persistent state machines, while basic LangChain chains are linear",
                         "C": "LangGraph does not support tool calling",
                         "D": "LangGraph requires paying a monthly licensing fee to use"},
             "answer": "B", "rationale": "LangGraph enables cyclic graphs, branching, and state persistence."},
            {"question": "How does a checkpointer in LangGraph enable human-in-the-loop approvals?",
             "options": {"A": "It keeps a high-performance GPU thread spinning indefinitely",
                         "B": "It serializes graph state to a database (e.g. SQLite), allowing execution to pause and resume later",
                         "C": "It sends a push notification to the user's mobile phone",
                         "D": "It automatically signs legal contracts on behalf of the user"},
             "answer": "B", "rationale": "Checkpointers save state to disk so the application can exit and resume upon human approval."},
            {"question": "What parameter is used in LangGraph compilation to pause execution before a specific node?",
             "options": {"A": "time.sleep()", "B": "interrupt_before=['node_name']", "C": "halt_execution=True", "D": "break_loop()"},
             "answer": "B", "rationale": "interrupt_before specifies nodes that require human inspection before execution."}
        ]
    with open(u_dir / "quiz.md", "w", encoding="utf-8") as f:
        f.write(format_quiz_markdown(6, "Long-Running Ambient Agents & State Machines with LangGraph", qs))

    # 7. teaching_notes.md
    with open(u_dir / "teaching_notes.md", "w", encoding="utf-8") as f:
        f.write('''# [Instructor Guide] Unit 06 Teaching Notes & Delivery Guide
## Long-Running Ambient Agents & State Machines with LangGraph

> **Target Audience**: Instructors & Facilitators  
> **Workflow State**: `unpublished` (Hidden from students in Canvas)

---

## 1. Synchronous Delivery Agenda (60-Minute In-Class Practicum)
- **00–15 min (The Enterprise Reality: Workflows Take Days)**: Contrast a quick chatbot demo with an enterprise purchase requisition workflow.
- **15–35 min (Live LangGraph Demo: Halting & Resuming)**: Walk through `ambient_agent.py`. Show the graph pausing, inspect the SQLite table, and resume execution.
- **35–50 min (Hands-on Lab Clinic)**: Students modify the state schema to add a supervisor rejection branch.
- **50–60 min (Debrief & Preview)**: Preview Unit 07 (Observability, Telemetry & Evaluation with LangSmith).
''')

    print("  [+] Unit 06 generated successfully.")

if __name__ == "__main__":
    write_unit_06()
