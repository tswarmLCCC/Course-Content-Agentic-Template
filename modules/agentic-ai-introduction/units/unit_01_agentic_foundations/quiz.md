# Unit 01 Knowledge Check: Agentic Foundations & Architectural Patterns

This assessment evaluates your conceptual mastery of agentic systems architecture, the ReAct reasoning framework, Anthropic's workflow taxonomy, and defensive tool engineering.

---

### Question 1
According to Anthropic's research paper *"Building Effective Agents"*, what is the primary architectural difference between a "Workflow" and an "Agent"?
* A) Workflows require proprietary fine-tuned models, whereas agents operate exclusively on open-source weights.
* B) Workflows orchestrate LLMs and tools via predefined, hardcoded code paths, whereas agents dynamically direct their own processes and tool usage.
* C) Workflows can only execute in terminal environments, whereas agents operate inside web browsers.
* D) Workflows allow multi-step loops, whereas agents are strictly constrained to single-turn prompt-response interactions.

### Question 2
In Smitha Kolan's Google Cloud Tech lecture, which agent pattern is characterized by breaking a complex objective into a structured strategy or task sequence upfront before dispatching execution?
* A) The Reactive Pattern
* B) The Sequential Pattern
* C) The Planning Pattern
* D) The Zero-Shot Pattern

### Question 3
In the ReAct framework developed by Yao et al. (ICLR 2023), what are the four repeating components of the execution loop?
* A) Prompt, Tokenize, Embed, Decode
* B) Thought, Action, Action Input, Observation
* C) System Prompt, User Input, Assistant Response, Log
* D) Plan, Fork, Merge, Commit

### Question 4
Why does the ReAct framework outperform pure Chain-of-Thought (CoT) reasoning on factual, multi-step tasks?
* A) CoT uses more parameters than ReAct during inference.
* B) CoT relies solely on internal parametric memory where hallucinations compound, whereas ReAct grounds reasoning with external observations from tools.
* C) ReAct disables the model's reasoning capabilities so it can execute raw shell scripts faster.
* D) CoT cannot generate syntactically valid JSON.

### Question 5
In Anthropic's "Prompt Chaining" workflow, what is the role of an intermediate "programmatic gate"?
* A) It encrypts the user's prompt using AES-256 before transmitting it over the network.
* B) It validates that the output of an upstream LLM call meets strict criteria before allowing the next step to execute.
* C) It routes the query to an external payment processor to verify token credits.
* D) It reduces the model's temperature to 0.0 automatically.

### Question 6
When is the "Routing" workflow preferred over loading all available tools into a single monolithic agent prompt?
* A) Only when operating without an internet connection.
* B) When tasks fall into distinct categories that benefit from specialized prompts, avoiding prompt bloat and tool distraction.
* C) When the developer wants the agent to run in an infinite `while True` loop.
* D) When the model needs to calculate floating point numbers without Python.

### Question 7
Anthropic defines two distinct variations of the "Parallelization" workflow. What are they?
* A) Asynchronous and Synchronous
* B) Sectioning (splitting into independent subtasks) and Voting (running the same task to get diverse outputs)
* C) Client-side and Server-side
* D) Encoder-based and Decoder-based

### Question 8
What is the primary difference between the "Orchestrator-Workers" workflow and standard "Parallelization"?
* A) Orchestrator-workers cannot use tools.
* B) In parallelization, subtasks are hardcoded in advance; in orchestrator-workers, subtasks are dynamically determined at runtime based on the input.
* C) Parallelization uses human reviewers, whereas orchestrator-workers is 100% automated.
* D) Orchestrator-workers requires running Kubernetes clusters locally.

### Question 9
In the "Evaluator-Optimizer" workflow (the pattern used in Smitha Kolan's blog writer), what role does the Evaluator model play?
* A) It converts the blog post into binary bytecode.
* B) It compiles and runs automated unit tests on the user's operating system.
* C) It critiques the generator's draft against explicit criteria and provides structured feedback for the next iteration.
* D) It routes incoming customer tickets to human support dispatchers.

### Question 10
In autonomous agent architectures, what provides the "ground truth" that enables the agent to evaluate its own progress?
* A) The model's internal temperature parameter.
* B) Environmental observations resulting from tool execution (e.g., API outputs, test results, database returns).
* C) The user's system clipboard history.
* D) The tokenizer's vocabulary size.

### Question 11
What does the "Poka-Yoke" principle mean in the context of Agent-Computer Interface (ACI) and tool design?
* A) Maximizing the number of optional parameters to provide maximum flexibility.
* B) Designing tool arguments and schemas to be mistake-proof so that it is difficult or impossible for the LLM to provide invalid inputs.
* C) Writing tool descriptions in Japanese to improve token efficiency.
* D) Storing all tool schemas inside an encrypted SQLite database.

