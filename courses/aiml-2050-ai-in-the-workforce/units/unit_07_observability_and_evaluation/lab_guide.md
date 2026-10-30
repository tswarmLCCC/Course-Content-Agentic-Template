# Unit 07 Applied Lab Guide: Automated Agent Evaluation Harness & Security Scorecard

> **Course**: AIML 2050 — AI in the Workforce  
> **Deliverable**: `unit07_eval_harness_[yourlastname].zip` (code + test logs + security scorecard)  
> **Total Points**: 50 Points  
> **Submission**: Native Canvas Assignment Upload

---

## 1. Scenario & Workplace Objective
You are the Lead QA & Security Engineer for an enterprise AI deployment. Management requires rigorous proof that the corporate agent is safe, grounded, and resistant to malicious attacks before it goes live. You will build an **Automated Evaluation Harness**, construct a structured **10-case test dataset**, implement **guardrail nodes**, and generate an auditable **Security Benchmark Scorecard**.

---

## 2. Step-by-Step Task Specifications

### Task 1: Construct the Evaluation Benchmark Dataset
Create a structured dataset (`evaluation_dataset.json` or `.xlsx`) containing at least **10 test cases**:
- **4 Standard Prompts**: Common operational queries testing accurate tool calling and RAG grounding.
- **3 Ambiguous Prompts**: Incomplete or poorly specified requests testing clarifying questions.
- **3 Adversarial Prompts**: Direct and indirect prompt injection attacks testing guardrail interception.
- Each record must include: `case_id`, `category`, `prompt_text`, `expected_action`, and `pass_criteria`.

### Task 2: Implement Input & Output Guardrail Filters
In your agent pipeline, implement defensive filters:
- **Input Guardrail**: Inspects user queries for prompt injection patterns, malicious keywords, and excessive prompt length.
- **Output Guardrail**: Sanitizes agent responses to prevent leaking internal system prompts or unmasked PII.

### Task 3: Build the Automated Evaluation Runner
Author an automated test harness (`run_eval.py`):
- Iterates through the 10 test cases and executes the agent pipeline.
- Automatically logs telemetry for every run (duration, tools called, status, guardrail results).
- Compares agent behavior against `expected_action` and assigns a binary PASS / FAIL.

### Task 4: Security Benchmark Scorecard & Analysis Report
Generate an executive evaluation report (`security_scorecard.md`):
- Overall pass percentage (aim for 90%+ pass rate).
- Detailed breakdown of passed vs failed cases.
- Before-and-after comparison showing how guardrails prevented prompt injection attacks from compromising tools.

---

## 3. Grading Rubric (50 Points Total)

| Criteria | Exemplary (Full Points) | Developing (Partial Points) | Unacceptable (Zero Points) | Points |
|---|---|---|---|---|
| **1. Benchmark Dataset Quality** | 10+ rigorously designed test cases across standard, ambiguous, and adversarial categories with explicit pass criteria. | Dataset present, but contains fewer than 10 cases or lacks adversarial prompts. | Vague or missing evaluation dataset. | **15** |
| **2. Guardrail Defense Mechanisms** | Robust input/output guardrails successfully intercept adversarial prompt injections and prevent tool hijack. | Basic guardrails present, but easily bypassed by simple prompt rephrasing. | No guardrail nodes implemented. | **15** |
| **3. Automated Test Harness & Telemetry** | Automated runner executes test suite; logs timing, tool calls, and pass/fail status to persistent file. | Runner requires manual execution of each prompt; logging is incomplete. | No automated test script provided. | **10** |
| **4. Security Scorecard & Analysis** | Thorough executive scorecard; clearly quantifies pass rate; articulate analysis of security failure modes. | Scorecard present, but lacks clear metrics or failure analysis. | Missing scorecard and analysis report. | **10** |
| **Total** | | | | **50** |
