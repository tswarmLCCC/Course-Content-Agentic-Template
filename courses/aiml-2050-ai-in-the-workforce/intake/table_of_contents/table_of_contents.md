# Intel Curriculum: Introduction to Agentic AI
## Ingested Table of Contents & Module Structure

> **Source Document**: `[Table of Contents] Introduction to Agentic AI.pptx`  
> **Source Provider**: Intel Digital Readiness Programs  
> **Total Raw Footprint**: 20 Modules + 5 Milestone Projects = 116 Hours of Learning Experiences  
> **Target Consolidation**: AIML 2050 (8 Weeks @ 6.0 Contact Hours/Week = 48 Contact Hours Total)

---

## 1. High-Level Course Architecture (5 Categories & 20 Modules)

```
Category 1: Agentic AI in Society (16 hrs)
├── Module 01: Demystifying Agentic AI (4h)
├── Module 02: Societal Impact of Agentic AI (4h)
├── Module 03: Agentic AI Ethics (4h)
└── Module 04: Project – Building the Case for a Responsible Agentic AI Solution (4h)

Category 2: Agentic AI in the Workplace (22 hrs)
├── Module 05: Working with AI Agents (Vertical vs Horizontal Agents) (4h)
├── Module 06: Using Agentic Tools for the Workplace (6h)
├── Module 07: Agentic AI Prototyping (6h)
└── Module 08: Project – Building a Business Solution Foundation (6h)

Category 3: Building AI Agents (No-Code) (32 hrs)
├── Module 09: Basic Agents (GPTs, Gems, Copilot Agents) (12h)
├── Module 10: Building Agents with Workflow Automation & Orchestration Tools – I (Relay.app, Lindy.ai) (6h)
├── Module 11: Building Agents with Workflow Automation & Orchestration Tools – II (n8n, Make, Zapier, MCP) (6h)
└── Module 12: Project – Build a No-Code Multi-Agent System (8h)

Category 4: Building AI Agents (Code) (26 hrs)
├── Module 13: Agentic Building Blocks with LangChain (6h)
├── Module 14: Long-Running Agents with LangGraph (6h)
├── Module 15: Governance for Autonomous Agents with LangSmith (6h)
└── Module 16: Project – Build Code Based Agent (8h)

Category 5: Running Local Agents (20 hrs)
├── Module 17: Hardware for Local Agents (CPU, GPU, NPU, RAM, VRAM) (4h)
├── Module 18: Software for Local Models (Ollama, Docker, OpenVINO, SQLite, FAISS) (4h)
├── Module 19: Sovereign Local AI Agent (AI Sovereignty, OpenVINO Model Server, SKILL.md) (4h)
└── Module 20: Project – Build a Local Agent (8h)
```

---

## 2. In-Depth Module Descriptions & Learning Outcomes

### Category 1: Agentic AI in Society (Modules 1–4)
| Module | Duration | Description | Target Learning Outcomes |
|---|:---:|---|---|
| **1. Demystifying Agentic AI** | 4h | Introduces Agentic AI vs automation, traditional AI, and GenAI. Autonomy, adaptability, contextual decision-making. Human role as supervisor, partner, or orchestrator. | Define Agentic AI; distinguish from automation/GenAI; identify key traits; describe organizational flow; understand human-AI collaboration shift. |
| **2. Societal Impact of Agentic AI** | 4h | Social, economic, cultural implications. Job roles, skills gaps, value chain disruption, sectoral adoption trends. | Analyze industry/labor market impacts; identify emerging competencies; evaluate sector trends and value chain transformation. |
| **3. Agentic AI Ethics** | 4h | Transparency, explainability, fairness, accountability. EU AI Act, NIST AI RMF, practical oversight, human-in-the-loop systems. | Identify ethical risks; apply responsible AI principles; describe governance frameworks (NIST, EU); discuss practical human oversight. |
| **4. Project – Building the Case for a Responsible Agentic AI Solution** | 4h | Realistic scenario designing end-to-end agentic proposal: use case, stakeholders, As-Is/To-Be workflows, NIST RMF alignment, 5–7 min video pitch. | Identify adoption barriers; apply change management (stakeholder mapping, phased rollout); deliver structured proposal video. |

### Category 2: Agentic AI in the Workplace (Modules 5–8)
| Module | Duration | Description | Target Learning Outcomes |
|---|:---:|---|---|
| **5. Working with AI Agents (Vertical vs Horizontal)** | 4h | Vertical (domain-specific) vs horizontal (cross-workflow) agents. Matching agents to business functions. Success metrics: ROI, cycle time, error rates. | Distinguish vertical vs horizontal agents; map agents to value streams; evaluate organizational readiness (data, change appetite). |
| **6. Using Agentic Tools for the Workplace** | 6h | Surveys mainstream productivity platforms with agentic features (email, docs, CRM, meetings). Role-based adoption playbook and change management. | Identify high-ROI workplace scenarios; apply role-based adoption; build lightweight tracker for time savings, quality, and adoption. |
| **7. Agentic AI Prototyping** | 6h | Rapid prototyping from idea to deployable prototype. Prompt crafting, real-time elements (APIs, databases), sharing for stakeholder feedback. | Compare prototyping tools; craft prompts to iteratively build prototypes; deploy and share live prototypes; integrate APIs; apply safeguards. |
| **8. Project – Building a Business Solution Foundation** | 6h | Design small business unit/service with AI agents: value prop, target customer, workflows, governance (NIST/ISO), live prototype demo during pitch. | Design & present business concept with working prototype; defend architectural choices; document governance; communicate commercial viability. |

