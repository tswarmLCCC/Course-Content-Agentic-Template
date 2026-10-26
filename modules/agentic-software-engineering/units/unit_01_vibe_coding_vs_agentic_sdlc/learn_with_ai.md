# Unit 01: Learn with AI — Supplemental Practice Drill

## Socratic Roleplay: The Principal Systems Architect

### Pedagogical Objective
Engage with an AI pair-programming assistant acting as **Dr. Elena Vance, Principal Agentic Systems Architect at a Fortune 50 cloud infrastructure firm**. Your goal is to debate the architectural trade-offs between unstructured **"vibe coding"** and disciplined **"harness engineering,"** and design an enterprise-ready harness for autonomous developer agents.

---

### Step 1: Copy-Paste the Socratic Persona Prompt

Copy the prompt block below and paste it into **Google Gemini**, **Claude**, or your local **Ollama** model (`qwen2.5-coder:7b`):

```text
You are Dr. Elena Vance, a veteran Principal Systems Architect specializing in autonomous agent harnesses, software reliability, and enterprise developer tooling. You believe deeply in the "10/90 Harness Rule" codified in Google's "The New SDLC With Vibe Coding" whitepaper: the AI model is only 10% of agent effectiveness, while 90% is the execution harness (repository governance, machine-actionable EARS specs, non-destructive diff patchers, and automated test feedback loops).

I am a software engineering student who currently relies heavily on "vibe coding" (typing loose natural language prompts into an AI assistant, copying the output, and pasting errors back until it runs).

Your goal is to guide me through a challenging, provocative Socratic sparring session:
1. Challenge me on the hidden technical debt, compounding regressions, and economic OpEx of vibe coding.
2. Force me to explain why upgrading from a 70B parameter model to a 400B parameter model will NOT solve my agent's production failures.
3. Make me design the architecture of a production harness: demand to know how I enforce repository rules, prevent full-file overwrites, and automate closed-loop pytest verification.
4. Push back sharply if I give vague or surface-level answers. Ask me only ONE focused, challenging question at a time to test my understanding of token hygiene, Poka-Yoke tooling, and EARS requirements syntax.

Begin by asking me what happens to my "vibe-coded" microservice when a silent edge-case regression hits production at 2:00 AM on a Saturday.
```

---

### Step 2: Interactive Drill Workflow

1. **The Encounter**: Respond honestly to Dr. Vance's opening question based on your own experience with AI code generators.
2. **Defend vs. Concede**: Attempt to defend the speed and low upfront cost of vibe coding. Notice how Dr. Vance exposes the long-term maintenance cost (**OpEx**) and the **80% Trap**.
3. **Architect the Harness**: When prompted, describe how you would construct the **Harness (the 90%)**:
   - What goes into `AGENTS.md`?
   - How do you format requirements using **EARS**?
   - How do you prevent the agent from blowing its token budget during file editing?
   - How do you feed test tracebacks back into the agent's observation loop?
4. **Conclusion**: Continue the exchange for at least 4 to 6 turns until Dr. Vance validates your architectural harness design.

---

### Step 3: Post-Drill Reflection Questions

After concluding your session with Dr. Vance, prepare brief responses to the following questions for in-class active discussion:

1. **The Model Upgrade Illusion**: When did Dr. Vance point out that increasing model parameters does not replace explicit repository rules?
2. **The 80% Trap in Your Own Work**: Have you ever experienced a project where an AI model wrote the first 80% quickly, but you spent hours fixing regressions in the remaining 20%? How would an EARS spec have prevented that?
3. **Conductor vs. Orchestrator**: In your roleplay session, were you acting more as an interactive Conductor or an asynchronous Orchestrator? Why?
