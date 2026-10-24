# Implementation Plan: Comprehensive Content & Tech Block Remediation

- **ID**: `specs/007-comprehensive-content-and-tech-block-remediation`
- **Status**: Approved
- **Created**: 2026-10-24
- **Associated Spec**: [spec.md](file:///c:/dev/Course-Content-Agentic-Template/courses/cosc-2060-data-engineering/specs/007-comprehensive-content-and-tech-block-remediation/spec.md)

---

## 1. Architectural Strategy & Content Reorganization

### A. Siloing Instructor Scripts vs. Student Practice
- **Current Issue**: Flipped classroom scripts (teleprompter cues, camera directions, synchronous agendas) were placed into `drills.md`, causing student drill pages in Canvas to display recording instructions and raw mermaid text.
- **Remediation**:
  1. Save instructor flipped classroom guides and video scripts into `courses/cosc-2060-data-engineering/units/unit_XX_*/teaching_notes.md`.
  2. `build_course.py` automatically detects `teaching_notes.md` via `find_file(u_dir, ["teaching.*notes"])` and compiles it into Canvas Item 8: `[Instructor Guide] Unit X Teaching Notes & Solutions` (Workflow State: Unpublished, hidden from students).
  3. Author dedicated, high-rigor student-facing `drills.md` for every unit featuring interactive `<details><summary>` self-checks, code execution order traces, and gotcha callouts.

### B. Cleaning Lab Guides (`lab_guide.md`)
- **Current Issue**: Lab guides began with an un-scaffolded Section 1 containing a large Python script with empty `# [YOUR QUERY HERE]` placeholders before introducing the actual scenario and starter template.
- **Remediation**:
  1. Remove the redundant Section 1 placeholder dump.
  2. Directly open with the real-world industrial scenario and business context.
  3. Ensure the starter code template is completely self-contained with embedded synthetic data generation (eliminating reliance on missing external files or confusing multi-path commands).
  4. Ensure grading rubrics and test assertion guidelines are crystal clear.

### C. Fixing Broken Relative Navigation (`overview.md`)
- **Current Issue**: Overview files link to `reading.md`, `drills.md`, `lab_guide.md` using relative Markdown links that 404 in Canvas LMS.
- **Remediation**:
  1. Update `overview.md` across all 8 units to use styled visual roadmap cards (e.g. `Step 1: Required Readings`, `Step 2: Practice Drills`, `Step 3: Applied Lab`, `Step 4: Knowledge Check`) that describe the weekly learning path without dead relative file links.

### D. Eliminating Dead Local URLs & Broken Tech Blocks
- **Current Issue**: `file:///c:/...` local absolute URLs and raw ````mermaid code blocks break in student browsers.
- **Remediation**:
  1. Strip all `file:///` URLs from Canvas source files.
  2. Replace raw ````mermaid flowcharts with clean, responsive semantic HTML tables or styled CSS flexbox cards.

---

## 2. Unit-by-Unit Implementation Arc

| Unit | Title | Drills Focus (`drills.md`) | Lab Guide Polish (`lab_guide.md`) | Instructor Silo (`teaching_notes.md`) |
|:---:|:---|:---|:---|:---|
| **01** | Relational Foundations | Look-ahead bias diagnostics, temporal window execution trace, DuckDB ASOF join syntax traps | Self-contained mock data generator, clear 100-pt rubric, zero leakage assertion | Flipped guide + 2 video scripts transferred from `unit_01_guide.md` |
| **02** | Anomaly Engines | Eager vs. lazy expression traces, Polars `.over()` partition gotchas, tank volume overflow math | Embedded fuel telemetry synthesizer, self-contained Isolation Forest starter | Flipped guide + 2 video scripts transferred from `unit_02_guide.md` |
| **03** | Visual Sensor Layer | Letterbox padding math derivations, BGR to RGB channel inversions, YOLO box normalization math | Clean camera manifest generator, image padding starter without placeholder dump | Flipped guide + 2 video scripts transferred from `unit_03_guide.md` |
| **04** | Text & Vector RAG | Cosine similarity dot product traces, lexical vs dense search traps, ChromaDB metadata filter rules | Embedded synthetic runbook corpus, ChromaDB retrieval starter | Flipped guide + 2 video scripts transferred from `unit_04_guide.md` |
| **05** | Data-as-a-Service | HTTP 422 validation traces, async event loop blocking gotchas, Pydantic Field constraints | Self-contained FastAPI logistics server starter with TestClient | Flipped guide + 2 video scripts transferred from `unit_05_guide.md` |
| **06** | Agentic Interfaces | JSON-RPC message envelope traces, prompt injection vulnerabilities, tool schema validation | Embedded MCP tool handler starter, Claude/Cursor simulation | Flipped guide + 2 video scripts transferred from `unit_06_guide.md` |
| **07** | Pipeline Orchestration | Kahn's algorithm topological trace, in-degree count calculations, asset caching vs recomputation | Complete Software-Defined Asset DAG starter with cycle detection | Flipped guide + 2 video scripts transferred from `unit_07_guide.md` |
| **08** | Capstone Defense | Multi-stage Docker layer caching, Pytest assertion gate traces, Dead Letter Queue isolation rules | Hermetic container verification suite, blind evaluation batch starter | Flipped guide + 2 video scripts transferred from `unit_08_guide.md` |

---

## 3. Cartridge Rebuild & Verification Strategy

1. **Rebuild Cartridge**:
   ```bash
   python .agents/skills/canvas-course-builder/build_course.py --config courses/cosc-2060-data-engineering/course_config.json --units-dir courses/cosc-2060-data-engineering/units --output courses/cosc-2060-data-engineering/COSC_2060_Complete.imscc
   ```
2. **Automated Audit**:
   - Run `scratch/verify_cartridge_fix.py` to confirm manifest and module integrity.
   - Run `scratch/audit_content_hygiene.py` asserting:
     - Zero occurrences of `file:///` across all compiled HTML files in `_cartridge_build/`.
     - Zero occurrences of raw ````mermaid in compiled HTML.
     - Zero occurrences of `[CAMERA ON INSTRUCTOR]` in student-facing HTML pages.
     - Presence of unpublished Instructor Guide pages for all 8 units.
3. **Git Commit**:
   - Commit all changes cleanly to Git.
