# Workspace State & Active Target Pointer

## Active Workspace Target
- **Active Target Type**: `Modular Import Bundle`
- **Active Target**: `modules/agentic-ai-introduction`
- **Target Title**: Introduction to Agentic AI & Autonomous Tools
- **Target Path**: `modules/agentic-ai-introduction/`
- **Active Iteration**: `specs/002-open-source-ollama-agent-project` (Stage 4: Completed & Verified)
- **Status**: Dual-backend multi-agent blog pipeline (Google Gemini + Local Ollama) fully built, tested with pytest, and verified in `modules/agentic-ai-introduction/projects/dual-agentic-blog/`. All 14 EARS requirements PASS.

---

## Registered Targets in Repository

### Full Semester Courses (`courses/`)
| Course ID | Course Title | Completed Slices | Active Stage | Directory |
|---|---|---|---|---|
| `cosc-2060-data-engineering` | COSC 2060: Modern Data Engineering & AI Infrastructure | Complete 8-Unit Ecosystem (4-Chapter OER & Video Reading Pages, Labs, Starters, Guides, 80 QTI Quizzes & Fully Verified Native `.imscc` Cartridge with Front Page & Accordions) | Production Ready for Canvas Import & Deployment | [courses/cosc-2060-data-engineering/](file:///c:/dev/Course-Content-Agentic-Template/courses/cosc-2060-data-engineering/README.md) |

### Standalone Module Bundles & Modular Imports (`modules/`)
| Module ID | Module Title | Completed Slices | Active Stage | Directory |
|---|---|---|---|---|
| `agentic-ai-introduction` | Introduction to Agentic AI & Autonomous Tools | Unit 01 (Foundations & Canvas Cartridge) + Dual-Backend Agentic Blog Project (Google Gemini + Ollama + Web UI) | Production Ready for Canvas Import & Local Lab Execution | [modules/agentic-ai-introduction/](file:///c:/dev/Course-Content-Agentic-Template/modules/agentic-ai-introduction/README.md) |

---

## Instructions for Agent
Before performing any course or module authoring work:
1. Verify the `Active Target` above.
2. Restrict all read, grep, write, and task execution activities strictly to that active silo's directory (`courses/<id>/` or `modules/<id>/`).
3. In Modular Import mode, compile using `--modular` and name cartridges with `_Modules_Import.imscc` or `_Standalone_Module.imscc` in the module directory.
4. Keep shared templates (`specs/_templates/`) and ADRs (`docs/ADRs/`) untouched unless specifically updating shared repository infrastructure.
