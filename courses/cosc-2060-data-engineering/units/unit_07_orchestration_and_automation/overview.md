# Unit 07 Overview: Orchestration, Resilient DAGs & Telemetry Alerting

Data engineering pipelines run in production 24/7/365. When network timeouts occur or upstream APIs fail, pipelines must self-heal or notify on-call engineers. Unit 07 focuses on workflow orchestration: constructing directed acyclic graphs (DAGs), idempotency, exponential backoff retries, and telemetry alerting.

---

## Weekly Contact Hour Budget (300 Minutes Total)
- **Conceptual Study & Readings (150 min)**: Study workflow orchestration principles, DAG dependency management, idempotency guarantees, and SLA monitoring.
- **Asynchronous Preparation & Drills (60 min)**: Diagram pipeline failure modes, retry policies, and backoff equations.
- **Hands-on Engineering Lab (90 min)**: Construct the Unsleeping Pipeline Orchestrator Lab with self-healing retries.

---

## Measurable Learning Objectives
By the end of this unit, you will be able to:
1. **Construct** dependency-ordered Directed Acyclic Graphs (DAGs) coordinating multistage data extraction and transformation.
2. **Implement** idempotent execution guarantees ensuring repeated pipeline runs produce identical state without duplicate records.
3. **Configure** exponential backoff retry policies and circuit breakers for transient network failures.
4. **Emit** structured logging and health check metrics alerting on SLA breaches.

---

## Weekly Learning Roadmap & Deliverables

Follow the sequential module workflow in Canvas to complete this unit:

1. **Step 1: Required Readings & Reference Architecture**  
   Study DAG orchestration principles, dependency resolution, idempotency guarantees, and Dead Letter Queue (DLQ) quarantine architectures in the module reading.
2. **Step 2: Diagnostic Drills & Syntax Checks**  
   Complete the asynchronous concept checks, topological sort dependency traces, and exponential backoff calculations before tackling the lab.
3. **Step 3: Applied Engineering Lab & Starter Code**  
   Build and test your resilient DAG pipeline orchestrator (`lab7_starter.py`) adhering to the 100-point rubric, then submit your script to the assignment dropbox.
4. **Step 4: Knowledge Check & Concept Verification**  
   Take the untimed 10-question formative assessment in Canvas (up to 3 attempts, highest score kept) to lock in key terminology and mental models.
