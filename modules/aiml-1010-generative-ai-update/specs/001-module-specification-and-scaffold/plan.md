# Technical & Architectural Plan: AIML 1010 Generative AI & Agentic Curriculum Update

- **Spec Reference**: [`spec.md`](./spec.md)
- **Status**: Executed & Verified

---

## 1. Technical Architecture & Approach

### A. Asset Extraction & Processing Pipeline
1. **Slide PDFs with Speaker Notes**:
   - Utilize host PowerPoint COM automation via PowerShell script (`export_slide_pdfs.ps1`) to export all `.pptx` decks directly into PDF with `PpPrintOutputType.ppPrintOutputNotesPages` (540x720 points portrait, slide at top, speaker notes at bottom).
   - Week 03 and Week 04 already have verified pre-rendered notes PDFs (`[Slides] Week 3 - GAI Prompt 1.pdf`, `[Slides] Week 4 - GAI Prompt 2.pdf`). The remaining 7 decks will be exported into `units/<module>/slides/` and unified into `web_resources/slides/`.

2. **Quiz Audit & QTI Compilation**:
   - Parse all 9 `[Quiz] ... .xlsx` files using Python openpyxl / zipfile parsing.
   - Run audit on questions:
     - Check grammar, options completeness (replace placeholders like "t" with substantive answers).
     - Verify correct answer key mapping against technical concepts in slide decks.
     - Add detailed rationales for each question.
   - Output clean Markdown quizzes following `unit_quiz_template.md`.
   - Compile each Markdown quiz using `qti_builder.py` into native QTI 1.2 XML structures.

3. **Discussion Topics (`imsdt_xmlv1p1`)**:
   - Canvas Common Cartridge stores discussions as two synchronized XML files:
     - `[topic_id].xml`: `<topic xmlns="http://www.imsglobal.org/xsd/imsccv1p1/imsdt_v1p1"><title>...</title><text texttype="text/html">...</text></topic>`
     - `[meta_id].xml`: `<topicMeta identifier="[meta_id]" xmlns="http://canvas.instructure.com/xsd/cccv1p0">...<topic_id>[topic_id]</topic_id><title>...</title><discussion_type>threaded</discussion_type>...</topicMeta>`
   - Formulate 3-4 rich discussion prompts per module replicating the exact style found in `ref/AIML 1010 Update/New Modules/aiml-1010-260-introduction-to-artificial-in-26-slash-fa-export.imscc`.

4. **Reading Pages (WikiPages)**:
   - Formulate structured HTML pages adhering to the DesignPLUS container format (`dp-wrapper`, `dp-header`, `dp-card`, `dp-callout`).
   - Include floating sidebar card with Unit Objectives.
   - Include active link to the slide PDF: `<a href="$IMS-CC-FILEBASE$/slides/[filename]?canvas_=1&amp;canvas_qs_wrap=1" target="_blank">`.
   - Inject mandatory Canvas WikiPage `<head>` metadata contract.

5. **Applied Assignments**:
   - Extract step-by-step instructions from `[Assignment] ... .pptx`.
   - Create `[assign_id]/[assign_id].html` and `assignment_settings.xml`.
   - Include interactive grading rubric table and upload specifications.

6. **Cartridge Assembler & Compiler**:
   - Enhance builder script with discussion topic support (`add_discussion_topic`).
   - Generate synchronized `imsmanifest.xml` and `course_settings/module_meta.xml`.
   - Validate all XML documents with `xml.etree.ElementTree`.
   - Pack into `AIML_1010_Generative_AI_Update_Modules_Import.imscc`.

---

## 2. ADR Conformance & Constraints

- **ADR-001 (Accessibility)**: All HTML typography uses high-contrast colors (`#1e3a8a`, `#0f172a`, `#334155`), alt tags on images, semantic headings (`<h2>`, `<h3>`, `<h4>`), and accessible table borders.
- **ADR-002 (Spec-Driven Development)**: Full traceability from `spec.md` to `plan.md` to `tasks.md` to implementation artifacts.
- **ADR-003 (Canvas Cartridge & DesignPLUS Theme Invariants)**:
  - All module titles are hyphenated without colons (`Module 01 - Demystifying Agentic AI`).
  - Pure DesignPLUS CSS classes used for banners and callouts.
  - Native WikiPage `<head>` metadata embedded in every page.
  - Modular Import mode: no front page or syllabus declared.

---

## 3. Dependency Graph & Risk Mitigation

- **COM Automation**: PowerPoint COM is verified working on the host (`PowerPoint.Application 16.0`). Run via unsandboxed PowerShell one-off export script.
- **Corrupted Quiz Data**: Python audit step logs every question and choice before compilation to catch missing or nonsensical choices.
- **Canvas Link Integrity**: Ensure all PDF filenames use URL-encoded spaces (`%20`) in `$IMS-CC-FILEBASE$` references.
