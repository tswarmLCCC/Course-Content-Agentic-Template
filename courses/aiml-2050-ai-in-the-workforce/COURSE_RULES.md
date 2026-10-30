# COURSE_RULES.md — AIML 2050 Invariants & Authoring Guidelines

These rules are permanent non-negotiables for **AIML 2050: AI in the Workforce**. Every AI agent, curriculum author, and script operating within this course silo MUST strictly adhere to them.

---

## Rule 1: Zero-Alteration Slide Decks & Explicit Reading Directives
1. **Preserve Vendor Slide Decks Intact**: The original Intel slide decks (`.pptx` / `.pdf`) must NEVER be modified, sliced, re-branded, or edited. Vendor file integrity must be preserved 100%.
2. **Explicit Student Slide Guidance**:
   - Because 20 source modules are synthesized into 8 accelerated weeks, students are NOT expected to read entire 100+ slide decks cover-to-cover.
   - On every unit's `Unit XX: Required Readings, Concepts & Video Lectures` Canvas WikiPage, the agent **shall provide an explicit, curated reading map** stating:
     - Exact slide deck filenames.
     - Precise slide numbers and section ranges to study (e.g., *"Study Slides 12–28 for Agentic Reasoning Loops and Slides 35–48 for Enterprise KPIs; skip Slides 49–65"*).
     - Rationale for why those specific slides matter for that week's applied project.

---

## Rule 2: Dedicated Open-Source Setup & Tool Guides as Separate Pages
1. **Standalone WikiPages for Open-Source Tools**:
   - Whenever a unit utilizes an open-source tool, runtime, library, or platform (e.g., Ollama, OpenVINO, SQLite, FAISS, LangChain, LangGraph, n8n, Docker) where an existing institutional guide does not already exist, the unit **shall include a dedicated, separate Canvas WikiPage**:
     - Convention: `Unit XX: Open-Source [Tool Name] Setup & Reference Guide`
2. **Standardized Structure for Open-Source Guide Pages**:
   - **Prerequisites & Hardware**: RAM/VRAM/OS requirements.
   - **Zero-Cost Installation**: Copy-paste terminal commands (PowerShell / Bash) for clean installation.
   - **Configuration & Environment**: Environment variables, local port settings, and zero-leakage security flags.
   - **Smoke Test Verification**: A 60-second test command to verify the tool is functioning before starting the lab.
   - **Troubleshooting FAQ**: Top 3 common failure modes and instant fixes.

---

## Rule 3: Backward Design Anchor (Outcome &rarr; Project &rarr; Scaffold)
1. **No Content Without a Project Anchor**: Never author a lecture or reading page in isolation. Each week is anchored to a single, workplace-authentic project deliverable submitted through SpeedGrader.
2. **Weekly 6.0 Contact-Hour Ceiling**: Content must be strictly budgeted to 360 minutes total per week.

---

## Rule 4: DesignPLUS & Accessibility Compliance
1. **WCAG 2.2 AA (ADR-001)**: Contrast ratio &ge; 4.5:1, semantic headings (`<h2>`, `<h3>`), native styled table borders, and zero raw markdown dumps.
2. **DesignPLUS Styling (ADR-003)**:
   - Banner ribbons ONLY on Unit Overview and Syllabus pages.
   - Hyphenated module titles (`Unit 01 - ...`) with zero colons.
   - Centered 1100x220 hero banner on course home page.
