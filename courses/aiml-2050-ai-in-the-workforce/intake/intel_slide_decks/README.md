# Intel Slide Decks Dropzone (`intake/intel_slide_decks/`)

Drop all raw Intel PowerPoint (`.pptx`) or PDF (`.pdf`) slide decks into this folder when you have them.

---

## What Happens When Decks Are Dropped Here
1. **Automated Extraction**:
   - Slide text, speaker notes, code snippets, and diagrams can be programmatically parsed using `python-pptx` or pdf extractors.
   - The workspace's `course-intake-scanner` can scan all decks across this folder to extract core competencies, concept hierarchies, and key topics.
2. **Pedagogical Alignment**:
   - The extracted topics will be cross-referenced against the `table_of_contents.md` and synthesized into the 8-week block structure.
3. **Slide Deck Re-Generation**:
   - We can re-render institutional, WCAG 2.1 AAA high-contrast 16:9 widescreen slides for each week using the workspace's `slide-deck-generator` skill, combining the best Intel diagrams with LCCC course branding.

---

## File Naming Convention
Drop files here using clear unit numbering when available (e.g., `Intel_Agentic_Unit_01.pptx`, `Intel_Agentic_Unit_02.pdf`, etc.).
