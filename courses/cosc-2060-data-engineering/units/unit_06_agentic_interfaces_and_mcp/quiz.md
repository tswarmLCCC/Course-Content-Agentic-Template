# Unit 06 Knowledge Check: Agentic AI Interfaces & Model Context Protocol (MCP)

### Question 1
What is the primary architectural purpose of Anthropic's Model Context Protocol (MCP)?
* A) To replace Python with a new proprietary agent programming language.
* B) To provide an open, standardized protocol allowing AI applications (like Claude or custom agents) to securely connect to external tools, databases, and context servers.
* C) To train foundational LLMs from scratch on local laptops.
* D) To automatically write student essays without user input.

### Question 2
In the Model Context Protocol (MCP), what are the three core primitives exposed by an MCP server to an AI client?
* A) Tables, Rows, and Columns.
* B) Tools (callable functions), Resources (data feeds/files), and Prompts (reusable templates).
* C) Sockets, Ports, and IP addresses.
* D) Users, Passwords, and Tokens.

### Question 3
How does an MCP server describe callable tools so an LLM can understand when and how to invoke them?
* A) By compiling the tool into an executable Windows `.exe` file.
* B) By publishing a declarative JSON Schema specifying the tool's name, description, required parameters, and data types.
* C) By sending an audio recording of the instructor explaining the tool.
* D) By writing raw assembly instructions into system memory.

### Question 4
Why is giving an autonomous AI agent unrestricted, direct SQL access (`execute(user_query)`) considered an extreme security vulnerability?
* A) Because SQL syntax is too difficult for AI models to understand.
* B) Prompt injection attacks or hallucinations can cause the agent to execute destructive DDL (`DROP TABLE`), exfiltrate confidential data, or consume massive cloud compute.
* C) Because SQL databases do not support network connections.
* D) Because LLMs only know how to communicate in YAML.

### Question 5
In defensive agentic engineering, what is the "Principle of Least Privilege" when designing MCP database tools?
* A) Exposing read-only, parameterized analytical tools with strict schema filters rather than open-ended administrative write access.
* B) Running all tools under the system root administrator account.
* C) Disabling error logging to make the tools run faster.
* D) Granting all tools the ability to modify server firewall settings.

### Question 6
What transport mechanism does MCP commonly use for local command-line and desktop AI integrations?
* A) Bluetooth Low Energy (BLE).
* B) Standard Input/Output (`stdio`) communication transmitting JSON-RPC 2.0 messages.
* C) Floppy disk transfers.
* D) Unencrypted FTP file transfers.

### Question 7
When an AI agent calls an MCP tool with invalid arguments (e.g. passing a string to an integer parameter), how should the MCP server respond?
* A) It should crash the server process immediately.
* B) It should return a structured JSON-RPC error payload describing the exact validation failure so the agent can self-correct its parameters.
* C) It should delete the database to prevent further errors.
* D) It should silently invent random data to fulfill the request.

### Question 8
What is the primary danger of exposing too many tools (e.g., 50+ detailed functions) to an AI agent simultaneously?
* A) The computer's monitor will begin flickering.
* B) Context window bloat, increased latency, higher inference cost, and a higher probability of tool hallucination or incorrect tool selection by the model.
* C) The Python interpreter will automatically uninstall itself.
* D) The tool descriptions will cause network cables to overheat.

### Question 9
Why must production MCP servers implement deterministic structured audit logging for every tool invocation?
* A) To meet regulatory compliance, reconstruct agent decision trajectories, and monitor tool latency, errors, and input parameters.
* B) Because MCP servers cannot function without printing text to a physical paper printer.
* C) To permit students to share answers during examinations.
* D) To bypass software licensing verification.

### Question 10
In the Model Context Protocol, what is the role of an MCP "Resource" compared to an MCP "Tool"?
* A) Resources are active functions with side effects; Tools are passive read-only text files.
* B) Resources provide passive, contextual data (like file contents, database logs, or schemas) for reading; Tools are executable functions that take arguments and perform actions.
* C) Resources can only be written in C++; Tools can only be written in HTML.
* D) Resources and Tools are 100% identical and have no functional difference.

## Answer Key
| Question # | Correct Answer | Concept Tested & Rationale |
| :--- | :--- | :--- |
| **1** | **B** | MCP standardizes the communication layer between client AI hosts and backend servers providing context, live data, and executable actions. |
| **2** | **B** | The MCP specification organizes capabilities into three primitives: Prompts (context templates), Resources (data payloads), and Tools (functions). |
| **3** | **B** | Tool signatures use standardized JSON Schema definitions; models parse descriptions and argument types to synthesize structured tool calls. |
| **4** | **B** | Naked SQL execution exposes the database to prompt injection, malicious deletion, and resource-exhausting Cartesian join attacks. |
| **5** | **A** | Least privilege restricts agents to parameter-constrained read/write endpoints with strict boundaries rather than unbounded administrative SQL privileges. |
| **6** | **B** | Standard I/O (stdio) with newline-delimited JSON-RPC messages is the default lightweight transport for local MCP client-server communication. |
| **7** | **B** | Informative error responses return validation messages allowing the LLM's reasoning loop to analyze the failure and retry with valid arguments. |
| **8** | **B** | Large toolsets consume valuable context window tokens, inflate latency, and confuse the model's selector attention, causing improper tool choice. |
| **9** | **A** | Immutable audit logs track inputs, outputs, timestamps, and model IDs, providing observability and forensic replayability for agent behavior. |
| **10** | **B** | Resources represent data attachments (read-only documents, logs, or schemas), whereas Tools represent actions with callable parameters and side effects. |
