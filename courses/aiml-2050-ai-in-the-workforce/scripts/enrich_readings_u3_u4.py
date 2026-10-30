#!/usr/bin/env python3
"""
Enriches Units 03 and 04 reading.md to 1815/COSC-2060 depth.
"""
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
UNITS_DIR = BASE_DIR / "units"

def enrich_unit_03():
    u_dir = UNITS_DIR / "unit_03_workplace_tools_and_prototyping"
    content = """# Unit 03: Required Readings, Concepts & Slide Guidance
## Workplace Productivity Tools & Rapid Prototyping

Welcome to the instructional study hub for **Unit 03: Workplace Productivity Tools & Rapid Prototyping**. This reading organizes core competencies into four structured chapters:

1. **Instructor Lecture & Narrative Deep Dive**: The Prototyping Paradox — Why Executive Slide Decks Fail and Working Web Apps Win.
2. **Physical Mental Models & Architecture**: The Three-Tier Architecture of Workplace Prototypes (UI, Logic, State).
3. **Curated Slide Reading Directives**: Exact study guidance for Intel Modules 06, 07, and 08.
4. **State Persistence, Telemetry & User Feedback**: Avoiding "vibe-coding" through structured database logging.

---

## 1. Instructor Lecture & Narrative Deep Dive

### The Prototyping Paradox: Why Slide Decks Fail in the Enterprise

In enterprise technology adoption, there is an iron law known as the **Prototyping Paradox**: *The more sophisticated an AI concept is on PowerPoint slides, the less likely business executives are to understand or approve it.*

In early 2024, a corporate innovation team spent four months and $180,000 preparing an exhaustive 65-slide pitch deck for an "AI-Powered Customer Onboarding Assistant." The deck contained market analysis, transformer architecture diagrams, and projected 400% ROI.

When presented to the Operating Committee, the proposal was rejected within 15 minutes. Why?
- Executives could not picture the human worker's day-to-day experience.
- The legal team raised abstract concerns about hallucination that the deck could not disprove.
- The business unit leader concluded: *"This sounds powerful, but it feels like theoretical vaporware."*

Three weeks later, a junior business analyst built a lightweight **Streamlit** prototype in two days. The prototype had an input form, connected to a local SQLite database, ran mock triage logic, and featured an interactive table showing logged tickets. She demonstrated it live on her laptop in a 5-minute meeting. The project was funded immediately.

#### The Lesson: Show, Don't Tell
In workforce AI, a rough, working prototype that a non-technical manager can click, test, and critique is worth 100 slide decks. Rapid prototyping collapses the feedback loop from months to hours.

---

## 2. Physical Mental Models & Architecture

### The Three-Tier Architecture of Rapid Workplace Prototypes

A robust workplace prototype cleanly separates concerns into three distinct layers:

```
┌────────────────────────────────────────────────────────┐
│ 1. Presentation Layer (UI/UX)                          │
│    Built with Streamlit, Gradio, or Lovable React      │
│    Provides dropdowns, parameter sliders, chat windows │
└──────────────────────────┬─────────────────────────────┘
                           │ User Input & Parameters
                           ▼
┌────────────────────────────────────────────────────────┐
│ 2. Logic & Reasoning Engine (The Core)                 │
│    System instructions, schema validation, LLM runtime │
│    Handles API orchestration and error recovery        │
└──────────────────────────┬─────────────────────────────┘
                           │ Read & Write Transactions
                           ▼
┌────────────────────────────────────────────────────────┐
│ 3. Persistent Data & State Layer (The Vault)           │
│    SQLite database, Supabase cloud store, or JSON logs │
│    Stores session history, ratings, and audit traces   │
└────────────────────────────────────────────────────────┘
```

### The Pitfall of "Vibe-Coding" Without State
Many prototypes fail in stakeholder testing because they are entirely stateless. When the user refreshes the browser, all context disappears. By incorporating a persistent SQLite table, the prototype:
1. Captures real prompt telemetry for engineering analysis.
2. Enables thumbs-up/down feedback collection from test users.
3. Proves to compliance officers that all automated actions leave an immutable audit trail.

---

## 3. Curated Slide Reading Directives

Refer to the following specific sections of the Intel presentation decks:

### A. From `[Slides] Module 06 - Agentic AI.pptx` (124 slides)
- **Study Slides 8–35 (Everyday Enterprise Workflows)**: Review productivity returns in CRM data entry, calendar coordination, and document synthesis.
- **Study Slides 61–84 (Agentic AI Tools for Business Operations)**: Analyze Microsoft Copilot, Google Workspace AI, and specialized vertical point solutions.
- **Study Slides 85–110 (Measuring Productivity Gains & Avoiding Pitfalls)**: Master metrics for measuring time saved per task, error reduction, and cognitive fatigue.
- *Skip Slides 36–60 & 111–124*.

### B. From `[Slides] Module 07 - Agentic AI.pptx` (154 slides)
- **Study Slides 8–41 (AI Prototyping Tools & Prompting)**: Compare Streamlit, Gradio, Lovable, and v0 for rapid deployment.
- **Study Slides 42–60 (UI/UX Design Principles for Human-AI Interaction)**: Master principles of streaming token output, optimistic updates, and affordances for manual override.
- **Study Slides 94–111 (Integrating Real-Time External Data)**: Learn how to bind UI widgets to SQLite and REST APIs.
- **Study Slides 112–135 (Deploying, Sharing & Collecting Feedback)**: Structured telemetry capture and user rating mechanisms.
- *Skip Slides 61–93 & 136–154*.

### C. From `[Slides] Module 08 - Agentic AI.pptx` (71 slides)
- **Study Slides 12–34 (Business Concept Ideation & Architecture)**: Structure rapid prototype architecture into presentation, logic, and data tiers.
- **Study Slides 44–64 (Risk Assessment & Stakeholder Demonstration)**: Strategies for pitching prototypes to operational leaders.

---

## 4. State Persistence, Telemetry & User Feedback

### Designing for Non-Deterministic Latency
LLM inference takes 3 to 15 seconds. If a web prototype freezes without feedback, users assume it has crashed.
- **Streaming Output**: Stream tokens in real time so the user perceives immediate response.
- **Progress Checkpoints**: Display explicit status spinners (*"1/3: Reading invoice...", "2/3: Querying database...", "3/3: Synthesizing summary..."*).
"""
    with open(u_dir / "reading.md", "w", encoding="utf-8") as f:
        f.write(content)
    print("  [+] Unit 03 reading.md enriched.")

