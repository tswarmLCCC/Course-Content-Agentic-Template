# Unit 04 Applied Lab Guide: Resilient Multi-Agent No-Code Orchestration Pipeline

> **Course**: AIML 2050 — AI in the Workforce  
> **Deliverable**: `unit04_pipeline_[yourlastname].json` + Test Matrix `.xlsx` + Demo Video  
> **Total Points**: 50 Points  
> **Submission**: Native Canvas Assignment Upload

---

## 1. Scenario & Workplace Objective
You are an Enterprise Automation Specialist tasked with building an automated, multi-step customer inquiry and triage system. The workflow must receive inbound customer inquiries via webhook or form, utilize an **Orchestrator Agent** to classify intent, route the task to specialized sub-agents, and execute external tool updates. Crucially, the system must include **automated error handling** and a **fallback branch** to ensure zero lost transactions.

---

## 2. Step-by-Step Task Specifications

### Task 1: Pipeline Architecture & Schema Definition
Design your workflow in n8n (or Make / Relay):
- **Trigger**: Inbound Webhook or Form trigger receiving customer data (`name`, `email`, `inquiry_text`, `priority`).
- **Orchestrator Agent**: An LLM node instructed to classify the inquiry into one of three categories (Technical Support, Billing / Refunds, General Inquiry).

### Task 2: Implement Specialized Sub-Agent Tool Branches
Build at least two specialized branches:
- **Branch A (Support / Triage)**: Extracts technical symptoms and drafts a response using an embedded knowledge base.
- **Branch B (Billing / Account)**: Validates account numbers and checks if refund amounts exceed escalation thresholds.

### Task 3: Implement Defensive Fallback & Error Handling
Add robust resilience mechanisms:
- Configure retry parameters on LLM nodes (at least 2 retries).
- Implement an explicit **Error Fallback Branch**: If the LLM produces malformed output or the API fails, route the payload to a "Manual Review Queue" (e.g. append to a Google Sheet or send an alert).

### Task 4: Testing Matrix & Video Demonstration
- Construct a testing spreadsheet (`test_matrix.xlsx`) recording at least **5 test runs** (2 standard prompts, 2 edge cases, 1 deliberate error case).
- Export your completed workflow as a `.json` file.
- Record a 3-minute video demonstrating successful workflow execution and fallback recovery.

---

## 3. Grading Rubric (50 Points Total)

| Criteria | Exemplary (Full Points) | Developing (Partial Points) | Unacceptable (Zero Points) | Points |
|---|---|---|---|---|
| **1. Orchestration Architecture & Workflow Logic** | Flawlessly routes inbound webhooks through Orchestrator to specialized sub-agent branches with structured data. | Linear workflow with minimal branching; lacks clear Orchestrator separation. | Broken pipeline; nodes fail to pass data across steps. | **15** |
| **2. Defensive Error Handling & Fallbacks** | Robust error trigger branch catches malformed inputs or API outages; routes to dead-letter queue. | Basic error handling present, but some failure modes cause silent execution termination. | Zero error handling; workflow crashes on bad inputs. | **15** |
| **3. Testing Matrix Completeness** | Documents 5+ realistic test cases with inputs, expected routing, actual results, and status. | Incomplete test matrix (fewer than 5 cases) or lacks edge-case testing. | Missing testing matrix. | **10** |
| **4. Deliverables & Demonstration Video** | Clean `.json` workflow export, comprehensive test spreadsheet, and articulate 3-minute video demonstration. | Video missing or exceeds time limit; JSON export corrupt or incomplete. | Missing video and invalid files. | **10** |
| **Total** | | | | **50** |
