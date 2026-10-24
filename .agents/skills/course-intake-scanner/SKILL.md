---
name: course-intake-scanner
description: >-
  Scans unstructured course assets, legacy decks, lecture transcripts, and brainstorms
  across knowledge drop zones to scaffold a structured competency map and course plan.
---

# Course Intake Scanner & Scaffolder Skill

This skill automates the intake and cataloging of unstructured curriculum materials into structured course outlines.

## Drop Zones Cataloged
- `knowledge_dump/raw_syllabi/`: Unformatted syllabus drafts and outlines.
- `knowledge_dump/legacy_decks/`: Previous PowerPoint slides and PDF presentations.
- `knowledge_dump/lecture_notes_and_transcripts/`: Raw video transcripts, audio logs, and classroom notes.
- `knowledge_dump/reference_literature/`: Technical documentation, cheat sheets, and academic papers.
- `knowledge_dump/ideas_and_brainstorms/`: Loose bullet points, wishlists, and project ideas.

## How to Execute
```bash
python scripts/intake_scanner.py
```
Output: Generates `scaffolded_course_plan.md` mapping inventoried files to target course competencies.
