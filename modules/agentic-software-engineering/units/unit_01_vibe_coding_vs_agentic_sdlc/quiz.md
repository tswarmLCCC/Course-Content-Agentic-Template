Quiz Title: Unit 01 Knowledge Check: Vibe Coding vs. Agentic SDLC & The 10/90 Harness Rule
Quiz Description: Formative assessment testing conceptual mastery of the 10/90 Harness Rule, EARS requirements syntax, software economics (CapEx vs. OpEx), and the developer's role as Conductor and Orchestrator. Up to 3 attempts allowed; highest score kept.

1. According to Google's whitepaper "The New SDLC With Vibe Coding", what does the "10/90 Rule" state regarding AI agent performance?
*a) The underlying foundation model accounts for approximately 10% of real-world success, while 90% relies on the surrounding execution harness (rules, context, tools, and verification).
b) Developers spend 10% of their time writing code and 90% of their time running unit tests.
c) 10% of developers use prompt engineering, while 90% rely entirely on autonomous multi-agent swarms.
d) Foundation models generate 90% of code with 10% latency overhead compared to human programmers.

2. What is the fundamental operational difference between "Vibe Coding" and "Agentic Engineering"?
*a) Vibe coding relies on unstructured natural language prompts and ad-hoc error pasting, whereas agentic engineering uses formal specifications, machine-actionable rules, and automated verification loops.
b) Vibe coding uses Python, whereas agentic engineering is restricted to compiled languages like Rust or C++.
c) Vibe coding requires local GPU hardware, while agentic engineering strictly uses cloud APIs.
d) Vibe coding is automated, whereas agentic engineering requires manual human approval for every line of code.

3. In software economic terms, why does casual "vibe coding" create an unsustainable debt curve?
*a) It offers deceptively low upfront capital expense (CapEx) but creates astronomical ongoing operational maintenance costs (OpEx) due to ungrounded regressions and missing architectural boundaries.
b) Cloud API token costs for generating initial code exceed the cost of hiring human senior software engineers.
c) It requires expensive enterprise licenses for IDE plugins before any prototype can be built.
d) It increases upfront CapEx by 500% while reducing ongoing OpEx to zero.

4. What is the primary cause of the "80% Trap" in generative AI development?
*a) LLMs rapidly produce plausible first drafts, but compounding error rates, context degradation, and lack of deterministic test feedback make resolving the final 20% of edge cases exponentially difficult.
b) Foundation models are intentionally rate-limited by cloud providers once an application reaches 80% completion.
c) Automated test runners are unable to compile Python code that exceeds 80 lines.
d) Human developers lose motivation after completing 80% of a feature.

5. Which of the following best exemplifies an "Ubiquitous" requirement using Easy Approach to Requirements Syntax (EARS)?
*a) The authentication service shall log all failed login attempts with timestamp and source IP to the audit database.
b) WHEN a user submits a valid token, the system shall redirect to the dashboard.
c) WHILE in maintenance mode, the system shall display a 503 Service Unavailable page.
d) IF the database connection drops, THEN the server shall retry connection every 5 seconds.

6. In EARS syntax, how is an "Event-Driven" requirement structured?
*a) WHEN [trigger event occurs], the [system] shall [response/action].
b) WHILE [in specific state], the [system] shall [behavior].
c) IF [unwanted condition], THEN the [system] shall [mitigation].
d) WHERE [optional feature enabled], the [system] shall [behavior].

7. A requirement states: "IF memory usage exceeds 90%, THEN the worker agent shall pause task execution and flush cached embeddings." Under EARS taxonomy, what type of requirement is this?
*a) Unwanted Behavior / Error Handling
b) Ubiquitous
c) Event-Driven
d) State-Driven

8. What is the primary role of machine-actionable repository governance files (such as `AGENTS.md` or `.cursorrules`) in an agentic harness?
*a) To establish explicit boundaries, coding standards, and negative constraints that prevent the model from overreaching or modifying forbidden files.
b) To compile Python source code into native machine assembly language.
c) To provide training datasets for fine-tuning open-source foundation models.
d) To measure the frames-per-second rendering rate of web user interfaces.

9. Why is a targeted diff-patching tool (`replace_chunk`) superior to a full-file overwrite tool (`write_file`) in an autonomous coding harness?
*a) Diff patching prevents output token truncation on long files, reduces inference latency, and eliminates accidental deletion of unrelated code.
b) Diff patching allows the model to bypass unit test verification.
c) Full-file overwrite tools cannot be executed inside Linux containers.
d) Diff patching encrypts source code using SHA-256 before writing to disk.

10. How does the manufacturing principle of "Poka-Yoke" apply to agent tool design?
*a) Designing tool interfaces with strict validation (e.g., verifying exact string matches and unique line occurrences) so that accidental file corruption is structurally impossible.
b) Allowing agents to run commands as root without authentication to accelerate deployment.
c) Forcing agents to generate code in Japanese to improve syntax efficiency.
d) Limiting all agent responses to exactly 100 tokens.

11. What distinguishes the developer's role as a "Conductor" from that of an "Orchestrator"?
*a) A Conductor engages in synchronous, real-time steering and sparring during design, while an Orchestrator designs the asynchronous factory floor, tool servers, and automated evaluation pipelines.
b) A Conductor writes unit tests, while an Orchestrator writes frontend HTML templates.
c) A Conductor uses proprietary cloud models, while an Orchestrator uses local open-source models.
d) A Conductor works solo, while an Orchestrator must manage human engineering teams of 20+ people.

12. A software team upgrades their coding agent from a 70B parameter model to a 400B parameter model, but the agent still repeatedly overwrites helper utilities and introduces syntax errors. What is the root cause?
*a) The execution harness lacks boundary rules and automated test-feedback gates; a larger model cannot compensate for a missing harness.
b) The 400B parameter model was trained on too few lines of Python code.
c) The team failed to convert their codebase to JavaScript.
d) Larger foundation models have no capacity for syntactic reasoning.

13. In the 4-Stage Iteration Lifecycle (Specify -> Plan -> Tasks -> Implement & Verify), why must the "Specify" stage occur before any code generation?
*a) To establish deterministic ground truth and eliminate ambiguity in human intent before an agent begins generating candidate solutions.
b) Because Python requires a compiled specification file to run.
c) To satisfy Canvas LMS course cartridge packaging standards.
d) Because foundation models cannot read planning documents.

14. What occurs during the "Closed-Loop Automated Verification" stage of a modern agentic harness?
*a) The harness executes unit tests in an isolated sandbox and feeds any failure tracebacks back into the agent's observation scratchpad for targeted self-healing.
b) The harness emails the project manager whenever an agent makes a syntax error.
c) The foundation model self-evaluates its own code using a single-turn prompt asking "Is this code correct?".
d) The agent halts permanently on the first failed assertion and requires human intervention.

15. What is "Progressive Disclosure" in context engineering?
*a) Exposing lightweight summaries and skill metadata headers first, loading full documentation only when an agent explicitly invokes that specific domain tool.
b) Printing all secret environment variables to the terminal during startup.
c) Gradually increasing the temperature parameter of the model during inference.
d) Dumping an entire 500-page enterprise API manual into the initial system prompt.
