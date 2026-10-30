# Unit 05: Required Readings, Concepts & Slide Guidance
## Code Foundations: The Modular AI Agent Stack

Welcome to the instructional study hub for **Unit 05: Code Foundations — The Modular AI Agent Stack**. This reading organizes core programming competencies into four structured chapters:

1. **Instructor Lecture & Narrative Deep Dive**: Peeling Back the Magic — Demystifying the Programmatic Agent Stack.
2. **Physical Mental Models & Architecture**: The ReAct Reasoning Loop & Pydantic Schemas as Contract Boundaries.
3. **Curated Slide Reading Directives**: Exact study guidance for Intel Module 13.
4. **Production Modular Architecture & Grounded Vector RAG**: Structuring code for enterprise reliability.

---

## 1. Instructor Lecture & Narrative Deep Dive

### Peeling Back the Magic: Demystifying Function Calling

To software developers encountering AI agents for the first time, "Function Calling" and "Agent Tools" can sound like magic. Many assume that the large language model physically compiles and executes Python code inside its neural network weights.

**In reality, an LLM is purely a next-token text prediction engine.** It cannot execute code, make network calls, or query a database.

Here is what actually happens when an agent calls a tool:
1. **The Contract**: Your Python script sends a prompt along with a JSON Schema describing available tools:
   ```json
   {
     "name": "get_stock_price",
     "description": "Retrieves the current market share price for a ticker symbol.",
     "parameters": {
       "type": "object",
       "properties": {
         "ticker": {"type": "string", "description": "Stock symbol, e.g. AAPL"}
       },
       "required": ["ticker"]
     }
   }
   ```
2. **The Output**: The model recognizes that answering the user's question requires real-time data. Instead of generating conversational text, it predicts tokens matching the tool structure:
   `{"tool": "get_stock_price", "args": {"ticker": "INTC"}}`
3. **The Interception**: The Python runtime halts LLM generation, reads the JSON output, looks up `get_stock_price` in a local dictionary of functions, and executes the local Python code.
4. **The Observation**: The output of the Python function (e.g., `"$22.50"`) is injected back into the LLM's conversation history as an **Observation**.
5. **The Final Answer**: The LLM synthesizes the observation into a natural language response: *"Intel is currently trading at $22.50."*

#### Why This Distinction Matters
Because tool calling is just text serialization, it is fragile. If the LLM outputs malformed JSON or hallucinates an argument, naive string parsers crash. Building reliable code agents requires **strict schema validation using Pydantic**.

---

## 2. Physical Mental Models & Architecture

### The ReAct (Reason + Act) Loop in Python

Pioneered by Yao et al. (2022), the ReAct pattern prompts the language model to interleave reasoning thoughts with specific tool invocations:

```
┌────────────────────────────────────────────────────────┐
│ USER PROMPT: "What is 15% tax on an order of 4 items   │
│              costing $35.00 each?"                     │
└──────────────────────────┬─────────────────────────────┘
                           │
                           ▼
┌────────────────────────────────────────────────────────┐
│ THOUGHT 1: "I need to calculate the subtotal first."   │
│ ACTION 1:  calculate(operation="multiply", a=4, b=35)  │
└──────────────────────────┬─────────────────────────────┘
                           │ Runtime executes Python function
                           ▼
┌────────────────────────────────────────────────────────┐
│ OBSERVATION 1: "140.0"                                 │
└──────────────────────────┬─────────────────────────────┘
                           │ Model receives observation
                           ▼
┌────────────────────────────────────────────────────────┐
│ THOUGHT 2: "The subtotal is $140. Now compute 15% tax."│
│ ACTION 2:  calculate(operation="multiply", a=140,      │
│                      b=0.15)                           │
└──────────────────────────┬─────────────────────────────┘
                           │ Runtime executes Python function
                           ▼
┌────────────────────────────────────────────────────────┐
│ OBSERVATION 2: "21.0"                                  │
└──────────────────────────┬─────────────────────────────┘
                           │ Goal accomplished!
                           ▼
┌────────────────────────────────────────────────────────┐
│ FINAL ANSWER: "The 15% tax on the order is $21.00."   │
└────────────────────────────────────────────────────────┘
```

### Pydantic Schemas as Contract Boundaries
By backing every tool with a **Pydantic BaseModel**, Python automatically validates incoming arguments:
- If valid, the function executes cleanly.
- If invalid, Pydantic catches the error and generates an immediate, structured feedback message back to the LLM (*"ValidationError: value 'five' is not a valid integer"*), allowing the agent to self-correct on the next iteration.

---

## 3. Curated Slide Reading Directives

Refer to the following specific sections of the Intel presentation deck in your course repository:

### From `[Slides] Module 13 - Agentic AI.pptx` (106 slides)
- **Study Slides 10–21 (Foundations of Running an AI Agent)**: Understand how LLMs communicate over REST APIs, HTTP POST payloads, system messages, and JSON response parsing.
- **Study Slides 22–74 (Building the Agent & The ReAct Pattern)**: Study the Reason &rarr; Act &rarr; Observe loop. Contrast single-turn zero-shot prompting with multi-turn iterative problem solving.
- **Study Slides 75–98 (Agent Tooling & Function Calling)**: Master how function signatures (name, description, parameter schemas) are serialized into LLM prompts, and how tool execution results are fed back into conversational memory.
- *Skip Slides 99–106* (bibliographies and index citations).

---

## 4. Production Modular Architecture & Grounded Vector RAG

### Modular Architecture Standards
Enterprise codebases strictly decouple reasoning logic from tool definitions:
- `agent.py`: Houses the central reasoning loop and execution controller.
- `tools.py`: Houses deterministic Python functions wrapped with schemas and error handlers.
- `retrieval.py`: Manages document embedding, vector indexing, and RAG search.
- `helpers/config.py`: Centralizes API keys, temperature settings, and model identifiers.
