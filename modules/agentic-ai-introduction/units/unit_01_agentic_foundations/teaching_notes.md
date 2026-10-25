# [Instructor Guide] Unit 01 Teaching Notes & Solutions
## Agentic AI Foundations: Synchronous Agendas, Video Scripts & Solution Keys

> **FOR INSTRUCTORS ONLY — UNPUBLISHED IN CANVAS**  
> *This document contains class delivery timing, whiteboard discussion sparring prompts, teleprompter recording scripts, and the complete master solution code.*

---

## 1. Synchronous Class Delivery Agenda (75-Minute In-Class Clinic)

| Time | Duration | Segment | Instructor Activity |
| :--- | :---: | :--- | :--- |
| **00:00 - 00:10** | 10 min | **Incident Retrospective** | Open with the "Runaway Agent Incident": Show how a poorly constrained while-loop cost a startup $8,400 in API tokens in 4 hours due to an unhandled 404 API error. |
| **00:10 - 00:25** | 15 min | **Whiteboard Sparring: CoT vs. ReAct** | Draw two columns on the board. Left: Chain-of-Thought (internal hallucination compounding). Right: ReAct (Thought $\to$ Action $\to$ Observation). Have students roleplay as the "Environment". |
| **00:25 - 00:45** | 20 min | **Live Coding Clinic ("I Do, We Do")** | Live-code the transition from a naive monolithic prompt to a 2-step prompt chain with an intermediate schema gate in Python. |
| **00:45 - 01:10** | 25 min | **Active Lab Hacking ("You Do")** | Students open `starter_blog_agents.py`. Challenge: Add a 4th validation rule checking for banned clichés ("delve", "testament", "in conclusion") and observe the Writer re-drafting. |
| **01:10 - 01:15** | 5 min | **Debrief & Synthesis** | Review the Anthropic Architectural Matrix: When to stay with workflows, and when it is actually worth paying for an agent. |

---

## 2. Whiteboard Sparring Prompts

1. **The "Why Not Just Make One Big Prompt?" Challenge**:
   - *Prompt*: "Why can't I just tell Claude or GPT-4 in a single prompt: 'You are an author, critic, fact-checker, and formatter. Write the blog post and check all 10 rules yourself'?"
   - *Expected Student Answer*: Attention diffusion, inability to grade one's own work objectively, loss of constraint tracking over long generation contexts.
2. **The "When is an Agent Overkill?" Challenge**:
   - *Prompt*: "Your boss wants to build an autonomous agent to process customer PDF invoices and save them to PostgreSQL. Is this a good use case for an agent?"
   - *Expected Student Answer*: No! The pipeline is invariant and structured. A deterministic **Prompt Chain (with Gates)** or standard OCR workflow is 10x cheaper, 5x faster, and has zero probability of deciding to do something unexpected.

---

## 3. Video Production Blueprint (Micro-Lecture Script)

- **[0:00 - CAMERA ON INSTRUCTOR]**:
  "Welcome to Unit 1. Up until today, you have probably used AI as a fancy autocomplete. You ask a question, it predicts tokens, you copy the answer. But what happens when the model is wrong? Today, we give models eyes and hands. We turn them into agents."
- **[1:30 - SCREEN SHARE: SLIDE 4 — The ReAct Architecture]**:
  "In 2022, researchers at Princeton and Google noticed something fascinating: models that only think get lost in their own heads. Models that only act fire blindly into tools. But when you interleave Thought, Action, and Observation—what we call the ReAct framework—the model grounds itself on environmental truth."
- **[4:15 - TERMINAL SCREENCAST: Running `starter_blog_agents.py`]**:
  "Watch this execution log. Turn 1: the writer submits a draft with only 49 words. The validator rejects it immediately. Notice the writer didn't crash—it received the critique, expanded its explanations, added the missing section, and passed on Turn 2. That is self-correcting agentic AI."

---

## 4. Master Solution Key (`solution_blog_agents.py`)

Below is the complete reference implementation demonstrating the extended pipeline with custom stylistic guards:

```python
#!/usr/bin/env python3
"""
Unit 01 Master Solution Key: Self-Correcting Multi-Agent Content Pipeline
"""
import json
from typing import Dict, Any, List, Optional

class MasterBlogPipeline:
    def __init__(self, max_iterations: int = 3):
        self.max_iterations = max_iterations
        self.banned_words = ["delve", "testament", "in conclusion", "tapestry"]

    def planner(self, topic: str) -> Dict[str, Any]:
        return {
            "title": f"The Engineering Truth About {topic}",
            "target_words": 150,
            "sections": [
                "The Architectural Friction",
                "Core Technical Deep Dive",
                "Production Takeaways & Tradeoffs"
            ]
        }

    def writer(self, plan: Dict[str, Any], critique: Optional[Dict[str, Any]] = None) -> str:
        if critique is None:
            # Deliberately imperfect draft 1
            return (
                f"# {plan['title']}\n\n"
                "## The Architectural Friction\n"
                "Building software with LLMs is challenging. In conclusion, we need better tools."
            )
        else:
            # Corrected draft 2 addressing all validator points
            return (
                f"# {plan['title']}\n\n"
                "## The Architectural Friction\n"
                "Production engineering teams often struggle with non-deterministic model behaviors. "
                "When systems rely on unconstrained generation, error rates compound across downstream services.\n\n"
                "## Core Technical Deep Dive\n"
                "By adopting the ReAct framework, developers decouple verbal reasoning from tool execution. "
                "Each tool invocation returns verifiable environmental state, enabling the agent to update "
                "its internal state before taking subsequent actions.\n\n"
                "## Production Takeaways & Tradeoffs\n"
                "Autonomous agents trade predictability and cost for flexibility. Teams must implement "
                "hard iteration caps, schema validation, and poka-yoke tool interfaces to prevent runaway loops."
            )

    def validator(self, text: str, plan: Dict[str, Any]) -> Dict[str, Any]:
        words = len(text.split())
        issues = []
        
        if words < 120 or words > 250:
            issues.append(f"Word count violation: {words} words (must be 120-250 words).")
            
        for sec in plan["sections"]:
            if f"## {sec}" not in text:
                issues.append(f"Missing required section: '## {sec}'.")
                
        for bw in self.banned_words:
            if bw in text.lower():
                issues.append(f"Contains forbidden cliché word: '{bw}'.")

        passed = len(issues) == 0
        return {
            "passed": passed,
            "score": 100 if passed else max(20, 100 - (len(issues) * 25)),
            "word_count": words,
            "issues": issues
        }

    def run(self, topic: str):
        plan = self.planner(topic)
        critique = None
        for i in range(1, self.max_iterations + 1):
            draft = self.writer(plan, critique)
            critique = self.validator(draft, plan)
            if critique["passed"]:
                return True, draft, i
        return False, draft, self.max_iterations

if __name__ == "__main__":
    pipeline = MasterBlogPipeline()
    passed, text, turns = pipeline.run("Agentic AI Foundations")
    print(f"Executed in {turns} turns. Passed={passed}")
    assert passed is True
```
