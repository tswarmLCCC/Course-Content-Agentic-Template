# Unit 05 Applied Lab Guide: Custom Modular Python Agent with RAG & Tool Calling

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
