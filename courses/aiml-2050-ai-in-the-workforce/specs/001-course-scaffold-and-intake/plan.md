# Technical & Architectural Plan: AIML 2050 Scaffold & Curriculum Intake

- **Spec Reference**: [`spec.md`](file:///c:/dev/Course-Content-Agentic-Template/courses/aiml-2050-ai-in-the-workforce/specs/001-course-scaffold-and-intake/spec.md)
- **Status**: Approved / Executing
- **Course**: AIML 2050: AI in the Workforce

---

## 1. Technical Architecture & Approach

### A. Course Delivery Architecture
- **Format**: 8-Week Accelerated Block (3 credits, 6.0 contact hours/week, 48 contact hours total).
- **LMS Target**: Canvas LMS via Common Cartridge 1.1/1.3 (`.imscc`) using native DesignPLUS theme integration.
- **Cartridge Output Target**: `courses/aiml-2050-ai-in-the-workforce/AIML_2050_Complete.imscc`.

### B. Ingested Intel Source Curriculum
- **Source Location**: Configured via `local_config.json` to local path (with dual Google Gemini & OpenAI tracks).
- **Total Raw Assets**: 20 Modules, 5 Milestone Projects, 23 Directory packages. Each module includes `.pptx` slides, `.pptx` assignments, `.docx` facilitator guides, `.xlsx` quizzes, and `Dependencies` folders with Python/Jupyter/JSON resources.

### C. 20 &rarr; 8 Workforce Curriculum Synthesis & Slide Reading Lists
To best prepare students for the modern enterprise workforce while managing cognitive load across 2,100+ raw slides, the curriculum pairs source modules into 8 weeks with explicit slide directives (see full mapping in [`synthesis_matrix.md`](file:///c:/dev/Course-Content-Agentic-Template/courses/aiml-2050-ai-in-the-workforce/intake/synthesis_matrix.md)):
1. **Week 1 (Mods 1, 2, 5)**: Opportunity Audit | *Slides*: Mod 01 (4–32, 67–79, 80–96), Mod 02 (8–40, 41–74), Mod 05 (44–61, 62–105) | *Guide*: Python Environment Setup.
2. **Week 2 (Mods 3, 4)**: Ethics & Governance | *Slides*: Mod 03 (8–34, 35–67, 94–121), Mod 04 (10–22, 23–36, 37–54) | *Guide*: NIST AI RMF Checklists.
3. **Week 3 (Mods 6, 7, 8)**: Productivity & Prototyping | *Slides*: Mod 06 (8–35, 61–84, 85–110), Mod 07 (8–41, 42–60, 94–111, 112–135), Mod 08 (12–34, 44–64) | *Guide*: Streamlit/Gradio Prototyping.
4. **Week 4 (Mods 9, 10, 11, 12)**: No-Code Orchestration | *Slides*: Mod 09 (8–39, 128–151, 152–170), Mod 10 (8–41, 42–66, 67–88), Mod 11 (36–52, 53–73), Mod 12 (10–38, 40–63) | *Guide*: Self-Hosting n8n Automation.
5. **Week 5 (Mod 13)**: Python Tool Calling | *Slides*: Mod 13 (10–21, 22–74, 75–98) | *Guide*: LangChain & Pydantic Tool Schemas.
6. **Week 6 (Mods 14, 16)**: Stateful Ambient Agents | *Slides*: Mod 14 (7–19, 20–37, 38–49, 50–60), Mod 16 (16–30, 31–50, 51–63) | *Guide*: LangGraph State Checkpointers.
7. **Week 7 (Mod 15)**: Observability & Evaluation | *Slides*: Mod 15 (8–29, 30–44, 45–56, 60–98) | *Guide*: LangSmith Telemetry & Ragas Test Suites.
8. **Week 8 (Mods 17, 18, 19, 20)**: Sovereign Local AI & Capstone | *Slides*: Mod 17 (8–41, 42–75), Mod 18 (7–23, 24–44, 45–52), Mod 19 (7–35, 36–62, 112–135), Mod 20 (8–32, 33–54, 55–80) | *Guide*: Local Model Serving with Ollama & OpenVINO.

### D. Contact Hour Budgeting (6.0 Hours per Week)
- 30 min: Unit Overview & Executive Roadmap
- 90 min: Required Readings, Concepts & Micro-Lectures (using curated slide directives)
- 60 min: Interactive Self-Check Drills (`<details>`) & Socratic AI Sparring
- 60 min: Guided Technical Lab Walkthrough
- 90 min: Applied Weekly Workplace Project Build (SpeedGrader upload)
- 30 min: Native QTI 1.2 Knowledge Check (15 questions, 3 attempts)

---

## 2. ADR Conformance & Constraints

- **ADR-001 (Accessibility)**: All student-facing HTML pages, rubrics, and slide decks must achieve WCAG 2.2 AA compliance (color contrast ratio &ge; 4.5:1, semantic headings, proper table scope tags).
- **ADR-002 (Spec-Driven Development)**: All unit deliverables must trace back directly to EARS requirements in iteration specs.
- **ADR-003 (Canvas Cartridge & DesignPLUS Theme Invariants)**:
  - Native WikiPage `<head>` with identifier, editing roles, and workflow state.
  - Hyphenated module titles (`Unit 01 - ...`) with zero colons.
  - DesignPLUS banner ribbons restricted to Overview and Syllabus pages.
  - 1100x220 hero banner bundled in `images/course_banner.jpg`.

---

## 3. Dependency Graph & Verification Strategy

- **Intake Verified**: All 20 Intel modules verified on disk via `local_config.json`.
- **Quiz Pipeline**: 20 Excel quiz files ready for conversion into Canvas QTI 1.2 XML banks via `qti_builder.py`.
- **Slide Engine Pipeline**: Slide decks can be programmatically audited and re-styled to 16:9 WCAG AAA via `slide-deck-generator`.
- **Unit Deliverables**: Each weekly unit will be developed iteratively following the 8-item sequence.
