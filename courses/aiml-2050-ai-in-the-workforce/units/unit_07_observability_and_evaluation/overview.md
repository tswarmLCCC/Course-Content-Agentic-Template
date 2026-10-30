# Unit 07 Overview: Agent Governance, Observability & Automated Evaluation

Welcome to Unit 07 of **AIML 2050: AI in the Workforce**. You cannot safely manage what you cannot observe. When deploying autonomous agents into enterprise production, software engineers and business leaders need real-time visibility into token expenditures, latency, tool call accuracy, and error rates. Furthermore, because language models are probabilistic, traditional unit tests are insufficient. This week, students master **Observability & Telemetry Tracing** (using LangSmith / OpenTelemetry), implement automated **Guardrail Nodes** to intercept prompt injection attacks, and construct an **Automated Evaluation Harness** with ground-truth test datasets.

---

## Weekly Contact Hour Budget (360 Minutes Total)
- **Conceptual Study & Readings (150 min)**: Study telemetry tracing, guardrails, LLM-as-a-judge evaluation, and curated slides from Intel Module 15.
- **Asynchronous Preparation & Drills (60 min)**: Complete diagnostic drills analyzing execution traces, prompt injection vectors, and evaluation metrics.
- **Applied Workplace Lab & Project (120 min)**: Build an automated evaluation harness and security benchmark scorecard testing agent resilience.
- **Knowledge Check (30 min)**: Complete the 10-question formative assessment in Canvas.

---

## Measurable Learning Objectives
By the end of this unit, you will be able to:
1. **Instrument** full execution telemetry tracing monitoring latency, token costs, and tool error rates across multi-step agent runs.
2. **Implement** defensive input/output guardrail filters intercepting adversarial prompt injections and sensitive data leakage.
3. **Construct** an automated evaluation dataset containing ideal, ambiguous, and adversarial benchmark test cases.
4. **Author** an automated evaluation harness that scores agent outputs against ground truth and produces an auditable security scorecard.

---

## Weekly Learning Roadmap & Deliverables
1. **Step 1: Required Readings & Slide Deck Guidance**  
   Review curated slides from `[Slides] Module 15` as specified in the reading guide.
2. **Step 2: Standalone Open-Source Setup Guide**  
   Review the Unit 07 Open-Source Guide for telemetry tracing, local logging, and automated evaluation frameworks.
3. **Step 3: Asynchronous Preparation & Diagnostic Drills**  
   Solve diagnostic drills exploring token drift, evaluation rubrics, and guardrail interception.
4. **Step 4: Applied Engineering Lab & Workplace Project**  
   Execute Project 7: Automated Agent Evaluation Harness & Security Benchmark Scorecard, submitting your test suite and report to Canvas SpeedGrader.
5. **Step 5: Unit 07 Knowledge Check**  
   Complete the native Canvas QTI quiz (3 attempts, highest score retained).
