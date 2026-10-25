# Unit 01: Required Readings, Concepts & Video Lectures

Welcome to the instructional lecture and research reading guide for **Unit 01: Agentic Foundations & Architectural Patterns**. This master guide bridges the gap between passive language models and autonomous agentic systems.

All weekly instructional materials are organized into four core pedagogical chapters:

1. **Chapter 1: Foundations of Agentic AI & The Three Core Patterns** — Grounded in our featured lecture by Smitha Kolan (Google Cloud Tech), exploring how modern AI moves beyond prompt-response into Sequential, Reactive, and Planning patterns.
2. **Chapter 2: The ReAct Framework — Synergizing Reasoning and Acting** — A deep dive into the landmark Princeton/Google research paper (*Yao et al., ICLR 2023*) demonstrating why interleaving internal verbal reasoning (Thoughts) with external tool calls (Actions) outperforms pure Chain-of-Thought or isolated tool use.
3. **Chapter 3: Workflows vs. Autonomous Agents (The Anthropic Architecture)** — The definitive industry architectural standard from Anthropic Engineering (*Erik S. & Barry Zhang, Dec 2024*), categorizing deterministic workflows (Prompt Chaining, Routing, Parallelization, Orchestrator-Workers, Evaluator-Optimizer) versus dynamic autonomous agents.
4. **Chapter 4: Agent-Computer Interfaces (ACI), Tool Design & Defensive Engineering** — Best practices for designing Poka-Yoke ("mistake-proof") tools, preventing infinite loops, handling token drift, and enforcing absolute environmental ground truth.

---

## Primary Video Lecture: AI Agents Explained (Google Cloud Tech)

Watch this video lecture hosted by **Smitha Kolan** on Google Cloud Tech before proceeding through the text chapters below. It provides a visual, practical mental model of autonomous agent loops and introduces the self-correcting multi-agent blog writer you will construct in this week's applied lab.

<div style="position: relative; padding-bottom: 56.25%; height: 0; overflow: hidden; max-width: 100%; border-radius: 8px; margin: 1.5rem 0;">
  <iframe style="position: absolute; top: 0px; left: 0px; width: 100%; height: 100%; border: 0px none currentcolor;" title="AI agents explained: Build your first agent in 8 minutes — Smitha Kolan (Google Cloud Tech)" src="https://www.youtube.com/embed/Zqno_vux6d8" loading="lazy" allowfullscreen="allowfullscreen" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share"></iframe>
</div>

<div style="margin: 0.5rem 0 1.5rem 0; font-size: 0.95em;">
  <em>Video not displaying in Canvas? <a href="https://www.youtube.com/watch?v=Zqno_vux6d8" target="_blank" rel="noopener noreferrer">Watch directly on YouTube: AI agents explained — Build your first agent in 8 minutes</a></em>
</div>

### Video Chapters & Verified Navigation:
- **0:00 — Introduction**: Beyond static chatbots to autonomous action.
- **1:15 — The ReAct Framework**: How reasoning and acting synergize to solve dynamic problems.
- **2:40 — Core Agent Patterns**: Sequential pipelines, Reactive feedback, and Upfront Planning.
- **4:30 — Hands-on Architecture**: Constructing Planner, Writer, and Validator agents.
- **6:10 — The Auto-Correcting Loop**: Catching mistakes and programmatically triggering retries.
- **7:35 — Testing & Evaluation**: Inspecting execution traces in the Agent Development Kit (ADK).

---

## Authoritative References & Academic Citations

This curriculum is built directly upon two seminal foundations in the artificial intelligence literature:

