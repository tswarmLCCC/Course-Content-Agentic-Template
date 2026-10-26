# Unit 01: Required Readings, Concepts & Video Lectures

Welcome to the foundational instructional lecture and research reading guide for **Unit 01: Vibe Coding vs. Agentic SDLC & The 10/90 Harness Rule**. This master guide deconstructs how software engineering is fundamentally evolving in the age of autonomous AI agents.

All weekly instructional materials are organized into four core pedagogical chapters:

1. **Chapter 1: The Collapse of Syntax & The Vibe Coding Trap** — Analyzing how generative AI shifts software development from syntax typing to architectural intent, and dissecting why casual "vibe coding" leads to the catastrophic "80% Trap."
2. **Chapter 2: The 10/90 Harness Rule — Model vs. Execution Harness** — Grounded in Google's landmark research, establishing why the foundation model accounts for only 10% of real-world agent success, while 90% is determined by the surrounding execution harness.
3. **Chapter 3: Spec-Driven Development (SDD) & Machine-Actionable Requirements** — Bridging human intent and agent determinism using Easy Approach to Requirements Syntax (EARS) and repository rule governance.
4. **Chapter 4: The Developer's Evolving Role — Conductor vs. Orchestrator** — Transitioning developer value from manual line-by-line coding to real-time interactive steering (Conducting) and asynchronous multi-agent delegation (Orchestrating).

---

## Primary Video Lecture: Google Just Dropped a Masterclass on Agentic Engineering

Watch this comprehensive video breakdown by AI educator **Cole Medin** before proceeding through the text chapters below. It analyzes Google's 51-page whitepaper (*The New SDLC With Vibe Coding*) and introduces the core tenets of modern harness engineering.

<div style="position: relative; padding-bottom: 56.25%; height: 0; overflow: hidden; max-width: 100%; border-radius: 8px; margin: 1.5rem 0;">
  <iframe style="position: absolute; top: 0px; left: 0px; width: 100%; height: 100%; border: 0px none currentcolor;" title="Google Just Dropped a Masterclass on Agentic Engineering — Cole Medin" src="https://www.youtube.com/embed/zbmuiaPuiNM" loading="lazy" allowfullscreen="allowfullscreen" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share"></iframe>
</div>

