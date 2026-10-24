# ADR-002: Spec-Driven Iteration Lifecycle

- **Status**: Accepted
- **Date**: 2026-10-23
- **Deciders**: Workspace Team & AI Assistant

## Context
Standard conversational LLM development ("vibe coding") relies on informal chat instructions, causing requirements drift, hidden assumptions, lost context across chat sessions, and unpredictable rework cycles. 

To ensure predictable, reliable development for course content, tools, and templates, the project requires an engineering discipline that forces alignment before execution.

## Decision
All non-trivial development in this repository shall follow **Spec-Driven Development (SDD)** organized in micro-iterations:

1. **Structured Requirements**: Every feature or content module must have a spec in `specs/<NNN-feature>/spec.md` with requirements written using EARS syntax (*Always, When, While, If-Then, Where*).
2. **Explicit Architecture & Plan**: Every spec is paired with a plan (`plan.md`) describing architecture, constraints, and explicitly defining "Out of Scope" items.
3. **Discrete Tasks with Verification**: Tasks (`tasks.md`) must be sequenced by dependency and include a testable verification check (`Check:`).
4. **Permanent Markdown Storage**: Specifications and task logs live as markdown in the repository, serving as the system of record.
5. **No Code/Content Without Spec Approval**: Agents must not produce production code or final content without a confirmed spec.

## Consequences
- Reduces backtracking and rework.
- Creates full traceability and auditability for curriculum and software modules.
- Enables seamless resumption of work across new chat conversations or agent handoffs.