def enrich_unit_04():
    u_dir = UNITS_DIR / "unit_04_no_code_agents_and_orchestration"
    content = """# Unit 04: Required Readings, Concepts & Slide Guidance
## No-Code Business Agents & Workflow Orchestration

Welcome to the instructional study hub for **Unit 04: No-Code Business Agents & Workflow Orchestration**. This reading organizes core automation competencies into four structured chapters:

1. **Instructor Lecture & Narrative Deep Dive**: The Silent Webhook Failure — When Cloud Automations Drop Critical Transactions.
2. **Physical Mental Models & Architecture**: Deterministic Pipes vs. Probabilistic Brains (The Golden Rule of Automation).
3. **Curated Slide Reading Directives**: Exact study guidance for Intel Modules 09, 10, 11, and 12.
4. **Defensive Workflow Architecture**: Retries, Exponential Backoff, Dead-Letter Queues, and Multi-Agent Orchestration.

---

## 1. Instructor Lecture & Narrative Deep Dive

### The Narrative of Integration: The Silent Webhook Failure

In mid-2024, a high-growth SaaS enterprise integrated an automated sales-triage pipeline using a cloud workflow orchestrator. The pipeline listened for incoming customer leads via webhooks from their web portal, passed the inquiry text to an LLM node to extract customer budget and intent, and created an account in their Salesforce CRM.

On the last day of the fiscal quarter, a marketing campaign drove 8,000 simultaneous submissions in two hours.

The cloud LLM provider began returning HTTP `429: Rate Limit Exceeded`. Because the workflow pipeline had no automated retry logic or dead-letter queue:
1. Every failed LLM node immediately aborted execution.
2. The orchestrator silently discarded the incoming webhook payloads without logging.
3. Over **3,200 high-intent enterprise leads vanished** with zero trace in the CRM.

Management did not discover the failure until sales executives noticed a 40% drop in expected quarterly revenue.

#### The Lesson: Build Defensive Pipelines
In enterprise automation, assuming 100% API uptime is fatal. A production orchestration pipeline must be built with **defensive resilience**:
- Webhook idempotency to prevent duplicate charging.
- Exponential backoff retries to ride out transient outages.
- Dead-letter queues that capture failed payloads to disk so zero data is ever lost.

---

## 2. Physical Mental Models & Architecture

### Deterministic Pipes vs. Probabilistic Brains

The most critical architectural principle in workflow engineering is **The Golden Rule of Automation**:
> *Never use an LLM for what a deterministic regex, lookup table, or mathematical formula can do reliably.*

```
┌────────────────────────────────────────────────────────┐
│               THE HYBRID AUTOMATION ENGINE             │
└──────────────────────────┬─────────────────────────────┘
                           │
       ┌───────────────────┴───────────────────┐
       ▼                                       ▼
┌──────────────────────────────┐┌──────────────────────────────┐
│  DETERMINISTIC PIPES (n8n)   ││ PROBABILISTIC BRAINS (LLM)   │
│  - Webhook listener          ││ - Summarize messy email text │
│  - HMAC authentication       ││ - Classify customer intent   │
│  - Database INSERT / UPDATE  ││ - Extract ambiguous line items│
│  - Mathematical pricing      ││ - Draft empathetic response  │
│  100% PREDICTABLE & EXACT    ││ PROBABILISTIC & CREATIVE     │
└──────────────────────────────┘└──────────────────────────────┘
```

### The Orchestrator-Worker Multi-Agent Topology
In complex multi-step processes, a single prompt cannot handle everything. Instead, deploy an **Orchestrator-Worker** model in n8n:
- **Orchestrator Agent**: Inspects incoming request, categorizes intent (e.g. Technical Support vs. Billing), and routes data to specialized sub-agents.
- **Worker Agents**: Specialized mini-agents equipped only with the specific tools and documents needed for their domain.

---

## 3. Curated Slide Reading Directives

Refer to the following specific sections of the Intel presentation decks:

### A. From `[Slides] Module 09 - Agentic AI.pptx` (173 slides)
- **Study Slides 8–39 (Designing Conversational Agents & Document Grounding)**: Learn how custom GPTs, Gems, and Copilot agents bind external documentation to prompts.
- **Study Slides 128–151 (Microsoft Copilot Studio & Connectors)**: Examine enterprise connectors (SharePoint, Dynamics 365, Power Automate).
- **Study Slides 152–170 (Comparative Evaluation of No-Code Platforms)**: Trade-offs between proprietary ecosystems vs open orchestrators.
- *Skip Slides 40–127*.

### B. From `[Slides] Module 10 - Agentic AI.pptx` (95 slides)
- **Study Slides 8–41 (No-Code Agent Builders & Mini-Agents)**: Contrast linear scripts with agentic decision nodes.
- **Study Slides 42–66 (Webhooks, Trigger Events & API Authentication)**: Master webhook payloads, HTTP methods, and Bearer token headers.
- **Study Slides 67–88 (Guardrails in Automated SaaS Workflows)**: Sanitizing outputs before firing external APIs.

### C. From `[Slides] Module 11 - Agentic AI.pptx` (81 slides)
- **Study Slides 36–52 (Advanced Orchestrators: n8n, Make, Zapier)**: Compare node execution graphs and data contracts.
- **Study Slides 53–73 (Error Handling, Retries & Dead-Letter Queues)**: Exponential backoff, error triggers, and fallback alerting.

### D. From `[Slides] Module 12 - Agentic AI.pptx` (69 slides)
- **Study Slides 10–38 (Multi-Agent System Scope & Architecture)**: Orchestrator-Worker patterns in no-code environments.
- **Study Slides 40–63 (Deliverables & Process Documentation)**: Documenting enterprise automation pipelines.

---

## 4. Defensive Workflow Architecture

### Implementing Dead-Letter Queues (DLQ)
When building pipelines in n8n:
1. Configure an **Error Trigger Node** that activates whenever any workflow step throws an unhandled exception.
2. In the error branch, append the raw payload, timestamp, and error message to an **Error Log Table** (in SQLite, Google Sheets, or Postgres).
3. Send an immediate notification to the system administrator via Slack or email.
"""
    with open(u_dir / "reading.md", "w", encoding="utf-8") as f:
        f.write(content)
    print("  [+] Unit 04 reading.md enriched.")

if __name__ == "__main__":
    enrich_unit_03()
    enrich_unit_04()
