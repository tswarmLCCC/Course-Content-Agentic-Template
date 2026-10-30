# Unit 04: Required Readings, Concepts & Slide Guidance
## No-Code Business Agents & Workflow Orchestration

> **Course**: AIML 2050 — AI in the Workforce  
> **Contact Allocation**: 150 Minutes  
> **Source Modules**: Intel Modules 09, 10, 11 & 12

---

## 1. Curated Slide Reading Directives

Refer to the following specific sections of the Intel presentation decks:

### A. From `[Slides] Module 09 - Agentic AI.pptx` (173 slides total)
- **Study Slides 8–39 (Designing Conversational Agents & Document Grounding)**: Learn how custom GPTs, Gems, and Copilot agents bind external documentation (PDFs, knowledge bases) to system prompts.
- **Study Slides 128–151 (Microsoft Copilot Studio & Connectors)**: Examine enterprise connectors (SharePoint, Dynamics 365, Power Automate).
- **Study Slides 152–170 (Comparative Evaluation of No-Code Agent Platforms)**: Understand trade-offs between proprietary ecosystem builders vs open orchestrators.
- *Skip Slides 40–127* (elementary prompting walkthroughs).

### B. From `[Slides] Module 10 - Agentic AI.pptx` (95 slides total)
- **Study Slides 8–41 (No-Code Agent Builders & Mini-Agents)**: Contrast linear scripts with agentic decision nodes.
- **Study Slides 42–66 (Webhooks, Trigger Events & API Authentication)**: Master webhook payloads, HTTP methods (POST, GET), and Bearer token / header authentication.
- **Study Slides 67–88 (Implementing Guardrails in Automated SaaS Workflows)**: Techniques for sanitizing LLM outputs before firing downstream API calls.

### C. From `[Slides] Module 11 - Agentic AI.pptx` (81 slides total)
- **Study Slides 36–52 (Advanced No-Code Orchestrators: n8n, Make, Zapier)**: Compare node execution graphs and data-passing contracts.
- **Study Slides 53–73 (Error Handling, Retries & Dead-Letter Queues)**: Master exponential backoff, error trigger nodes, and administrative fallback notifications.

### D. From `[Slides] Module 12 - Agentic AI.pptx` (69 slides total)
- **Study Slides 10–38 (Multi-Agent System Scope & Architecture)**: Study the Orchestrator-Worker pattern in no-code environments.
- **Study Slides 40–63 (Deliverables & Process Documentation)**: Standards for documenting enterprise automation pipelines.

---

## 2. Core Conceptual Deep Dive: Resilient Workflow Orchestration

### Deterministic Pipes vs. Probabilistic Agents
Enterprise automation requires a hybrid balance:
- **Deterministic Workflows (n8n / Make)**: Handle trigger events, data transformations, API authentication, and routing. These steps must happen predictably 100% of the time.
- **Probabilistic Agents (LLM Nodes)**: Handle unstructured cognitive tasks (e.g. summarizing a messy email, classifying customer sentiment, extracting invoice line items).
- **Golden Rule**: *Never use an LLM for what a deterministic regex or lookup table can do reliably.*

### The Orchestrator-Worker Architecture in n8n
```
                    [ Inbound Webhook / Trigger ]
                                  │
                                  ▼
                    [ Orchestrator Agent Node ]
               (Decomposes request & selects workers)
                                  │
                 ┌────────────────┴────────────────┐
                 ▼                                 ▼
      [ Research Worker Node ]           [ Math / SQL Worker Node ]
      - Queries Knowledge Store          - Queries Database
                 │                                 │
                 └────────────────┬────────────────┘
                                  ▼
                    [ Response Synthesizer Node ]
                                  │
                                  ▼
               [ Outbound Action / Email / Notification ]
```

### Defensive Error Handling & Dead-Letter Queues
If an LLM API experiences a 503 outage or returns malformed JSON, a production pipeline must not silently fail:
1. **Automated Retries**: Retry up to 3 times with exponential backoff (1s, 2s, 4s).
2. **Fallback Model**: If Model A fails, automatically route to Model B.
3. **Dead-Letter Queue (DLQ)**: If all retries fail, write the raw payload to an error table and send an emergency alert to the human administrator.