### Question 12
Why does Anthropic strongly recommend requiring **absolute filepaths** rather than relative paths in agent tool definitions?
* A) Relative paths are forbidden by the Linux file system standard.
* B) Language models easily lose track of the current working directory across multi-turn interactions, leading to file-not-found errors or editing the wrong file.
* C) Absolute paths compress better in the model's tokenizer.
* D) Relative paths cause immediate CUDA out-of-memory errors on GPU servers.

### Question 13
What is the most critical defensive mitigation against a "runaway execution loop" in an autonomous agent?
* A) Disabling the agent's ability to read error messages.
* B) Enforcing a strict maximum iteration threshold (`max_iterations = N`) combined with duplicate-action interception.
* C) Running the model with temperature set to 1.5.
* D) Removing all docstrings from tool definitions.

### Question 14
What is the primary architectural purpose of Anthropic's **Model Context Protocol (MCP)**?
* A) To replace Python with C++ for faster inference.
* B) To provide an open standard protocol allowing agents to connect securely to a growing ecosystem of external tools, data sources, and servers via a uniform interface.
* C) To compress JPEG images into vector embeddings.
* D) To automatically write legal patents for AI software.

### Question 15
What is the fundamental architectural tradeoff when choosing an **Autonomous Agent** over a **Deterministic Workflow**?
* A) Agents offer greater flexibility on open-ended problems, but introduce higher latency, higher token costs, and compounding error probabilities.
* B) Workflows are more expensive and slower than agents in 100% of enterprise scenarios.
* C) Agents produce zero hallucinations, whereas workflows always hallucinate.
* D) Workflows require GPU clusters, while agents run locally on microcontrollers.

---

## Answer Key

| Question # | Correct Answer | Concept Tested & Rationale |
| :---: | :---: | :--- |
| **1** | **B** | **Workflows vs. Agents**: Workflows orchestrate LLMs through predefined, hardcoded code paths; agents dynamically direct their own processes and tool usage at runtime. |
| **2** | **C** | **Planning Pattern**: In Kolan's taxonomy, the Planning pattern maps out a strategic multi-step plan upfront to accomplish complex objectives before execution. |
| **3** | **B** | **ReAct Loop**: Yao et al. defined the ReAct framework as an alternating sequence of Thought (verbal reasoning), Action (tool selection), Action Input (arguments), and Observation (environment feedback). |
| **4** | **B** | **Grounding & Synergistic Reasoning**: Pure Chain-of-Thought suffers from compounding hallucination; ReAct uses environmental observations to continuously ground and correct reasoning. |
| **5** | **B** | **Programmatic Gates**: Gates provide deterministic validation checks between steps in a prompt chain to prevent bad or invalid states from propagating downstream. |
| **6** | **B** | **Routing Workflow**: Routing classifies intent and sends requests to specialized prompts with minimal, relevant tools, preventing prompt bloat and context distraction. |
| **7** | **B** | **Parallelization Archetypes**: Sectioning breaks tasks into independent concurrent subtasks; Voting runs identical prompts to find consensus and minimize false positives. |
| **8** | **B** | **Dynamic vs. Static Decomposition**: Parallelization executes hardcoded subtasks; Orchestrator-Workers dynamically decomposes tasks at runtime based on the input. |
| **9** | **C** | **Evaluator-Optimizer Loop**: The Evaluator acts as an automated critic, grading the draft against a rubric and feeding actionable critiques back to the Writer. |
| **10** | **B** | **Environmental Ground Truth**: Real-world observations (tool execution returns, test outcomes, error logs) provide the objective ground truth that guides agent decisions. |
| **11** | **B** | **Poka-Yoke ACI**: Poka-Yoke mistake-proofs tools so arguments are constrained, types are strict, and docstrings guide the model away from failure states. |
| **12** | **B** | **Path Anchoring**: Across multi-turn interactions, models experience context drift regarding current working directories; absolute paths eliminate path ambiguity. |
| **13** | **B** | **Runaway Loop Control**: Enforcing hard iteration limits (`max_iterations`) and detecting duplicate failing actions prevents catastrophic infinite token consumption. |
| **14** | **B** | **Model Context Protocol (MCP)**: MCP provides a universal, open standard for exposing tools, prompts, and resources to agent clients across diverse environments. |
| **15** | **A** | **Core Architectural Tradeoff**: Autonomous agents provide extreme adaptability on open-ended problems, but trade off deterministic predictability, latency, and token cost. |
