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

## Weekly Milestones & Deliverables
- [ ] Read [Unit 07 Required Readings & Concepts](reading.md).
- [ ] Complete [Unit 07 Asynchronous Preparation & Drills](drills.md).
- [ ] Implement and test [Unit 07 Applied Lab Assignment](lab_guide.md).
- [ ] Complete [Unit 07 Knowledge Check](quiz.md) (10 questions, 3 attempts).
