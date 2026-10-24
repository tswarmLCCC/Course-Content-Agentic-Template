---
name: slide-deck-generator
description: >-
  Programmatically generates 16:9 widescreen, WCAG 2.1 AAA high-contrast PowerPoint (.pptx)
  presentations adhering to the 5 universal slide archetypes and institutional design standards.
---

# Slide Deck Generation Engine Skill

This skill provides programmatic PowerPoint slide deck generation adhering to institutional standards for higher education and enterprise training.

## Core Capabilities
- **Widescreen 16:9 Output:** Formats slides to `13.333" x 7.5"` widescreen canvas.
- **WCAG 2.1 AAA Contrast:** Strict navy, slate, ice blue, and gold color palettes.
- **5 Proven Slide Archetypes:**
  1. Split-Hero Title Slide
  2. High-Contrast Section Divider Slide
  3. Two-Column Comparison / Architecture Slide
  4. Full-Width Sequential Flow / Process Slide
  5. Code Syntax Container Slide (strict left-aligned monospace font)
- **100% Speaker Notes Coverage:** Injects instructional commentary, live-coding prompts, and common student pitfalls into PPTX notes.

## How to Execute
```python
from scripts.slide_engine import SlideEngine

prs = SlideEngine.create_presentation()

# 1. Title Slide
SlideEngine.add_title_slide(
    prs,
    org_badge="LCCC",
    course_name="CMAP 1815: Modern SQL",
    unit_title="Unit 01: Relational Fundamentals",
    unit_subtitle="Selection, Projection & Data Filtering",
    meta_info="Instructor: Tim Swarm | LCCC Computer Science"
)

# 2. Section Divider
SlideEngine.add_section_divider(
    prs,
    section_num="SECTION 01",
    section_title="The Relational Model",
    subtitle="Why tabular structure beats hierarchical storage"
)

# 3. Two-Column Card
SlideEngine.add_two_column_slide(
    prs,
    badge="Architecture",
    title="Declarative vs. Imperative Paradigms",
    col1_title="Declarative (SQL)",
    col1_points=["Describe WHAT data you need", "Query planner decides execution", "Engine optimizes paths"],
    col2_title="Imperative (Python/C)",
    col2_points=["Specify HOW to retrieve step-by-step", "Manual nested loops", "Hard-coded memory allocations"],
    notes="Emphasize that SQL abstracts away the underlying disk scan algorithm."
)

prs.save("output/unit_01_presentation.pptx")
```