### Category 3: Building AI Agents (No-Code) (Modules 9–12)
| Module | Duration | Description | Target Learning Outcomes |
|---|:---:|---|---|
| **9. Building Basic Agents (GPTs, Gems, Copilot Agents)** | 12h | OpenAI Custom GPTs, Google Gemini Gems, Microsoft Copilot Studio. Document context handling, external actions, baseline governance. | Compare GPTs, Gems, and Copilot; configure basic context-grounded agent; apply governance (human oversight, permissions, logging). |
| **10. Workflow Automation & Orchestration – I** | 6h | Automation-first agents (Relay.app, Lindy.ai). Sales enrichment, support triage, meeting-to-task, guardrails for sensitive actions. | Design automation-first agent integrating SaaS tools; implement confirmation prompts/approval steps; align with compliance KPIs. |
| **11. Workflow Automation & Orchestration – II** | 6h | Multi-step orchestration with n8n, Make, Zapier. Combining LLM reasoning with deterministic logic, HTTP nodes, MCP for no-code, failure drills. | Build resilient hybrid workflow; use HTTP/MCP nodes for custom APIs; simulate and resolve workflow errors with retries and logging. |
| **12. Project – Build a No-Code Multi-Agent System** | 8h | Design and deploy end-to-end multi-agent system solving real organizational challenge: requirements brief, workflow diagram, risk register, demo. | Deliver working multi-agent system reading, reasoning, and acting across &ge;2 systems with documented guardrails and cost-benefit framing. |

### Category 4: Building AI Agents (Code) (Modules 13–16)
| Module | Duration | Description | Target Learning Outcomes |
|---|:---:|---|---|
| **13. Agentic Building Blocks with LangChain** | 6h | ReAct, planner-executor, HTTP/API requests, JSON schemas, the AI agent stack (models, memory, RAG, tools, MCP, orchestration). | Explain API/HTTP/JSON agent foundations; define reasoning loops; implement agent stack layers; validate robust tool/function schemas. |
| **14. Long-Running Agents with LangGraph** | 6h | Ambient vs ReAct agents; persistence, state graphs, threads, autonomous loops. Approval gates, recovery rules, LangSmith tracing. | Compare chat vs ambient agents; build stateful workflows with LangGraph; apply stop conditions and human approval gates; observe in LangSmith. |
| **15. Governance for Autonomous Agents with LangSmith** | 6h | Safety, compliance, auditability. Prompt injection defense, sandboxing, tool permissions, trace inspection, evaluation and monitoring plans. | Explain autonomous governance; match risks to controls; design sandboxed workflows; use traces for audit; create evaluation plans. |
| **16. Project – Build an Agent through Code-Based Approach** | 8h | Real workflow agent (research triage, data validation, assistant). Integrate &ge;2 tools with retries, observability, automated tests, peer review. | Deliver code agent with automated test suite; justify architectural choices; demonstrate operational readiness with monitoring and guardrails. |

### Category 5: Running Local Agents (Modules 17–20)
| Module | Duration | Description | Target Learning Outcomes |
|---|:---:|---|---|
| **17. Hardware for Local Agents** | 4h | Privacy, low-latency, and cost control drivers. RAM, VRAM, SSD, CPU, GPU, NPU functions. Model sizing formulas and hardware budget planning. | Explain local use cases; differentiate RAM/VRAM/storage; compare CPU/GPU/NPU inference; calculate hardware limits; budget local vs cloud. |
| **18. Software for Local Models** | 4h | Ollama, Docker Model Runner, OpenVINO. SQLite databases, FAISS vector stores, open-source model cards, benchmarks, and local evaluation. | Install & run models locally; manage local SQLite & FAISS vector stores; interpret model cards; benchmark and test local open-source models. |
| **19. Sovereign Local AI Agent** | 4h | AI sovereignty (data, model, infrastructure). Agent assets, validated `SKILL.md` files, OpenVINO Model Server, policy-as-configuration, SBOM packaging. | Distinguish fully local vs hybrid agents; map confidential computing boundaries; manage skill assets via `SKILL.md`; package with SBOM. |
| **20. Project – Build a Local Agent** | 8h | Private local assistant running on Intel PCs; stores data locally, queries private documents, evaluation benchmarks and video demonstration. | Build, evaluate, and demonstrate an autonomous private local assistant running entirely on-device with zero external data leakage. |
