# Task List: 011-sophomore-readability-and-pdf-spotcheck

- [x] **Task 1: Spot-check `COSC_2060_Course_Book.pdf` (pages 8, 68, 91, 206) and Unit 2 `coding_clinic.ipynb`** (`REQ-03`)
  - *Check*: Verify zero `__CODE_BLOCK_` or `\$` leaks in extracted PDF text and valid JSON/code in Unit 2 `coding_clinic.ipynb`.
- [x] **Task 2: Sophomore readability & jargon pass on Units 2–4 (`reading.md`, `drills.md`, `lab_guide.md`)** (`REQ-01`, `REQ-02`)
  - *Check*: Verify plain-English definitions for GIL/Arrow/distance metrics (Unit 2), HWC/CHW/SIMD/DMA/letterboxing (Unit 3), and embeddings/HNSW/cosine similarity (Unit 4).
- [x] **Task 3: Sophomore readability & jargon pass on Units 5–8 (`reading.md`, `drills.md`, `lab_guide.md`)** (`REQ-01`, `REQ-02`)
  - *Check*: Verify plain-English definitions for ASGI/Pydantic/HTTP status codes (Unit 5), JSON-RPC/MCP guardrails (Unit 6), DAG/topological sort/idempotency/DLQ (Unit 7), and multi-stage Docker/blind batch (Unit 8).
- [x] **Task 4: Sync sandbox `study_guide.md` files, rebuild `.imscc` & `.pdf`, push sandbox if changed, and update `CURRENT.md`** (`REQ-03`)
  - *Check*: Run `build_course.py` and `build_course_book.py` with exit code 0, verify zero leaks, and update `CURRENT.md`.
