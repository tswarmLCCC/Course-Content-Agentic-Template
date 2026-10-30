# Unit 06 Overview: Long-Running Ambient Agents & State Machines with LangGraph

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
