# Unit 02 Overview: Harness Architecture, Context Engineering & Rule Governance

<div class="dp-header dp-basic-bar" style="background: #1e3a8a; color: #ffffff; padding: 1.5rem; border-radius: 6px; margin-bottom: 1.5rem;">
  <h1 style="margin: 0; color: #ffffff; font-size: 1.8rem;">Unit 02: Harness Architecture, Context Engineering &amp; Rule Governance</h1>
  <p style="margin: 0.5rem 0 0 0; opacity: 0.9;">Machine-Actionable Repository Governance (AGENTS.md), Context Token Economics &amp; Progressive Disclosure via Modular Skills</p>
</div>

---

## 1. Executive Summary & Pedagogical Context

In Unit 01, we established the fundamental law of Agentic Engineering: **The 10/90 Harness Rule**. In Unit 02, we open the hood of the harness and engineer its internal context architecture.

As context windows expand from 8K to 1M+ tokens, developers fall into the **Prompt Bloat Fallacy**—stuffing entire codebases, API manuals, and rules into the system prompt. This introduces severe context degradation ("lost-in-the-middle"), high latency, and massive token costs.

Unit 02 teaches **Context Engineering & Progressive Disclosure**:
- Designing machine-actionable repository rule files (`AGENTS.md`, `.cursorrules`) that enforce negative constraints and architectural invariants.
- Structuring lightweight **Skill Registries** (`.agents/skills/`) where agents dynamically discover and load domain instructions on demand rather than cluttering the initial context.
- Building non-destructive AST-aware tools and diff patchers.

---

## 2. Weekly Contact Hour Budget (300 Minutes Total)
- **Conceptual Study & Video Lecture (150 min)**: Context economics, token decay, progressive disclosure patterns, and repository governance standards.
- **Asynchronous Preparation & Drills (60 min)**: Context budget calculations, skill routing simulations, and designing negative constraints.
- **Hands-on Engineering Lab (90 min)**: Building a dynamic skill registry and context filter that selectively injects domain instructions based on task intent.

---

## 3. Measurable Learning Objectives
1. **Analyze** token economics and cognitive degradation curves across expanded context windows.
2. **Formulate** machine-actionable repository governance rules (`AGENTS.md`) that prevent destructive agent actions.
3. **Architect** a progressive disclosure skill system that dynamically injects tool instructions on demand.
4. **Implement** an AST-aware context filter in Python that trims token bloat while preserving semantic ground truth.
