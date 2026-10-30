# Unit 08: Asynchronous Preparation & Diagnostic Drills
## Sovereign Local AI, On-Device Runtime & Final Capstone Defense

> **Time Commitment**: ~60 Minutes (Asynchronous Self-Study)  
> **Target Mastery**: VRAM calculation formulas, quantization trade-offs, data sovereignty verification.

---

## 1. Readiness Checklist
- [ ] Studied hardware sizing and quantization in `[Slides] Module 17` and `[Slides] Module 18`.
- [ ] Installed and verified local model inference via Ollama.
- [ ] Created and validated a `SKILL.md` configuration file.

---

## 2. Formative Diagnostic Drills

<details>
<summary>Drill 1: A business wants to run a 14B parameter model locally on laptops with 16 GB unified RAM. Can it run in FP16? What quantization is required?</summary>

**Architectural Rationale:**
In FP16 (16-bit), a 14B model requires ~35 GB of RAM, which will crash on a 16 GB machine. Quantizing to 4-bit (INT4 / GGUF) reduces memory to ~8.75 GB, fitting comfortably within the 16 GB threshold while leaving memory for the OS and application context.
</details>

<details>
<summary>Drill 2: Why does sovereign local AI fulfill HIPAA and defense compliance mandates that public cloud APIs cannot?</summary>

**Architectural Rationale:**
Under strict privacy regulations (HIPAA, FERPA, ITAR), transmitting protected health records or defense data across third-party cloud servers introduces legal liability and breach risk. A sovereign local agent runs on an air-gapped or firewall-isolated workstation; all prompts, embeddings, and outputs remain strictly inside local RAM and disk, guaranteeing zero third-party data exfiltration.
</details>

<details>
<summary>Drill 3: What is the primary purpose of packaging agent tools into a standardized SKILL.md file?</summary>

**Architectural Rationale:**
A SKILL.md file standardizes the agent identity, operational constraints, allowed tool definitions, and governance rules in a single portable, version-controlled markdown file. This decouples the agent logic from proprietary platforms, allowing it to be audited and executed across diverse runtimes.
</details>
