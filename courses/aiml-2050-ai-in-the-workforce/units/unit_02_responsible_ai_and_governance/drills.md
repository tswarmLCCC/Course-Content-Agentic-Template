# Unit 02: Asynchronous Preparation & Diagnostic Drills
## Responsible AI, Risk Management & Enterprise Governance

> **Time Commitment**: ~60 Minutes (Asynchronous Self-Study)  
> **Target Mastery**: NIST AI RMF functions, agent failure modes, Human-in-the-Loop escalation design.

---

## 1. Readiness Checklist
- [ ] Studied slides on autonomous failure modes in `[Slides] Module 03`.
- [ ] Reviewed the four core NIST AI RMF functions (GOVERN, MAP, MEASURE, MANAGE).
- [ ] Examined the Tiered Escalation Decision Tree in the Open-Source Guide.

---

## 2. Formative Diagnostic Drills

<details>
<summary>Drill 1: Why is an agent 'Loop Lock' significantly more dangerous than a standard software crash?</summary>

**Architectural Rationale:**
When traditional software crashes, it halts execution and stops consuming resources. When an autonomous agent encounters an unexpected error without an iteration ceiling, its reasoning engine attempts to "fix" the problem by retrying variations of the action repeatedly. This can exhaust expensive LLM API token quotas within minutes, overwhelm downstream third-party APIs, and trigger secondary rate-limiting penalties across the enterprise.
</details>

<details>
<summary>Drill 2: In the NIST AI RMF, what is the fundamental distinction between the 'MAP' and 'MEASURE' functions?</summary>

**Architectural Rationale:**
- **MAP** is qualitative and contextual: It identifies the system's operational boundaries, business context, relevant stakeholders, and potential hazards before implementation.
- **MEASURE** is quantitative and empirical: It applies formal metrics, test datasets, benchmark suites, and statistical tracking (e.g. measuring hallucination rate, latency, token drift, and false-positive escalation frequency) over the system's lifecycle.
</details>

<details>
<summary>Drill 3: What constitutes 'Indirect Prompt Injection', and why are agentic tool-calling systems particularly vulnerable?</summary>

**Architectural Rationale:**
Indirect prompt injection occurs when malicious adversarial text is embedded in third-party data retrieved by the agent (e.g., a customer review, a parsed resume, a web scrape, or an email). Because the LLM processes this retrieved text as part of its prompt context, the malicious instructions can hijack the agent's reasoning loop, tricking the agent into executing privileged tools (e.g., deleting records, sending sensitive emails) under the attacker's direction.
</details>

<details>
<summary>Drill 4: Why should Tier 3 escalation gates require cryptographic or role-based authentication rather than simple conversational confirmation?</summary>

**Architectural Rationale:**
If an agent asks in a chat interface: *"Should I proceed with transferring $10,000? (Reply yes/no)"*, an attacker or prompt injection could trick the LLM into answering its own question or misinterpreting a user statement. A true Tier 3 gate interrupts code execution, stores state out-of-band in a secure database, and requires a human supervisor to log into an authenticated dashboard to physically sign off on the transaction.
</details>
