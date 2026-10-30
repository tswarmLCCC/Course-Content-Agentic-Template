# Unit 01: Required Readings, Concepts & Slide Guidance

> **Course**: AIML 2050 — AI in the Workforce  
> **Contact Allocation**: 150 Minutes  
> **Source Modules**: Intel Modules 01, 02 & 05

---

## 1. Curated Slide Reading Directives

To master this week's competencies without cognitive overload, refer to the following specific sections of the Intel presentation slide decks located in your course materials repository. *Do not read every slide; follow the curated directives below:*

### A. From `[Slides] Module 01 - Agentic AI.pptx` (126 slides total)
- **Study Slides 4–32 (Fundamentals of Agentic AI)**: Understand the core definition of an AI agent, the shift from rule-based systems to probabilistic reasoning, and autonomy vs. human oversight.
- **Study Slides 67–79 (The Agentic AI Workflow)**: Pay specific attention to the four-phase cyclic loop: *Perception → Reasoning → Action → Observation*.
- **Study Slides 80–96 (Agentic AI in the Real World)**: Review enterprise examples across customer service, logistics routing, and software engineering.
- *Skip Slides 97–126* (breakout workshop slides and bibliography).

### B. From `[Slides] Module 02- Agentic AI.pptx` (120 slides total)
- **Study Slides 8–40 (Agentic AI in the Workplace)**: Review the economic impact on knowledge work, the concept of AI as a cognitive multiplier, and task decomposition.
- **Study Slides 41–74 (Future Workforce Readiness)**: Analyze the difference between eliminating entire jobs vs. reallocating task bundles to agents, and the emerging role of human orchestrators.
- *Skip Slides 75–120* (sector-specific deep dives across specialized niche industries).

### C. From `[Slides] Module 05 - Agentic AI.pptx` (130 slides total)
- **Study Slides 44–61 (Horizontal vs. Vertical Agentic Systems)**: Compare generalized, cross-functional agents (e.g. email/scheduling assistants) with highly specialized vertical agents (e.g. legal compliance or clinical diagnostic agents).
- **Study Slides 62–105 (Value Stream Mapping & Readiness Assessment)**: Master the step-by-step methodology for mapping process lead time, identifying process bottlenecks, and assessing organizational data readiness.
- *Skip Slides 8–43 & 106–130* (recap slides and general reading).

---

## 2. Core Conceptual Deep Dive: The Agentic Paradigm

### The Perception-Action Loop
Unlike standard Generative AI (where an LLM simply predicts tokens in a single conversational turn), an **AI Agent** possesses an autonomous execution loop:
1. **Perception**: Receiving external state (user prompt, API webhook, file upload, database trigger).
2. **Reasoning & Planning**: Decomposing high-level goals into sequential actions using reasoning frameworks (ReAct, Chain-of-Thought).
3. **Action Execution**: Invoking external tools (querying a database, calling a REST API, executing Python code).
4. **Observation & Reflection**: Inspecting tool outputs, evaluating whether the goal is achieved, and correcting course if errors occur.

```
       ┌───────────────────────────────┐
       │     Perception / Trigger      │
       └──────────────┬────────────────┘
                      ▼
       ┌───────────────────────────────┐
       │     Reasoning & Planning      │◄───────┐
       └──────────────┬────────────────┘        │
                      ▼                         │
       ┌───────────────────────────────┐        │
       │    Tool Execution / Action    │        │
       └──────────────┬────────────────┘        │
                      ▼                         │
       ┌───────────────────────────────┐        │
       │    Observation & Feedback     ├────────┘
       └───────────────────────────────┘
```

### Value Stream Mapping (VSM) in the Enterprise
Before deploying agents, organizations must map their existing processes:
- **Lead Time (Total Elapsed Time)**: The total duration from request initiation to final customer delivery.
- **Process Time (Touch Time)**: The actual duration where human workers are actively performing cognitive work.
- **Wait Time (Bottleneck / Delay)**: Time spent sitting in queues, waiting for approvals, or delayed hand-offs.
- **Agentic Opportunity Score**: High when wait time is large due to repetitive information lookup or routine routing.
