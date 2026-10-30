# Unit 03: Required Readings, Concepts & Slide Guidance
## Workplace Productivity Tools & Rapid Prototyping

> **Course**: AIML 2050 — AI in the Workforce  
> **Contact Allocation**: 150 Minutes  
> **Source Modules**: Intel Modules 06, 07 & 08

---

## 1. Curated Slide Reading Directives

Refer to the following specific sections of the Intel presentation decks in your course materials repository:

### A. From `[Slides] Module 06 - Agentic AI.pptx` (124 slides total)
- **Study Slides 8–35 (Integrating Agentic AI in Everyday Enterprise Workflows)**: Review enterprise productivity gains in email management, document drafting, CRM data entry, and project tracking.
- **Study Slides 61–84 (Overview of Agentic AI Tools for Business Operations)**: Analyze Microsoft Copilot, Google Gemini for Workspace, and specialized workplace point solutions.
- **Study Slides 85–110 (Measuring Productivity Gains & Avoiding Pitfalls)**: Master quantitative productivity tracking (time saved per task, error rates, cognitive fatigue reduction).
- *Skip Slides 36–60 & 111–124* (specialized niche case studies and concluding remarks).

### B. From `[Slides] Module 07 - Agentic AI.pptx` (154 slides total)
- **Study Slides 8–41 (Overview of AI Prototyping Tools & Prompting)**: Compare code vs low-code prototyping tools (Streamlit, Gradio, Lovable, v0).
- **Study Slides 42–60 (UI/UX Design Principles for Human-AI Interaction)**: Master principles of streaming feedback, optimistic UI updates, and clear affordances for human intervention.
- **Study Slides 94–111 (Integrating Real-Time External Data into Prototypes)**: Learn how to bind prototypes to SQLite, Supabase, and REST APIs.
- **Study Slides 112–135 (Deploying, Sharing & Collecting Stakeholder Feedback)**: Understand telemetry capture and structured feedback widgets (thumbs up/down, rating scales).
- *Skip Slides 61–93 & 136–154*.

### C. From `[Slides] Module 08 - Agentic AI.pptx` (71 slides total)
- **Study Slides 12–34 (Developing a Business Concept / Ideation & Architecture)**: Structure rapid prototype architecture into Presentation Layer, Logic Layer, and Data Layer.
- **Study Slides 44–64 (Risk Assessment Mapping & Stakeholder Demonstration)**: Best practices for pitching prototypes to business unit owners.

---

## 2. Core Conceptual Deep Dive: Rapid Prototyping Architecture

### The Three-Layer Prototype Architecture
A robust workplace prototype separates concerns into three distinct layers:
1. **Presentation Layer (UI/UX)**: Built using rapid frameworks like **Streamlit** or **Gradio** in Python, or **Lovable** in React. Provides chat inputs, parameter sliders, file uploaders, and data visualization.
2. **Logic & Reasoning Layer**: Houses the system prompts, model parameter configurations (temperature, top_p), and tool-calling logic.
3. **Data & State Layer**: A local SQLite database or cloud Supabase instance that stores session history, user logs, and transaction records.

```
       ┌────────────────────────────────────────────────────────┐
       │   Presentation Layer: Streamlit / Gradio Web UI         │
       │   - User Prompt Input | Parameter Controls | Results   │
       └──────────────────────────┬─────────────────────────────┘
                                  │ User Request
                                  ▼
       ┌────────────────────────────────────────────────────────┐
       │   Logic Layer: Prompt Engine & LLM Runtime             │
       │   - System Instructions | Schema Validation            │
       └──────────────────────────┬─────────────────────────────┘
                                  │ Read / Write
                                  ▼
       ┌────────────────────────────────────────────────────────┐
       │   Data Layer: Persistent Store (SQLite / Supabase)     │
       │   - Session Logs | User Ratings | Transaction Audit    │
       └────────────────────────────────────────────────────────┘
```

### The Pitfall of "Vibe-Coding" Without State
Many prototypes fail in stakeholder reviews because they are stateless: when the user refreshes the page, all conversation context, uploaded files, and generated outputs disappear. By incorporating a persistent database (even a lightweight SQLite file), the prototype captures real user interaction data that can be audited, evaluated, and used to train future production models.
