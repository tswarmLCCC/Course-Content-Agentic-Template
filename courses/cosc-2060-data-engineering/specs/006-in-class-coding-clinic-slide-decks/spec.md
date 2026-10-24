# Feature Specification: In-Class Slot 2 Coding Clinic Slide Decks

- **ID**: `specs/006-in-class-coding-clinic-slide-decks`
- **Status**: In Review
- **Created**: 2026-10-24
- **Target Completion**: 45 minutes

---

## 1. Objective & Target Audience
- **Primary Persona**: Computer Science Instructor facilitating 75-minute synchronous classroom sessions (Slot 2 of the 4-slot model) and undergraduate students (sophomores) at Laramie County Community College (LCCC).
- **Problem Statement**: While students have asynchronous reading guides (Slot 1) and interactive Jupyter transition notebooks, instructors need a professional, high-rigor visual presentation to guide the 75-minute in-class coding clinic. Without structured visual slides, whiteboard sparring lacks anchor diagrams, incident retrospectives lose narrative urgency, and notebook transitions feel disorganized.
- **One Job**: Programmatically generate 8 production-grade 16:9 widescreen PowerPoint (`.pptx`) presentations (one per unit) adhering to WCAG 2.1 AAA contrast and the 5 universal slide archetypes, providing 100% speaker notes to orchestrate the Slot 2 live coding clinic.

---

## 2. Requirements (EARS Syntax)

### Universal Slide Design & Accessibility
- `REQ-01`: **Always**: Every presentation file **shall** be generated in native 16:9 widescreen format (`13.333" x 7.5"` canvas dimensions) using the workspace skill `.agents/skills/slide-deck-generator/scripts/slide_engine.py`.
- `REQ-02`: **Always**: Every presentation **shall** comply with WCAG 2.1 AAA high-contrast standards using the institutional color palette: Dark Navy (`#002055`), Canvas Light Slate (`#F8FAFC`), Ice Blue (`#F3F7FC`), Warm Cream (`#FFFDF0`), Midnight Slate (`#111827`), and Vibrant Gold (`#FFC001`).
- `REQ-03`: **Always**: Every slide containing code **shall** use Archetype 5 (Code Container) with strict left-aligned monospace font (`Consolas`), dark slate background (`#111827`), and high-contrast cyan syntax text (`#8AD4FF`).
- `REQ-04`: **Always**: Every slide across all 8 decks **shall** contain complete, non-empty instructor speaker notes with time management cues (e.g., `[10-25 min]`), class discussion prompts, and notebook execution instructions.

### Pedagogical Structure (Slot 2 Live Clinic Alignment)
- `REQ-05`: **Always**: Each unit deck **shall** contain 11 to 13 focused slides strictly following the 75-minute Slot 2 clinic progression:
  1. *Slide 1 (Split-Hero Title)*: Course code, Unit number, Clinic topic, and Instructor metadata.
  2. *Slide 2 (Two-Column)*: Clinic Agenda & 75-Minute Session Roadmap.
  3. *Slide 3 (Full-Width Card)*: Incident Retrospective & Production Outage Case Study.
  4. *Slide 4 (Section Divider)*: Section 1 — The Naive Data Science Prototype.
  5. *Slide 5 (Code Container)*: The Naive Code & Bottleneck (Pandas/Scikit-learn/PIL/Pickle limitations).
  6. *Slide 6 (Section Divider)*: Section 2 — The Modern Data Engineering Engine.
  7. *Slide 7 (Two-Column Comparison)*: Architectural Mechanics (Why the Engine Wins: SIMD, Columnar, Async, DAG).
  8. *Slide 8 (Code Container)*: Production Engine Refactoring & Syntax Leap.
  9. *Slide 9 (Full-Width Card)*: Benchmark, Profiling & Mathematical Parity Gate.
  10. *Slide 10 (Section Divider)*: Section 3 — Live Sparring & Defensive Engineering.
  11. *Slide 11 (Two-Column)*: "I Do, We Do" Notebook Clinic & Take-Home Challenge.
  12. *Slide 12 (Full-Width Card)*: Summary Key Takeaways & Bridge to Slot 3 Lab.
- `REQ-06`: **When** presenting the Incident Retrospective (Slide 3), the slide **shall** highlight the exact business cost, downtime, or latency regression observed in production before modern engine refactoring.
- `REQ-07`: **When** presenting the benchmark (Slide 9), the slide **shall** cite the verified performance numbers from the automated test runs (e.g., DuckDB 4.4x, Polars 18.9x, OpenCV 150 FPS, ChromaDB Rank #1 recall, FastAPI 2.3ms, MCP 147k calls/sec).
- `REQ-08`: **While** the instructor presents Slide 11, the speaker notes **shall** direct students to launch their local Jupyter notebook (`unit_XX_ds_to_engine.ipynb`) and complete the designated live refactoring cells.

### Unit Scope & Deliverables
- `REQ-09`: **Always**: The generator **shall** create 8 standalone `.pptx` presentations saved to `courses/cosc-2060-data-engineering/content/slides/`:
  - `unit_01_coding_clinic.pptx`: Relational Foundations (Pandas `merge_asof` $\rightarrow$ DuckDB `ASOF LEFT JOIN`).
  - `unit_02_coding_clinic.pptx`: Time-Series Anomaly Detection (Pandas `groupby.apply` $\rightarrow$ Polars Lazy Expressions).
  - `unit_03_coding_clinic.pptx`: Computer Vision Ingestion (PIL/Matplotlib $\rightarrow$ OpenCV C-Contiguous Tensors).
  - `unit_04_coding_clinic.pptx`: Unstructured Text & Vector RAG (TF-IDF Lexical $\rightarrow$ ChromaDB Dense Vector Search).
  - `unit_05_coding_clinic.pptx`: Data-as-a-Service APIs (Unvalidated Pickle $\rightarrow$ FastAPI + Pydantic v2 Async API).
  - `unit_06_coding_clinic.pptx`: Agentic Interfaces (Manual String Formatting $\rightarrow$ MCP JSON-RPC 2.0 Server).
  - `unit_07_coding_clinic.pptx`: Pipeline Orchestration (Monolithic Linear Cells $\rightarrow$ Software-Defined Asset DAG).
  - `unit_08_coding_clinic.pptx`: Capstone Production Defense (Fragile Scripts $\rightarrow$ Docker Container + Pytest Gate).

---

## 3. Deliberately Out of Scope
- Modifying the underlying Jupyter transition notebooks (already verified and complete).
- Copying python slide scripts into course content directories (violates monorepo sandboxing; must use `.agents/skills/slide-deck-generator/`).
- Generating 4:3 standard aspect ratio decks or non-standard color templates.

---

## 4. Acceptance Criteria & Definition of Done
- [ ] All 8 `.pptx` presentation files exist in `courses/cosc-2060-data-engineering/content/slides/`.
- [ ] Every slide deck has exactly 12 slides matching the required archetypes and 16:9 widescreen layout.
- [ ] 100% of slides contain non-empty speaker notes for the instructor.
- [ ] Code slides strictly enforce left-aligned monospace font with syntax-highlighted contrast.
- [ ] Automated verification script validates all 8 presentations without errors.
- [ ] Course documentation and README updated with slide deck references.
