# Unit 02: Open-Source Guide — NIST AI RMF Audit Templates & Governance Checklists

> **Course**: AIML 2050 — AI in the Workforce  
> **Toolchain**: NIST AI RMF 1.0, Open-Source Risk Registers, Markdown / Excel Templates  
> **Cost**: $0.00 (Zero-cost institutional standards)

---

## 1. Overview & Institutional Standards
This guide provides open-source governance tools and templates derived from the **NIST AI Risk Management Framework (NIST AI RMF 1.0)**. In accordance with LCCC policies and industry best practices, every automated agent deployed in an enterprise setting must maintain an auditable Risk Control Matrix and an explicit Human-in-the-Loop escalation protocol.

---

## 2. NIST AI RMF Risk Control Matrix Template

When designing your enterprise governance deliverable, adopt this standardized markdown structure:

```markdown
| Risk ID | Hazard / Failure Mode | NIST Function | Impact Severity (1–5) | Likelihood (1–5) | Prevention Control | Detection Mechanism | Recovery / Fail-Safe Procedure |
|:---|:---|:---|:---:|:---:|:---|:---|:---|
| **RSK-01** | Indirect Prompt Injection via external PDF | MAP / MANAGE | 5 | 3 | Sandboxed parser stripping prompt delimiters; strict Pydantic schema validation | Automated regex detector flagging system keyword anomalies | Immediate session termination; alert sent to security team |
| **RSK-02** | Runaway Execution Loop (API Hammering) | MEASURE / MANAGE | 3 | 4 | Max iteration ceiling (e.g. max 5 tool calls per user turn) | Token consumption rate limiter monitoring active graphs | Automatic circuit breaker killing the agent process |
| **RSK-03** | Unauthorized Financial Transfer | GOVERN / MANAGE | 5 | 2 | API key restricted to read-only; payment API requires HMAC signature | Transaction anomaly monitor checking amounts >$500 | Mandatory Tier 3 human approval gate before webhook fire |
| **RSK-04** | Hallucinated Regulatory Compliance Advice | MEASURE / GOVERN | 4 | 3 | Grounded RAG with strict citation retrieval; temperature set to 0.0 | Confidence threshold scoring; flag outputs with low source match | Route inquiry to licensed human compliance officer |
```

---

## 3. Tiered Escalation Decision Tree

```
                       [ Incoming Event / Task Request ]
                                      │
                                      ▼
                        Is action purely Read-Only?
                         ├── YES ──► [ Tier 1: Execute Autonomously ]
                         └── NO
                              │
                              ▼
                Does transaction involve >$500 or PII?
                         ├── NO  ──► [ Tier 2: Agent Prepares Draft &
                         │                     Awaits Supervisor Click ]
                         └── YES ──► [ Tier 3: Hard Stop / Dual-Key Human
                                               Approval Required ]
```

---

## 4. Open-Source Resources & Official Standards
- **NIST AI RMF 1.0 Document**: [NIST Special Publication AI 100-1](https://www.nist.gov/itl/ai-risk-management-framework)
- **NIST AI RMF Playbook**: Operational guidance for MAP, MEASURE, and MANAGE functions.
- **OWASP Top 10 for Large Language Model Applications**: Reference catalog for prompt injections, data poisoning, and excessive agency.
