# Unit 02 Applied Lab Guide: Enterprise AI Governance Charter & Human-in-the-Loop Protocol

> **Course**: AIML 2050 — AI in the Workforce  
> **Deliverable**: `unit02_governance_charter_[yourlastname].pdf` + Video Pitch Link  
> **Total Points**: 50 Points  
> **Submission**: Native Canvas Assignment Upload

---

## 1. Scenario & Workplace Objective
You have been appointed as the Lead AI Governance Officer for a regional enterprise (e.g., healthcare clinic network, regional bank, logistics distributor, or state government agency). The executive team wants to deploy autonomous agents to streamline customer operations and record processing. However, the Board of Directors will not release capital until you present an **Enterprise AI Governance Charter**, an auditable **NIST AI RMF Risk Control Matrix**, and an ironclad **Human-in-the-Loop (HITL) Escalation Protocol**.

---

## 2. Step-by-Step Task Specifications

### Task 1: Enterprise System Profile & Stakeholder Mapping
Select an operational agentic use case (e.g. Automated Medical Prior Authorization Agent, Commercial Loan Pre-Approval Agent, or Automated Procurement Agent). Document:
- Business mission and operational boundary.
- Direct stakeholders (frontline staff, managers, clients).
- Indirect stakeholders (regulators, IT security, audit teams).

### Task 2: NIST AI RMF Risk Control Matrix
Construct a detailed Risk Control Matrix adhering to NIST AI RMF 1.0 containing at least **4 distinct failure modes**:
1. Runaway execution loop / API exhaustion.
2. Data exfiltration or PII leakage.
3. Indirect prompt injection / unauthorized tool invocation.
4. Algorithmic bias or discriminatory decision drift.
*For each risk, specify: Risk ID, NIST Function, Severity (1–5), Likelihood (1–5), Prevention Control, Detection Mechanism, and Recovery Procedure.*

### Task 3: Tiered Human-in-the-Loop (HITL) Escalation Protocol
Design a tiered escalation policy defining exactly which actions the agent can perform independently vs. when a human supervisor must intervene:
- **Tier 1 (Autonomous)**: List at least 3 low-risk, read-only actions.
- **Tier 2 (Soft Approval Gate)**: List at least 2 actions requiring single-supervisor review.
- **Tier 3 (Hard Approval Gate)**: List at least 1 high-stakes action requiring dual-key authorization and permanent audit logging.
- Include an ASCII or Mermaid decision flow diagram illustrating how transactions pass through these gates.

### Task 4: Executive Pitch & Defense (Video Recording)
Record a concise, professional 5-minute video presentation (via Loom, Teams, Zoom, or YouTube unlisted):
- Defend your governance charter to executive leadership.
- Explain how your tiered escalation protocol accelerates productivity without sacrificing security.
- Demonstrate one specific failure scenario and how your fail-safe control mitigates it.

---

## 3. Grading Rubric (50 Points Total)

| Criteria | Exemplary (Full Points) | Developing (Partial Points) | Unacceptable (Zero Points) | Points |
|---|---|---|---|---|
| **1. Enterprise Scope & Stakeholder Mapping** | Exhaustively identifies operational boundaries, direct/indirect stakeholders, and business context. | Identifies general use case, but stakeholder analysis is shallow or missing key actors. | Vague or undefined business scenario; no stakeholder mapping. | **10** |
| **2. NIST AI RMF Risk Control Matrix** | Identifies 4+ realistic agentic hazards with robust prevention, detection, and recovery controls mapped to NIST functions. | Identifies hazards, but controls are generic (e.g., "be careful") without technical specificity. | Missing required failure modes; no clear NIST mapping. | **15** |
| **3. Tiered HITL Protocol & Decision Logic** | Clear, unambiguous 3-tier escalation structure with explicit authorization thresholds and visual flow diagram. | Tiered structure is present, but escalation boundaries are ambiguous or lack fail-safes. | No clear human-in-the-loop gates defined. | **15** |
| **4. Executive Pitch & Presentation Quality** | Polished 5-minute executive briefing; articulate technical defense; demonstrates clear governance maturity. | Video submitted but exceeds/under-runs time limit or lacks executive polish. | Video missing, broken link, or inaudible audio. | **10** |
| **Total** | | | | **50** |
