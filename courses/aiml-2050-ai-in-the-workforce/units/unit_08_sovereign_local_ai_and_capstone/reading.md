# Unit 08: Required Readings, Concepts & Slide Guidance
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

$$	ext{Memory Required (GB)} pprox \left(rac{	ext{Parameters (Billions)} 	imes 	ext{Bits per Weight}}{8}ight) 	imes 1.25	ext{ (Context Overhead)}$$

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
