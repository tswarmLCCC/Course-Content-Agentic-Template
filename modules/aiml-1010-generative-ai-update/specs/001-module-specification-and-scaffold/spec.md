# Feature Specification: AIML 1010 Generative AI & Agentic Curriculum Update

- **ID**: `specs/001-module-specification-and-scaffold`
- **Status**: Completed & Verified
- **Created**: 2026-10-29
- **Target Completion**: 9 Modular Units packaged into Common Cartridge (`.imscc`)

---

## 1. Objective & Target Audience

- **Primary Persona**: Undergraduate college students taking AIML 1010 (Introduction to Artificial Intelligence) who need accessible, clear, step-by-step instruction on Generative AI and Agentic AI workflows.
- **Problem Statement**: The legacy AIML 1010 course shell lacks current industry coverage of LLM architectures, diffusion models, fine-tuning, prompt engineering frameworks, and agentic workflows. Source curriculum updates exist in raw PPTX, XLSX, and DOCX files across 9 topic folders in `./ref/AIML 1010 Update/New Modules/`, but need to be systematically audited, formatted with DesignPLUS styling, linked to speaker-annotated PDFs, and packaged for import into an existing Canvas course shell.
- **One Job**: Produce a single, modular Canvas Common Cartridge (`AIML_1010_Generative_AI_Update_Modules_Import.imscc`) containing all 9 modernized units, with zero destructive overrides to the host course shell.

---

## 2. Requirements (EARS Syntax)

### Ubiquitous Requirements (Always)
- `REQ-01`: The modular package **shall** compile into a valid Canvas Common Cartridge (`.imscc`) named `AIML_1010_Generative_AI_Update_Modules_Import.imscc`.
- `REQ-02`: The package **shall** operate in Modular Import mode without overwriting or defining a host course front page (`home-page.html`), course navigation, or institutional syllabus (`syllabus.html`).
- `REQ-03`: Each of the 9 modules **shall** adhere to ADR-003 hyphenated title syntax (e.g. `Module 01 - Demystifying Agentic AI`, `Week 03 - Prompt Engineering I`) with no colons (`:`) to prevent DesignPLUS accordion truncation.
- `REQ-04`: Every student-facing WikiPage **shall** include the mandatory Canvas WikiPage `<head>` metadata contract (`identifier`, `workflow_state="active"`, `editor_type="rce"`, `editing_roles="teachers"`) to prevent iframe download sandboxing.
- `REQ-05`: All web content, HTML color contrasts, and typography **shall** comply with WCAG 2.1 AA / WCAG 2.2 AA (ADR-001).

### Slide PDF Requirements
- `REQ-06`: For each of the 9 modules, the system **shall** produce an annotated 540x720 portrait "Notes Pages" PDF containing the slide visual at top and complete instructor speaker notes at the bottom.
- `REQ-07`: All generated slide PDFs **shall** be packaged under `web_resources/slides/` inside the cartridge.

### Reading Page Requirements
- `REQ-08`: For each of the 9 modules, the system **shall** generate a `Reading - [Topic]` WikiPage styled to match the reference cartridge (`reading-introduction-to-generative-ai.html`), featuring:
  - DesignPLUS container header with icon and unit title.
  - Floating sidebar card displaying Unit Objectives derived from the facilitator guide.
  - Active download/preview link to the corresponding slide PDF: `<a href="$IMS-CC-FILEBASE$/slides/[filename]?canvas_=1&amp;canvas_qs_wrap=1" target="_blank">`.
  - Comprehensive reading briefing notes synthesized from the slide deck content and facilitator notes.
  - Student Exercises / Discussion Callout block (`dp-callout`).

### Quiz & Assessment Requirements
- `REQ-09`: **When** reading each module's source quiz spreadsheet (`[Quiz] ... .xlsx`), the system **shall** audit all questions, choices, and answers for grammatical accuracy, completeness, factual correctness, and alignment with introductory AI concepts.
- `REQ-10`: **If** a quiz question contains corrupted, truncated, or incorrect answers (e.g., placeholder "t", wrong answer key references), **then** the system **shall** correct the option text and align the answer key before QTI generation.
- `REQ-11`: The system **shall** convert each audited quiz into a native Canvas QTI 1.2 package (`assessment_qti.xml`, `assessment_meta.xml`, and `non_cc_assessments/[id].xml.qti`).

### Discussion Board Requirements
- `REQ-12`: For each of the 9 modules, the system **shall** generate a native Canvas Discussion Topic (`Discussion: [Topic]`) utilizing Canvas `imsdt_xmlv1p1` and `topicMeta` XML architecture.
- `REQ-13`: Each discussion topic **shall** replicate the structural style from the reference cartridge, including:
  - Clear asynchronous interaction timeline and participation guidelines.
  - 3 to 4 structured discussion prompts with "Context" and "Discussion Question" grounded in the unit's technical concepts.
  - An optional group presentation / homework sharing prompt.

### Applied Assignment Requirements
- `REQ-14`: For each of the 9 modules, the system **shall** convert the student lab deck (`[Assignment] ... .pptx`) into a native Canvas Assignment (`[assign_id]/[assign_id].html` and `assignment_settings.xml`) specifying submission types (`online_text_entry,online_upload`), allowed extensions, and a structured HTML grading rubric.

---

## 3. Deliberately Out of Scope
- No course-wide front page (`home-page.html`), course banner, or syllabus file generation (this cartridge is strictly for modular import into an existing shell).
- No alteration of the host course assignment grading scheme or institutional grading policies.
- No external unauthenticated third-party JavaScript dependencies.

---

## 4. Acceptance Criteria & Definition of Done
- [x] 9 slide deck PDFs generated with speaker notes and stored in `web_resources/slides/`.
- [x] 9 quizzes audited, corrected, converted to Markdown, and compiled to native QTI 1.2 XML.
- [x] 9 discussion topics compiled into `imsdt_xmlv1p1` and `topicMeta` XML format.
- [x] 9 reading pages formatted with DesignPLUS markup and linked to slide PDFs.
- [x] 9 applied assignments generated with step-by-step instructions and rubrics.
- [x] All 9 modules structured in `module_meta.xml` and `imsmanifest.xml` with synchronized hex IDs.
- [x] Zero XML syntax errors via `xml.etree.ElementTree`.
- [x] Canvas Common Cartridge `AIML_1010_Generative_AI_Update_Modules_Import.imscc` compiled cleanly.
