# Unit 07: Required Readings, Concepts & Slide Guidance
## Agent Governance, Observability & Automated Evaluation

> **Course**: AIML 2050 — AI in the Workforce  
> **Contact Allocation**: 150 Minutes  
> **Source Module**: Intel Module 15 (Governance with LangSmith)

---

## 1. Curated Slide Reading Directives

Refer to the following specific sections of the Intel presentation deck in your course materials repository:

### From `[Slides] Module 15 - Agentic AI.pptx` (102 slides total)
- **Study Slides 8–29 (Governance in Agentic AI)**: Review enterprise safety, regulatory compliance, accountability, and auditable logging standards.
- **Study Slides 30–44 (Implementing Guardrails)**: Master techniques for intercepting direct/indirect prompt injections, sanitizing PII, and restricting tool execution permissions.
- **Study Slides 45–56 (Risk Categories & Enterprise Control Matrices)**: Deep dive into operational risk scoring and mitigation workflows.
- **Study Slides 60–98 (Monitoring, Telemetry Tracing & Evaluating Agents)**: Learn how execution traces track every reasoning step, LLM token count, latency spike, and tool call. Study test dataset construction and automated evaluation pipelines.
- *Skip Slides 57–59 & 99–102*.

---

## 2. Core Conceptual Deep Dive: Observability & Evaluation

### The Four Pillars of Agent Observability
Traditional application monitoring tracks CPU, memory, and HTTP response codes. Agent observability requires tracking cognitive and operational metrics:
1. **Trace Trees**: Visualizing every node in an agent run (User Prompt &rarr; System Prompt &rarr; Thought &rarr; Tool Call &rarr; Observation &rarr; Final Answer).
2. **Token & Cost Accounting**: Measuring input/output tokens per turn to detect runaway loops and optimize model selection.
3. **Latency Profiling**: Identifying whether delays originate in model inference, vector database lookup, or external API response times.
4. **Tool Accuracy & Failure Rate**: Quantifying how often tool calls fail due to schema validation errors or network timeouts.

### Automated Evaluation: Why Unit Tests Fail for LLMs
In standard software, `add(2, 2)` always equals `4`. In agentic systems, user inputs vary and model outputs are probabilistic.
To evaluate agents at scale, enterprises build **Automated Evaluation Harnesses**:
- **Ground Truth Test Datasets**: Standardized spreadsheets containing test prompts, expected tool calls, and reference criteria.
- **LLM-as-a-Judge**: A separate evaluator model prompted with strict rubric guidelines to score the candidate agent's output for Accuracy, Safety, and Groundedness.
