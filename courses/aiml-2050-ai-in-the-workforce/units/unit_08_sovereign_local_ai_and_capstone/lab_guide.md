# Unit 08 Applied Capstone Guide: Sovereign Workplace Agent & Executive Defense

> **Course**: AIML 2050 — AI in the Workforce  
> **Deliverable**: Complete Codebase (`.zip`) + Capstone Slide Deck (`.pptx`/`.pdf`) + 7-Minute Defense Recording  
> **Total Points**: 100 Points (Comprehensive Course Capstone — 30% of Grade)  
> **Submission**: Native Canvas Assignment Upload

---

## 1. Executive Scenario & Capstone Objective
You are presenting your final Capstone Project to the Executive Steering Committee and Chief Technology Officer. You have engineered an end-to-end, sovereign workplace AI solution that solves a critical operational friction in an enterprise domain (Healthcare Operations, Legal / Compliance, Financial Audit, or HR Talent Management). The solution runs locally with private data storage, enforces NIST governance standards, includes Human-in-the-Loop escalation, and delivers quantifiable ROI.

---

## 2. Comprehensive Deliverables Checklist

### Deliverable A: Working Sovereign Python Codebase
1. **Local Model Execution**: Runs on a local quantized model (via Ollama or OpenVINO) with zero external cloud transmission.
2. **Local Vector Memory**: Local RAG pipeline (SQLite or FAISS) querying private corporate documents.
3. **Validated Tools**: At least two deterministic tools backed by Pydantic schemas.
4. **`SKILL.md`**: Specification file documenting capabilities, tool interfaces, and governance tripwires.
5. **Zero-Leakage Audit**: Network trace or code proof confirming no data is transmitted externally.

### Deliverable B: Capstone Slide Deck (10–12 Slides)
- **Slide 1**: Executive Title & Domain Scenario
- **Slide 2**: Problem Statement & Current Value Stream Map (As-Is bottlenecks)
- **Slide 3**: Proposed Solution & Future Value Stream Map (To-Be agent integration)
- **Slide 4**: System Architecture (Presentation, Logic, State, Local Model)
- **Slide 5**: Local Hardware Sizing & Compute Plan (RAM/VRAM calculation)
- **Slide 6**: NIST AI RMF Risk Control Matrix & Human-in-the-Loop Escalation Gates
- **Slide 7**: Automated Evaluation & Security Benchmark Scorecard
- **Slide 8**: Financial ROI & Workforce Reallocation Projections
- **Slide 9**: Implementation Roadmap & Change Management Strategy
- **Slide 10**: Summary & Steering Committee Call-to-Action

### Deliverable C: 7-Minute Executive Video Defense
Record a professional 7-minute presentation defending your capstone:
- **0:00–2:00**: Problem statement, business domain, and ROI case.
- **2:00–4:30**: Live technical walkthrough of the local agent running offline, demonstrating local RAG and tool execution.
- **4:30–6:00**: Governance defense: NIST risk matrix and human-in-the-loop escalation.
- **6:00–7:00**: Executive conclusion and Q&A anticipation.

---

## 3. Capstone Grading Rubric (100 Points Total)

| Evaluation Criteria | Exemplary (Full Points) | Developing (Partial Points) | Unacceptable (Zero Points) | Points |
|---|---|---|---|---|
| **1. Sovereign Architecture & Local Runtime** | Flawlessly executes locally via Ollama/OpenVINO with local vector store; zero external data leakage verified; valid `SKILL.md`. | Runs partially locally, but relies on external cloud APIs for certain tasks. | Broken codebase; fails to run or requires external cloud subscriptions. | **25** |
| **2. Technical Depth & Tool Integration** | Robust Pydantic tools; state persistence; handles edge cases gracefully; clean modular code structure. | Tools functional, but lack schema validation or error handling. | Minimal or non-functional tool calling. | **25** |
| **3. Governance, NIST Alignment & HITL** | Comprehensive NIST Risk Control Matrix; clear 3-tier Human-in-the-Loop escalation gates; auditable fail-safes. | Basic governance mentioned, but lacks technical controls or tiered escalation. | No risk assessment or governance controls. | **25** |
| **4. Executive Defense & Slide Deck** | Highly articulate 7-minute defense; professional 10+ slide deck; compelling ROI calculation and business presence. | Presentation submitted but exceeds/under-runs time limit; slides lack polish or financial analysis. | Missing video or slide deck; unplayable recording. | **25** |
| **Total** | | | | **100** |
