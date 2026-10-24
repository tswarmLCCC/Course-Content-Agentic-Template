# Unit 06 Overview: Agentic AI Interfaces & Model Context Protocol (MCP)

Autonomous AI agents require standardized, secure mechanisms to inspect databases and invoke tools. Unit 06 explores the cutting edge of AI infrastructure: implementing the Model Context Protocol (MCP) to transform static analytical pipelines into intelligent, tool-calling agent backends.

---

## Weekly Contact Hour Budget (300 Minutes Total)
- **Conceptual Study & Readings (150 min)**: Deep dive into Model Context Protocol (MCP) architecture, JSON-RPC protocol transport, tool schemas, and safety boundaries.
- **Asynchronous Preparation & Drills (60 min)**: Model deterministic tool definitions and audit prompt injection defenses.
- **Hands-on Engineering Lab (90 min)**: Build a production MCP Fleet Maintenance Tool Server.

---

## Measurable Learning Objectives
By the end of this unit, you will be able to:
1. **Implement** standard JSON-RPC tool endpoints adhering to the Model Context Protocol (MCP) standard.
2. **Expose** analytical database queries and anomaly checks as callable agent tools with explicit parameter contracts.
3. **Construct** sandboxed execution safeguards preventing unauthorized DDL or destructive mutations by autonomous LLMs.
4. **Audit** agent tool execution logs with deterministic structured telemetry.

---

## Weekly Learning Roadmap & Deliverables

Follow the sequential module workflow in Canvas to complete this unit:

1. **Step 1: Required Readings & Reference Architecture**  
   Study Model Context Protocol (MCP) specifications, JSON-RPC 2.0 framing, tool schema contracts, and AI safety boundaries in the module reading.
2. **Step 2: Diagnostic Drills & Syntax Checks**  
   Complete the asynchronous concept checks, JSON-RPC message validation, and sandboxing guardrail drills before tackling the lab.
3. **Step 3: Applied Engineering Lab & Starter Code**  
   Build and test your secure logistics MCP tool server (`lab6_starter.py`) adhering to the 100-point rubric, then submit your script to the assignment dropbox.
4. **Step 4: Knowledge Check & Concept Verification**  
   Take the untimed 10-question formative assessment in Canvas (up to 3 attempts, highest score kept) to lock in key terminology and mental models.
