# Feature Specification: Comprehensive Content & Tech Block Remediation

- **ID**: `specs/007-comprehensive-content-and-tech-block-remediation`
- **Status**: Approved
- **Created**: 2026-10-24
- **Target Completion**: 60 minutes

---

## 1. Objective & Target Audience
- **Primary Persona**: College sophomore students taking COSC 2060 and faculty instructors delivering the course through Canvas LMS.
- **Problem Statement**:
  1. Student-facing `drills.md` pages across all 8 units currently contain raw instructor video recording teleprompter scripts (e.g. `[CAMERA ON INSTRUCTOR]`, `[00:00 - 00:45] HOOK & TITLE CARD`), broken ````mermaid code blocks (which render as raw text in Canvas), and dead local `file:///` URLs.
  2. Applied lab guides (`lab_guide.md`) contain confusing, un-scaffolded Section 1 code blocks with empty `# [YOUR QUERY HERE]` placeholders before the actual graded lab and starter template.
  3. Overview pages contain broken relative `.md` markdown links (`reading.md`, `drills.md`) that 404 in Canvas.
  4. Instructor notes are currently conflated with student drill pages instead of being cleanly siloed into unpublished Canvas instructor pages.
- **One Job**: Perform a systematic, triple-checked content and tech block remediation across all pages in Units 1 through 8, transforming `drills.md` into authentic student-facing formative self-checks, cleaning up `lab_guide.md`, removing dead `file:///` URLs and unrendered mermaid blocks, routing instructor recording scripts to `teaching_notes.md`, rebuilding the Canvas Common Cartridge (`.imscc`), and committing the repository to Git.

---

## 2. Requirements (EARS Syntax)

### Universal Content Hygiene & Tech Blocks
- `REQ-01`: **Always**: Every page in the course **shall** be free of unrendered ````mermaid code blocks, teleprompter video cues (`[CAMERA ON INSTRUCTOR]`), and dead local file system URLs (`file:///c:/...`).
- `REQ-02`: **Always**: Every code block in course pages **shall** contain complete, syntactically valid code or clear instructional examples, eliminating empty `[YOUR QUERY HERE]` placeholder dumps.
- `REQ-03`: **Always**: All internal navigation links within Canvas pages **shall** use clean, styled HTML cards or valid Canvas navigation references, eliminating broken relative `.md` links (e.g. `reading.md`).

### Authentic Student-Facing Drills (`drills.md`)
- `REQ-04`: **Always**: Each unit's `drills.md` **shall** serve as an authentic, high-value formative practice hub for students containing:
  1. Unit Time Budget (60 min asynchronous allocation) & Readiness Checklist.
  2. 4–5 Foundational Concept Self-Checks with expandable `<details><summary>` answer keys providing deep pedagogical explanations.
  3. 2–3 Code Execution Order & Syntax Traces ("Spot the Bug" / "Predict the Output") with `<details><summary>` explanations.
  4. Defensive Engineering Gotchas & Common Anti-Patterns Callout Box.
  5. Preparation briefing for the upcoming In-Class Coding Clinic (Slot 2).

### Lab Guides & Scaffolding (`lab_guide.md`)
- `REQ-05`: **Always**: Each unit's `lab_guide.md` **shall** follow a clean, uncluttered structure:
  1. Executive Scenario & Business Context (realistic industrial friction).
  2. Graded Challenge Specifications (Part 1, Part 2, Part 3) with exact schema contracts.
  3. Self-Contained, Runnable Starter Template (`labX_starter.py`) with built-in mock data generation and defensive test assertions.
  4. 100-Point Detailed Evaluation Rubric.
  5. Standalone submission verification commands runnable in standard terminal.

### Instructor Siloing (`teaching_notes.md`)
- `REQ-06`: **Always**: Instructor video recording scripts, synchronous agendas, and solution keys **shall** be cleanly siloed into `teaching_notes.md` in each unit folder, compiled by `build_course.py` into unpublished Canvas WikiPages (`[Instructor Guide] Unit X Teaching Notes & Solutions`).

### Compilation & Git Versioning
- `REQ-07`: **When** all 8 unit folders are remediated, the system **shall** compile a clean, verified Canvas Common Cartridge (`courses/cosc-2060-data-engineering/COSC_2060_Complete.imscc`).
- `REQ-08`: **Always**: The compiled cartridge **shall** pass all XML syntax checks, manifest validations, and DesignPLUS structure audits.
- `REQ-09`: **When** verification passes 100%, all changes **shall** be committed cleanly to Git with a descriptive commit message.

---

## 3. Deliberately Out of Scope
- Modifying the verified Python transition notebooks in `content/notebooks/` (already 100% parity verified).
- Modifying the verified PowerPoint slide decks in `content/slides/` (already audited 100% PASS).
- Modifying institutional syllabus grading scale or college accreditation text.

---

## 4. Acceptance Criteria & Definition of Done
- [ ] All 8 `drills.md` files remediated with authentic student-facing self-checks and `<details><summary>` answer keys.
- [ ] All 8 `lab_guide.md` files cleaned of redundant `[YOUR QUERY HERE]` placeholder blocks.
- [ ] All 8 `overview.md` files updated to eliminate broken relative `.md` links.
- [ ] All 8 unit folders contain `teaching_notes.md` housing the flipped classroom scripts.
- [ ] Canvas Common Cartridge (`COSC_2060_Complete.imscc`) recompiled and verified via `scratch/verify_cartridge_fix.py`.
- [ ] Zero unrendered mermaid blocks or dead `file:///` URLs in the compiled cartridge.
- [ ] Complete git commit preserving all deliverables.
