# Unit 08: Required Readings, Concepts & Slide Guidance
## Sovereign Local AI, On-Device Runtime & Final Capstone Defense

> **Course**: AIML 2050 — AI in the Workforce  
> **Contact Allocation**: 150 Minutes  
> **Source Modules**: Intel Modules 17, 18, 19 & 20

---

## 1. Curated Slide Reading Directives

Refer to the following specific sections of the Intel presentation decks:

### A. From `[Slides] Module 17 - Agentic AI.pptx` (81 slides total)
- **Study Slides 8–41 (Hardware Requirements for Local AI)**: Master CPU vs GPU vs NPU architectures, unified memory, and memory bandwidth bottlenecks.
- **Study Slides 42–75 (Serving Models Locally vs Cloud Costs & Enterprise Privacy Drivers)**: Calculate total cost of ownership (TCO): cloud token subscription costs vs on-premise hardware capital expenditures. Master privacy regulations (HIPAA, FERPA).

### B. From `[Slides] Module 18 - Agentic AI.pptx` (56 slides total)
- **Study Slides 7–23 (Software Stack for Local Agents)**: Overview of Ollama, Docker, OpenVINO, SQLite, and local FAISS vector memory.
- **Study Slides 24–44 (Model Optimization & Quantization)**: Master quantization formats (FP16 &rarr; INT8 &rarr; INT4 / GGUF), perplexity loss, and tokens-per-second benchmarks.
- **Study Slides 45–52 (Building a Local System Management Agent)**: Practical execution patterns for local CLI agents.

### C. From `[Slides] Module 19 - Agentic AI.pptx` (162 slides total)
- **Study Slides 7–35 (Sovereign AI & Confidential Computing)**: Air-gapped networks, preventing telemetry exfiltration, and local data isolation.
- **Study Slides 36–62 (Assets of an Agentic Application & SKILL.md Standards)**: Structure file-based skill assets, tool configurations, and prompt instructions.
- **Study Slides 112–135 (Policy-as-Configuration & Packaging for Release)**: Versioning, licensing, and enterprise packaging.
- *Skip Slides 63–111 & 136–162*.

### D. From `[Slides] Module 20 - Agentic AI.pptx` (102 slides total)
- **Study Slides 8–32 (Capstone System Requirements & Architecture Specification)**: Capstone scoping and technical specification standards.
- **Study Slides 33–54 (Local Agent Development & Offline Data Integration)**: Building offline RAG stores and local tool bindings.
- **Study Slides 55–80 (Evaluation, Risk Assessment, Packaging & Executive Defense)**: Executive presentation structure and defense rubrics.

---

## 2. Core Conceptual Deep Dive: Sovereign Local AI Architecture

### The Hardware Sizing Formula for Local Models
To determine if a PC can run a local model, calculate the required memory:
$$VRAM = (Parameters * BitsPerWeight / 8) * 1.25$$

- **7 Billion Parameter Model in FP16 (16-bit)**: ~17.5 GB VRAM (Requires expensive high-end GPU).
- **7 Billion Parameter Model in INT4 / GGUF (4-bit)**: ~4.4 GB RAM (Runs smoothly on any standard modern laptop with 8–16 GB RAM!).

### The Sovereign Local AI Stack
1. **Workplace Interface**: Desktop UI or terminal client.
2. **Local Runtime (Ollama / OpenVINO)**: Serving quantized model on localhost with zero external transmission.
3. **Local State & Vector Memory**: SQLite and FAISS persistent stores.
4. **SKILL.md Specifications**: Standardized skill and tool declarations.
