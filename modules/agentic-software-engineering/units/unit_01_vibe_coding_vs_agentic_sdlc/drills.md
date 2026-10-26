# Unit 01: Formative Self-Check Drills & Conceptual Exercises

Test your understanding of **Vibe Coding, The 10/90 Harness Rule, Spec-Driven Development (SDD), and Conductor vs. Orchestrator Roles** before attending the synchronous lab session.

Complete each scenario independently, then click the collapsible card to reveal the expert architectural breakdown and solution.

---

### Drill 1: The 10/90 Rule in Practice
**Scenario:**  
A software startup notices that their AI coding agent frequently introduces regressions into their production codebase—it accidentally deletes environment variables, overwrites helper functions, and introduces deprecated API parameters. The lead engineer suggests upgrading their model from a 70B parameter open-source model to an expensive 400B parameter proprietary model.

**Question:**  
Under Google's **10/90 Harness Rule**, will upgrading the foundation model resolve these issues? Why or why not, and what specific architectural components should the engineering team build instead?

<details>
<summary><strong>View Architectural Analysis &amp; Solution</strong></summary>

**Analysis:**  
**No, upgrading the foundation model will not solve these regressions.**

According to the 10/90 Harness Rule:
$$\text{Agent System Success} = \text{Model (10\%)} + \text{Harness (90\%)}$$

The underlying AI model accounts for only ~10% of agent effectiveness—namely raw semantic parsing and token prediction. Upgrading from 70B to 400B parameters makes the model slightly better at complex reasoning, but does **not** give it:
1. **Repository Boundary Governance**: Without an `AGENTS.md` file or explicit negative constraints, even a 400B model will happily overwrite helper functions or delete environment variables in its attempt to be "helpful."
2. **Non-Destructive Tooling**: If the agent's file modification tool is a crude full-file overwrite (`write_file`) rather than a targeted diff patcher (`replace_file_content`), the agent will continue truncating code and wiping existing helper methods.
3. **Closed-Loop Verification**: If the agent does not receive automated linter errors or unit test failures back in its context scratchpad, it cannot catch its own regressions before declaring a task complete.

**Solution:** The team must engineer the **Harness (the 90%)**:
- Enforce strict repository rules (`AGENTS.md`) prohibiting full-file rewrites and deletion of environment variables.
- Replace full-file write tools with targeted diff-replacement tools that validate line numbers.
- Add an automated pre-commit test runner hook that rejects any agent output that fails `pytest` or `ruff` linting.
</details>

---

### Drill 2: Calculating the CapEx vs. OpEx Debt Curve
**Scenario:**  
Two engineering teams are tasked with building a customer notification microservice:
- **Team Alpha ("Vibe Coders")**: Types loose conversational prompts into an AI assistant, receives 400 lines of generated code in 30 minutes, tests it manually with two curl commands, and commits it directly to the staging branch.
- **Team Beta ("Agentic Engineers")**: Spends 45 minutes writing an EARS specification document (`spec.md`), defining an implementation plan (`plan.md`), configuring repository rules, and writing automated unit test assertions *before* letting an agent generate the code.

**Question:**  
Compare the Capital Expense (CapEx) and Operational Expense (OpEx) of Team Alpha versus Team Beta over the next 12 months in production.

<details>
<summary><strong>View Architectural Analysis &amp; Solution</strong></summary>

**Analysis:**  
- **Team Alpha (Vibe Coding)**:
  - **CapEx (Initial Cost)**: Extremely low (~0.5 hours of human developer time + pennies in AI tokens).
  - **OpEx (Ongoing Maintenance Cost)**: **Astronomically high.** Because there is no specification, no negative constraints, and no test harness, the code is an ungrounded black box. When edge cases occur in production (e.g., rate limits, malformed payloads, network timeouts), Team Alpha will spend dozens of hours debugging mysterious crashes. Each time an agent is prompted to fix a bug, it will cause regressions in other functions ("The 80% Trap").
- **Team Beta (Agentic Engineering)**:
  - **CapEx (Initial Cost)**: Moderate (~1.5 hours of human developer time to author the spec, plan, and test suite).
  - **OpEx (Ongoing Maintenance Cost)**: **Predictable and flat.** Because the code is governed by an explicit EARS contract and backed by automated test suites, any future changes or automated agent patches must pass all regression assertions before landing in production.

**Takeaway:** Vibe coding offers immediate gratification at the cost of crippling long-term maintenance debt. Agentic engineering requires higher upfront rigor to guarantee near-zero operational maintenance.
</details>

---

