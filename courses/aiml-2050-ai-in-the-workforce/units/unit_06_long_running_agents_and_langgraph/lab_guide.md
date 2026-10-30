# Unit 06 Applied Lab Guide: Stateful Ambient Agent with SQLite Memory & Human Approval Gate

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
