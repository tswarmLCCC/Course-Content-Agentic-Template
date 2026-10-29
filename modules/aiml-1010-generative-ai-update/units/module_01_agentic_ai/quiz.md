# Module 01 Knowledge Check: Demystifying Agentic AI

**Course**: AIML 1010: Introduction to Artificial Intelligence  
**Assessment Type**: Multiple Choice Knowledge Check  
**Allowed Attempts**: 3 | **Scoring Policy**: Keep Highest Score | **Points Possible**: 30.0

---

## Assessment Questions

### Question 1
What is the most fundamental characteristic that defines any AI Agent?

* A) Operates exclusively in a fully observable, deterministic, and static environment
* B) Relies strictly on hardcoded rules without learning or perceptual capabilities
* C) Possesses human-level consciousness and general artificial intelligence
* D) Perceives its environment through sensors/inputs and autonomously takes actions to achieve goals

### Question 2
What is the primary advantage of a Model-based Reflex Agent over a Simple Reflex Agent?

* A) It evaluates sequences of actions based on a mathematical utility function
* B) It maintains an internal state to track unobserved aspects of the partially observable environment
* C) It guarantees selecting the globally optimal action by computing all future possibilities
* D) It directly maps immediate sensory inputs to actions using condition-action rules without memory

### Question 3
What is the key differentiator between Agentic AI and conventional AI systems?

* A) Agentic AI focuses solely on generating human-like creative writing, while conventional AI focuses on automation
* B) Agentic AI and conventional AI are identical terms used interchangeably in industry
* C) Agentic AI demonstrates autonomous goal decomposition, tool use, and multi-step iterative action, rather than just single-turn predictions
* D) Agentic AI is restricted to offline data processing without interacting with external environments

### Question 4
In the context of Agentic AI, what does the Tooling (or Function Calling) module primarily enable the agent to do?

* A) Permanently fine-tune the base model weights on local user data
* B) Evaluate internal token logits against human preference benchmarks
* C) Convert natural language prompts into compressed vector embeddings
* D) Interact with external software, APIs, calculators, and databases to perform actions beyond internal reasoning

### Question 5
What is the primary focus of the Reflection phase in an agentic workflow?

* A) Reviewing the outcome of past actions/plans and adjusting internal strategy for subsequent steps
* B) Tokenizing input prompts into subword integer arrays
* C) Compressing long context windows into fixed-size summary embeddings
* D) Generating random alternative responses to increase temperature

### Question 6
Which two factors must a Goal-based Agent primarily consider when selecting an action?

* A) The current system clock and total memory allocation
* B) The target goal state and the predicted outcomes of candidate actions
* C) The hardware GPU architecture and compiler optimization flags
* D) The length of historical user prompts and token budgets

### Question 7
Which characteristic best defines a Utility-based Agent?

* A) It selects actions solely based on binary goal achievement, ignoring preferences or efficiency
* B) It reacts strictly to real-time inputs without tracking history or future consequences
* C) It follows an immutable hardcoded decision tree regardless of context
* D) It uses a continuous utility function to weigh trade-offs and choose the most desirable or optimal outcome among competing goals

### Question 8
Which of the following is a key capability that differentiates Agentic AI from traditional standalone LLMs?

* A) Ability to predict the next token in a static prompt
* B) Autonomous multi-step execution using external tools, error-checking, and memory without requiring human prompts at every sub-step
* C) Generation of grammatically correct English responses
* D) Processing inputs using Transformer self-attention mechanisms

### Question 9
In an Agentic AI architecture, what is a 'tool'?

* A) The pre-training dataset used to train the base foundational model
* B) The GPU cluster executing tensor floating-point calculations
* C) The internal activation function inside multi-head attention layers
* D) An external function, API, script, or service that the model can invoke via structured schema to interact with the world

### Question 10
Which statement best characterizes modern Human-AI collaboration in Agentic AI systems?

* A) Humans are entirely replaced across all enterprise decision loops
* B) Humans act as supervisors and collaborators (Human-in-the-Loop), providing high-level intent, guardrails, and approvals while agents handle execution
* C) AI agents operate with complete unmonitored autonomy in mission-critical legal and medical settings
* D) Humans only interact with agents during initial model weights compilation

---

## Answer Key

| Question # | Correct Answer | Concept Tested & Rationale |
| :--- | :--- | :--- |
| **1** | **D** | An AI agent is fundamentally defined by its perception-action cycle: perceiving an environment and executing actions autonomously toward a specific objective. |
| **2** | **B** | Model-based reflex agents maintain internal state representing the world that cannot currently be seen, overcoming the limitation of simple reflex agents in partially observable worlds. |
| **3** | **C** | Agentic AI moves beyond single-turn prompt-response interactions to systems that autonomously plan, call tools, reflect on intermediate outputs, and execute multi-step workflows. |
| **4** | **D** | Tool calling allows an LLM agent to bridge the gap between static model weights and dynamic external environments—querying APIs, querying databases, running code, and triggering actions. |
| **5** | **A** | Self-reflection allows agents to critique their own intermediate outputs, identify errors or failed tool calls, and refine their execution plans iteratively. |
| **6** | **B** | Goal-based agents combine knowledge of current states with goal descriptions and world models to evaluate how candidate actions bring the agent closer to the desired goal. |
| **7** | **D** | Utility-based agents map states to real numbers (utility), enabling principled trade-off analysis when multiple conflicting goals exist or when success is probabilistic. |
| **8** | **B** | Traditional LLMs generate single responses to static prompts. Agentic AI loops autonomously: taking actions, receiving feedback from tools/environments, and continuing until the objective is achieved. |
| **9** | **D** | A tool in agentic systems is an executable software interface (API, database connector, calculator, bash terminal) described by a schema that the agent calls to interact with reality. |
| **10** | **B** | Effective agentic systems utilize Human-in-the-Loop (HITL) patterns: agents handle high-throughput discovery, synthesis, and execution, while humans steer strategy, review sensitive actions, and provide governance. |
