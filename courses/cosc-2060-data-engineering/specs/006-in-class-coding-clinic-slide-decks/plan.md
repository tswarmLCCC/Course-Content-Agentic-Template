# Implementation Plan: In-Class Slot 2 Coding Clinic Slide Decks

- **ID**: `specs/006-in-class-coding-clinic-slide-decks`
- **Status**: In Review
- **Created**: 2026-10-24
- **Associated Spec**: [spec.md](file:///c:/dev/Course-Content-Agentic-Template/courses/cosc-2060-data-engineering/specs/006-in-class-coding-clinic-slide-decks/spec.md)

---

## 1. Architectural Strategy & Design System

### Core Engine & Portability
- To preserve monorepo sandboxing and avoid code duplication across courses, all presentations will be generated programmatically using `.agents/skills/slide-deck-generator/scripts/slide_engine.py`.
- Slide generation will be orchestrated via a reusable course script: `courses/cosc-2060-data-engineering/scripts/generate_slide_decks.py` executed via `C:\Python\Python311\python.exe`.
- Deliverables will be placed in `courses/cosc-2060-data-engineering/content/slides/`.

### 16:9 Widescreen Canvas & WCAG 2.1 AAA Color System
- Dimensions: `13.333" x 7.5"` (SlideEngine default).
- Background: Canvas Light Slate (`#F8FAFC`) for cards, Dark Navy (`#002055`) for Hero/Section dividers.
- Cards: Ice Blue (`#F3F7FC` / `#C2D6EC` border) and Warm Cream (`#FFFDF0` / `#F0CD5A` border).
- Code Containers: Midnight Slate (`#111827` / `#374151` border) with high-contrast Cyan text (`#8AD4FF`) strictly left-aligned in `Consolas`.
- Fonts: Arial (Headlines/Badges), Calibri (Body), Consolas (Code).

### 12-Slide Archetype Template per Unit
Every unit deck follows an identical, rigorously timed 75-minute instructional arc:
1. **Slide 1**: `build_split_hero_title` — Split-Hero Title Slide (LCCC, Course Code, Unit Name, Instructor).
2. **Slide 2**: `build_two_column` — Clinic Flow & 75-Min Agenda (Outage Review, Sparring, Notebook, Defense).
3. **Slide 3**: `build_full_width_card` — Production Incident Retrospective & Financial/SLA Outage Impact.
4. **Slide 4**: `build_section_divider` — Section 01: The Naive Data Science Prototype.
5. **Slide 5**: `build_code_slide` — The Naive Script & The Scaling Wall (Code Container + Left Spec Card).
6. **Slide 6**: `build_section_divider` — Section 02: Modern Data Engineering Engine.
7. **Slide 7**: `build_two_column` — Architectural Mechanics (Naive Single-Threaded vs Modern Engine).
8. **Slide 8**: `build_code_slide` — Production Refactoring & Engine Syntax (Code Container + Left Spec Card).
9. **Slide 9**: `build_full_width_card` — Benchmarks, Profiling & Output Parity Verification.
10. **Slide 10**: `build_section_divider` — Section 03: Live Sparring & Defensive Hardening.
11. **Slide 11**: `build_two_column` — "I Do, We Do" Notebook Clinic & Take-Home Defensive Challenge.
12. **Slide 12**: `build_full_width_card` — Unit Takeaways, Architectural Summary & Bridge to Slot 3 Lab.

---

## 2. Unit Content Mapping (Units 1–8)

| Unit | Title & Subtitle | Incident / War Story | Naive DS Prototype | DE Engine & Benchmark | Defensive Challenge |
|:---:|:---|:---|:---|:---|:---|
| **01** | Relational Foundations: Point-in-Time Event Joins | Fleet telemetry join timeout ($180k delay penalties) | Pandas `pd.merge_asof` (Single-core, memory duplicate) | DuckDB `ASOF LEFT JOIN` (Parquet pushdown, 4.4x speedup) | Unsorted timestamps & null sensor handling |
| **02** | Time-Series Engines: Rolling Anomaly Windows | IoT server memory blowup ($45k cloud compute spike) | Pandas `groupby.apply` (Python GIL, serialized loop) | Polars Lazy Expressions `.over()` (SIMD, 18.9x speedup) | Sudden vehicle disconnection / missing time buckets |
| **03** | Multimodal Vision: High-Throughput Tensor Ingestion | Drone camera buffer overflow (Framerate dropped to 12 FPS) | PIL + Matplotlib (Slow decoding, non-contiguous copy) | OpenCV Letterbox + C-Contiguous (150 FPS, zero-copy) | Corrupt EXIF orientations & partial JPEGs |
| **04** | Unstructured Text: Dense Vector Retrieval & RAG | Keyword search failure during critical IT outage | Scikit-learn TF-IDF (Lexical only, misses synonyms) | ChromaDB HNSW Indexing (Dense embeddings, Rank #1 recall) | Out-of-vocabulary terms & metadata injection |
| **05** | Data-as-a-Service: Production REST Serving | Silent production outage from unvalidated pickle | Raw Python dict / unvalidated Pickle (Memory leak, crash) | FastAPI + Pydantic v2 (Async I/O, 2.3ms, HTTP 422 defense) | Malformed JSON payloads & schema drift |
| **06** | Agentic Interfaces: Model Context Protocol (MCP) | Hallucinated parameters & brittle LLM prompt parsing | Manual prompt string concatenation (Regex parsing fail) | MCP Server JSON-RPC 2.0 (`tools/call`, 147k calls/sec) | Tool schema mismatch & unexpected runtime errors |
| **07** | Pipeline Orchestration: Software-Defined Asset DAGs | Multi-hour rerun cascade after upstream failure | Monolithic Jupyter cells (Linear top-to-bottom script) | Software-Defined Asset DAG (Topological sort, cache reuse) | Upstream schema drift & cycle detection |
| **08** | Capstone Defense: Docker & Automated CI/CD Gates | "Works on my machine" deployment disaster | Ad-hoc manual scripts (No tests, untracked env) | Dockerized Pytest Quality Gate (DLQ, test defense) | Silent upstream data corruption & DLQ exhaustion |

---

## 3. Implementation Steps

1. **Step 1**: Create `courses/cosc-2060-data-engineering/scripts/generate_slide_decks.py` encoding the rich metadata, incident cases, code snippets, benchmarks, and 100% complete speaker notes for all 8 decks.
2. **Step 2**: Execute generator via `C:\Python\Python311\python.exe` to produce all 8 `.pptx` presentations into `courses/cosc-2060-data-engineering/content/slides/`.
3. **Step 3**: Develop and run an automated validation script `scratch/verify_slide_decks.py` to audit:
   - 8 decks present
   - 16:9 canvas dimensions (`13.333" x 7.5"`)
   - Exactly 12 slides per deck (96 total slides)
   - 100% non-empty speaker notes across all 96 slides
   - Monospace font and left-alignment on all code containers.
4. **Step 4**: Update unit drill guides, flipped classroom guides, course README, and master README with slide deck links.
5. **Step 5**: Conduct a pass/fail verification audit against all EARS requirements in `spec.md`.

---

## 4. Verification Strategy & Acceptance Tests
- Automated script: `scratch/verify_slide_decks.py`
- Visual sampling: Check slide structure, code syntax contrast, and speaker notes formatting.
- Audit criteria: 100% pass across all 96 slides.
