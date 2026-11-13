# Feature Specification: Sophomore Readability Polish Loop (Units 2–8) & Course Book PDF Verification

- **ID**: `specs/011-sophomore-readability-and-pdf-spotcheck`
- **Status**: Completed
- **Created**: 2026-11-13
- **Target Completion**: Single-session iterative pass

---

## 1. Objective & Target Audience
- **Primary Persona**: College sophomores enrolled in COSC 2060 with introductory SQL (`CMAP 1815`) and introductory Python backgrounds, reading the course in Canvas or `COSC_2060_Course_Book.pdf`.
- **Problem Statement**: While structural formatting and GitHub-only workflows are now fixed, Units 2–8 still contain dense technical terms (e.g., GIL, SIMD, DMA, HNSW, JSON-RPC, ASGI, idempotency, multi-stage Docker) and occasional code walkthrough jumps that may confuse a sophomore reading the material for the first time.
- **One Job**: Run a systematic, unit-by-unit sophomore readability and clarity pass across Units 2–8, verify `COSC_2060_Course_Book.pdf` rendering on previously failing pages, and recompile the cartridge, PDF, and student sandbox if any text changes are made.

---

## 2. Requirements (EARS Syntax)
- `REQ-01` (**Sophomore Jargon & Concept Scaffolding**): **While** reading Units 2–8 (`reading.md`, `drills.md`, `lab_guide.md`), every specialized term or acronym (such as GIL, Apache Arrow, Euclidean/Manhattan distance, SIMD, HNSW, ASGI, idempotency, multi-stage builds) **shall** be introduced with a plain-English explanation or concrete analogy at first use.
- `REQ-02` (**Step-by-Step Code Clarity**): **Where** a unit explains multi-step code (e.g., Polars expressions, OpenCV letterboxing, ChromaDB chunking, FastAPI endpoints, MCP tools, Dagster DAGs, Dockerfiles), the prose **shall** explain *what* each step does and *why* before or alongside the code block without unexplained leaps.
- `REQ-03` (**PDF & Cartridge Verification**): **When** readability edits are complete, `COSC_2060_Course_Book.pdf`, `COSC_2060_Complete.imscc`, and `student_sandbox_template/` **shall** be rebuilt/synced and verified with zero rendering leaks on pages 8, 68, 91, and 206.

---

## 3. Deliberately Out of Scope
- Changing unit topics, datasets, grading weights, or lab architecture.
- Modifying Unit 1 (already reviewed in detail) or any course outside `courses/cosc-2060-data-engineering/`.

---

## 4. Acceptance Criteria & Definition of Done
- [ ] Units 2–8 audited and polished for sophomore readability (`REQ-01`, `REQ-02`).
- [ ] `COSC_2060_Course_Book.pdf` and `COSC_2060_Complete.imscc` rebuilt and verified (`REQ-03`).
- [ ] `student_sandbox_template/` synced and pushed if `study_guide.md` or `lab_guide.md` changed.

