# Feature Specification: Teach-First Conceptual Bridges Across Units 2–8 Readings

- **ID**: `specs/012-teach-first-reading-bridges`
- **Status**: Completed
- **Created**: 2026-11-13
- **Target Completion**: Multi-unit reading pass

---

## 1. Objective & Target Audience
- **Primary Persona**: College sophomores with introductory SQL (`CMAP 1815`) and introductory Python backgrounds reading Units 2–8.
- **Problem Statement**: Several sections in Units 2–8 `reading.md` jump too abruptly from a story or SQL callback straight into code (e.g., *"Just as we used arithmetic and CASE WHEN in Unit 1 SQL..."* → 10 lines of Polars expressions) without first teaching *how* the library's feature works overall, *how* it differs from previous tools, and *why* engineers use it before applying it to the unit's dataset.
- **One Job**: Keep all existing storytelling and technical depth in Units 2–8 `reading.md`, while adding clear **"Teach-First" 3-step bridges** (Contrast/Difference → General Functionality & Purpose → Specific Application) before every new technique or API pattern.

---

## 2. Requirements (EARS Syntax)
- `REQ-01` (**Teach-First 3-Step Pattern**): **Where** a unit's `reading.md` introduces a new library method, syntax pattern, or architectural mechanism (in Units 2–8), the prose **shall** first explain (1) how it differs from prior tools/concepts, (2) how the functionality works overall and what its general engineering use is, and (3) how it applies to the unit's concrete story/dataset.
- `REQ-02` (**Preserve Stories & Depth**): **While** adding teaching bridges, the system **shall** preserve all existing real-world stories, case studies (e.g., Driver 42, Ruler Distortion), code examples, and reference links.
- `REQ-03` (**Sync, Rebuild & Verify**): **When** Units 2–8 `reading.md` updates are complete, `student_sandbox_template/units/*/study_guide.md`, `COSC_2060_Complete.imscc`, `COSC_2060_Course_Book.pdf`, and `COSC-2060-Student-Sandbox` on GitHub **shall** be synced, rebuilt, and verified with zero rendering or link errors.

---

## 3. Deliberately Out of Scope
- Removing or shortening existing storytelling, case studies, or code examples.
- Modifying Unit 1, quizzes, or lab starter code logic.

---

## 4. Acceptance Criteria & Definition of Done
- [ ] Units 2–8 `reading.md` each include Teach-First 3-step bridges before new code/API patterns (`REQ-01`, `REQ-02`).
- [ ] `student_sandbox_template/` synced & pushed; `.imscc` and `.pdf` rebuilt cleanly (`REQ-03`).
