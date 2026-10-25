# Unit 01 Overview: Agentic Foundations & Architectural Patterns

Welcome to Unit 01 of **Agentic AI: Autonomous Agents & Tool Use**. This unit establishes the foundational architecture of agentic artificial intelligence: understanding how modern systems evolve beyond passive prompt-response language models into autonomous, goal-directed engines capable of reasoning, calling tools, inspecting environment state, and self-correcting errors.

---

## Weekly Contact Hour Budget (300 Minutes Total)
- **Conceptual Study & Video Lecture (150 min)**: Watch the featured lecture (*"AI agents explained"* by Smitha Kolan), study the Yao et al. ReAct paper, and master Anthropic's 5 core agentic workflows.
- **Asynchronous Preparation & Drills (60 min)**: Trace ReAct execution loops, classify workflow vs. agent problems, and debug state transition gotchas.
- **Hands-on Engineering Lab (90 min)**: Build an auto-correcting multi-agent blog writer pipeline in Python with a Planner, Writer, and Validator loop.

---

## Measurable Learning Objectives
By the end of this unit, you will be able to:
1. **Differentiate** deterministic prompt workflows (chaining, routing, parallelization) from autonomous agents with environmental feedback loops based on Anthropic's research taxonomy.
2. **Deconstruct** the ReAct framework (Reasoning + Acting) into distinct Thought, Action, Action Input, and Observation states.
3. **Analyze** architectural tradeoffs (latency, token cost, compounding error rates) when selecting between workflows and autonomous agents.
4. **Implement** an auto-correcting multi-agent Python system featuring automated critique, validation gates, and deterministic loop termination.

---

## Weekly Learning Roadmap & Deliverables

Follow the sequential module workflow in Canvas to complete this unit:

1. **Step 1: Required Readings, Video Lecture & Architectural Foundations**  
   Watch the embedded Google Cloud Tech lecture and study the 4-chapter reading guide covering Kolan's patterns, the ReAct paper, and Anthropic's building blocks.
2. **Step 2: Diagnostic Drills & ReAct State Traces**  
   Complete the formative self-check drills, trace prompt chain execution order, and verify answers using interactive reveal cards.
3. **Step 3: Applied Engineering Lab & Multi-Agent Starter Code**  
   Implement the 3-agent auto-correcting blog pipeline (`starter_blog_agents.py`) adhering to the 100-point rubric, and submit your code to Canvas.
4. **Step 4: Knowledge Check & Concept Verification**  
   Take the 15-question formative QTI assessment in Canvas (up to 3 attempts, highest score kept) to demonstrate mastery of agentic architecture.
