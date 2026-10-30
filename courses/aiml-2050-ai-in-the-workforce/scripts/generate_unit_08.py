#!/usr/bin/env python3
"""
Generates Unit 08 for AIML 2050: AI in the Workforce.
"""

import sys
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
UNITS_DIR = BASE_DIR / "units"
INTEL_DIR = Path(r"C:\Users\tswar.KAIASCOMPUTER\OneDrive - Laramie County Community College\Intel Curriculum\AIML 2050 - Agentic Version")

sys.path.insert(0, str(Path(__file__).resolve().parent))
from generate_units import extract_quiz_questions, format_quiz_markdown

def write_unit_08():
    u_dir = UNITS_DIR / "unit_08_sovereign_local_ai_and_capstone"
    u_dir.mkdir(parents=True, exist_ok=True)
    
    # 1. overview.md
    with open(u_dir / "overview.md", "w", encoding="utf-8") as f:
        f.write('''# Unit 08 Overview: Sovereign Local AI, On-Device Runtime & Final Capstone Defense

Welcome to Unit 08—the capstone culmination of **AIML 2050: AI in the Workforce**. In highly regulated industries (healthcare, defense, finance, and legal), sending sensitive organizational data or customer records to public cloud APIs violates privacy mandates (HIPAA, FERPA, GDPR). The future of enterprise AI lies in **Sovereign Local AI**—running optimized, quantized open-source models directly on corporate PCs and edge hardware with zero external data leakage. This week, students master local model serving with **Ollama and OpenVINO**, author structured **`SKILL.md`** skill packages, and present their comprehensive **Workforce AI Capstone Solution** in an executive defense.

---

## Weekly Contact Hour Budget (360 Minutes Total)
- **Conceptual Study & Readings (150 min)**: Study local model runtimes, hardware constraints (CPU/GPU/NPU/VRAM), quantization formats, and curated slides from Intel Modules 17, 18, 19, and 20.
- **Asynchronous Preparation & Drills (60 min)**: Complete diagnostic drills on VRAM calculation, GGUF quantization trade-offs, and `SKILL.md` packaging.
- **Applied Capstone Practicum & Defense (120 min)**: Deploy a sovereign on-device agent with local vector memory, zero external network leakage, and present a 7-minute executive video defense.
- **Knowledge Check (30 min)**: Complete the 10-question formative assessment in Canvas.

---

## Measurable Learning Objectives
By the end of this unit, you will be able to:
1. **Calculate** hardware compute and memory requirements (RAM, VRAM, NPU) for running quantized open-source models on enterprise PCs.
2. **Deploy** and benchmark quantized local language models using Ollama and OpenVINO with zero external internet connectivity.
3. **Author** standardized, portable `SKILL.md` specification files defining agent capabilities and system operational boundaries.
4. **Deliver** an executive capstone presentation defending an end-to-end workforce AI solution, ROI analysis, and governance framework.

---

## Weekly Learning Roadmap & Deliverables
1. **Step 1: Required Readings & Slide Deck Guidance**  
   Review curated slides from `[Slides] Module 17`, `[Slides] Module 18`, `[Slides] Module 19`, and `[Slides] Module 20`.
2. **Step 2: Standalone Open-Source Setup Guide**  
   Review the Unit 08 Open-Source Guide for local model serving with Ollama, OpenVINO, and local FAISS vector indexing.
3. **Step 3: Asynchronous Preparation & Diagnostic Drills**  
   Solve diagnostic drills calculating memory sizing formulas, offline token benchmarks, and data sovereignty audits.
4. **Step 4: Comprehensive Capstone Project & Executive Defense**  
   Execute Project 8 (Capstone): Sovereign On-Device Workplace Agent & Executive Defense, submitting your codebase, slides, and defense recording.
5. **Step 5: Unit 08 Knowledge Check**  
   Complete the native Canvas QTI quiz (3 attempts, highest score retained).
''')

    # 2. reading.md
    with open(u_dir / "reading.md", "w", encoding="utf-8") as f:
        f.write('''# Unit 08: Required Readings, Concepts & Slide Guidance
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
''')

    # 3. open_source.md
    with open(u_dir / "open_source.md", "w", encoding="utf-8") as f:
        f.write('''# Unit 08: Open-Source Guide — Local Model Serving with Ollama & OpenVINO on Intel PCs

> **Course**: AIML 2050 — AI in the Workforce  
> **Toolchain**: Ollama, OpenVINO, Python 3.10+, SQLite / FAISS  
> **Cost**: $0.00 (Zero-cost, 100% offline local inference)

---

## 1. Overview
This guide provides the complete setup for running private, sovereign language models locally using **Ollama** and Python with zero cloud API keys and zero internet data transmission.

---

## 2. Installing and Running Ollama
1. Download and install Ollama from https://ollama.com.
2. Pull a lightweight, high-performance quantized model:
```powershell
ollama run llama3.2:1b
```
3. Verify that the local REST server is active on `http://localhost:11434`.

---

## 3. Python Local Sovereign Agent Script

Save as `local_agent.py`:
```python
import requests
import json
import sqlite3

OLLAMA_URL = "http://localhost:11434/api/generate"
MODEL_NAME = "llama3.2:1b"

def query_local_llm(prompt: str, system_prompt: str = "") -> str:
    # Queries local Ollama instance with zero external cloud transmission
    payload = {
        "model": MODEL_NAME,
        "prompt": prompt,
        "system": system_prompt,
        "stream": False,
        "options": {
            "temperature": 0.2
        }
    }
    try:
        response = requests.post(OLLAMA_URL, json=payload, timeout=60)
        response.raise_for_status()
        return response.json().get("response", "").strip()
    except Exception as e:
        return f"Local Inference Error: {e}"

if __name__ == "__main__":
    print(f"[*] Testing sovereign connection to local {MODEL_NAME}...")
    ans = query_local_llm("Explain data sovereignty in two concise sentences.")
    print("\n[+] Local Model Output:\n", ans)
```

---

## 4. The Standardized SKILL.md Pattern

Save as `SKILL.md`:
```yaml
---
name: sovereign-workforce-assistant
description: Private on-device assistant for processing sensitive workplace documentation with zero cloud leakage.
version: 1.0.0
author: LCCC AI Program
tools:
  - name: local_sqlite_query
    description: Queries local internal database records.
  - name: local_policy_lookup
    description: Performs cosine search over local offline text documents.
governance:
  cloud_transmission_allowed: false
  pii_sanitization_required: true
  max_iterations: 5
---

# Operational Instructions
You are a sovereign enterprise AI assistant operating entirely on local hardware. You have no connection to external cloud APIs. All company data must remain strictly isolated on this device.
```
''')

    # 4. drills.md
    with open(u_dir / "drills.md", "w", encoding="utf-8") as f:
        f.write('''# Unit 08: Asynchronous Preparation & Diagnostic Drills
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
''')

    # 5. lab_guide.md
    with open(u_dir / "lab_guide.md", "w", encoding="utf-8") as f:
        f.write('''# Unit 08 Applied Capstone Guide: Sovereign Workplace Agent & Executive Defense

> **Course**: AIML 2050 — AI in the Workforce  
> **Deliverable**: Complete Codebase (`.zip`) + Capstone Slide Deck (`.pptx`/`.pdf`) + 7-Minute Defense Recording  
> **Total Points**: 100 Points (Comprehensive Course Capstone — 30% of Grade)  
> **Submission**: Native Canvas Assignment Upload

---

## 1. Executive Scenario & Capstone Objective
You are presenting your final Capstone Project to the Executive Steering Committee and Chief Technology Officer. You have engineered an end-to-end, sovereign workplace AI solution that solves a critical operational friction in an enterprise domain (Healthcare Operations, Legal / Compliance, Financial Audit, or HR Talent Management). The solution runs locally with private data storage, enforces NIST governance standards, includes Human-in-the-Loop escalation, and delivers quantifiable ROI.

---

## 2. Comprehensive Deliverables Checklist

### Deliverable A: Working Sovereign Python Codebase
1. **Local Model Execution**: Runs on a local quantized model (via Ollama or OpenVINO) with zero external cloud transmission.
2. **Local Vector Memory**: Local RAG pipeline (SQLite or FAISS) querying private corporate documents.
3. **Validated Tools**: At least two deterministic tools backed by Pydantic schemas.
4. **`SKILL.md`**: Specification file documenting capabilities, tool interfaces, and governance tripwires.
5. **Zero-Leakage Audit**: Network trace or code proof confirming no data is transmitted externally.

### Deliverable B: Capstone Slide Deck (10–12 Slides)
- **Slide 1**: Executive Title & Domain Scenario
- **Slide 2**: Problem Statement & Current Value Stream Map (As-Is bottlenecks)
- **Slide 3**: Proposed Solution & Future Value Stream Map (To-Be agent integration)
- **Slide 4**: System Architecture (Presentation, Logic, State, Local Model)
- **Slide 5**: Local Hardware Sizing & Compute Plan (RAM/VRAM calculation)
- **Slide 6**: NIST AI RMF Risk Control Matrix & Human-in-the-Loop Escalation Gates
- **Slide 7**: Automated Evaluation & Security Benchmark Scorecard
- **Slide 8**: Financial ROI & Workforce Reallocation Projections
- **Slide 9**: Implementation Roadmap & Change Management Strategy
- **Slide 10**: Summary & Steering Committee Call-to-Action

### Deliverable C: 7-Minute Executive Video Defense
Record a professional 7-minute presentation defending your capstone:
- **0:00–2:00**: Problem statement, business domain, and ROI case.
- **2:00–4:30**: Live technical walkthrough of the local agent running offline, demonstrating local RAG and tool execution.
- **4:30–6:00**: Governance defense: NIST risk matrix and human-in-the-loop escalation.
- **6:00–7:00**: Executive conclusion and Q&A anticipation.

---

## 3. Capstone Grading Rubric (100 Points Total)

| Evaluation Criteria | Exemplary (Full Points) | Developing (Partial Points) | Unacceptable (Zero Points) | Points |
|---|---|---|---|---|
| **1. Sovereign Architecture & Local Runtime** | Flawlessly executes locally via Ollama/OpenVINO with local vector store; zero external data leakage verified; valid `SKILL.md`. | Runs partially locally, but relies on external cloud APIs for certain tasks. | Broken codebase; fails to run or requires external cloud subscriptions. | **25** |
| **2. Technical Depth & Tool Integration** | Robust Pydantic tools; state persistence; handles edge cases gracefully; clean modular code structure. | Tools functional, but lack schema validation or error handling. | Minimal or non-functional tool calling. | **25** |
| **3. Governance, NIST Alignment & HITL** | Comprehensive NIST Risk Control Matrix; clear 3-tier Human-in-the-Loop escalation gates; auditable fail-safes. | Basic governance mentioned, but lacks technical controls or tiered escalation. | No risk assessment or governance controls. | **25** |
| **4. Executive Defense & Slide Deck** | Highly articulate 7-minute defense; professional 10+ slide deck; compelling ROI calculation and business presence. | Presentation submitted but exceeds/under-runs time limit; slides lack polish or financial analysis. | Missing video or slide deck; unplayable recording. | **25** |
| **Total** | | | | **100** |
''')

    # 6. quiz.md
    mod17_xlsx = INTEL_DIR / "Module 17 - Agentic AI" / "(Quiz) Module 17 - Agentic AI.xlsx"
    qs = extract_quiz_questions(mod17_xlsx)
    if not qs or len(qs) < 5:
        qs = [
            {"question": "How much RAM/VRAM does a 7-billion parameter model quantized to 4-bit (INT4 / GGUF) require for local inference?",
             "options": {"A": "Approximately 4.5 GB to 5 GB",
                         "B": "At least 64 GB",
                         "C": "Over 128 GB of specialized VRAM",
                         "D": "Less than 100 Megabytes"},
             "answer": "A", "rationale": "7B parameters at 4 bits per weight requires roughly 4.5 to 5 GB of memory."},
            {"question": "What is the primary compliance advantage of deploying Sovereign Local AI agents in healthcare organizations?",
             "options": {"A": "It automatically generates medical diagnoses with 100% accuracy",
                         "B": "Patient health records (PHI) remain strictly on-premise, guaranteeing HIPAA compliance without third-party data leakage",
                         "C": "It eliminates the need for doctors and nurses",
                         "D": "It allows cloud providers to train models on patient data"},
             "answer": "B", "rationale": "Sovereign execution ensures PHI never leaves local organizational custody."},
            {"question": "In modular agent engineering, what is the role of a 'SKILL.md' specification file?",
             "options": {"A": "It compiles Python source code into machine code",
                         "B": "It provides a portable, standardized definition of an agent's identity, operational constraints, and allowed tool schemas",
                         "C": "It overrides hardware temperature controls",
                         "D": "It installs operating system drivers"},
             "answer": "B", "rationale": "SKILL.md defines tools, prompts, and constraints in a standardized portable format."}
        ]
    with open(u_dir / "quiz.md", "w", encoding="utf-8") as f:
        f.write(format_quiz_markdown(8, "Sovereign Local AI, On-Device Runtime & Final Capstone Defense", qs))

    # 7. teaching_notes.md
    with open(u_dir / "teaching_notes.md", "w", encoding="utf-8") as f:
        f.write('''# [Instructor Guide] Unit 08 Teaching Notes & Delivery Guide
## Sovereign Local AI, On-Device Runtime & Final Capstone Defense

> **Target Audience**: Instructors & Facilitators  
> **Workflow State**: `unpublished` (Hidden from students in Canvas)

---

## 1. Synchronous Delivery Agenda (60-Minute In-Class Practicum)
- **00–15 min (The Enterprise Frontier: Sovereign Edge AI)**: Discuss the rapid shift from cloud API subscriptions to local PCs powered by NPUs and quantized models.
- **15–30 min (Capstone Jury Rubric Calibration)**: Walk students through the 100-point rubric. Emphasize that technical depth, governance, and business ROI carry equal weight.
- **30–50 min (Live Speed-Pitch Practice)**: Have students give 60-second elevator pitches of their capstone problem and solution to peer reviewers.
- **50–60 min (Course Wrap-up & Career Pathways)**: Debrief the 8-week journey: from VSM opportunity audits to no-code orchestration, code agents, LangGraph state machines, observability, and sovereign deployment.
''')

    print("  [+] Unit 08 generated successfully.")

if __name__ == "__main__":
    write_unit_08()
