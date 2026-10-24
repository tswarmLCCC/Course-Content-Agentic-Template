# Specification 004: OER Readings & Video-Integrated Instructional Architecture

## Status
- **Course**: `cosc-2060-data-engineering` (COSC 2060: Modern Data Engineering & AI Infrastructure)
- **Active Stage**: Stage 1 — Specify
- **Author**: Antigravity Assistant & Faculty Lead
- **Target Unit**: Unit 01 (Vectorized In-Process OLAP & Point-in-Time Joins)

---

## 1. Problem Statement & User Intent
The previous iteration generated synthetic, isolated text for the reading and lecture pages without grounding student learning in authoritative, external Open Educational Resources (OER) or real-world documentation. Furthermore, asynchronous video instruction was missing or disjointed.

The user mandate requires:
1. **Curate Real External OER Materials**: Research and link to authoritative, open documentation and technical references (DuckDB, Apache Arrow, Parquet, temporal leakage).
2. **Build Instruction On Top Of (Not In Place Of) OERs**: Author the conceptual deep dives, mental models (e.g., "Filing Cabinets vs. Columnar Straws"), real-world catastrophe narratives ($10M Delivery Delay), and hands-on query walkthroughs as an instructional layer that synthesizes and frames those external readings.
3. **Embed High-Quality Video Lectures**: Embed verified 16:9 YouTube video players with exact timestamps and external watch links directly into the Canvas WikiPage.
4. **Adhere to the Proven 4-Chapter DesignPLUS Architecture**: Follow the established structure of `ref/unit_reading_example.html` with:
   - Chapter 1: Instructor Lecture & Conceptual Deep Dive
   - Chapter 2: Required Readings & Authoritative Tutorial Guides
   - Chapter 3: Required Micro-Video Lectures (Embedded 16:9 players with timestamps)
   - Chapter 4: Institutional Video Lecture Embeds
5. **Prototype Unit 1 First**: Deliver a complete, high-fidelity prototype slice of Unit 1 for user inspection before replicating across Units 2–8.

---

## 2. Target Audience & Pedagogical Context
- **Audience**: College Sophomores (2nd-year undergraduates in Computer Science / Data Science).
- **Prerequisites**: Introductory SQL (SELECT, FROM, WHERE, simple joins) and introductory Machine Learning (features, labels, train/test splits, scikit-learn).
- **Cognitive Load Guardrails**: Concrete physical analogies before abstract algebraic syntax; defensive SQL design (why models fail when trained on future data) before mathematical window definitions.

---

## 3. EARS Requirements Specification

### Chapter 1: Instructor Lecture & Conceptual Deep Dive
- **EARS-001 (Ubiquitous)**: The page shall introduce Unit 1 with measurable Bloom's taxonomy objectives bridging introductory SQL/ML with defensive AI data engineering.
- **EARS-002 (Event - Problem Context)**: When framing the necessity of temporal data engineering, the lecture shall present the "$10M Delivery Delay" case study demonstrating how naive SQL joins cause look-ahead bias and production model collapse.
- **EARS-003 (Ubiquitous)**: The lecture shall explain physical storage models using the "Row Filing vs. Columnar Straws" mental model, contrasting OLTP (PostgreSQL, tuple-at-a-time, cache misses) with OLAP (DuckDB, vectorized chunks, SIMD execution).
- **EARS-004 (Ubiquitous)**: The lecture shall demonstrate step-by-step query construction progressing from naive failure, to window function lagging (`ROWS BETWEEN 5 PRECEDING AND 1 PRECEDING`), to native DuckDB `ASOF JOIN`.
- **EARS-005 (Ubiquitous)**: The lecture shall include interactive self-check questions, guided code walkthroughs, and an FAQ resolving common student traps (e.g., `<` vs. `<=`, null handling, column order in `USING`).

### Chapter 2: Required Readings & Authoritative Tutorial Guides
- **EARS-006 (Ubiquitous)**: Chapter 2 shall link directly to at least five verified, authoritative external OER/documentation resources:
  1. DuckDB Official `ASOF JOIN` Query Syntax Reference (`https://duckdb.org/docs/sql/query_syntax/asof_join`).
  2. DuckDB Engineering Blog: Fuzzy Temporal Lookups (`https://duckdb.org/2023/09/15/asof-join-fuzzy-temporal-lookups.html`).
  3. Apache Arrow Columnar In-Memory Architecture (`https://arrow.apache.org/overview/`).
  4. DuckDB Parquet Ingestion & Pushdown Optimization (`https://duckdb.org/docs/data/parquet/overview`).
  5. DuckDB Window Functions Specification (`https://duckdb.org/docs/sql/window_functions`).
- **EARS-007 (Ubiquitous)**: Every external reading link shall include a 2–3 sentence instructional blurb explaining exactly what the student must extract from the reading and how it relates to their weekly lab.

### Chapter 3: Required Micro-Video Lectures (Embedded)
- **EARS-008 (Ubiquitous)**: Chapter 3 shall embed responsive 16:9 YouTube iframes (`class="dp-embed-wrapper"`, `padding-bottom: 56.25%`, `loading="lazy"`) with title attributes and accessible direct watch links:
  1. Fireship: *DuckDB in 100 Seconds* (`uHm6FEb2Re4`).
  2. CMU Database Group (Prof. Andy Pavlo): *Storage Models & Database Compression (NSM vs. DSM)* (`5gXn5fLkbM0`, starting at 15:20).
  3. Bill Wallis: *SQL ASOF Join in DuckDB & Snowflake* (`zy89zKipsQg`).
  4. *Feature Engineering: Point-in-Time Correctness & Avoiding Data Leakage* (`T1dJfh1KlYA`).
- **EARS-009 (Ubiquitous)**: Each video item shall display a prominent title, timestamp annotation, iframe container, and fallback external hyperlink opening in a new tab (`target="_blank" rel="noopener"`).

### Chapter 4: Institutional Video Lecture Embeds
- **EARS-010 (Ubiquitous)**: Chapter 4 shall provide an institutional video lecture container with dashed borders and placeholder slots for campus recordings, announcements, and local walkthroughs.

### Packaging & Compiler Integration
- **EARS-011 (Ubiquitous)**: The portable cartridge compiler (`build_course.py`) shall compile the 4-chapter structure into `wiki_content/unit-01-readings.html` using DesignPLUS accordion panels (`div.dp-panel-group` with `h2.dp-panel-heading` and `div.dp-panel-content` within `div.dp-panels-wrapper.dp-accordion-plus`).
- **EARS-012 (Ubiquitous)**: The syllabus button on `home-page.html` shall link to `$WIKI_REFERENCE$/pages/{p_orient_syl_id}` with `data-course-type="wikiPages"` to guarantee zero broken links in Canvas.
- **EARS-013 (Ubiquitous)**: All generated HTML deliverables shall conform to ADR-001 (WCAG 2.1 AA) and ADR-002 (Spec-Driven Traceability).

---

## 4. Out of Scope
- Modifying Units 2–8 content files until the Unit 1 prototype is approved by the user.
- Modifying DesignPLUS color tokens, primary palette (#1e3a8a, #2563eb), or core CSS layout.
- Adding third-party external Python dependencies to `canvas-course-builder` (must remain standard library only).