<div style="margin: 0.5rem 0 1.5rem 0; font-size: 0.95em;">
  <em>Video not displaying in Canvas? <a href="https://www.youtube.com/watch?v=zbmuiaPuiNM" target="_blank" rel="noopener noreferrer">Watch directly on YouTube: Google Just Dropped a Masterclass on Agentic Engineering (It's SO Good)</a></em>
</div>

### Video Chapters & Conceptual Timestamps:
- **0:00 — Introduction**: The paradigm shift from casual prompting to production agentic engineering.
- **2:15 — The New SDLC Whitepaper**: Deconstructing Google and Kaggle's landmark research publication.
- **5:30 — The Spectrum of AI Development**: Contrasting "vibe coding" with disciplined agentic workflows.
- **8:45 — The 10/90 Harness Rule**: Why 90% of autonomous performance lives in tools, rules, and context.
- **14:20 — The 80% Trap & The CapEx/OpEx Dilemma**: How rapid prototyping creates massive maintenance debt.
- **19:10 — Context Engineering & Progressive Disclosure**: Managing token hygiene and dynamic skill injection.
- **24:35 — The Conductor vs. The Orchestrator**: The two future archetypes of software developers.
- **29:50 — Conclusion & Engineering Takeaways**: Building reproducible agent systems.

---

## Authoritative References & Academic Citations

This curriculum is built directly upon foundational engineering publications from industry leaders:

1. **Google's New SDLC Whitepaper**:
   > **Osmani, A., Saboo, S., & Kartakis, S. (2026).** *The New SDLC With Vibe Coding: How AI Agents and Context Harnesses are Transforming the Software Development Life Cycle.* Published by Google & Kaggle.
2. **Anthropic's Agentic Systems Framework**:
   > **Erik S. & Barry Zhang (2024).** *Building Effective Agents.* Anthropic Engineering & Research. [anthropic.com/research/building-effective-agents](https://www.anthropic.com/research/building-effective-agents).
3. **Easy Approach to Requirements Syntax (EARS)**:
   > **Mavin, A., Wilkinson, P., Harwood, A., & Novak, M. (2009).** *Easy Approach to Requirements Syntax (EARS).* 17th IEEE International Requirements Engineering Conference (RE '09), Atlanta, GA, pp. 317-322.

---

## Chapter 1: The Collapse of Syntax & The Vibe Coding Trap

### 1.1 Programming as Translation: The Historical Friction
For seven decades, software engineering has essentially functioned as a two-stage cognitive translation process:
1. **Domain Understanding & Conceptual Abstraction**: The engineer analyzes a business or physical problem and designs an abstract logic flow (algorithms, data structures, state machines).
2. **Syntax Translation**: The engineer translates that abstract mental model into formal, highly unforgiving programming syntax (semicolons, curly braces, pointer arithmetic, type signatures, and boilerplate).

```
[Real-World Problem] ──> [Abstract Architecture] ──> [Syntax Translation (Friction Tax)] ──> [Executable Machine Code]
```

Historically, Computer Science and Software Engineering degree programs spent 70% to 80% of their instructional contact hours teaching students to overcome that second step: mastering syntax, debugging compile errors, and navigating boilerplate APIs.

### 1.2 The Collapse of Syntax
With modern large language models trained on tens of billions of lines of source code, **syntax translation is effectively solved**. As Google's whitepaper highlights, over **41% of all newly committed code across major repositories is generated by AI models**. When given a clear prompt, an LLM can emit syntactically flawless Python, TypeScript, or Go in milliseconds.

Because syntax is no longer a bottleneck, developer behavior has fundamentally shifted toward what Andrej Karpathy termed **"Vibe Coding"**:
> *"There's a new kind of coding I call 'vibe coding', where you entirely give in to the vibes, embrace every impatience, and forget that the code even exists. You just talk to the model, run what it gives you, and paste errors back until it works."*

### 1.3 The Vibe Coding Trap: Low CapEx, Astronomical OpEx
While vibe coding is an exhilarating experience for personal side-projects and rapid greenfield prototyping, it behaves like an unregulated payday loan in professional software engineering.

In business and economic terms, software costs fall into two categories:
- **Capital Expense (CapEx)**: The upfront cost to design, architect, and initially author a software component.
- **Operational Expense (OpEx)**: The ongoing cost to test, debug, refactor, patch, secure, and maintain that component over its operational lifespan.

```
+-----------------------------------------------------------------------------------+
| THE ECONOMIC CURVE OF VIBE CODING VS. AGENTIC ENGINEERING                          |
+-----------------------------------------------------------------------------------+
| Cost ($)                                                                          |
|   ^                                                                               |
|   |         /  VIBE CODING (Low CapEx, Exponential OpEx)                          |
|   |        /   (Hidden regressions, context drift, security flaws)               |
|   |       /                                                                       |
|   |      /                                                                        |
|   |     /      ----------------------------------------                           |
|   |    /       AGENTIC ENGINEERING (Higher CapEx, Predictable Flat OpEx)          |
|   |   /        (Spec-Driven, Automated Tests, Harness Governed)                   |
|   |  /                                                                            |
|   | /                                                                             |
|   +------------------------------------------------------------> Time in Production|
+-----------------------------------------------------------------------------------+
```

With vibe coding:
- **CapEx approaches near zero**: A developer prompts an LLM and receives 500 lines of working code in 30 seconds for $0.02 in tokens.
- **OpEx approaches infinity**: Because the developer never established formal requirements, boundary invariants, or unit test suites, the code is an ungrounded black box. When a regression appears six months later, no one knows why specific design decisions were made. 

### 1.4 Deconstructing "The 80% Trap"
Every developer who relies heavily on unstructured prompting experiences **The 80% Trap**:

```
[0% to 80% Progress] : Achieved in 30 Minutes via Prompting  ──> "This is the future!"
[80% to 100% Progress]: Stalled for 3 Weeks in Regression Loops ──> "Why does it keep breaking?"
```

Why does the agent hit an impenetrable wall at 80% completion?
1. **Compounding Context Degradation**: As the chat transcript grows to thousands of tokens, the LLM suffers from "lost-in-the-middle" attention dispersion. It forgets initial design rules and begins contradicting earlier assumptions.
2. **Whack-A-Mole Regressions**: Asking the agent to fix a bug in Module C causes it to rewrite Module A, breaking Module B in the process. Without a regression test harness, the agent operates blind.
3. **Absence of Ground Truth**: An LLM is an autoregressive token predictor. It has no intrinsic concept of correctness—only statistical plausibility. Without external verification (unit tests, AST compilers, type checkers), it will assert with absolute confidence that broken code is fully functional.

---

## Chapter 2: The 10/90 Harness Rule — Model vs. Execution Harness

### 2.1 The Core Equation of Agentic Engineering
When autonomous agents fail, junior developers instinctively blame the foundation model: *"We need to upgrade from a 70B parameter open-source model to a 400B frontier model!"* or *"We need the newest benchmark-topping checkpoint!"*

Google's research demonstrates that this intuition is fundamentally incorrect:

$$\text{Agent Performance} = \text{Model (10\%)} + \text{Harness (90\%)}$$

The underlying AI model provides the raw cognitive engine—parsing natural language semantics, proposing candidate logic, and formatting structured tokens. That capability is necessary, but represents only **10%** of what determines whether an agent successfully completes an enterprise engineering task.

The remaining **90% is the Harness**: the engineered environment, repository rule boundaries, tool schemas, sandboxed execution runtimes, and automated verification loops that constrain and guide the model.

```
+-----------------------------------------------------------------------------------+
| THE ANATOMY OF AN AGENTIC HARNESS (90% OF THE SYSTEM)                              |
+-----------------------------------------------------------------------------------+
|                                                                                   |
|  +-----------------------------------------------------------------------------+  |
|  | 1. REPOSITORY GOVERNANCE & BOUNDARIES                                       |  |
|  |    - AGENTS.md / .cursorrules: Explicit negative constraints & conventions   |  |
|  |    - Single Source of Truth pointers (CURRENT.md)                           |  |
|  |    - Monorepo Silo Sandboxes (Forbidding cross-directory file pollution)    |  |
|  +-----------------------------------------------------------------------------+  |
|                                       │                                           |
|                                       ▼                                           |
|  +-----------------------------------------------------------------------------+  |
|  | 2. CONTEXT ENGINEERING & PROGRESSIVE DISCLOSURE                             |  |
|  |    - Dynamic Skill Registries (.agents/skills/) instead of monolithic prompts|  |
|  |    - AST symbol indexers & targeted grep retrieval                          |  |
|  +-----------------------------------------------------------------------------+  |
|                                       │                                           |
|                                       ▼                                           |
|  +----------------------------------+ +-----------------------------------------+ |
|  | 3. RAW COGNITIVE CORE (10%)       | | 4. POKA-YOKE TOOL CONTRACTS (FAST-MCP)   | |
|  |    - Local: Qwen 2.5 Coder (7B)  | |    - Pydantic schema validation          | |
|  |    - Cloud: Google Gemini Flash  | |    - Targeted non-destructive diff patch | |
|  |    - Parametric reasoning        | |    - Prohibiting full-file rewrites      | |
|  +----------------------------------+ +-----------------------------------------+ |
|                                       │                                           |
|                                       ▼                                           |
|  +-----------------------------------------------------------------------------+  |
|  | 5. CLOSED-LOOP VERIFICATION & REGRESSION GATES                              |  |
|  |    - Isolated subprocess test runners (pytest / vitest)                     |  |
|  |    - AST syntax linting & type checks before committing changes              |  |
|  |    - Traceback reflection scratchpad (Max iteration retry bounds)          |  |
|  +-----------------------------------------------------------------------------+  |
|                                                                                   |
+-----------------------------------------------------------------------------------+
```

### 2.2 The Four Pillars of the Harness

#### Pillar 1: Repository Rules & Negative Constraints (`AGENTS.md`)
Models are naturally inclined toward "helpful overreach": if asked to fix a database query, an unconstrained agent might refactor the entire ORM schema, upgrade three major library versions, and delete uncommitted working tree changes.
A production harness provides **machine-actionable rules** that enforce negative constraints:
- *"Never rewrite an entire file; make targeted diff replacements only."*
- *"Never install unapproved third-party dependencies."*
- *"Never mark a task complete without executing and displaying the test command output."*

#### Pillar 2: Non-Destructive Tooling (Diff Patching vs. File Overwrite)
In early agent implementations, agents modified code by generating the complete contents of a file and overwriting it on disk. For a 500-line file where only one line needed changing, this introduced massive latency, blew token budgets, and frequently truncated the bottom half of the file.
Modern harnesses enforce **Poka-Yoke ("mistake-proof") tools**: the agent must submit exact line numbers and matching search chunks to apply targeted diffs.

#### Pillar 3: Context Hygiene & Progressive Disclosure
Dumping an entire project's documentation, API schemas, and historical code into a single system prompt leads to prompt bloat, high cost, and hallucination. 
As Google's paper explains, a well-engineered harness uses **progressive disclosure**: it exposes lightweight summaries and metadata headers first. Only when the agent explicitly invokes a specific domain tool or skill does the harness inject the detailed instructions into the active context window.

#### Pillar 4: Closed-Loop Automated Verification (The Feedback Loop)
Human engineers do not push code to production without running tests; agents should never be allowed to either. The harness executes automated test runners in an isolated sandbox subprocess. If tests fail, the exit code and stderr traceback are injected back into the agent's observation scratchpad, prompting a targeted fix.

---

## Chapter 3: Spec-Driven Development (SDD) & Machine-Actionable Requirements

### 3.1 Why Natural Language Fails Autonomous Agents
Casual conversational language is inherently ambiguous:
- *"Make the login system secure."* (What authentication scheme? What password entropy? What session timeout?)
- *"Make the UI responsive."* (What screen breakpoints? Desktop-first or mobile-first?)
- *"Optimize the data pipeline."* (Optimize for throughput, memory footprint, or query latency?)

When a human developer receives a vague prompt, they make assumptions based on tacit domain experience. When an LLM receives a vague prompt, it hallucinates plausible-sounding defaults that often clash with enterprise architecture.

**Spec-Driven Development (SDD)** solves this by enforcing written, unambiguous contracts *before* any implementation begins.

### 3.2 The EARS Requirements Standard
In modern agentic engineering, requirements are formulated using **EARS** (*Easy Approach to Requirements Syntax*), an international standard developed by Rolls-Royce and IEEE for mission-critical systems. EARS replaces unstructured prose with structured grammatical templates:

<table class="dp-table" style="width: 100%; border-collapse: collapse; margin: 1.5rem 0;">
  <thead>
    <tr style="background: #1e3a8a; color: #ffffff;">
      <th scope="col" style="padding: 0.75rem; text-align: left; border: 1px solid #cbd5e1;">EARS Pattern</th>
      <th scope="col" style="padding: 0.75rem; text-align: left; border: 1px solid #cbd5e1;">Grammar Template</th>
      <th scope="col" style="padding: 0.75rem; text-align: left; border: 1px solid #cbd5e1;">Agentic Engineering Example</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th scope="row" style="padding: 0.75rem; border: 1px solid #cbd5e1; font-weight: bold;">Ubiquitous (Always)</th>
      <td style="padding: 0.75rem; border: 1px solid #cbd5e1;"><code>The [system] shall [behavior]</code></td>
      <td style="padding: 0.75rem; border: 1px solid #cbd5e1;">The harness <strong>shall</strong> log all tool invocations with millisecond timestamps to <code>execution.log</code>.</td>
    </tr>
    <tr style="background: #f8fafc;">
      <th scope="row" style="padding: 0.75rem; border: 1px solid #cbd5e1; font-weight: bold;">Event-Driven (When)</th>
      <td style="padding: 0.75rem; border: 1px solid #cbd5e1;"><code>WHEN [trigger], the [system] shall [action]</code></td>
      <td style="padding: 0.75rem; border: 1px solid #cbd5e1;"><strong>WHEN</strong> a unit test fails, the agent <strong>shall</strong> extract the failure traceback and re-evaluate the targeted patch.</td>
    </tr>
    <tr>
      <th scope="row" style="padding: 0.75rem; border: 1px solid #cbd5e1; font-weight: bold;">State-Driven (While)</th>
      <td style="padding: 0.75rem; border: 1px solid #cbd5e1;"><code>WHILE [in state], the [system] shall [behavior]</code></td>
      <td style="padding: 0.75rem; border: 1px solid #cbd5e1;"><strong>WHILE</strong> running in offline mode, the harness <strong>shall</strong> route all inference calls strictly to local Ollama.</td>
    </tr>
    <tr style="background: #f8fafc;">
      <th scope="row" style="padding: 0.75rem; border: 1px solid #cbd5e1; font-weight: bold;">Unwanted / Error (If-Then)</th>
      <td style="padding: 0.75rem; border: 1px solid #cbd5e1;"><code>IF [unwanted event], THEN the [system] shall [mitigation]</code></td>
      <td style="padding: 0.75rem; border: 1px solid #cbd5e1;"><strong>IF</strong> the retry count exceeds 3 iterations, <strong>THEN</strong> the harness <strong>shall</strong> abort execution and raise an EscalationReport.</td>
    </tr>
    <tr>
      <th scope="row" style="padding: 0.75rem; border: 1px solid #cbd5e1; font-weight: bold;">Optional Feature (Where)</th>
      <td style="padding: 0.75rem; border: 1px solid #cbd5e1;"><code>WHERE [feature enabled], the [system] shall [behavior]</code></td>
      <td style="padding: 0.75rem; border: 1px solid #cbd5e1;"><strong>WHERE</strong> <code>GEMINI_API_KEY</code> is set in environment, the system <strong>shall</strong> prioritize Google Gemini Flash.</td>
    </tr>
  </tbody>
 </table>

### 3.3 The 4-Stage Iteration Lifecycle
By pairing EARS requirements with a strict 4-stage lifecycle, engineering teams eliminate the 80% Trap:

```
[1. Specify] ──────> [2. Plan] ──────> [3. Tasks] ──────> [4. Implement & Verify]
 (spec.md)            (plan.md)          (tasks.md)        (pytest & audit evidence)
```

1. **Stage 1: Specify (`spec.md`)**: Define target persona, problem statement, EARS requirements, and explicit out-of-scope boundaries. Stop for human review.
2. **Stage 2: Plan (`plan.md`)**: Map requirements to architectural patterns, schema contracts, and ADR invariants. Stop for human review.
3. **Stage 3: Tasks (`tasks.md`)**: Decompose plan into ordered, bite-sized tasks (15–30 min increments) with runnable `Check:` commands.
4. **Stage 4: Implement & Verify**: Implement one task at a time, execute checks, and conduct an audit against every EARS requirement.

---

## Chapter 4: The Developer's Evolving Role — Conductor vs. Orchestrator

### 4.1 Moving Upstream: From Syntax Author to System Architect
As AI agents assume responsibility for line-by-line syntax generation, human engineers are not being replaced; their responsibilities are moving **upstream**. 

Writing syntax was the lowest-leverage activity in software engineering. High-leverage activities have always been:
- **System boundary definition**: What should the software do, and what must it never do?
- **Domain trade-off evaluation**: Latency vs. memory, consistency vs. availability, CapEx vs. OpEx.
- **Verification & quality gating**: Proving empirically that a system behaves deterministically under stress.

Google's whitepaper categorizes the modern developer into two operational archetypes:

```
+-----------------------------------------------------------------------------------+
| THE TWO ARCHETYPES OF THE MODERN AGENTIC SOFTWARE ENGINEER                         |
+-----------------------------------------------------------------------------------+
|                                                                                   |
|  1. THE CONDUCTOR (Synchronous, Real-Time Interactive Steering)                    |
|     - Engages in real-time "sparring" with the agent during design & specification|
|     - Provides immediate guardrail corrections when the agent veers off course    |
|     - Conducts pair-programming reviews, checking diffs before applying changes   |
|     - Mental Model: Like an orchestra conductor directing individual musicians    |
|                                                                                   |
|  2. THE ORCHESTRATOR (Asynchronous, Multi-Agent Delegation & Systems Engineering)  |
|     - Designs the factory floor: builds the harness, rules, and tool servers      |
|     - Delegates long-running, multi-step tasks to autonomous background agents    |
|     - Establishes benchmark suites, pass@k evaluation metrics, and regression gates|
|     - Monitors token economics, inference budgets, and telemetry logs            |
|     - Mental Model: Like a manufacturing plant manager designing the assembly line|
|                                                                                   |
+-----------------------------------------------------------------------------------+
```

### 4.2 The Conductor in Practice
When acting as a Conductor, the engineer works tightly in the loop:
- **One Question at a Time**: Instead of letting the agent output a monolithic 2,000-line draft, the Conductor asks focused questions, challenging assumptions on edge cases.
- **Sparring & Stress-Testing**: The Conductor tests the agent's proposed architecture: *"What happens if the database connection drops during step 3?"* or *"How will this scale if traffic spikes 100x?"*
- **Surgical Steering**: The Conductor inspects the agent's plan before execution, pruning unnecessary steps and refining constraints.

### 4.3 The Orchestrator in Practice
When acting as an Orchestrator, the engineer builds the scaffolding that allows agents to operate autonomously with safety:
- **Standardized Protocols**: Implementing Model Context Protocol (MCP / FastMCP) servers so agents interact through strongly typed Pydantic contracts rather than fragile ad-hoc API wrappers.
- **Automated Regression Harnesses**: Constructing CI/CD pipelines where candidate agent patches are automatically checked against comprehensive unit and integration test matrices.
- **Token Hygiene & Telemetry**: Tracking cost-per-task, context window consumption, and token degradation across agent runs.

---

## Chapter Summary & Lab Preview

In this unit's applied lab, you will step into the shoes of both the Conductor and the Orchestrator:
- You will inspect an unstructured "vibe-coded" script that breaks silently on edge cases.
- You will construct an **Automated Spec-Driven Development (SDD) Agent Harness** in Python (`starter_sdd_harness.py`).
- Your harness will ingest an EARS specification, formulate a plan, generate candidate functions, execute a test suite in an isolated subprocess, and iteratively patch syntax/logic defects until 100% of assertions pass—using either Google Gemini or local Ollama.
