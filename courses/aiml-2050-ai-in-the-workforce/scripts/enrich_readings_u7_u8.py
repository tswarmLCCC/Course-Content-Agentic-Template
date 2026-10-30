#!/usr/bin/env python3
"""
Enriches Units 07 and 08 reading.md to 1815/COSC-2060 depth.
"""
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
UNITS_DIR = BASE_DIR / "units"

def enrich_unit_07():
    u_dir = UNITS_DIR / "unit_07_observability_and_evaluation"
    content = """# Unit 07: Required Readings, Concepts & Slide Guidance
## Agent Governance, Observability & Automated Evaluation

Welcome to the instructional study hub for **Unit 07: Agent Governance, Observability & Automated Evaluation**. This reading organizes core evaluation competencies into four structured chapters:

1. **Instructor Lecture & Narrative Deep Dive**: The Flying Blind Dilemma — Managing What You Cannot Observe.
2. **Physical Mental Models & Architecture**: The Observability Quad (Traces, Latency, Token Accounting & Failure Profiling).
3. **Curated Slide Reading Directives**: Exact study guidance for Intel Module 15.
4. **Automated Evaluation Suites & Defensive Guardrail Filters**: Ground-truth benchmarking vs. probabilistic variation.

---

## 1. Instructor Lecture & Narrative Deep Dive

### The Flying Blind Dilemma: The $8,000 Midnight Loop

In early 2025, an enterprise customer service team deployed an autonomous triage agent connected to their helpdesk portal. The agent used a modern cloud LLM API, equipped with a vector knowledge base and ticket tagging tools.

At 1:15 AM on a Saturday, an automated monitoring system sent a routine diagnostic alert email to the helpdesk:
`"ALERT: Server memory at 78% on node-04"`.

The agent received the email, parsed it, and reasoned: *"This is a technical alert. I must notify the IT system."* It called a tool to send a confirmation ticket. 
The IT system immediately replied with an automated confirmation: *"Ticket #9901 created for alert"*.
The agent perceived the new email: *"A new ticket has been created. I must acknowledge it."*

Because the developers had implemented **zero telemetry tracing or loop detection**:
- The agent entered an infinite autonomous loop between itself and the IT auto-responder.
- Over 6 hours, it executed **48,000 back-and-forth LLM inference calls**.
- By 7:00 AM, the company had burned **$8,400 in API token fees**, and the helpdesk was clogged with 24,000 duplicate ticket updates.

#### The Lesson: Observability is a Production Prerequisite
You cannot safely manage what you cannot observe. In traditional software, logging HTTP 200 vs 500 status codes is enough. **Agentic systems require cognitive telemetry**:
- Tracking total tokens and financial cost per user session.
- Profiling latency across individual reasoning thoughts vs tool executions.
- Detecting repetitive tool invocations and tripping automated circuit breakers.

---

## 2. Physical Mental Models & Architecture

### The Observability Quad

```
┌────────────────────────────────────────────────────────┐
│               THE AGENT OBSERVABILITY QUAD             │
└──────────────────────────┬─────────────────────────────┘
                           │
       ┌───────────────────┼───────────────────┐
       ▼                   ▼                   ▼
┌──────────────┐    ┌──────────────┐    ┌──────────────┐
│  Trace Trees │    │  Cost & Token│    │  Latency     │
│  & Node Flow │    │  Accounting  │    │  Profiling   │
└──────┬───────┘    └──────┬───────┘    └──────┬───────┘
       │                   │                   │
Step-by-step        Tracks prompt       Identifies
reasoning chain     and completion      whether delay is
from user prompt    tokens per turn     LLM inference or
to tool observation to catch spikes     external API
```

### Why Traditional Unit Tests Fail on AI Agents
In traditional software, `assert add(2, 2) == 4` is absolute and deterministic.
In agentic AI, testing is probabilistic:
- If a user asks *"Can I expense my dinner?"*, the agent might say *"Yes, up to $75 with receipt"* or *"Meal expenses are reimbursable up to seventy-five dollars"*.
- Exact string assertion fails even when the model's behavior is 100% correct.

To test agents systematically, teams implement **Automated Evaluation Harnesses**:
- Standardized test datasets covering: (1) Standard Ideal Prompts, (2) Ambiguous Edge Cases, and (3) Adversarial Prompt Injections.
- **LLM-as-a-Judge**: An independent evaluator model scored against a structured rubric (Factual Grounding, Safety, Coherence).

---

## 3. Curated Slide Reading Directives

Refer to the following specific sections of the Intel presentation deck:

### From `[Slides] Module 15 - Agentic AI.pptx` (102 slides)
- **Study Slides 8–29 (Governance in Agentic AI)**: Safety, regulatory compliance, accountability, and auditability.
- **Study Slides 30–44 (Implementing Guardrails)**: Direct and indirect prompt injection defense, PII sanitization, and permission sandboxing.
- **Study Slides 45–56 (Risk Categories & Enterprise Control Matrices)**: Operational risk scoring and mitigation strategies.
- **Study Slides 60–98 (Monitoring, Telemetry Tracing & Evaluating Agents)**: Execution traces, token accounting, and test dataset benchmarking.
- *Skip Slides 57–59 & 99–102*.

---

## 4. Automated Evaluation Suites & Defensive Guardrail Filters

### Input and Output Guardrail Filters
A production agent wraps the model with defensive filters:
- **Input Guardrails**: Regex patterns and semantic classifiers that intercept prompt injection attempts (*"Ignore previous instructions"*, *"System override"*) before they reach the model.
- **Output Guardrails**: Sanitizers that ensure the model never leaks internal system prompts, API keys, or raw personally identifiable information (PII).
"""
    with open(u_dir / "reading.md", "w", encoding="utf-8") as f:
        f.write(content)
    print("  [+] Unit 07 reading.md enriched.")

