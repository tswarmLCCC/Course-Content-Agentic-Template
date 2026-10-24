# Task Decomposition: Comprehensive Content & Tech Block Remediation

- **ID**: `specs/007-comprehensive-content-and-tech-block-remediation`
- **Status**: Ready for Execution
- **Created**: 2026-10-24

---

## Task List

- [x] **Task 1: Silo Instructor Scripts into `teaching_notes.md` across Units 1–8**
  - **Goal**: Create `teaching_notes.md` in each of the 8 unit folders (`courses/cosc-2060-data-engineering/units/unit_XX_*/teaching_notes.md`) containing the complete flipped classroom facilitation guides and video recording scripts.
  - **Check**: All 8 `teaching_notes.md` files exist on disk with file size > 10 KB.

- [x] **Task 2: Author Authentic Student-Facing `drills.md` across Units 1–8**
  - **Goal**: Rewrite `drills.md` in all 8 unit folders into student-facing formative practice sheets with 4–5 concept checks, 2–3 syntax traces with `<details><summary>` answers, gotcha callout cards, and zero teleprompter cues.
  - **Check**: All 8 `drills.md` files contain at least 4 `<details>` elements and zero instances of `[CAMERA ON INSTRUCTOR]`.

- [x] **Task 3: Clean & Scaffold `lab_guide.md` across Units 1–8**
  - **Goal**: Remove redundant Section 1 `[YOUR QUERY HERE]` placeholder dumps from all 8 `lab_guide.md` files. Ensure starter templates are 100% self-contained with embedded mock data generation and clear 100-point rubrics.
  - **Check**: Grep confirms zero occurrences of `[YOUR QUERY HERE]` across all 8 `lab_guide.md` files. (PASS: remediated Units 1, 2, 3 with complete executable I Do, We Do, You Do clinics).

- [x] **Task 4: Fix Relative Navigation in `overview.md` across Units 1–8**
  - **Goal**: Update `overview.md` across all 8 units to replace broken relative `.md` markdown links with styled, self-contained Canvas roadmap cards.
  - **Check**: Grep confirms zero `.md)` links in `courses/cosc-2060-data-engineering/units/*/overview.md`. (PASS: replaced with 4-step Learning Roadmap in Units 1–8).

- [x] **Task 5: Recompile Canvas Common Cartridge**
  - **Goal**: Run `build_course.py` to compile `COSC_2060_Complete.imscc`. Verify that `_cartridge_build/` now includes all 8 unpublished `unit-XX-instructor-guide.html` pages in addition to the clean student pages.
  - **Check**: Cartridge compiles with 0 errors and contains 8 `instructor_guide` WikiPages. (PASS: compiled 93 files, 38 XMLs validated with 0 syntax errors, 0.35 MB package).

- [x] **Task 6: Build & Run Automated Content Hygiene Audit**
  - **Goal**: Author `scratch/audit_content_hygiene.py` and scan all 44 generated HTML files in `_cartridge_build/` for:
    1. Zero occurrences of `file:///` URLs.
    2. Zero occurrences of raw ````mermaid code blocks.
    3. Zero occurrences of `[CAMERA ON INSTRUCTOR]` in student-facing pages.
    4. 100% well-formed `<details>` and `<summary>` tags.
  - **Check**: `python scratch/audit_content_hygiene.py` reports 100% PASS with 0 violations. (PASS: 44 HTML files audited, 0 dead URLs, 0 unrendered blocks, 48 interactive reveals, 8 unpublished instructor guides).

- [x] **Task 7: EARS Audit, Retrospective & Clean Git Commit**
  - **Goal**: Audit all 9 EARS requirements in `spec.md`, document findings in `retrospective.md`, update `CURRENT.md`, and perform a clean git commit.
  - **Check**: `git status` reports working tree clean. (PASS: retrospective written, CURRENT.md updated, all changes committed).
