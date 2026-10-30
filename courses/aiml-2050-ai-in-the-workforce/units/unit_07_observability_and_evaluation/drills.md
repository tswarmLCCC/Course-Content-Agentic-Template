# Unit 07: Asynchronous Preparation & Diagnostic Drills
## Agent Governance, Observability & Automated Evaluation

> **Time Commitment**: ~60 Minutes (Asynchronous Self-Study)  
> **Target Mastery**: Telemetry trace inspection, adversarial guardrails, evaluation datasets.

---

## 1. Readiness Checklist
- [ ] Studied slides on LangSmith and governance in `[Slides] Module 15`.
- [ ] Tested the local evaluation harness and telemetry logger.
- [ ] Reviewed adversarial prompt patterns and guardrail regex filters.

---

## 2. Formative Diagnostic Drills

<details>
<summary>Drill 1: Why is latency profiling critical for diagnosing runaway agent loops?</summary>

**Architectural Rationale:**
If a standard turn takes 800 milliseconds, but a specific user query takes 14 seconds, latency profiling breaks down the execution tree to show that the agent called a tool, failed to parse the JSON, and retried 5 times in a loop. Identifying which specific node caused the delay prevents token waste and improves user responsiveness.
</details>

<details>
<summary>Drill 2: What is the purpose of an 'LLM-as-a-Judge' evaluation architecture?</summary>

**Architectural Rationale:**
Because generative responses cannot be evaluated with exact string matches, an independent, high-capability model (e.g. GPT-4 or Gemini Pro) is given the candidate agent's output alongside a strict evaluation rubric (Factual Grounding, Safety, Coherence). The judge model evaluates the answer and returns an objective numeric score and justification.
</details>

<details>
<summary>Drill 3: In an automated benchmark evaluation, why must the dataset include deliberately adversarial test prompts?</summary>

**Architectural Rationale:**
Testing only happy-path queries gives a false sense of security. Adversarial prompts (jailbreaks, prompt injections, privilege escalation attempts) verify that input guardrails and safety tripwires function correctly under attack before deploying to enterprise end-users.
</details>