def enrich_unit_08():
    u_dir = UNITS_DIR / "unit_08_sovereign_local_ai_and_capstone"
    content = """# Unit 08: Required Readings, Concepts & Slide Guidance
## Sovereign Local AI, On-Device Runtime & Final Capstone Defense

Welcome to the capstone instructional study hub for **Unit 08: Sovereign Local AI, On-Device Runtime & Final Capstone Defense**. This reading organizes core capstone competencies into four structured chapters:

1. **Instructor Lecture & Narrative Deep Dive**: The Privacy Mandate — Why Enterprise AI is Moving from Cloud to Edge.
2. **Physical Mental Models & Architecture**: The Physics of Local LLMs (Memory Sizing Formulas & Quantization).
3. **Curated Slide Reading Directives**: Exact study guidance for Intel Modules 17, 18, 19, and 20.
4. **Standardized Packaging & The Capstone Defense**: `SKILL.md` specifications and executive presentation structure.

---

## 1. Instructor Lecture & Narrative Deep Dive

### The Privacy Mandate: Why Regulated Industries Cannot Use Public Cloud APIs

In late 2024, a major defense contractor and an international healthcare conglomerate both issued strict internal bans on commercial cloud LLM APIs. 

The rationale was straightforward:
- **Legal Compliance**: Under HIPAA (healthcare) and ITAR/CMMC (defense), transmitting patient records or defense schematics across third-party cloud servers introduces severe regulatory liability.
- **Intellectual Property Leaks**: Even when cloud providers offer "zero-data-retention" enterprise tiers, organizations cannot eliminate the risk of vendor subpoena, accidental telemetry logging, or cloud breach.
- **The Financial TCO Equation**: For enterprises processing millions of transactions daily, paying per-token API subscriptions becomes vastly more expensive than running quantized models locally on existing on-premise hardware.

#### The Sovereign AI Paradigm
**Sovereign Local AI** means the model, the vector database, the runtime, and the toolchain run 100% on the local physical workstation or private on-premise server:
- Zero packets leave the local network.
- The computer can operate with the Wi-Fi disabled (air-gapped).
- Organizational data remains in strict physical custody.

---

## 2. Physical Mental Models & Architecture

### The Physics of Local LLMs: Hardware Sizing & Quantization

To run language models locally, understanding physical memory constraints is essential.
The primary bottleneck for local LLMs is not raw compute speed; **it is memory capacity and memory bandwidth**.

$$\text{Memory Required (GB)} \approx \left(\frac{\text{Parameters (Billions)} \times \text{Bits per Weight}}{8}\right) \times 1.25\text{ (Context Overhead)}$$

```
MODEL: 7 Billion Parameter LLM (e.g., Llama 3)

1. FULL PRECISION (FP16 - 16-bit):
   (7 * 16 / 8) * 1.25 = 17.5 GB VRAM
   - Requires expensive dedicated high-end GPU ($1,500+).
   - Crashes on standard business laptops.

2. QUANTIZED INT4 / GGUF (4-bit):
   (7 * 4 / 8) * 1.25 = 4.38 GB RAM
   - Fits comfortably on any modern enterprise PC or laptop with 8–16 GB RAM!
   - Quantization compresses weights from 16-bit floating point down to 4-bit integers with less than 1% loss in task accuracy.
```

### The Sovereign Local AI Stack
```
┌────────────────────────────────────────────────────────┐
│ 1. Workplace UI / Desktop Interface                    │
└──────────────────────────┬─────────────────────────────┘
                           │ Local REST (http://localhost:11434)
                           ▼
┌────────────────────────────────────────────────────────┐
│ 2. Local Runtime: Ollama / OpenVINO Model Server       │
│    - INT4 Quantized Open-Source Model (Llama 3.2, etc.)│
│    - CPU, GPU, and Intel NPU Hardware Acceleration     │
└──────────────────────────┬─────────────────────────────┘
                           │ Tool Execution & Retrieval
                           ▼
┌────────────────────────────────────────────────────────┐
│ 3. Sovereign Local Store (Air-Gapped / Zero Internet)   │
│    - SQLite Persistent State | FAISS Vector Store      │
│    - Portable SKILL.md Declarations & Secure Tools     │
└────────────────────────────────────────────────────────┘
```

---

## 3. Curated Slide Reading Directives

Refer to the following specific sections of the Intel presentation decks:

### A. From `[Slides] Module 17 - Agentic AI.pptx` (81 slides)
- **Study Slides 8–41 (Hardware Requirements for Local AI)**: CPU vs GPU vs NPU architectures, unified memory, and memory bandwidth bottlenecks.
- **Study Slides 42–75 (Serving Models Locally vs Cloud Costs)**: Total Cost of Ownership (TCO) comparisons and enterprise privacy compliance drivers (HIPAA, FERPA).

### B. From `[Slides] Module 18 - Agentic AI.pptx` (56 slides)
- **Study Slides 7–23 (Software Stack for Local Agents)**: Overview of Ollama, Docker, OpenVINO, SQLite, and FAISS.
- **Study Slides 24–44 (Model Optimization & Quantization)**: Quantization formats (GGUF, INT4/INT8) and tokens-per-second benchmarks.
- **Study Slides 45–52 (Building a Local System Management Agent)**: Practical implementation patterns.

### C. From `[Slides] Module 19 - Agentic AI.pptx` (162 slides)
- **Study Slides 7–35 (Sovereign AI & Confidential Computing)**: Air-gapped isolation and data sovereignty.
- **Study Slides 36–62 (Assets of an Agentic Application & SKILL.md Standards)**: Structure file-based skill assets and tool configurations.
- **Study Slides 112–135 (Policy-as-Configuration & Packaging)**: Versioning, licensing, and enterprise deployment.
- *Skip Slides 63–111 & 136–162*.

### D. From `[Slides] Module 20 - Agentic AI.pptx` (102 slides)
- **Study Slides 8–32 (Capstone System Requirements & Specification)**: Requirements engineering for capstone projects.
- **Study Slides 33–54 (Local Development & Offline Data Integration)**: Offline vector stores and local tool binding.
- **Study Slides 55–80 (Evaluation, Risk Assessment & Executive Defense)**: Structuring executive presentations.

---

## 4. Standardized Packaging & The Capstone Defense

### The `SKILL.md` Configuration Standard
To ensure agent capabilities are portable across runtime environments, package tool definitions into a declarative `SKILL.md` file:
- Declares the agent's name, version, and operational boundary.
- Formally specifies tool parameters and required inputs.
- Enforces strict governance flags (`cloud_transmission_allowed: false`, `pii_sanitization_required: true`).

### Delivering a Winning Executive Capstone Defense
Your 7-minute executive presentation must balance technical execution with business strategy:
1. **The Business Problem (2 min)**: As-Is Value Stream Map and quantifiable pain points.
2. **The Technical Demonstration (2.5 min)**: Live demo running offline on Ollama/OpenVINO with local RAG and tool execution.
3. **The Governance Defense (1.5 min)**: NIST AI RMF risk matrix and tiered Human-in-the-Loop escalation gates.
4. **ROI & Workforce Impact (1 min)**: Projected time savings, financial payback period, and employee upskilling strategy.
"""
    with open(u_dir / "reading.md", "w", encoding="utf-8") as f:
        f.write(content)
    print("  [+] Unit 08 reading.md enriched.")

if __name__ == "__main__":
    enrich_unit_07()
    enrich_unit_08()
