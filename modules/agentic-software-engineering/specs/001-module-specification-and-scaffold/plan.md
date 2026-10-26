# Technical & Architectural Plan: Agentic Software Engineering 3-Unit Modular Bundle

- **Spec Reference**: [`spec.md`](file:///c:/dev/Course-Content-Agentic-Template/modules/agentic-software-engineering/specs/001-module-specification-and-scaffold/spec.md)
- **Status**: Draft — In Review
- **Active Silo**: `modules/agentic-software-engineering/`

---

## 1. Technical Architecture & Component Layout

### A. Directory & Unit Architecture
```
modules/agentic-software-engineering/
├── README.md                                         # Module overview & curriculum map
├── module_config.json                                # Canvas cartridge configuration
├── Agentic_Software_Engineering_Modules_Import.imscc # Compiled Canvas cartridge (.imscc)
├── specs/
│   └── 001-module-specification-and-scaffold/        # Active SDD iteration
│       ├── spec.md
│       ├── plan.md
│       └── tasks.md
└── units/
    ├── unit_01_vibe_coding_vs_agentic_sdlc/
    │   ├── overview.md                               # Canvas WikiPage: Contact hour budget & roadmap
    │   ├── reading.md                                # Canvas WikiPage: 4-chapter OER guide + video
    │   ├── drills.md                                 # Canvas WikiPage: Collapsible self-check drills
    │   ├── lab_guide.md                              # Canvas WikiPage: Lab instructions & rubric
    │   ├── rubric.md                                 # 100-point speed-grader rubric
    │   ├── starter_sdd_harness.py                    # Student lab starter code (dual-backend)
    │   ├── test_sdd_harness.py                       # Automated pytest suite for verification
    │   ├── learn_with_ai.md                          # Canvas WikiPage: Socratic AI practice drill
    │   ├── quiz.md                                   # QTI 1.2 markdown quiz (text2qti format)
    │   └── teaching_notes.md                         # Unpublished instructor guide & solution key
    ├── unit_02_harness_architecture_and_context/     # (Scaffolded directory)
    └── unit_03_fastmcp_and_multiagent_verification/  # (Scaffolded directory)
```

### B. Dual-Backend Agent Architecture (`starter_sdd_harness.py`)
To ensure zero financial burden and complete lab portability, the harness supports:
1. **Google Gemini Flash Backend**: Uses `https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash:generateContent` via direct lightweight HTTP `requests` (no heavyweight SDK dependency). Activated when `GEMINI_API_KEY` is present.
2. **Local Ollama Backend**: Uses `http://localhost:11434/api/generate` with model `qwen2.5-coder:7b` (or `14b`). Automatically activated when `GEMINI_API_KEY` is absent or when `USE_LOCAL_OLLAMA=true`.
3. **Deterministic Simulation Mock**: For automated test environments and offline verification when Ollama is not actively running, providing 100% deterministic test coverage.

### C. The Spec-Driven Development (SDD) Harness Engine
The lab harness implements an autonomous cycle:
1. **Ingest Specification**: Parses EARS requirements (`REQ-01` through `REQ-NN`).
2. **Architect Plan**: Generates targeted function signatures and docstrings.
3. **Generate Code**: Emits candidate implementation code.
4. **Isolated Test Execution**: Executes a test runner in an isolated subprocess.
5. **Deterministic Gate**: Evaluates pass/fail status. If failed, feeds traceback back into context for targeted patch generation up to 3 iterations.

---

## 2. ADR Conformance & Invariants

- **ADR-001 (Accessibility - WCAG 2.2 AA)**:
  - All text meets high-contrast 4.5:1 minimums (e.g., `#1e3a8a` navy on `#ffffff` white).
  - All data tables use `<th scope="col">` and `<th scope="row">` attributes.
  - Video embeds feature fully accessible responsive containers with direct fallback links and descriptive `title` attributes.
  - Collapsible self-check elements use semantic `<details>` and `<summary>` tags.
- **ADR-002 (Spec-Driven Development)**:
  - Every file and code artifact maps directly to requirements in `spec.md`.
  - All tasks in `tasks.md` will contain concrete, runnable `Check:` commands.
- **ADR-003 (Canvas Cartridge & DesignPLUS Invariants)**:
  - Module titles use hyphens rather than colons (e.g., `Unit 01 - Vibe Coding vs. Agentic SDLC`).
  - Native DesignPLUS wrapper classes (`dp-header`, `dp-basic-bar`, `dp-callout`, `dp-table`) are used exclusively without clashing inline CSS.
  - WikiPages include clean, valid `<head><title>Page Title</title></head>` metadata.

---

## 3. Dependency Graph & Risk Mitigation

| Dependency | Purpose | Failure Mode | Mitigation Strategy |
|---|---|---|---|
| `text2qti` | Compiles `quiz.md` into Canvas QTI 1.2 XML | Syntax errors in quiz formatting | Pre-validate quiz schema with regex checks; text2qti test compilation. |
| `build_course.py` | Compiles `.imscc` zip cartridge | Missing manifest files or invalid XML | Run build with `--modular` flag; verify zip integrity with Python `zipfile`. |
| `Ollama` / `Qwen 2.5 Coder` | Local model inference | Ollama daemon not running or low RAM | Dual-backend design with automatic mock/Gemini fallback mode. |
| `pytest` | Verification of student harness | Missing dependency or broken import | Keep tests self-contained in standard library + pytest. |

---

## 4. Definition of Done for this Phase
1. `modules/agentic-software-engineering/units/unit_01_vibe_coding_vs_agentic_sdlc/` fully authored with all 8 Canvas items + starter code + tests.
2. Automated test suite `test_sdd_harness.py` executed with 100% pass rate.
3. `Agentic_Software_Engineering_Modules_Import.imscc` compiled with 0 errors.
4. Full audit verifying compliance against every EARS requirement in `spec.md`.
