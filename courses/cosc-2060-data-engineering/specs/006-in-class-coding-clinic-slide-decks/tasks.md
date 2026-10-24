# Task Decomposition: In-Class Slot 2 Coding Clinic Slide Decks

- **ID**: `specs/006-in-class-coding-clinic-slide-decks`
- **Status**: Ready for Execution
- **Created**: 2026-10-24

---

## Task List

- [x] **Task 1: Output Directory & Environment Verification**
  - **Goal**: Create `courses/cosc-2060-data-engineering/content/slides/` and verify `python-pptx` runtime in Python 3.11.
  - **Check**: Directory exists and `C:\Python\Python311\python.exe -c "import pptx"` exits code 0.

- [x] **Task 2: Author Slide Generation Script**
  - **Goal**: Implement `courses/cosc-2060-data-engineering/scripts/generate_slide_decks.py` importing `SlideEngine` from `.agents/skills/slide-deck-generator/scripts/slide_engine.py`. Define data dictionaries for Units 1–8 covering title, agenda, incident retrospective, naive code, engine mechanics, engine refactoring, verified benchmarks, live sparring, and comprehensive speaker notes.
  - **Check**: File compiles cleanly with `C:\Python\Python311\python.exe -m py_compile .agents/skills/slide-deck-generator/scripts/build_clinic_decks.py`.

- [x] **Task 3: Execute Generation Script to Produce All 8 PPTX Decks**
  - **Goal**: Run `generate_slide_decks.py` to create `unit_01_coding_clinic.pptx` through `unit_08_coding_clinic.pptx` in `courses/cosc-2060-data-engineering/content/slides/`.
  - **Check**: All 8 `.pptx` files exist on disk with file size > 30 KB each.

- [x] **Task 4: Build & Execute Automated Presentation Test Harness**
  - **Goal**: Author `scratch/verify_slide_decks.py` to parse all 8 PPTX files with `pptx.Presentation`, asserting:
    1. Slide count = exactly 12 per deck (96 total slides across 8 units).
    2. Canvas dimensions = 13.333" x 7.5" (16:9 widescreen).
    3. Speaker notes coverage = 100% (non-empty, > 25 characters per slide).
    4. Code containers (Slide 5 and Slide 8) use Consolas monospace font.
  - **Check**: `C:\Python\Python311\python.exe scratch/verify_slide_decks.py` exits with code 0 and reports 100% PASS across all 96 slides.

- [x] **Task 5: Integrate Presentation Decks into Course Documentation**
  - **Goal**: Update course `README.md` and the 8 flipped classroom guides (`unit_XX_guide.md`) to include direct links and facilitation notes for each `.pptx` deck alongside the transition notebooks.
  - **Check**: Grep confirms all 8 `unit_XX_coding_clinic.pptx` links present in `courses/cosc-2060-data-engineering/README.md`.

- [x] **Task 6: EARS Requirements Audit & Retrospective**
  - **Goal**: Perform a complete pass/fail audit against all 9 EARS requirements in `spec.md`, document results in `retrospective.md`, and update `CURRENT.md`.
  - **Check**: `retrospective.md` created with 9/9 PASS.
