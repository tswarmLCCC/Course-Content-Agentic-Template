# Unit 01: Learn with AI — Supplemental Practice Drill

> **Category**: Socratic AI Practice & Architecture Review  
> **Target Mastery**: Interactive Sparring with AI on Agentic Edge Cases, Tool Poisoning & Runaway Loops

---

## 1. The AI Roleplay Paradigm: Architecture Reviewer

In this course, AI is your interactive technical sparring partner and critical code reviewer. In this exercise, you will instruct a free conversational model (ChatGPT Free, Claude Free, Gemini Free, or Copilot Free) to act as a **Principal AI Systems Architect** stress-testing your multi-agent design.

Do not ask the AI to write your code for you. Instead, use the master prompt below to have the model challenge your architecture, identify subtle loop traps, and propose edge cases.

---

## 2. Copy-and-Paste Master Sparring Prompt

Copy and paste the exact prompt block below into your AI chat interface:

```text
You are acting as a Principal AI Systems Architect conducting a technical design review on my autonomous multi-agent pipeline. 

My system is composed of:
1. A Planner Agent that decomposes a topic into a 3-part outline.
2. A Writer Agent that drafts content following the outline.
3. A Validator Agent that grades word count (120-250 words) and checks for required section headings.
4. An Agent Coordinator that manages an Evaluator-Optimizer loop with a max_iterations=3 cap.

Do NOT write code for me. Instead, act as a Socratic reviewer and ask me 3 tough architectural questions:
1. How does my architecture defend against "critic thrashing" (where the validator repeatedly complains about mutually contradictory requirements)?
2. What happens if a tool returns a 10MB JSON response or times out after 30 seconds?
3. How can I guarantee that the Planner's output is immune to prompt injection if the user input contains malicious system override instructions?

Ask me the questions one at a time, listen to my proposed answers, critique my engineering rationale, and suggest production-grade hardening techniques.
```

---

## 3. The 100% Free AI Tool Matrix

Every AI drill in this unit is compatible with free web tiers:

- **ChatGPT Free Tier**: [chatgpt.com](https://chatgpt.com) (GPT-4o-mini / Free tier)
- **Anthropic Claude Free Tier**: [claude.ai](https://claude.ai) (Claude 3.5 Sonnet / Haiku web interface)
- **Google Gemini Free Tier**: [gemini.google.com](https://gemini.google.com) (Google account login)
- **Microsoft Copilot Free Tier**: [copilot.microsoft.com](https://copilot.microsoft.com) (Free web chat)

---

## 4. The Golden Verification Protocol

> **The Empirical Verification Mandate:**  
> Never accept code or architecture recommendations from an AI model at face value! Every proposed mechanism (such as error handling, timeout bounds, or schema validation) must be tested and proven directly in your local Python environment before submission.
