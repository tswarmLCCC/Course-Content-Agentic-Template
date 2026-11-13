# Implementation Plan: Teach-First Conceptual Bridges (Units 2–8)

- **Spec**: [spec.md](spec.md)

## Strategy
1. Upgrade **Unit 2** `reading.md` Section 2b (`.filter()`, `.with_columns()` + `.alias()`, `.shift(1).over()`, and whole-column `.mean()`/`.std()` broadcasting) as the gold-standard pattern.
2. Audit and upgrade **Units 3–8** `reading.md` Section `2b` (and any other abrupt `Just as...` / code-first transitions) using the same 3-step Teach-First pattern:
   - **Unit 3**: NumPy `(H, W, C)` arrays vs. Python lists, OpenCV `imread` / `cvtColor` / `resize` / `copyMakeBorder` mechanics & general use before applying to truck letterboxing & YOLO labels.
   - **Unit 4**: Python `re` (regex) & string splitting vs. overlapping semantic chunking + ChromaDB vector collections & metadata before applying to maintenance manuals.
   - **Unit 5**: Local Python functions vs. HTTP endpoints, Pydantic `BaseModel` type contracts, and FastAPI routing overall before applying to logistics delay/route APIs.
   - **Unit 6**: Direct function calls vs. JSON Schema self-description, parameter guardrails, and JSON-RPC 2.0 envelopes overall before applying to MCP fleet tools.
   - **Unit 7**: Linear scripts vs. Directed Acyclic Graphs (DAGs), `@asset` dependencies, exponential backoff retries, and Dead-Letter Queues overall before applying to fleet heartbeats.
   - **Unit 8**: Local `venv` vs. Docker container layers, `pytest` fixture contracts, and blind evaluation batches overall before applying to the capstone defense.
3. Sync all updated `reading.md` files to `student_sandbox_template/units/*/study_guide.md`, push to GitHub, and rebuild `.imscc` + `.pdf`.