1. **The ReAct Paper**:
   > **Yao, S., Zhao, J., Yu, D., Du, N., Shafran, I., Narasimhan, K., & Cao, Y. (2023).** *ReAct: Synergizing Reasoning and Acting in Language Models.* Published at the Eleventh International Conference on Learning Representations (ICLR 2023). [arXiv:2210.03629](https://arxiv.org/abs/2210.03629).
2. **The Anthropic Agentic Systems Paper**:
   > **Erik S. & Barry Zhang (2024).** *Building Effective Agents.* Anthropic Engineering & Research, Published December 19, 2024. [anthropic.com/research/building-effective-agents](https://www.anthropic.com/research/building-effective-agents).

---

## Chapter 1: Foundations of Agentic AI & The Three Core Patterns

### 1.1 The Fundamental Paradigm Shift: From Predictors to Decision Engines
For the past several years, developers have interacted with Large Language Models (LLMs) primarily as **stateless function approximations**:
$$\text{Output} = \text{LLM}(\text{Prompt})$$

When you ask an LLM to generate an essay, explain quantum computing, or translate code, the model generates tokens autoregressively from its frozen internal parametric weights. While impressive, this paradigm exhibits severe operational bottlenecks:
- **Knowledge Horizon Cutoff**: The model has no access to information created after its pre-training checkpoint.
- **Parametric Hallucination**: When unsure of a factual claim, the model generates plausible-sounding fiction rather than admitting uncertainty.
- **Passive Execution**: The model cannot check its own work, inspect a filesystem, query an enterprise SQL database, or fix a syntax error it produced.

**Agentic AI transforms this dynamic.** An agent is an LLM paired with:
1. **Sensors / Context**: Memory and environment retrieval (RAG, documentation, historical logs).
2. **Effectors / Tools**: External executable functions (APIs, calculators, terminal shells, code compilers).
3. **A Decision Loop**: A control harness that inspects environmental observations, evaluates progress toward an objective, and decides what action to execute next.

### 1.2 The Three Fundamental Patterns (Smitha Kolan)
In her Google Cloud Tech lecture, Smitha Kolan identifies the three fundamental architectural patterns that govern agentic systems:

```
Pattern 1: Sequential (Linear Pipeline)
[Input] ──> [Agent A: Outline] ──> [Agent B: Draft] ──> [Agent C: Proofread] ──> [Output]

Pattern 2: Reactive (Event & Feedback Loop)
               ┌─────────── Observation ───────────┐
               ▼                                   │
[Input] ──> [Agent Decision] ──> [Action / Tool] ──┘

Pattern 3: Planning (Hierarchical Strategic Plan)
[Goal] ──> [Planner Agent] ──> Decompose into [Step 1, Step 2, Step 3] 
                                    │
                                    ├──> Dispatches to Worker A
                                    └──> Dispatches to Worker B
```

#### 1. Sequential Pattern (Pipelines)
In a **Sequential** pattern, execution proceeds along a predetermined, linear chain. The output of Agent A becomes the strict input of Agent B. 
- *When to use*: Assembly-line tasks where the required subtasks are invariant (e.g., Extract text from PDF $\to$ Clean markdown $\to$ Translate to Spanish).
- *Tradeoff*: High predictability, but zero autonomy to adapt if an upstream step fails.

#### 2. Reactive Pattern (Environment Feedback)
In a **Reactive** pattern, the agent does not follow a rigid script. It evaluates incoming data or environmental signals, selects a tool, receives an observation, and reactively determines its next step.
- *When to use*: Interactive debugging, terminal navigation, database exploration, or customer ticket resolution where each subsequent action depends strictly on what the previous action discovered.

#### 3. Planning Pattern (Hierarchical Decomposition)
In a **Planning** pattern, a specialized controller model analyzes a complex goal upfront, breaks it down into a directed acyclic graph (DAG) or sequence of sub-goals, and assigns specialized sub-agents or tools to execute each part.
- *When to use*: Large-scale engineering problems (e.g., refactoring a multi-module repository, conducting comprehensive competitor research across 20 web domains).

---

## Chapter 2: The ReAct Framework — Reason + Act in Language Models

### 2.1 Why Pure Reasoning or Pure Acting Fails
Prior to 2022, research in language model problem-solving was split into two isolated camps:
1. **Pure Reasoning (Chain-of-Thought / CoT)**: Prompting the model to "think step-by-step." While CoT improves mathematical reasoning, the model relies entirely on its internal memory. When reasoning about factual, temporal, or API-specific tasks, it suffers from compounding hallucination—a single false assumption early in the chain derails all subsequent logic.
2. **Pure Acting (Action-Only / Tool-Use)**: Equipping the model with tools (e.g., search engines, Python REPLs) without internal reasoning. In action-only architectures, the model blindly fires queries into the environment without tracking its high-level strategy, leading to repetitive searches, inability to recover from unexpected errors, and prompt thrashing.

### 2.2 The ReAct Breakthrough (Yao et al., 2022)
In the landmark paper *"ReAct: Synergizing Reasoning and Acting in Language Models"* (Princeton & Google Research), Shunyu Yao and colleagues demonstrated that **interleaving reasoning traces with external actions** unlocks unprecedented problem-solving reliability.

In the ReAct framework, the model alternates between:
- **Thought**: The model writes a free-form natural language reflection about its current state, what it knows, what is missing, and what it should do next.
- **Action**: The model chooses an explicit, structured action from a fixed catalog of tools (e.g., `Search[query]`, `Lookup[keyword]`, `Calculate[expression]`).
- **Action Input**: The specific parameters fed into the tool.
- **Observation**: The external environment (API, Python script, or database) executes the action and injects the raw result back into the prompt context.

```
┌────────────────────────────────────────────────────────┐
│                   THE ReAct LOOP                       │
│                                                        │
│   ┌─────────────┐                                      │
│   │   Thought   │ (Model reflects on state & strategy) │
│   └──────┬──────┘                                      │
│          ▼                                             │
│   ┌─────────────┐                                      │
│   │   Action    │ (Model selects executable tool)      │
│   └──────┬──────┘                                      │
│          ▼                                             │
│   ┌─────────────┐                                      │
│   │ Observation │ (Environment returns raw data)       │
│   └──────┬──────┘                                      │
│          │                                             │
│          └──────── Loop until Final Answer ────────────┘
└────────────────────────────────────────────────────────┘
```

### 2.3 Concrete ReAct Execution Trace
Consider an agent asked to verify an enterprise logistics fact: *"What is the payload capacity of the freight aircraft used in Route 402, and does it exceed our 45-ton cargo requirement?"*

Here is an authentic ReAct execution trace:

```text
Question: What is the payload capacity of the freight aircraft used in Route 402, and does it exceed our 45-ton requirement?

Thought 1: I need to find which aircraft model operates on Route 402. Let me query the route database.
Action 1: QueryDatabase[SELECT aircraft_type FROM routes WHERE route_id = 'Route_402']
Observation 1: aircraft_type: "Boeing 767-300F"

Thought 2: Route 402 uses a Boeing 767-300F. Now I need to look up the maximum structural payload capacity for a Boeing 767-300F in tons.
Action 2: LookupAircraftSpecs["Boeing 767-300F", "max_payload_tonnes"]
Observation 2: max_payload_tonnes: 52.7 metric tonnes (approx. 58.0 US short tons)

Thought 3: The capacity is 52.7 metric tonnes (58.0 US tons). The shipment requirement is 45 tons. 52.7 tonnes (and 58 tons) is strictly greater than 45 tons. I have all information needed to answer.
Action 3: Finish[The Boeing 767-300F used on Route 402 has a maximum payload capacity of approximately 52.7 metric tonnes (58 US tons), which safely exceeds the 45-ton requirement.]
```

**Why this matters**: Notice how `Thought 2` prevented hallucination. If the model had tried to guess the payload without `Action 1`, it might have hallucinated a Boeing 737 or Airbus A321. The environment grounded the reasoning; the reasoning directed the environment.

---

## Chapter 3: Workflows vs. Autonomous Agents (The Anthropic Architecture)

In their seminal December 2024 paper *"Building Effective Agents"*, Anthropic engineers Erik S. and Barry Zhang established a crucial industry taxonomy: distinguishing between **Workflows** and **Autonomous Agents**.

```
┌────────────────────────────────────────────────────────────────────────┐
│                        AGENTIC SYSTEMS TAXONOMY                        │
├───────────────────────────────────┬────────────────────────────────────┤
│             WORKFLOWS             │               AGENTS               │
├───────────────────────────────────┼────────────────────────────────────┤
│ • Predefined, hardcoded code paths│ • Model dynamically directs its own│
│ • High predictability & low drift │   process and tool usage           │
│ • Deterministic state transitions │ • High flexibility & adaptability  │
│ • Lower latency & cost            │ • Trades higher cost/latency for   │
│ • Ideal for structured processes  │   open-ended problem solving       │
└───────────────────────────────────┴────────────────────────────────────┘
```

Anthropic identifies **The Augmented LLM** as the foundational atom (an LLM equipped with retrieval, tools, and memory), and details the **Five Canonical Workflow Patterns** before graduating to fully autonomous agents:

### 3.1 Pattern 1: Prompt Chaining (with Gates)
Prompt chaining decomposes a complex task into a sequential pipeline where each LLM call tackles an easier, isolated sub-problem. 

```
[Prompt 1: Outline] ──> [Code Gate: Validate Structure] ──> [Prompt 2: Draft] ──> [Output]
```
- **The Gate Concept**: Between LLM calls, programmatic Python gates validate that the intermediate representation conforms to strict criteria (e.g., valid JSON schema, minimum word count, no forbidden keywords) before proceeding.
- **When to use**: Document generation, multi-stage translation, or multi-step analysis where steps are predictable.

### 3.2 Pattern 2: Routing
Routing classifies an input and directs it to a specialized downstream prompt, toolset, or model tier.

```
                     ┌──> [Technical Support Prompt / Tools]
                     │
[User Input] ──> [Router] ──> [Billing & Refund Prompt / Tools]
                     │
                     └──> [Route to Small Model (Haiku) for FAQ]
```
- **Specialization & Cost Optimization**: Routing prevents prompt bloat. Instead of loading 50 tool definitions into one massive system prompt, the router selects the exact 3 tools needed. It also allows routing easy queries to fast, cost-effective models (e.g., Claude 3.5 Haiku) and hard queries to frontier models (e.g., Claude 3.5 Sonnet).

### 3.3 Pattern 3: Parallelization (Sectioning & Voting)
Parallelization leverages simultaneous LLM calls whose outputs are programmatically merged. It manifests in two primary archetypes:
1. **Sectioning**: Splitting an independent task into chunks (e.g., evaluating 5 different security compliance rules simultaneously across 5 parallel LLM calls).
2. **Voting**: Running the identical prompt across multiple calls with distinct system personas or temperature settings to find consensus and minimize false positives (e.g., automated vulnerability detection).

### 3.4 Pattern 4: Orchestrator-Workers
In this pattern, a central **Orchestrator LLM** dynamically inspects an input, breaks it down into subtasks on the fly, dispatches them to **Worker LLMs**, and synthesizes the results.

```
                      ┌──> [Worker A: Edit File 1] ──┐
                      │                              │
[Task] ──> [Orchestrator] ─┼──> [Worker B: Edit File 2] ──┼──> [Synthesize / Test]
                      │                              │
                      └──> [Worker C: Write Test]   ──┘
```
- **Difference from Parallelization**: In parallelization, subtasks are hardcoded in advance. In Orchestrator-Workers, the subtasks are generated dynamically at runtime based on what the orchestrator observes.

### 3.5 Pattern 5: Evaluator-Optimizer (Critique Loop)
One LLM call generates a solution, while a separate **Evaluator LLM** critiques the output against concreterubric criteria in an iterative loop.

```
       ┌──────────────── Critique & Feedback ───────────────┐
       ▼                                                   │
[Generator LLM] ──> [Draft] ──> [Evaluator LLM: Check Rubric]
                                         │
                                   Passes Rubric?
                                         ├── Yes ──> [Final Output]
                                         └── No  ──> [Loop with Feedback]
```
- **This is the exact pattern featured in Smitha Kolan's blog writer**: A Writer agent drafts content, a Validator agent evaluates formatting and length constraints, and a Loop agent feeds specific critique back to the Writer until the validation gate passes.

### 3.6 Autonomous Agents: When to Graduate
When a problem is so open-ended that the sequence of steps cannot be predicted in advance (e.g., fixing a bug in an unknown repository or navigating a complex API), you graduate from workflows to **Autonomous Agents**. 
- The agent runs in a continuous loop: observing the environment, calling tools, and reacting to ground-truth feedback until a stopping condition is achieved.
- **The Core Tradeoff**: Autonomous agents offer maximum flexibility, but introduce non-determinism, higher latency, higher token costs, and compounding error probability.

---

## Chapter 4: Agent-Computer Interfaces (ACI), Tool Engineering & Defensive Guardrails

### 4.1 "Poka-Yoke" Tool Design
In industrial manufacturing, the Japanese concept of *Poka-Yoke* ($\text{ポカヨケ}$) means "mistake-proofing": designing mechanisms so that operators cannot make mistakes (e.g., a SIM card slot shaped so it can only be inserted in one orientation).

In their paper, Anthropic emphasizes that **developers must spend just as much effort on the Agent-Computer Interface (ACI) as on human UI/UX**. If a tool interface is ambiguous, the LLM will inevitably misuse it.

#### Rules for Poka-Yoke Tool Design:
1. **Never use relative filepaths**: When models navigate directories, they lose track of the working directory. Always enforce **absolute paths** in tool arguments (`/workspace/project/main.py`, not `../../main.py`).
2. **Avoid counting overhead**: Asking an LLM to supply exact line counts (like diff chunk headers `@@ -12,4 +12,6 @@`) causes frequent failures because tokenizers do not perceive character/line counts intuitively. Design tools that accept target replacement strings or unique identifiers instead.
3. **Write Docstrings for a Junior Developer**: Tool descriptions are system prompts! Clearly specify parameter types, edge cases, allowed values, and provide an explicit example of a successful call.

### 4.2 Deterministic Stopping Conditions & Loop Control
The greatest hazard in autonomous agent architectures is the **runaway execution loop**: an agent encounters an unhandled error, retries the exact same failing action, and burns thousands of API tokens in an infinite recursion.

Every production agent loop must enforce three non-negotiable defensive controls:
1. **Hard Max-Iteration Cap (`max_iterations = N`)**: If the agent fails to reach a terminal state within $N$ turns (typically 3–5 for simple tasks, 10–15 for complex coding tasks), the loop forcefully aborts and surfaces a human-in-the-loop alert.
2. **State Deduplication**: The harness tracks the hash of tool calls and arguments. If the exact same tool call produces the exact same error twice consecutively, the loop intercepts the call and prompts the model to select an alternative strategy.
3. **Structured Schema Validation**: All tool inputs and outputs must pass Pydantic or JSON schema validation before execution. If validation fails, the error message returned to the agent must specify the exact missing or malformed property.

---

## Chapter Summary & Architectural Decision Matrix

When designing a production AI feature, consult this architectural decision matrix:

| Architectural Pattern | Mechanism | Primary Strength | Typical Weakness | Ideal Production Use Case |
| :--- | :--- | :--- | :--- | :--- |
| **Augmented LLM** | Single call + RAG/Tools | Low latency, simple | Limited to 1-turn tasks | Answering factual FAQ with documentation |
| **Prompt Chaining** | Sequential pipeline with gates | High consistency, verifiable | Rigid, cannot branch | Step-by-step document synthesis |
| **Routing** | Input classification classifier | Specialized prompts, low cost | Router classification error | Multi-intent customer support triage |
| **Parallelization** | Concurrent calls + voting/merge | High coverage, diversity | Token multiplication | Automated security code audits |
| **Evaluator-Optimizer** | Generator $\to$ Critic $\to$ Loop | High quality, self-healing | High latency (2–3x calls) | Multi-agent blog/report generation |
| **Autonomous Agent** | Dynamic ReAct loop + tools | Extreme flexibility | Non-deterministic, high cost | SWE-bench coding & open-ended research |
