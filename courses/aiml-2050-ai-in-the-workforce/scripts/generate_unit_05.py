#!/usr/bin/env python3
"""
Generates Unit 05 for AIML 2050: AI in the Workforce.
"""

import sys
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
UNITS_DIR = BASE_DIR / "units"
INTEL_DIR = Path(r"C:\Users\tswar.KAIASCOMPUTER\OneDrive - Laramie County Community College\Intel Curriculum\AIML 2050 - Agentic Version")

sys.path.insert(0, str(Path(__file__).resolve().parent))
from generate_units import extract_quiz_questions, format_quiz_markdown

def write_unit_05():
    u_dir = UNITS_DIR / "unit_05_code_foundations_and_langchain"
    u_dir.mkdir(parents=True, exist_ok=True)
    
    # 1. overview.md
    with open(u_dir / "overview.md", "w", encoding="utf-8") as f:
        f.write('''# Unit 05 Overview: Code Foundations — The Modular AI Agent Stack

Welcome to Unit 05 of **AIML 2050: AI in the Workforce**. While no-code tools provide rapid automation, enterprise production systems require full programmatic control over data structures, token budgets, error recovery, and tool execution contracts. This week marks our transition to code-first agent engineering. Students demystify the agent stack in Python, master the **ReAct (Reason + Act)** cyclic loop without framework abstractions, enforce defensive **Pydantic** input validation, and assemble a modular agent equipped with Retrieval-Augmented Generation (RAG) and external tool calling.

---

## Weekly Contact Hour Budget (360 Minutes Total)
- **Conceptual Study & Readings (150 min)**: Study API communication contracts, the ReAct pattern, tool schema validation, and curated slides from Intel Module 13.
- **Asynchronous Preparation & Drills (60 min)**: Complete diagnostic drills tracing ReAct execution loops, Pydantic type safety, and vector similarity retrieval.
- **Applied Workplace Lab & Project (120 min)**: Construct a custom modular Python agent with RAG and validated tool calling, tested across 9 prompt scenarios.
- **Knowledge Check (30 min)**: Complete the 10-question formative assessment in Canvas.

---

## Measurable Learning Objectives
By the end of this unit, you will be able to:
1. **Explain** the programmatic HTTP/JSON communication contracts between LLMs and external software APIs.
2. **Implement** the fundamental ReAct (Reason &rarr; Act &rarr; Observe) execution loop in pure Python.
3. **Construct** defensive Pydantic tool schemas that validate inputs and return structured error messages upon malformed calls.
4. **Assemble** a production-ready modular Python agent combining a vector knowledge retriever (RAG) and deterministic calculation tools.

---

## Weekly Learning Roadmap & Deliverables
1. **Step 1: Required Readings & Slide Deck Guidance**  
   Review curated slides from `[Slides] Module 13` as specified in the reading guide.
2. **Step 2: Standalone Open-Source Setup Guide**  
   Review the Unit 05 Open-Source Guide for LangChain, Pydantic schemas, and lightweight RAG indexing.
3. **Step 3: Asynchronous Preparation & Diagnostic Drills**  
   Solve diagnostic drills exploring tool signature parsing, cosine similarity scoring, and ReAct exception handling.
4. **Step 4: Applied Engineering Lab & Workplace Project**  
   Execute Project 5: Custom Modular Python Agent with RAG & Tool Calling, submitting your codebase and test matrix to Canvas SpeedGrader.
5. **Step 5: Unit 05 Knowledge Check**  
   Complete the native Canvas QTI quiz (3 attempts, highest score retained).
''')

    # 2. reading.md
    with open(u_dir / "reading.md", "w", encoding="utf-8") as f:
        f.write('''# Unit 05: Required Readings, Concepts & Slide Guidance
## Code Foundations: The Modular AI Agent Stack

> **Course**: AIML 2050 — AI in the Workforce  
> **Contact Allocation**: 150 Minutes  
> **Source Module**: Intel Module 13 (Building Blocks with LangChain)

---

## 1. Curated Slide Reading Directives

Refer to the following specific sections of the Intel presentation deck in your course materials repository:

### From `[Slides] Module 13 - Agentic AI.pptx` (106 slides total)
- **Study Slides 10–21 (Foundations of Running an AI Agent)**: Understand how LLMs communicate over REST APIs, HTTP POST payloads, system messages, and JSON response parsing.
- **Study Slides 22–74 (Building the Agent & The ReAct Pattern)**: Study the Reason &rarr; Act &rarr; Observe loop. Contrast single-turn zero-shot prompting with multi-turn iterative problem solving.
- **Study Slides 75–98 (Agent Tooling & Function Calling)**: Master how function signatures (name, description, parameter schemas) are serialized into LLM prompts, and how tool execution results are fed back into conversational memory.
- *Skip Slides 99–106* (bibliographies and index citations).

---

## 2. Core Conceptual Deep Dive: Anatomy of a Code Agent

### The ReAct (Reason + Act) Loop
Pioneered by Yao et al. (2022), the ReAct pattern prompts the language model to interleave reasoning thoughts with specific tool invocations:
1. **Thought**: The model evaluates the user's objective and existing context ("The user wants the total price including 8% tax for 5 units at $40 each. I need to calculate the base price first.").
2. **Action**: The model outputs a structured tool call (`calculate(operation="multiply", a=5, b=40)`).
3. **Observation**: The runtime halts LLM generation, executes the local Python function, and returns the output (`200`).
4. **Thought**: The model digests the observation ("The base price is $200. Now I must calculate 8% tax.").
5. **Action**: `calculate(operation="multiply", a=200, b=1.08)` &rarr; **Observation**: `216`.
6. **Final Answer**: "The total price including tax is $216.00."

### Why Pydantic Schemas are Non-Negotiable
Language models generate text. When asking an LLM to invoke a tool, an unconstrained prompt might return `"5 units"` (a string) instead of `5` (an integer), or `"40 dollars"` instead of `40.0`. 
By backing every tool with a **Pydantic BaseModel**, Python automatically validates incoming arguments:
- If valid, the function executes cleanly.
- If invalid, Pydantic catches the error and generates an immediate, structured feedback message back to the LLM (*"ValidationError: value 'five' is not a valid integer"*), allowing the agent to self-correct on the next iteration.

### The Modular Agent Architecture
Enterprise agent codebases avoid monolithic scripts by organizing code into clean modules:
- `agent.py`: Houses the central reasoning loop and execution controller.
- `tools.py`: Houses deterministic Python functions wrapped with schemas and error handlers.
- `retrieval.py`: Manages document embedding, vector indexing, and RAG search.
- `helpers/config.py`: Centralizes API keys, temperature settings, and model identifiers.
''')

    # 3. open_source.md
    with open(u_dir / "open_source.md", "w", encoding="utf-8") as f:
        f.write('''# Unit 05: Open-Source Guide — LangChain & Pydantic Tool Schemas in Python

> **Course**: AIML 2050 — AI in the Workforce  
> **Toolchain**: Python 3.10+, Pydantic v2, Requests, FAISS / SQLite  
> **Cost**: $0.00 (Zero-cost local runtime)

---

## 1. Overview
This guide provides working starter code demonstrating how to define type-safe tool schemas using **Pydantic** and execute the ReAct reasoning loop in Python.

---

## 2. Environment Setup
In your virtual environment (`aiml_env`), install the necessary libraries:
```powershell
pip install pydantic python-dotenv requests numpy
```

---

## 3. Defining Type-Safe Tools with Pydantic

Save as `tools.py`:
```python
from pydantic import BaseModel, Field
from typing import Literal

class CalculatorInput(BaseModel):
    operation: Literal["add", "subtract", "multiply", "divide"] = Field(
        description="The mathematical operation to execute"
    )
    a: float = Field(description="The first operand")
    b: float = Field(description="The second operand")

def calculate(args: dict) -> str:
    # Executes basic arithmetic with rigorous input validation
    try:
        validated = CalculatorInput(**args)
        if validated.operation == "add":
            return str(validated.a + validated.b)
        elif validated.operation == "subtract":
            return str(validated.a - validated.b)
        elif validated.operation == "multiply":
            return str(validated.a * validated.b)
        elif validated.operation == "divide":
            if validated.b == 0:
                return "Error: Division by zero is undefined."
            return str(validated.a / validated.b)
    except Exception as e:
        return f"Input Validation Error: {e}"

class PolicySearchInput(BaseModel):
    query: str = Field(description="The workplace policy keyword or question to search")

# Mock corporate knowledge base
MOCK_KNOWLEDGE = {
    "vacation": "Employees receive 15 days of paid annual leave accruing monthly.",
    "remote": "Remote work is permitted up to 2 days per week with supervisor approval.",
    "expense": "Meal expenses are capped at $75/day and require itemized receipts."
}

def search_policy(args: dict) -> str:
    # Searches corporate policy documentation
    try:
        validated = PolicySearchInput(**args)
        q = validated.query.lower()
        matches = [v for k, v in MOCK_KNOWLEDGE.items() if k in q]
        if matches:
            return " ".join(matches)
        return "No specific corporate policy found matching query. Escalate to HR."
    except Exception as e:
        return f"Policy Search Error: {e}"
```

---

## 4. ReAct Loop Controller

Save as `agent.py`:
```python
import json
from tools import calculate, search_policy

TOOLS = {
    "calculate": calculate,
    "search_policy": search_policy
}

def run_agent_turn(tool_name: str, tool_args: dict) -> str:
    # Executes tool action and returns observation
    if tool_name not in TOOLS:
        return f"Error: Tool '{tool_name}' does not exist. Available tools: {list(TOOLS.keys())}"
    print(f"[*] Executing Action: {tool_name} with args {tool_args}")
    observation = TOOLS[tool_name](tool_args)
    print(f"[<] Observation: {observation}")
    return observation

if __name__ == "__main__":
    print("Testing Tool Execution Pipeline...")
    obs1 = run_agent_turn("calculate", {"operation": "multiply", "a": 12, "b": 15})
    obs2 = run_agent_turn("search_policy", {"query": "remote work policy"})
    print("Tool pipeline operational!")
```
''')

    # 4. drills.md
    with open(u_dir / "drills.md", "w", encoding="utf-8") as f:
        f.write('''# Unit 05: Asynchronous Preparation & Diagnostic Drills
## Code Foundations: The Modular AI Agent Stack

> **Time Commitment**: ~60 Minutes (Asynchronous Self-Study)  
> **Target Mastery**: ReAct execution loops, Pydantic type validation, tool error recovery.

---

## 1. Readiness Checklist
- [ ] Studied slides on the ReAct pattern in `[Slides] Module 13`.
- [ ] Verified Pydantic v2 installation in your Python environment.
- [ ] Tested local execution of `tools.py` and `agent.py`.

---

## 2. Formative Diagnostic Drills

<details>
<summary>Drill 1: Why does string-based tool calling fail in enterprise applications without Pydantic validation?</summary>

**Architectural Rationale:**
Large language models generate probabilistic natural language. If you instruct an LLM to output a raw string like `"calculate: 5 * 40"`, slight phrasing differences will break regex or string-split parsing. Pydantic enforces an exact JSON schema contract: if the LLM produces a string for a float field, Pydantic coerces it or returns a structured error message indicating the exact field that failed.
</details>

<details>
<summary>Drill 2: What should an agent do when a tool execution returns an error message like "Error: Database connection timeout"?</summary>

**Architectural Rationale:**
The agent must feed the error string back into the prompt context as an **Observation**. During the next **Reasoning** phase, the model inspects the error and can choose an alternative action (e.g., retrying with exponential backoff, falling back to a cached local file, or reporting the outage to the user) rather than silently crashing.
</details>

<details>
<summary>Drill 3: In a RAG pipeline, why is cosine similarity preferred over keyword matching for agent context retrieval?</summary>

**Architectural Rationale:**
Keyword search (e.g., SQL `LIKE` or grep) only matches exact characters. If a user asks *"Can I work from home on Fridays?"*, keyword search will miss a document titled *"Telecommuting and Remote Operations Guidelines"*. Cosine similarity compares semantic vector embeddings in high-dimensional space, identifying documents with identical conceptual meaning regardless of the specific vocabulary used.
</details>
''')

    # 5. lab_guide.md
    with open(u_dir / "lab_guide.md", "w", encoding="utf-8") as f:
        f.write('''# Unit 05 Applied Lab Guide: Custom Modular Python Agent with RAG & Tool Calling

> **Course**: AIML 2050 — AI in the Workforce  
> **Deliverable**: `unit05_agent_[yourlastname].zip` (codebase + test report)  
> **Total Points**: 50 Points  
> **Submission**: Native Canvas Assignment Upload

---

## 1. Scenario & Workplace Objective
You are a Senior AI Developer hired to build a specialized, code-based workplace assistant (e.g. Facilities Operations Assistant, Financial Expense Auditing Agent, or Legal Compliance Navigator). The solution must be fully modular, utilize **Pydantic** for tool schemas, incorporate a **RAG knowledge retriever** over company policies, and execute the **ReAct reasoning loop** with defensive error recovery.

---

## 2. Step-by-Step Task Specifications

### Task 1: Modular Project Directory Structure
Create a clean, production-grade project structure:
```
workplace_agent/
├── agent.py            # Central ReAct reasoning loop & controller
├── tools.py            # Deterministic tools with Pydantic validation
├── retrieval.py        # Vector / keyword RAG store over documents in docs/
├── docs/               # At least 2 corporate policy documents (.txt or .md)
├── helpers/
│   └── config.py       # API keys, temperature, model definitions
└── test_harness.py     # Automated testing suite
```

### Task 2: Implement Validated Tools
In `tools.py`, create at least **two deterministic tools**:
- Each tool must be backed by a Pydantic `BaseModel` defining argument types, defaults, and field descriptions.
- Each tool must include comprehensive exception handling returning descriptive string errors upon failure.

### Task 3: Implement RAG Knowledge Retrieval
In `retrieval.py`, implement document retrieval over your corporate policy files:
- Split documents into logical sections or chunks.
- Provide a `search_docs(query: str)` function that returns relevant excerpts with source citations.

### Task 4: 9-Prompt Test Suite & Evaluation Report
In `test_harness.py`, test your agent across **9 diverse test cases**:
- **3 Ideal / Standard Prompts**: Requiring calculation and document lookup.
- **3 Ambiguous Prompts**: Incomplete information requiring the agent to ask clarifying questions.
- **3 Malformed / Bad Prompts**: Deliberately invalid inputs testing Pydantic validation and error recovery.
- Output a clean test report (`test_report.txt` or `.md`) logging prompt, action taken, and final outcome.

---

## 3. Grading Rubric (50 Points Total)

| Criteria | Exemplary (Full Points) | Developing (Partial Points) | Unacceptable (Zero Points) | Points |
|---|---|---|---|---|
| **1. Code Architecture & Modularity** | Clean 4-part modular structure; zero hardcoded secrets; clear separation of reasoning, tools, and data. | Partially modular; some tools defined inside main script; messy imports. | Monolithic single-file script; poor formatting. | **15** |
| **2. Pydantic Tool Schemas & Validation** | Robust Pydantic schemas for all tools; catches malformed inputs gracefully and returns structured error feedback. | Tools defined, but lack Pydantic validation or crash on bad inputs. | No validation; uncaught runtime exceptions. | **15** |
| **3. RAG Knowledge Store & Retrieval** | Clean document chunking; accurate retrieval returning source citations; grounded responses. | Retrieval present, but returns full documents or lacks citation grounding. | Missing RAG store; hardcoded answers. | **10** |
| **4. 9-Prompt Test Harness & Report** | Comprehensive test suite covering standard, ambiguous, and adversarial prompts with complete logs. | Incomplete test suite (fewer than 9 prompts) or missing error logs. | No test harness or execution evidence provided. | **10** |
| **Total** | | | | **50** |
''')

    # 6. quiz.md
    mod13_xlsx = INTEL_DIR / "Module 13 - Agentic AI" / "(Quiz) Module 13 - Agentic AI.xlsx"
    qs = extract_quiz_questions(mod13_xlsx)
    if not qs or len(qs) < 5:
        qs = [
            {"question": "In the ReAct (Reason + Act) prompting framework, what happens during the 'Observation' phase?",
             "options": {"A": "The model generates a picture of the user's computer screen",
                         "B": "The agent inspects the output returned by the executed external tool",
                         "C": "The model trains its internal weights on new dataset tokens",
                         "D": "The user manually rewrites the system prompt"},
             "answer": "B", "rationale": "Observation captures external tool outputs and returns them to the model context."},
            {"question": "Why is Pydantic widely adopted for agentic tool definitions in Python?",
             "options": {"A": "It compiles Python code into C++ machine binaries",
                         "B": "It enforces strict type validation and automatic schema generation for LLM function calling",
                         "C": "It eliminates the need for vector databases",
                         "D": "It provides free unlimited access to commercial LLM APIs"},
             "answer": "B", "rationale": "Pydantic provides runtime data validation and generates JSON schemas for tool calling."},
            {"question": "What is the primary objective of Retrieval-Augmented Generation (RAG) in an enterprise agent?",
             "options": {"A": "To compress neural network layers to reduce GPU memory",
                         "B": "To ground the agent's responses in authoritative external documents and eliminate hallucinations",
                         "C": "To bypass user authentication mechanisms",
                         "D": "To allow the agent to execute code without human review"},
             "answer": "B", "rationale": "RAG retrieves relevant external text chunks to ground model answers in verified facts."}
        ]
    with open(u_dir / "quiz.md", "w", encoding="utf-8") as f:
        f.write(format_quiz_markdown(5, "Code Foundations: The Modular AI Agent Stack", qs))

    # 7. teaching_notes.md
    with open(u_dir / "teaching_notes.md", "w", encoding="utf-8") as f:
        f.write('''# [Instructor Guide] Unit 05 Teaching Notes & Delivery Guide
## Code Foundations: The Modular AI Agent Stack

> **Target Audience**: Instructors & Facilitators  
> **Workflow State**: `unpublished` (Hidden from students in Canvas)

---

## 1. Synchronous Delivery Agenda (60-Minute In-Class Practicum)
- **00–15 min (The 'Magic' vs Code Reality Check)**: Show students what happens under the hood when LangChain or OpenAI invokes a tool (it's just a JSON payload!).
- **15–35 min (Live Coding Clinic: Building ReAct in 25 Lines)**: Write a basic while-loop in Python that executes a tool call and appends the result to the messages array.
- **35–50 min (Pydantic Debugging Challenge)**: Provide students with a broken tool schema receiving bad inputs and have them write custom validators.
- **50–60 min (Debrief & Preview)**: Connect ReAct loops to Unit 06 (LangGraph and cyclic state machines).
''')

    print("  [+] Unit 05 generated successfully.")

if __name__ == "__main__":
    write_unit_05()
