# Feature Specification: AIML 2050 Course Architecture & Intake Scaffolding

- **ID**: `courses/aiml-2050-ai-in-the-workforce/specs/001-course-scaffold-and-intake`
- **Course**: AIML 2050: AI in the Workforce
- **Status**: Draft (In Stage 1 Intake & Scaffolding)
- **Created**: 2026-10-30
- **Target Completion**: 8-Week Accelerated Block Structure

---

## 1. Objective & Target Audience

- **Primary Persona**: College sophomores, non-traditional learners, and workforce upskilling students seeking practical applied competence in workplace AI and agentic automation.
- **Problem Statement**: Standard college AI courses are either excessively theoretical (math/deep learning proofs) or too shallow (basic consumer prompting). Workforce learners need hands-on competence designing, orchestrating, governing, and evaluating enterprise-grade AI agents and toolchains.
- **One Job**: Establish an 8-week accelerated course structure (6.0 contact hours/week = 48 hours total) that synthesizes ~16 source units (~4 hours each) of Intel agentic curriculum, defining explicit weekly learning outcomes and cumulative workforce projects.

---

## 2. Requirements (EARS Syntax)

### Always (Ubiquitous Requirements)
- `REQ-01`: The course silo **shall** reside strictly within `courses/aiml-2050-ai-in-the-workforce/` without polluting global shared directories or cross-referencing external course silos.
- `REQ-02`: The course **shall** adhere to an 8-week accelerated block schedule providing exactly 6.0 contact hours per week (48 contact hours total).
- `REQ-03`: Every weekly unit **shall** employ Backward Design, establishing 2–3 measurable Learning Outcomes and a concrete workplace Project Deliverable before authoring instructional media.
- `REQ-04`: Every weekly unit **shall** follow the standardized Canvas 8-Item Sequence (Overview with DesignPLUS Ribbon, Required Reading/Lectures, Async Drills with `<details>`, Applied Lab Guide, SpeedGrader Lab Assignment, Learn with AI Drill, QTI 1.2 Knowledge Check, and Unpublished Instructor Guide).

### When (Event-Driven Requirements)
- `REQ-05`: **When** the raw Intel curriculum materials or Table of Contents are supplied in `intake/`, the agent **shall** execute a structural mapping that pairs and synthesizes ~16 source units into 8 coherent weeks.
- `REQ-06`: **When** source materials exceed the 6.0 contact-hour weekly budget, the agent **shall** pare back low-value or redundant exercises while preserving core workforce competencies.

### While (State-Driven Requirements)
- `REQ-07`: **While** in Stage 1 & 2 planning, the agent **shall** validate cognitive load and prerequisite ordering to ensure concepts build progressively from single-agent tool execution to multi-agent swarms and Model Context Protocol (MCP) integrations.

### If-Then (Error & Unwanted Behavior)
- `REQ-08`: **If** source content contains proprietary, obsolete, or non-executable code dependencies, **then** the agent **shall** substitute standardized, zero-cost, open-source alternatives conforming to the Zero-Cost Infrastructure playbook.
- `REQ-09`: **If** module titles are authored, **then** they **shall** use hyphens (` - `) instead of colons (`:`) to prevent DesignPLUS accordion truncation.

### Where (Optional Configurations)
- `REQ-10`: **Where** synchronous lab sessions occur, each weekly unit **shall** provide an unpublished Instructor Teaching Notes page containing delivery timelines, active learning prompts, and solution keys.
- `REQ-11`: **Where** a weekly unit utilizes an open-source tool, runtime, or library (e.g., Ollama, OpenVINO, SQLite, FAISS, LangChain, n8n), the unit **shall** provide a dedicated, standalone Open-Source Tool Setup & Reference Guide WikiPage.
- `REQ-12`: The course **shall** maintain vendor Intel slide decks completely unaltered, and **shall** provide explicit slide range and section study instructions on the unit reading page directing students to the precise slides relevant to that week's competencies.

---

## 3. Deliberately Out of Scope
- Authoring final unit HTML/XML deliverables before source curriculum intake is reviewed and approved.
- Low-level machine learning model training from scratch (focus is applied workforce agent orchestration, not PyTorch neural net backprop).
- Cloud services requiring paid student credit cards (all labs must execute via free tiers, local Ollama/LM Studio runtimes, or provided institutional API gateways).

---

## 4. Acceptance Criteria & Definition of Done
- [x] Course silo initialized with `README.md`, `course_config.json`, `syllabus.md`, and `intake/` dropzone.
- [x] `CURRENT.md` and master `README.md` updated with AIML 2050 as the active workspace target.
- [ ] Source Table of Contents / materials ingested and mapped into the 8-week synthesis matrix.
- [ ] Weekly Learning Outcomes and Project Deliverables established for all 8 weeks.
- [ ] Conforms to ADR-001 (WCAG 2.2 AA accessibility) and ADR-003 (Canvas DesignPLUS standards).
