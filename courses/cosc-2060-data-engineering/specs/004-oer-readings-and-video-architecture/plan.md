# Implementation Plan 004: OER Readings & Video-Integrated Instructional Architecture

## Status
- **Course**: `cosc-2060-data-engineering`
- **Active Stage**: Stage 2 — Plan
- **Preceding Spec**: [spec.md](file:///c:/dev/Course-Content-Agentic-Template/courses/cosc-2060-data-engineering/specs/004-oer-readings-and-video-architecture/spec.md)

---

## 1. Architectural Strategy & Reference Model
This plan transitions the Unit 1 Reading Page from a plain text markdown dump to the proven 4-chapter DesignPLUS interactive hub established in `ref/unit_reading_example.html`:

```
<div id="dp-wrapper" class="dp-wrapper ...">
  <header class="dp-header ..."> Unit 01: Required Readings, Concepts & Video Lectures </header>
  <div class="dp-content-block"> Unit Overview & 4-Chapter Navigation Roadmap </div>
  <div class="dp-panels-wrapper dp-accordion-plus ...">
    1. Chapter 1: Instructor Lecture & Conceptual Deep Dive (Authored Synthesis)
    2. Chapter 2: Required Readings & Authoritative Tutorial Guides (Real OER Links)
    3. Chapter 3: Required Micro-Video Lectures (Embedded 16:9 YouTube Players)
    4. Chapter 4: Institutional Video Lecture Embeds (Campus Lecture Slot)
  </div>
</div>
```

---

## 2. Content Architecture: Unit 1

### Chapter 1: Instructor Lecture & Conceptual Deep Dive
Author an instructional synthesis that builds *on top of* the external readings rather than attempting to replace an entire database textbook:
1. **The $10M Delivery Delay**: Grounding narrative on look-ahead bias and model collapse when training on future weather observations.
2. **Row Filing vs. Columnar Straws**: Physical memory and disk layout analogy comparing PostgreSQL (NSM) with DuckDB/Arrow (DSM), cache locality, and vectorization.
3. **Defensive SQL Construction**:
   - Step 1: The naive query and why it produces 99% notebook accuracy and 51% production collapse.
   - Step 2: The window function workaround (`ROWS BETWEEN 5 PRECEDING AND 1 PRECEDING`).
   - Step 3: Native DuckDB `ASOF JOIN` with exact equality and temporal inequality (`ON routes.dep_time >= weather.obs_time`).
4. **Guided Code Walkthroughs**: Python + DuckDB scripts demonstrating how to ingest, join, and verify zero temporal leakage.
5. **Formative Knowledge Checks & FAQ**: Common edge cases (tie-breaking, missing prior values, performance comparison).

### Chapter 2: Required Readings & Authoritative Tutorial Guides
Curate 5 verified, authoritative external documentation guides:
1. **DuckDB `ASOF JOIN` Official Documentation**
   - URL: `https://duckdb.org/docs/sql/query_syntax/asof_join`
   - Description: Definitive reference for syntax, `ON` vs. `USING` clauses, tie-breaking rules, and NULL handling.
2. **DuckDB Engineering Blog: Fuzzy Temporal Lookups**
   - URL: `https://duckdb.org/2023/09/15/asof-join-fuzzy-temporal-lookups.html`
   - Description: Detailed breakdown of the merge-join pipeline and why ASOF join avoids expensive Cartesian products.
3. **Apache Arrow Columnar In-Memory Architecture**
   - URL: `https://arrow.apache.org/overview/`
   - Description: Foundational standard for zero-copy memory buffers, SIMD vectorization, and data interchange.
4. **DuckDB Parquet Ingestion & Pushdown Optimization**
   - URL: `https://duckdb.org/docs/data/parquet/overview`
   - Description: Practical guide to reading compressed columnar files with projection and filter pushdown.
5. **DuckDB Window Functions Reference**
   - URL: `https://duckdb.org/docs/sql/window_functions`
   - Description: Reference for frame clauses (`ROWS BETWEEN`), partitions, and rolling statistical aggregations.

### Chapter 3: Required Micro-Video Lectures (Embedded)
Embed 4 verified YouTube micro-lectures with 16:9 responsive wrappers, lazy loading, and direct timestamp links:
1. **Fireship: DuckDB in 100 Seconds**
   - Video ID: `uHm6FEb2Re4`
   - Duration / Start: Full (0:00)
   - Focus: High-velocity architectural overview of DuckDB and in-process OLAP.
2. **CMU Database Group (Prof. Andy Pavlo): Storage Models & Database Compression**
   - Video ID: `5gXn5fLkbM0`
   - Duration / Start: Starts at 15:20 (`?start=920`)
   - Focus: Deep dive into NSM (Row Stores) vs. DSM (Column Stores), memory bandwidth, and analytical query execution.
3. **Bill Wallis: SQL ASOF Join in DuckDB & Snowflake**
   - Video ID: `zy89zKipsQg`
   - Duration / Start: Full (0:00)
   - Focus: Live code demonstration of temporal timestamp alignment using ASOF join.
4. **Feature Engineering: Point-in-Time Correctness & Avoiding Data Leakage**
   - Video ID: `T1dJfh1KlYA`
   - Duration / Start: Full (0:00)
   - Focus: Why machine learning models fail when feature pipelines leak future event state.

### Chapter 4: Institutional Video Lecture Embeds
Campus-specific placeholder slot matching `ref/unit_reading_example.html` with dashed styling for faculty lecture recordings.

---

## 3. Toolchain & Compiler Integration
- Update `courses/cosc-2060-data-engineering/units/unit_01_relational_foundations/reading.md` (and corresponding markdown source in `content/readings/unit_01_relational_foundation.md`) to follow the 4-chapter standard.
- Update `canvas-course-builder/build_course.py`:
  - When rendering reading pages, if the markdown contains the 4 chapters (or when reading a structured reading markdown), render the page using `render_designplus_html` with the 4 accordion panels (`div.dp-panel-group` and `h2.dp-panel-heading`) matching `ref/unit_reading_example.html`.
- Run compiler to produce updated `COSC_2060_Complete.imscc`.
- Run verification script to confirm:
  - `home-page.html` has working wiki syllabus link.
  - `unit-01-readings.html` contains the 4-panel accordion, real OER links, and embedded 16:9 YouTube iframes.

---

## 4. Verification Protocol
1. **Visual & Structural Audit**: Inspect `_cartridge_build/wiki_content/unit-01-readings.html` to confirm all 4 chapters, iframes, and OER links are present.
2. **Link & Iframe Integrity Check**: Ensure all external URLs (DuckDB, Arrow, YouTube) are syntactically valid and use HTTPS with `rel="noopener"`.
3. **Cartridge Compilation**: Successfully compile `courses/cosc-2060-data-engineering/COSC_2060_Complete.imscc` without errors.
4. **Browser Subagent / Automated DOM Inspection**: Verify the rendered HTML in a headless or automated check to validate accordion layout and responsiveness.
