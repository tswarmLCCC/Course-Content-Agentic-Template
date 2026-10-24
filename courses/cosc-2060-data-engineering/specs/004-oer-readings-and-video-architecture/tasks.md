# Tasks 004: OER Readings & Video-Integrated Instructional Architecture

## Status
- **Course**: `cosc-2060-data-engineering`
- **Active Stage**: Stage 3 — Tasks
- **Preceding Plan**: [plan.md](file:///c:/dev/Course-Content-Agentic-Template/courses/cosc-2060-data-engineering/specs/004-oer-readings-and-video-architecture/plan.md)

---

## Task Decomposition & Execution Order

- [x] **Task 1: Author Unit 1 4-Chapter Reading Source Document**
  - **Description**: Rewrite `courses/cosc-2060-data-engineering/units/unit_01_relational_foundations/reading.md` (and copy to `courses/cosc-2060-data-engineering/content/readings/unit_01_relational_foundation.md`) to embody the 4-chapter structure:
    - Chapter 1: Instructor Lecture & Conceptual Deep Dive (The $10M Delivery Delay, Row Filing vs. Columnar Straws, step-by-step query construction, guided practice, FAQ).
    - Chapter 2: Required Readings & Authoritative Tutorial Guides (DuckDB ASOF JOIN, DuckDB Blog, Apache Arrow, Parquet overview, DuckDB Window Functions).
    - Chapter 3: Required Micro-Video Lectures (Fireship DuckDB `uHm6FEb2Re4`, CMU Andy Pavlo `5gXn5fLkbM0`, Bill Wallis ASOF join `zy89zKipsQg`, Feature Engineering `T1dJfh1KlYA`).
    - Chapter 4: Institutional Video Lecture Embeds.
  - **Check**: Verify the markdown file contains exact headers for each of the 4 chapters and valid URLs for all external documentation and video IDs.

- [x] **Task 2: Enhance Compiler to Render 4-Chapter Accordion on Reading Pages**
  - **Description**: Update `.agents/skills/canvas-course-builder/build_course.py` (and `html_styler.py` if needed) so that when parsing reading pages with structured chapters (or `render_designplus_html`), it formats them into the standard DesignPLUS accordion panels (`div.dp-panels-wrapper.dp-accordion-plus` containing `div.dp-panel-group` with `h2.dp-panel-heading` and `div.dp-panel-content`), matching `ref/unit_reading_example.html`.
  - **Check**: Run compiler and check that `_cartridge_build/wiki_content/unit-01-readings.html` contains the `dp-accordion-plus` container, the 4 panel groups, the embedded iframes, and the OER links.

- [x] **Task 3: Recompile Master Canvas Cartridge**
  - **Description**: Run `python .agents/skills/canvas-course-builder/build_course.py --config courses/cosc-2060-data-engineering/course_config.json --units courses/cosc-2060-data-engineering/units --output courses/cosc-2060-data-engineering/COSC_2060_Complete.imscc`.
  - **Check**: Ensure compile completes with 0 errors and generates `COSC_2060_Complete.imscc`.

- [x] **Task 4: Run Verification & Audit Script**
  - **Description**: Execute a verification script that audits:
    1. `home-page.html` for working `$WIKI_REFERENCE$/pages/{p_orient_syl_id}` syllabus link.
    2. `unit-01-readings.html` for 4-panel accordion structure, iframe embeds (`dp-embed-wrapper`), and external OER hyperlinks with `rel="noopener"`.
    3. WCAG compliance (iframe titles, color contrast, table headers).
  - **Check**: Verification script outputs `PASS` across all criteria.

- [x] **Task 5: Present Prototype Slice to User**
  - **Description**: Document findings and provide the user with clear evidence and links to inspect the Unit 1 prototype slice before proceeding to the remaining units.
  - **Check**: User reviewed and approved rollout via `ask_question`.

- [x] **Task 6: Author Unit 2 4-Chapter Reading Document (The Anomaly Engine)**
  - **Description**: Rewrite `units/unit_02_anomaly_detection_engines/reading.md` (and `content/readings/unit_02_anomaly_engine.md`) with 4 chapters:
    - Chapter 1: Polars Rust engine, Streaming LazyFrames, vectorized outlier detection (Z-score, IQR, Isolation Forest).
    - Chapter 2: Real OER readings (Polars User Guide, Scikit-Learn Outlier Detection, Apache Arrow IPC).
    - Chapter 3: Embedded videos (Rob Mulla Polars `VHqn7ufiilE`, StatQuest outlier detection, Arrow zero-copy).
    - Chapter 4: Institutional Video Lecture Embeds.
  - **Check**: Verify all 4 chapters, links, and iframes exist in markdown.

- [x] **Task 7: Author Unit 3 4-Chapter Reading Document (The Visual Sensor Layer)**
  - **Description**: Rewrite `units/unit_03_visual_sensor_and_multimodal_layer/reading.md` (and `content/readings/unit_03_visual_sensor_layer.md`) with 4 chapters:
    - Chapter 1: OpenCV image decoding, BGR vs RGB channels, aspect-ratio preserving letterboxing, YOLO format conversions.
    - Chapter 2: Real OER readings (OpenCV Docs, Ultralytics YOLO specs, Albumentations, PyTorch Vision).
    - Chapter 3: Embedded videos (PyTorch in 100s `ORMx45xqWkA`, OpenCV computer vision preprocessing, YOLO formats).
    - Chapter 4: Institutional Video Lecture Embeds.
  - **Check**: Verify all 4 chapters, links, and iframes exist in markdown.

- [x] **Task 8: Author Unit 4 4-Chapter Reading Document (Unstructured Text & Vector RAG)**
  - **Description**: Rewrite `units/unit_04_unstructured_text_and_vector_rag/reading.md` (and `content/readings/unit_04_unstructured_text_rag.md`) with 4 chapters:
    - Chapter 1: Tokenization, dense vector embeddings, chunking strategies, ChromaDB indexing, cosine similarity.
    - Chapter 2: Real OER readings (Hugging Face Sentence-Transformers, ChromaDB Docs, Pinecone Learning).
    - Chapter 3: Embedded videos (Vector Databases in 100s `klTvEwg3oJ4`, Sentence Transformers, ChromaDB RAG).
    - Chapter 4: Institutional Video Lecture Embeds.
  - **Check**: Verify all 4 chapters, links, and iframes exist in markdown.

- [x] **Task 9: Author Unit 5 4-Chapter Reading Document (Data as a Service)**
  - **Description**: Rewrite `units/unit_05_data_as_a_service_and_apis/reading.md` (and `content/readings/unit_05_data_as_a_service.md`) with 4 chapters:
    - Chapter 1: REST APIs for ML inference, async endpoints, Pydantic v2 schemas, serialization, latency benchmarking.
    - Chapter 2: Real OER readings (FastAPI Tutorial, Pydantic v2 Docs, Starlette/Uvicorn).
    - Chapter 3: Embedded videos (RESTful APIs in 100s `-MTSQjw5DrM`, Pydantic v2, FastAPI ML deployment).
    - Chapter 4: Institutional Video Lecture Embeds.
  - **Check**: Verify all 4 chapters, links, and iframes exist in markdown.

- [x] **Task 10: Author Unit 6 4-Chapter Reading Document (The Agentic Interface / MCP)**
  - **Description**: Rewrite `units/unit_06_agentic_interfaces_and_mcp/reading.md` (and `content/readings/unit_06_agentic_interface_mcp.md`) with 4 chapters:
    - Chapter 1: Autonomous AI tool calling, Anthropic Model Context Protocol (MCP), JSON-RPC 2.0, Ollama local bridges.
    - Chapter 2: Real OER readings (MCP Official Spec, Anthropic Tool Use, JSON-RPC 2.0 Spec).
    - Chapter 3: Embedded videos (Matt Pocock MCP tutorial, MCP Server with Python & SQLite, LLM Tool Calling).
    - Chapter 4: Institutional Video Lecture Embeds.
  - **Check**: Verify all 4 chapters, links, and iframes exist in markdown.

- [x] **Task 11: Author Unit 7 4-Chapter Reading Document (Orchestration & Automation)**
  - **Description**: Rewrite `units/unit_07_orchestration_and_automation/reading.md` (and `content/readings/unit_07_orchestration_automation.md`) with 4 chapters:
    - Chapter 1: Directed Acyclic Graphs (DAGs), Declarative Software-Defined Assets (SDA), idempotency, backfilling.
    - Chapter 2: Real OER readings (Dagster Docs, Prefect Docs, DataOps principles).
    - Chapter 3: Embedded videos (Dagster Data Orchestration, Software-Defined Assets, Automated Pipelines).
    - Chapter 4: Institutional Video Lecture Embeds.
  - **Check**: Verify all 4 chapters, links, and iframes exist in markdown.

- [x] **Task 12: Author Unit 8 4-Chapter Reading Document (Capstone Defense & Production)**
  - **Description**: Rewrite `units/unit_08_capstone_defense_and_production/reading.md` (and `content/readings/unit_08_capstone_defense.md`) with 4 chapters:
    - Chapter 1: Production containerization, multi-stage Dockerfiles, non-root security, reproducibility, blind batch defense.
    - Chapter 2: Real OER readings (Docker Best Practices, Multi-stage Builds, OWASP Container Security).
    - Chapter 3: Embedded videos (Docker in 100s `Gjnup-PuquQ`, Docker for Data Engineering, Multi-stage builds).
    - Chapter 4: Institutional Video Lecture Embeds.
  - **Check**: Verify all 4 chapters, links, and iframes exist in markdown.

- [x] **Task 13: Recompile Master Canvas Cartridge & Comprehensive 8-Unit Audit**
  - **Description**: Recompile `COSC_2060_Complete.imscc` and execute an end-to-end audit verifying that all 8 unit reading pages contain the 4-panel DesignPLUS accordions, valid OER documentation links, and embedded 16:9 YouTube video players.
  - **Check**: Audit passes with 0 failures across all 8 units.

- [x] **Task 14: Update Living Documentation (`README.md` & `CURRENT.md`)**
  - **Description**: Update repository documentation to reflect the complete 8-unit OER and video-integrated curriculum architecture.
  - **Check**: Documentation files updated and verified.
