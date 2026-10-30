# Unit 05 Overview: Code Foundations — The Modular AI Agent Stack

Welcome to Unit 05 of **AIML 2050: AI in the Workforce**. While no-code tools provide rapid automation, enterprise production systems require full programmatic control over data structures, token budgets, error recovery, and tool execution contracts. This week marks our transition to code-first agent engineering. Students demystify the agent stack in Python, master the **ReAct (Reason + Act)** cyclic loop without framework abstractions, enforce defensive **Pydantic** input validation, and assemble a modular agent equipped with Retrieval-Augmented Generation (RAG) and external tool calling.

---

## Weekly Contact Hour Budget (360 Minutes Total)
- **Conceptual Study & Readings (150 min)**: Study API communication contracts, the ReAct pattern, tool schema validation, and curated slides from Intel Module 13.
- **Asynchronous Preparation & Drills (60 min)**: Complete diagnostic drills tracing ReAct execution loops, Pydantic type safety, and vector similarity retrieval.
- **Applied Workplace Lab & Project (120 min)**: Construct a custom modular Python agent with RAG and validated tool calling, tested across 9 prompt scenarios.
- **Knowledge Check (30 min)**: Complete the 10-question formative assessment in Canvas.

---

## Measurable Learning Objectives
By the end of this unit, you will be able to:
1. **Explain** the programmatic HTTP/JSON communication contracts between LLMs and external software APIs.
2. **Implement** the fundamental ReAct (Reason &rarr; Act &rarr; Observe) execution loop in pure Python.
3. **Construct** defensive Pydantic tool schemas that validate inputs and return structured error messages upon malformed calls.
4. **Assemble** a production-ready modular Python agent combining a vector knowledge retriever (RAG) and deterministic calculation tools.

---

## Weekly Learning Roadmap & Deliverables
1. **Step 1: Required Readings & Slide Deck Guidance**  
   Review curated slides from `[Slides] Module 13` as specified in the reading guide.
2. **Step 2: Standalone Open-Source Setup Guide**  
   Review the Unit 05 Open-Source Guide for LangChain, Pydantic schemas, and lightweight RAG indexing.
3. **Step 3: Asynchronous Preparation & Diagnostic Drills**  
   Solve diagnostic drills exploring tool signature parsing, cosine similarity scoring, and ReAct exception handling.
4. **Step 4: Applied Engineering Lab & Workplace Project**  
   Execute Project 5: Custom Modular Python Agent with RAG & Tool Calling, submitting your codebase and test matrix to Canvas SpeedGrader.
5. **Step 5: Unit 05 Knowledge Check**  
   Complete the native Canvas QTI quiz (3 attempts, highest score retained).
