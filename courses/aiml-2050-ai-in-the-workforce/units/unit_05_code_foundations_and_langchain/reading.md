# Unit 05: Required Readings, Concepts & Slide Guidance
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
