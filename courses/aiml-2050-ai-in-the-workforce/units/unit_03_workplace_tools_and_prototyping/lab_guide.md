# Unit 03 Applied Lab Guide: Interactive Workplace Prototype with Live Data Integration

> **Course**: AIML 2050 — AI in the Workforce  
> **Deliverable**: `unit03_prototype_[yourlastname].zip` (code + db) + 3-minute video demo link  
> **Total Points**: 50 Points  
> **Submission**: Native Canvas Assignment Upload

---

## 1. Scenario & Workplace Objective
You are tasked with building a working prototype for a specific business unit (e.g., HR benefits advisor, IT incident triage assistant, or sales lead qualification assistant). Department stakeholders need to test the tool, review its reasoning, and provide feedback. You will construct a functional web prototype (using **Streamlit**, **Gradio**, or **Lovable**), connect it to a persistent database (SQLite or Supabase), and maintain a prompt engineering iteration log.

---

## 2. Step-by-Step Task Specifications

### Task 1: Problem Definition & Persona Design
Define the target workplace problem:
- Target department and user persona (e.g., HR Coordinator managing leave requests).
- Expected inputs (structured forms, free-text inquiries, document uploads).
- Expected outputs (actionable advice, policy citations, formatted ticket drafts).

### Task 2: Build the Interactive UI/UX
Construct the web interface:
- Intuitive controls for selecting scenarios or inputting user requests.
- Clear status indicators while the agent is processing.
- Clean formatting of agent responses (markdown, bullet points, data tables).

### Task 3: Implement Persistent Data Logging
Bind the application to a live backend database (SQLite or Supabase):
- Every interaction must log: timestamp, user input, agent response, and execution metadata.
- Provide a telemetry view in the UI showing recent transaction history.
- Include a user feedback widget (thumbs up/down or 1–5 rating) that updates the database record.

### Task 4: Prompt Engineering Iteration Log & Screencast
Document your prompt engineering process:
- Include at least **3 documented prompt iterations** showing how you refined system instructions to eliminate edge-case failures.
- Record a 3-minute screen recording demonstrating the working prototype, database logging, and feedback mechanism.

---

## 3. Grading Rubric (50 Points Total)

| Criteria | Exemplary (Full Points) | Developing (Partial Points) | Unacceptable (Zero Points) | Points |
|---|---|---|---|---|
| **1. UI/UX Design & Usability** | Intuitive, professional interface; handles empty inputs gracefully; displays status indicators. | Functional interface, but layout is cluttered or unformatted. | Broken UI; uncaught exceptions crash the application. | **15** |
| **2. Database Integration & Telemetry** | Seamlessly logs every interaction to persistent database (SQLite/Supabase); includes telemetry view. | Database connected, but fails to log certain fields or resets data on reload. | No database integration; stateless session. | **15** |
| **3. Prompt Iteration Log** | Thorough documentation of 3+ prompt iterations showing measurable improvements and edge-case handling. | Mentions prompt changes, but lacks clear comparison of versions. | No prompt engineering log provided. | **10** |
| **4. Demonstration Video Quality** | Clear 3-minute walkthrough demonstrating inputs, outputs, database verification, and user feedback. | Video provided but exceeds time limit or fails to demonstrate database persistence. | Missing or unplayable video demonstration. | **10** |
| **Total** | | | | **50** |
