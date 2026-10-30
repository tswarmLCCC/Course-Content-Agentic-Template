# Unit 03: Asynchronous Preparation & Diagnostic Drills
## Workplace Productivity Tools & Rapid Prototyping

> **Time Commitment**: ~60 Minutes (Asynchronous Self-Study)  
> **Target Mastery**: UI/UX design patterns, session state management, database telemetry.

---

## 1. Readiness Checklist
- [ ] Studied slides on AI prototyping in `[Slides] Module 07`.
- [ ] Installed Streamlit in your local Python virtual environment.
- [ ] Verified local database read/write with SQLite.

---

## 2. Formative Diagnostic Drills

<details>
<summary>Drill 1: Why is streaming token output critical for human-AI interaction in workplace prototypes?</summary>

**Architectural Rationale:**
Large language models and agentic reasoning loops can take 5 to 15 seconds to synthesize complex responses. If a prototype displays a frozen blank screen or static spinner, users assume the application has crashed and will refresh or abandon the page. Streaming tokens immediately (or rendering a step-by-step progress checklist: *"Querying database...", "Synthesizing answer..."*) provides continuous feedback and perceived zero latency.
</details>

<details>
<summary>Drill 2: When building a web prototype with Streamlit, why must conversational state be stored in `st.session_state` instead of standard global variables?</summary>

**Architectural Rationale:**
Streamlit executes the entire Python script from top to bottom on every user interaction (button click, text change, dropdown selection). Standard local variables are reset to their initial values on every re-run. `st.session_state` preserves variables across multiple script executions for a specific user session.
</details>

<details>
<summary>Drill 3: What security risk occurs when API keys are hard-coded into prototype frontend scripts?</summary>

**Architectural Rationale:**
Hard-coding API keys directly in source code risks accidental exposure when sharing code repositories (Git commits, cloud deployments, or student file submissions). API keys must always be stored in environment variables (e.g. `.env` files parsed via `python-dotenv` or Streamlit Secrets `st.secrets`), with `.env` added to `.gitignore`.
</details>
