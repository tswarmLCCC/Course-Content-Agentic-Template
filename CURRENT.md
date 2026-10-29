# Workspace State & Active Target Pointer

## Active Workspace Target
- **Active Target Type**: `Modular Import Bundle`
- **Active Target**: `modules/aiml-1010-generative-ai-update`
- **Target Title**: AIML 1010: Generative AI & Agentic Curriculum Update
- **Target Path**: `modules/aiml-1010-generative-ai-update/`
- **Active Iteration**: `specs/001-module-specification-and-scaffold` (Stage 4: Completed & Verified)
- **Status**: Production-ready 9-unit modular Canvas Common Cartridge (`AIML_1010_Generative_AI_Update_Modules_Import.imscc`, 28.6 MB) compiled with 0 XML errors. Includes all 9 notes-pages slide PDFs, 9 audited QTI 1.2 quizzes, 9 DesignPLUS reading pages, 9 native assignments with rubrics, and 9 imsdt_xmlv1p1 discussion topics. 100% PASS on all 14 EARS requirements.

---

## Registered Targets in Repository

### Full Semester Courses (`courses/`)
| Course ID | Course Title | Completed Slices | Active Stage | Directory |
|---|---|---|---|---|
| `cosc-2060-data-engineering` | COSC 2060: Modern Data Engineering & AI Infrastructure | Complete 8-Unit Ecosystem (4-Chapter OER & Video Reading Pages, Labs, Starters, Guides, 80 QTI Quizzes & Fully Verified Native `.imscc` Cartridge with Front Page & Accordions) | Production Ready for Canvas Import & Deployment | [courses/cosc-2060-data-engineering/](file:///c:/dev/Course-Content-Agentic-Template/courses/cosc-2060-data-engineering/README.md) |

### Standalone Module Bundles & Modular Imports (`modules/`)
| Module ID | Module Title | Completed Slices | Active Stage | Directory |
|---|---|---|---|---|
| `aiml-1010-generative-ai-update` | AIML 1010: Generative AI & Agentic Curriculum Update | Ingestion of 9 modular units (Agentic AI, Prompt Eng I & II, Transformers, Diffusion, Pre-Training, Fine-Tuning, Prototyping, Alignment) into modular Canvas cartridge | Production Ready (Stage 4 Completed & Verified) | [modules/aiml-1010-generative-ai-update/](file:///c:/dev/Course-Content-Agentic-Template/modules/aiml-1010-generative-ai-update/README.md) |
| `agentic-ai-introduction` | Introduction to Agentic AI & Autonomous Tools | Unit 01 (Foundations & Canvas Cartridge) + Dual-Backend Agentic Blog Project (Google Gemini + Ollama + Web UI) | Production Ready for Canvas Import & Local Lab Execution | [modules/agentic-ai-introduction/](file:///c:/dev/Course-Content-Agentic-Template/modules/agentic-ai-introduction/README.md) |
| `agentic-software-engineering` | Agentic Software Engineering & The New SDLC | Initial Scaffolding & 3-Unit In-Depth Architecture (Harness Engineering, Spec-Driven SDLC, FastMCP & Verification) | Stage 4: Completed & Verified | [modules/agentic-software-engineering/](file:///c:/dev/Course-Content-Agentic-Template/modules/agentic-software-engineering/README.md) |

---

## Instructions for Agent
Before performing any course or module authoring work:
1. Verify the `Active Target` above.
2. Restrict all read, grep, write, and task execution activities strictly to that active silo's directory (`courses/<id>/` or `modules/<id>/`).
3. In Modular Import mode, compile using `--modular` and name cartridges with `_Modules_Import.imscc` or `_Standalone_Module.imscc` in the module directory.
4. Keep shared templates (`specs/_templates/`) and ADRs (`docs/ADRs/`) untouched unless specifically updating shared repository infrastructure.
