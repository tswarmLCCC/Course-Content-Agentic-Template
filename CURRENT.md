# Workspace State & Active Target Pointer

## Active Workspace Target
- **Active Target Type**: `Full 8-Week Accelerated Course`
- **Active Target**: `courses/aiml-2050-ai-in-the-workforce`
- **Target Title**: AIML 2050: AI in the Workforce
- **Target Path**: `courses/aiml-2050-ai-in-the-workforce/`
- **Active Iteration**: `specs/001-course-scaffold-and-intake` (Stage 2: Plan In Review — Awaiting Approval)
- **Status**: Intel curriculum ingested (20 modules & 5 projects, 2,100+ slides). 20-to-8 synthesis recommendation revised with explicit slide reading lists and standalone open-source guides. Awaiting user review and formal approval before task execution.

---

## Registered Targets in Repository

### Full Semester Courses (`courses/`)
| Course ID | Course Title | Completed Slices | Active Stage | Directory |
|---|---|---|---|---|
| `aiml-2050-ai-in-the-workforce` | AIML 2050: AI in the Workforce | Initial 8-week accelerated scaffold, intake dropzone, course config, and backward-design iteration specification | Active Stage 1 (Curriculum Intake & Synthesis) | [courses/aiml-2050-ai-in-the-workforce/](file:///c:/dev/Course-Content-Agentic-Template/courses/aiml-2050-ai-in-the-workforce/README.md) |
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