### Drill 3: EARS Syntax Classification & Reformulation
**Scenario:**  
A junior product manager hands you the following informal, unstructured prompt:
> *"The agent should make sure payments over $1,000 require admin approval, and if the fraud score is higher than 85 it needs to be blocked completely. Also log everything to PostgreSQL."*

**Question:**  
Decompose and rewrite this requirement into three formal, machine-actionable **EARS** statements:
1. One Ubiquitous requirement
2. One Event-Driven requirement
3. One Unwanted/Error (If-Then) requirement

<details>
<summary><strong>View Architectural Analysis &amp; Solution</strong></summary>

**Formal EARS Reformulation:**

1. **Ubiquitous (Always):**
   - `REQ-01`: The payment gateway **shall** log all transaction attempts with timestamp, transaction ID, and client IP to the PostgreSQL audit ledger.
2. **Event-Driven (When):**
   - `REQ-02`: **WHEN** a payment request amount exceeds $1,000.00 USD, the payment gateway **shall** pause transaction execution and place the state in `PENDING_ADMIN_APPROVAL`.
3. **Unwanted Behavior (If-Then):**
   - `REQ-03`: **IF** the fraud risk score exceeds 85, **THEN** the payment gateway **shall** immediately reject the transaction, return an `HTTP 403 Forbidden` error, and notify the security operations center.

**Why this matters for agents:** A language model given the original unstructured prompt might allow payments over $1,000 to process without an admin if the fraud score is low. The EARS syntax makes boundary conditions mathematically unambiguous.
</details>

---

### Drill 4: Conductor vs. Orchestrator Operational Decisions
**Scenario:**  
For each of the following engineering tasks, identify whether the developer is acting primarily as a **Conductor** (interactive, real-time steering) or an **Orchestrator** (asynchronous delegation & systems engineering):

1. An engineer observes an agent generating candidate functions in real time, interrupts the process to clarify an ambiguous edge case, and guides the agent toward a specific caching algorithm.
2. An engineer designs an automated GitHub Actions CI/CD workflow where three background agents independently run AST linters, execute unit test matrices, and generate security vulnerability reports on incoming pull requests.
3. An engineer conducts a sparring session with an agent, answering multiple-choice trade-off questions to align on database indexing before any code is generated.
4. An engineer writes a Model Context Protocol (FastMCP) server that exposes sanitized SQLite queries and terminal sandboxes to a pool of autonomous worker agents.

<details>
<summary><strong>View Architectural Analysis &amp; Solution</strong></summary>

**Classification & Rationale:**

1. **Conductor**: The engineer is interacting synchronously, providing real-time feedback and steering the agent mid-flight like a musical conductor guiding a soloist.
2. **Orchestrator**: The engineer has designed the "factory floor"—an asynchronous multi-agent pipeline governed by automated evaluation gates.
3. **Conductor**: The engineer is actively engaging in real-time sparring, shaping requirements and pruning architectural paths through interactive dialogue.
4. **Orchestrator**: The engineer is building the execution harness (tool schemas, protocols, sandboxes) that enables autonomous agents to operate safely without direct human oversight.
</details>

---

### Drill 5: Non-Destructive Tooling & The "Poka-Yoke" Principle
**Scenario:**  
An agentic coding harness allows agents to call either `overwrite_file(path, new_content)` or `replace_chunk(path, start_line, end_line, target_content, replacement_content)`. An agent tasked with adding a single logging statement to a 1,200-line configuration file calls `overwrite_file`.

**Question:**  
What three distinct failure modes are introduced by calling `overwrite_file`, and how does enforcing `replace_chunk` adhere to the **Poka-Yoke** (mistake-proofing) manufacturing principle?

<details>
<summary><strong>View Architectural Analysis &amp; Solution</strong></summary>

**Failure Modes of `overwrite_file`:**
1. **Token Window Truncation**: If the file is 1,200 lines long, emitting the entire file may exceed the model's output token limit (typically 4,096 or 8,192 tokens), silently truncating the bottom third of the file on disk.
2. **Silent Regression & Drift**: In the process of re-generating 1,200 lines, the model may subtly alter unrelated function signatures, remove comments, or introduce indentation syntax errors.
3. **High Latency & Token Cost**: Generating 1,200 lines of code requires ~3,000 output tokens and takes 15–30 seconds. Replacing a single chunk takes ~50 output tokens and completes in 500 milliseconds.

**The Poka-Yoke Principle:**  
Poka-Yoke is an industrial engineering term meaning "mistake-proofing"—designing a system such that errors are structurally impossible to commit. By removing `overwrite_file` from the agent's available tools and requiring `replace_chunk` with exact substring matching, the harness makes accidental file truncation impossible. If the agent's target substring does not exactly match the file content, the harness immediately errors before touching disk.
</details>
