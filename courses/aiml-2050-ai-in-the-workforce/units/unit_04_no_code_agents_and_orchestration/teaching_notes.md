# [Instructor Guide] Unit 04 Teaching Notes & Delivery Guide
## No-Code Business Agents & Workflow Orchestration

> **Target Audience**: Instructors & Facilitators  
> **Workflow State**: `unpublished` (Hidden from students in Canvas)

---

## 1. Synchronous Delivery Agenda (60-Minute In-Class Practicum)
- **00–15 min (Hook & The Fragility of APIs)**: Demonstrate what happens when a third-party API changes a JSON key or goes down. Show the difference between a broken pipe vs. a resilient fallback.
- **15–35 min (Live n8n Multi-Agent Build)**: Walk through setting up an Orchestrator node that inspects incoming text and branches to either an IT Support or Billing node.
- **35–50 min (Break the Workflow Clinic)**: Students send intentionally malformed JSON to each other's webhooks to verify that error fallback branches capture the payload.
- **50–60 min (Debrief & Code Transition)**: Preview Unit 05, explaining that no-code orchestrators teach the exact state-machine logic we will implement in Python with LangChain and LangGraph.
