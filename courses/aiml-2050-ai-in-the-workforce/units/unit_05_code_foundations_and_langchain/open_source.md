# Unit 05: Open-Source Guide — LangChain & Pydantic Tool Schemas in Python

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
