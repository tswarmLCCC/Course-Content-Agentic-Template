# Unit 05: Asynchronous Preparation & Diagnostic Drills
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
