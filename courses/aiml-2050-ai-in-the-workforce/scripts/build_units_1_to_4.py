#!/usr/bin/env python3
"""
Builds Units 01 through 04 for AIML 2050.
"""

import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
UNITS_DIR = BASE_DIR / "units"
INTEL_DIR = Path(r"C:\Users\tswar.KAIASCOMPUTER\OneDrive - Laramie County Community College\Intel Curriculum\AIML 2050 - Agentic Version")

sys_path = Path(__file__).resolve().parent
import sys
sys.path.insert(0, str(sys_path))
from generate_units import extract_quiz_questions, format_quiz_markdown

def write_unit_01():
    u_dir = UNITS_DIR / "unit_01_foundations_of_agentic_ai"
    u_dir.mkdir(parents=True, exist_ok=True)
    
    # 1. overview.md
    with open(u_dir / "overview.md", "w", encoding="utf-8") as f:
        f.write("""# Unit 01 Overview: Foundations of Agentic AI & The Enterprise Landscape

Welcome to Unit 01 of **AIML 2050: AI in the Workforce**. This week establishes the strategic and technical foundation of modern agentic systems in enterprise business environments. Students explore how autonomous reasoning loops (Perception → Reasoning → Action → Observation) fundamentally differ from legacy Robotic Process Automation (RPA) and standard conversational chatbots, analyze labor and workforce reallocation trends, and conduct Value Stream Mapping to identify high-ROI automation opportunities.

---

## Weekly Contact Hour Budget (360 Minutes Total)
- **Conceptual Study & Readings (150 min)**: Study the core readings on agentic loops, enterprise value streams, and curated slides from Intel Modules 01, 02, and 05.
- **Asynchronous Preparation & Drills (60 min)**: Complete the self-check diagnostic exercises with interactive accordion answer keys.
- **Applied Workplace Lab & Project (120 min)**: Conduct an Enterprise Workflow Value Stream Map & Agentic Opportunity Audit adhering to the native grading rubric.
- **Knowledge Check (30 min)**: Complete the 10-question formative assessment in Canvas.

---

## Measurable Learning Objectives
By the end of this unit, you will be able to:
1. **Differentiate** agentic perception-action loops from traditional deterministic RPA and static generative chat interfaces.
2. **Classify** horizontal vs vertical agent architectures across enterprise business functions (Finance, HR, Operations, Support).
3. **Analyze** workforce transformation trends, differentiating task reallocation from whole-job displacement.
4. **Construct** a Current-State and Future-State Value Stream Map (VSM) quantifying lead time, delay points, and projected ROI for an enterprise process.

---

## Weekly Learning Roadmap & Deliverables
1. **Step 1: Required Readings & Slide Deck Guidance**  
   Review curated slides from `[Slides] Module 01`, `[Slides] Module 02`, and `[Slides] Module 05` as mapped in the reading guide.
2. **Step 2: Standalone Open-Source Setup Guide**  
   Verify your local Python 3.10+ runtime, pip, and Git environment using the Unit 01 Open-Source Setup Guide.
3. **Step 3: Asynchronous Preparation & Diagnostic Drills**  
   Solve the scenario drills testing agent taxonomy, task suitability, and VSM calculation before starting the lab.
4. **Step 4: Applied Engineering Lab & Workplace Project**  
   Execute the Value Stream Mapping & Agentic Opportunity Audit project and submit your deliverable to SpeedGrader.
5. **Step 5: Unit 01 Knowledge Check**  
   Complete the native Canvas QTI quiz (3 attempts, highest score retained).
""")

    # 2. reading.md
    with open(u_dir / "reading.md", "w", encoding="utf-8") as f:
        f.write("""# Unit 01: Required Readings, Concepts & Slide Guidance

> **Course**: AIML 2050 — AI in the Workforce  
> **Contact Allocation**: 150 Minutes  
> **Source Modules**: Intel Modules 01, 02 & 05

---

## 1. Curated Slide Reading Directives

To master this week's competencies without cognitive overload, refer to the following specific sections of the Intel presentation slide decks located in your course materials repository. *Do not read every slide; follow the curated directives below:*

### A. From `[Slides] Module 01 - Agentic AI.pptx` (126 slides total)
- **Study Slides 4–32 (Fundamentals of Agentic AI)**: Understand the core definition of an AI agent, the shift from rule-based systems to probabilistic reasoning, and autonomy vs. human oversight.
- **Study Slides 67–79 (The Agentic AI Workflow)**: Pay specific attention to the four-phase cyclic loop: *Perception → Reasoning → Action → Observation*.
- **Study Slides 80–96 (Agentic AI in the Real World)**: Review enterprise examples across customer service, logistics routing, and software engineering.
- *Skip Slides 97–126* (breakout workshop slides and bibliography).

### B. From `[Slides] Module 02- Agentic AI.pptx` (120 slides total)
- **Study Slides 8–40 (Agentic AI in the Workplace)**: Review the economic impact on knowledge work, the concept of AI as a cognitive multiplier, and task decomposition.
- **Study Slides 41–74 (Future Workforce Readiness)**: Analyze the difference between eliminating entire jobs vs. reallocating task bundles to agents, and the emerging role of human orchestrators.
- *Skip Slides 75–120* (sector-specific deep dives across specialized niche industries).

### C. From `[Slides] Module 05 - Agentic AI.pptx` (130 slides total)
- **Study Slides 44–61 (Horizontal vs. Vertical Agentic Systems)**: Compare generalized, cross-functional agents (e.g. email/scheduling assistants) with highly specialized vertical agents (e.g. legal compliance or clinical diagnostic agents).
- **Study Slides 62–105 (Value Stream Mapping & Readiness Assessment)**: Master the step-by-step methodology for mapping process lead time, identifying process bottlenecks, and assessing organizational data readiness.
- *Skip Slides 8–43 & 106–130* (recap slides and general reading).

---

## 2. Core Conceptual Deep Dive: The Agentic Paradigm

### The Perception-Action Loop
Unlike standard Generative AI (where an LLM simply predicts tokens in a single conversational turn), an **AI Agent** possesses an autonomous execution loop:
1. **Perception**: Receiving external state (user prompt, API webhook, file upload, database trigger).
2. **Reasoning & Planning**: Decomposing high-level goals into sequential actions using reasoning frameworks (ReAct, Chain-of-Thought).
3. **Action Execution**: Invoking external tools (querying a database, calling a REST API, executing Python code).
4. **Observation & Reflection**: Inspecting tool outputs, evaluating whether the goal is achieved, and correcting course if errors occur.

```
       ┌───────────────────────────────┐
       │     Perception / Trigger      │
       └──────────────┬────────────────┘
                      ▼
       ┌───────────────────────────────┐
       │     Reasoning & Planning      │◄───────┐
       └──────────────┬────────────────┘        │
                      ▼                         │
       ┌───────────────────────────────┐        │
       │    Tool Execution / Action    │        │
       └──────────────┬────────────────┘        │
                      ▼                         │
       ┌───────────────────────────────┐        │
       │    Observation & Feedback     ├────────┘
       └───────────────────────────────┘
```

### Value Stream Mapping (VSM) in the Enterprise
Before deploying agents, organizations must map their existing processes:
- **Lead Time (Total Elapsed Time)**: The total duration from request initiation to final customer delivery.
- **Process Time (Touch Time)**: The actual duration where human workers are actively performing cognitive work.
- **Wait Time (Bottleneck / Delay)**: Time spent sitting in queues, waiting for approvals, or delayed hand-offs.
- **Agentic Opportunity Score**: High when wait time is large due to repetitive information lookup or routine routing.
""")

    # 3. open_source.md
    with open(u_dir / "open_source.md", "w", encoding="utf-8") as f:
        f.write("""# Unit 01: Open-Source Guide — Setting Up Python & Environment Verification

> **Course**: AIML 2050 — AI in the Workforce  
> **Toolchain**: Python 3.10+, pip, virtual environments (`venv`), Git  
> **Cost**: $0.00 (Zero-cost local infrastructure)

---

## 1. Prerequisites & System Requirements
- **OS**: Windows 10/11, macOS, or Linux.
- **RAM**: Minimum 8 GB (16 GB recommended).
- **Disk Space**: At least 5 GB free.

---

## 2. Step-by-Step Installation Commands

### Windows (PowerShell)
```powershell
# 1. Verify Python installation (Must be 3.10 or higher)
python --version

# 2. Upgrade pip to the latest release
python -m pip install --upgrade pip

# 3. Create an isolated course virtual environment
python -m venv aiml_env

# 4. Activate the virtual environment
.\\aiml_env\\Scripts\\Activate.ps1

# 5. Install foundational data & notebook packages
pip install jupyterlab requests pydantic python-dotenv
```

### macOS / Linux (Bash)
```bash
python3 --version
python3 -m venv aiml_env
source aiml_env/bin/activate
pip install --upgrade pip
pip install jupyterlab requests pydantic python-dotenv
```

---

## 3. 60-Second Smoke Test Verification

Create a file named `test_env.py` and run it:
```python
import sys
import pydantic
import requests

print("=" * 50)
print(f"Python Version:   {sys.version.split()[0]}")
print(f"Pydantic Version: {pydantic.__version__}")
print(f"Requests Version: {requests.__version__}")
print("STATUS: Environment is ready for AIML 2050!")
print("=" * 50)
```

Run:
```powershell
python test_env.py
```
**Expected Output**: Clean output printing package versions and `STATUS: Environment is ready for AIML 2050!`.

---

## 4. Troubleshooting FAQ
1. **Execution Policy Error in PowerShell**: Run `Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser`.
2. **`python` not recognized**: Ensure you checked *"Add Python to PATH"* during Windows installer setup.
3. **Port collision on Jupyter**: Run `jupyter lab --port 8890`.
""")

    # 4. drills.md
    with open(u_dir / "drills.md", "w", encoding="utf-8") as f:
        f.write("""# Unit 01: Asynchronous Preparation & Diagnostic Drills
## Foundations of Agentic AI & Enterprise Opportunity Audits

> **Time Commitment**: ~60 Minutes (Asynchronous Self-Study)  
> **Target Mastery**: Agentic loops, horizontal vs vertical taxonomy, Value Stream Mapping metrics.

---

## 1. Readiness Checklist
- [ ] Studied the four-phase cyclic reasoning loop (Perceive, Reason, Act, Observe).
- [ ] Reviewed slides on Horizontal vs. Vertical Agentic Systems in `[Slides] Module 05`.
- [ ] Verified local Python 3.10+ virtual environment using the Open-Source Setup Guide.

---

## 2. Formative Diagnostic Drills

<details>
<summary>Drill 1: What distinguishes an AI Agent from a traditional RPA (Robotic Process Automation) script?</summary>

**Architectural Rationale:**
- **Traditional RPA:** Operates on rigid, deterministic rules (e.g. click coordinate X, copy text Y, paste into column Z). If the UI button moves 5 pixels or an input format changes, the RPA script crashes.
- **AI Agent:** Operates on probabilistic reasoning, natural language goal decomposition, and autonomous error recovery. It inspects dynamic tool outputs, handles unstructured input variations, and adjusts its plan to reach the objective.
</details>

<details>
<summary>Drill 2: When is a Vertical Agent preferred over a Horizontal Agent in the enterprise?</summary>

**Architectural Rationale:**
- **Horizontal Agents** excel at broad, cross-functional productivity tasks (e.g. meeting transcription, email drafting, general calendar scheduling) across all departments.
- **Vertical Agents** are strictly required when tasks demand deep regulatory compliance, domain-specific ontologies, or specialized data schemas (e.g., medical claims coding, legal patent discovery, financial risk modeling).
</details>

<details>
<summary>Drill 3: In Value Stream Mapping, why is high 'Wait Time' the strongest indicator for AI agent automation?</summary>

**Architectural Rationale:**
In most business processes (e.g. employee onboarding or loan triage), the actual *Touch Time* (human cognitive work) is only 15 minutes, while the *Lead Time* is 4 days due to batching, manual routing, and waiting in inbox queues. An AI agent can evaluate documents, apply business rules, and trigger downstream APIs in seconds, eliminating 95%+ of the queue wait time.
</details>

<details>
<summary>Drill 4: What is the primary risk of automating a broken or unstandardized business workflow with an AI agent?</summary>

**Architectural Rationale:**
Automating an unstandardized workflow simply accelerates error propagation at scale ("automating chaos"). If clear business rules, data schemas, and human escalation boundaries are not documented first in an As-Is value stream map, the agent will produce unpredictable outputs and loop locks.
</details>
""")

    # 5. lab_guide.md
    with open(u_dir / "lab_guide.md", "w", encoding="utf-8") as f:
        f.write("""# Unit 01 Applied Lab Guide: Enterprise Workflow Value Stream Map & Agent Opportunity Audit

> **Course**: AIML 2050 — AI in the Workforce  
> **Deliverable**: `unit01_opportunity_audit_[yourlastname].pdf` or `.docx`  
> **Total Points**: 50 Points  
> **Submission**: Native Canvas Assignment Upload

---

## 1. Scenario & Workplace Objective
You are an Enterprise AI Solutions Analyst hired by a mid-sized organization. Management wants to deploy agentic AI to increase productivity, but department heads are overwhelmed by vendor hype. Your job is to select one real-world operational workflow (e.g., employee onboarding, customer support triage, expense reimbursement, or procurement ordering) and produce an **Enterprise Agentic Opportunity Audit**.

---

## 2. Step-by-Step Task Specifications

### Task 1: Select an End-to-End Business Workflow
Select a complete workflow that has:
- A clear trigger (e.g., new hire form submitted, invoice received).
- At least 4 distinct steps involving multiple actors or systems.
- Measurable business outcomes (lead time, error rate, operational cost).

### Task 2: Create the Current-State Value Stream Map (As-Is)
Document each step in a workflow diagram or structured table:
- Who performs the task?
- What systems or tools are touched?
- What is the Touch Time (active work) vs. Wait Time (idle/queue delay)?
- Where do human judgment calls occur vs. routine data lookup?

### Task 3: Design the Future-State Agentic Value Stream Map (To-Be)
Redesign the workflow integrating an AI agent:
- Identify whether the agent is **Horizontal** or **Vertical**.
- Specify the agent's Perception trigger, Reasoning responsibilities, and Tool Actions.
- Define explicit **Human-in-the-Loop** checkpoints for high-risk decisions.
- Calculate projected time savings (e.g. reducing lead time from 72 hours to 2 hours).

### Task 4: Executive Synthesis & Operational KPIs
Summarize your findings in a 2–3 page executive brief including:
1. Executive Problem Statement
2. As-Is and To-Be Value Stream Maps
3. ROI & Time-Savings Projections
4. Key Performance Indicators (Cycle Time, Accuracy, Escalation Rate)

---

## 3. Grading Rubric (50 Points Total)

| Criteria | Exemplary (Full Points) | Developing (Partial Points) | Unacceptable (Zero Points) | Points |
|---|---|---|---|---|
| **1. Current-State VSM Accuracy** | Thoroughly identifies all actors, touch times, queue delays, and pain points across the end-to-end process. | Identifies major steps, but lacks clear touch time vs. wait time metrics. | Vague or missing workflow steps; no clear pain points identified. | **15** |
| **2. Future-State Agentic Architecture** | Clearly specifies agent role (horizontal vs vertical), tool integration points, and human-in-the-loop escalation boundaries. | Proposes AI assistance, but lacks specific tool integration or human review checkpoints. | Unrealistic "magic AI" proposal with no technical grounding or human oversight. | **15** |
| **3. ROI & Metric Quantification** | Quantifies cycle time reduction, cost impact, and establishes 3+ actionable operational KPIs. | Mentions general productivity gains, but lacks numeric baseline comparisons. | No quantitative analysis or metrics provided. | **10** |
| **4. Executive Quality & Clarity** | Professional business formatting, clear diagrams, concise prose, and complete executive summary. | Minor formatting flaws; diagrams difficult to read or text overly informal. | Unformatted draft; missing diagrams or required sections. | **10** |
| **Total** | | | | **50** |
""")

    # 6. quiz.md
    mod1_xlsx = INTEL_DIR / "Module 01 - Agentic AI" / "[Quiz] Module 01 - Agentic AI.xlsx"
    qs = extract_quiz_questions(mod1_xlsx)
    if not qs:
        # Fallback questions if xlsx is missing
        qs = [
            {"question": "What is the most fundamental characteristic that defines any AI Agent?",
             "options": {"A": "Operates in a fully observable, deterministic, and static environment",
                         "B": "Involves a Large Language Model (LLM)",
                         "C": "Possesses human-level consciousness",
                         "D": "Monitors its environment and executes actions autonomously involving LLMs and tools"},
             "answer": "D", "rationale": "Autonomous action and environment monitoring define agentic systems."},
            {"question": "What is the primary advantage of a Model-based Reflex Agent over a Simple Reflex Agent?",
             "options": {"A": "Evaluates sequences based on utility functions",
                         "B": "Maintains an internal model to track unobserved aspects of the environment",
                         "C": "Considers all future possibilities simultaneously",
                         "D": "Directly maps current inputs to actions with zero memory"},
             "answer": "B", "rationale": "Internal state tracking distinguishes model-based agents from pure reflex."}
        ]
    with open(u_dir / "quiz.md", "w", encoding="utf-8") as f:
        f.write(format_quiz_markdown(1, "Foundations of Agentic AI & Opportunity Audits", qs))

    # 7. teaching_notes.md
    with open(u_dir / "teaching_notes.md", "w", encoding="utf-8") as f:
        f.write("""# [Instructor Guide] Unit 01 Teaching Notes & Delivery Guide
## Foundations of Agentic AI & Enterprise Opportunity Audits

> **Target Audience**: Instructors & Facilitators  
> **Workflow State**: `unpublished` (Hidden from students in Canvas)

---

## 1. Synchronous Delivery Agenda (60-Minute In-Class Practicum)
- **00–15 min (Hook & Real-World Friction)**: Discuss the difference between ChatGPT prompting vs. autonomous agents. Show why automating a broken process fails.
- **15–30 min (Value Stream Mapping Walkthrough)**: Walk through a live whiteboard session of an HR employee onboarding process. Measure touch time (30 min) vs. wait time (5 days).
- **30–50 min (Active Learning Clinic - You Do)**: Put students in pairs to map the As-Is state of a familiar business process (e.g. IT laptop provisioning).
- **50–60 min (Debrief & Project Expectations)**: Review the SpeedGrader rubric and preview Unit 02 (Responsible Governance).

---

## 2. Common Student Misconceptions & Gotchas
- **"Agents replace entire departments"**: Clarify that agents automate *task bundles*, not full professions. Human orchestrators remain accountable.
- **"AI will just figure out the steps"**: Remind students that an agent requires well-defined data schemas and deterministic tool definitions to operate safely.
""")

    print("  [+] Unit 01 generated successfully.")

write_unit_01()
