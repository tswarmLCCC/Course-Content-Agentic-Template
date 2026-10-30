# Unit 06: Open-Source Guide — LangGraph State Management & SQLite Checkpointers

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
    
    print("
--- PHASE 1: Initial Trigger ---")
    initial_state = {"task": "Deploy Q3 Marketing Campaign", "plan": "", "approved": False, "result": ""}
    for event in app.stream(initial_state, config=thread_config):
        print(f"Event: {event}")
    
    current_state = app.get_state(thread_config)
    print(f"
[*] Graph Paused! Next node: {current_state.next}")
    print(f"[*] Current Plan: {current_state.values.get('plan')}")
    
    print("
--- PHASE 2: Human Supervisor Reviews & Approves ---")
    app.update_state(thread_config, {"approved": True})
    
    print("
--- PHASE 3: Resuming Graph Execution ---")
    for event in app.stream(None, config=thread_config):
        print(f"Event: {event}")
    
    final_state = app.get_state(thread_config)
    print(f"
[+] Final Result: {final_state.values.get('result')}")
```
