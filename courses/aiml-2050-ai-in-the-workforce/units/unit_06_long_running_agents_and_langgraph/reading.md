# Unit 06: Required Readings, Concepts & Slide Guidance
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
