# Task Checklist: AIML 1010 Generative AI & Agentic Curriculum Update

- **Spec Reference**: [`spec.md`](./spec.md)
- **Plan Reference**: [`plan.md`](./plan.md)

---

## Task Execution Sequence

- [x] **Task 1: Slide Decks to Notes-Pages PDFs Generation**
  - **Action**: Export all 9 slide decks (`.pptx`) with speaker notes to 540x720 Notes Pages PDFs using PowerPoint COM automation and verify all 9 PDF files are generated and readable.
  - **Files Modified**: `modules/aiml-1010-generative-ai-update/units/*/slides/*.pdf`, `scripts/export_slide_pdfs.ps1`
  - **Check**: Verified: all 9 PDFs rendered with speaker notes (e.g., Module 01: 4.4 MB, Week 10: 3.5 MB, Week 11: 4.9 MB, Week 15: 5.3 MB).

- [x] **Task 2: Quiz Audit, Correction, and QTI 1.2 Compilation**
  - **Action**: Parse each `[Quiz] ... .xlsx` spreadsheet, audit questions for accuracy and typos (e.g. replacing placeholder options and verifying correct answers), output formatted Markdown quiz files, and compile them into native QTI 1.2 XML packages.
  - **Files Modified**: `modules/aiml-1010-generative-ai-update/units/*/quiz.md`, `units/*/qti/`
  - **Check**: Verified: 9 clean Markdown quizzes written and 9 native QTI 1.2 XML packages compiled (10 questions each, 90 questions total, 0 parse errors).

- [x] **Task 3: Author Discussion Topics (Canvas `imsdt_xmlv1p1`)**
  - **Action**: Author 9 discussion boards formatted with asynchronous participation instructions, 3-4 structured conceptual/applied prompts, and optional group presentation tasks matching the reference cartridge style.
  - **Files Modified**: `modules/aiml-1010-generative-ai-update/units/*/discussion.json`
  - **Check**: Verified: 9 structured discussion definitions generated in full reference cartridge layout.

- [x] **Task 4: Author Applied Lab Assignments**
  - **Action**: Extract lab steps, tool workflows, and objectives from `[Assignment] ... .pptx` files and generate native Canvas assignment HTML with rubric tables and `assignment_settings.xml`.
  - **Files Modified**: `modules/aiml-1010-generative-ai-update/units/*/assignment.html`, `assignment_settings.json`
  - **Check**: Verified: 9 native Canvas assignments created with 50.0 pts rubric tables and upload configurations.

- [x] **Task 5: Author DesignPLUS Reading Pages with Linked Slide PDFs**
  - **Action**: Author 9 DesignPLUS-styled `Reading - [Topic]` WikiPages with unit objectives card, slide briefing notes synthesized from slides and facilitator guides, `$IMS-CC-FILEBASE$/slides/` PDF links, and student exercise callouts.
  - **Files Modified**: `modules/aiml-1010-generative-ai-update/units/*/reading.html`
  - **Check**: Verified: 9 DesignPLUS reading pages with unit objectives, active PDF links (`$IMS-CC-FILEBASE$/slides/...`), and mandatory `<head>` metadata contract.

- [x] **Task 6: Modular Cartridge Assembly, XML Validation & Verification Audit**
  - **Action**: Compile the complete 9-unit package into `AIML_1010_Generative_AI_Update_Modules_Import.imscc` using our enhanced modular builder, perform ElementTree XML validation, and audit all EARS requirements.
  - **Files Modified**: `modules/aiml-1010-generative-ai-update/AIML_1010_Generative_AI_Update_Modules_Import.imscc`
  - **Check**: Verified: 60 XML files parsed with 0 syntax errors, 88 files packed into 28.6 MB `.imscc` cartridge. Full automated audit passed 100% across all 14 EARS requirements.

---

## Verification & Retrospective Audit
- [x] Run full test/verification suite (`python modules/aiml-1010-generative-ai-update/scripts/verify_cartridge.py`).
- [x] Audit against every requirement in `spec.md` (Pass/Fail table: 14/14 PASS).
- [ ] User review and sign-off.
