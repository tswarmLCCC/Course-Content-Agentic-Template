# Unit 01 Applied Lab Guide: Building an Automated Spec-Driven Development (SDD) Harness

<div class="dp-header dp-basic-bar" style="background: #1e3a8a; color: #ffffff; padding: 1.5rem; border-radius: 6px; margin-bottom: 1.5rem;">
  <h1 style="margin: 0; color: #ffffff; font-size: 1.8rem;">Unit 01 Applied Lab: Automated Spec-Driven Development (SDD) Harness</h1>
  <p style="margin: 0.5rem 0 0 0; opacity: 0.9;">Hands-on Engineering: Building the 90% Harness, Poka-Yoke Diff Patching, and Closed-Loop Pytest Self-Correction</p>
</div>

---

## 1. Lab Overview & Learning Goals

In this lab, you will transition from a casual "vibe coder" to a disciplined **Agentic Software Engineer**. Rather than writing raw code by hand or blindly prompting an AI chat window, you will build the software **harness** that governs an autonomous coding agent.

Your automated harness will:
1. Ingest machine-actionable specifications formulated in **EARS** (*Easy Approach to Requirements Syntax*).
2. Generate an implementation plan and candidate Python module.
3. Execute automated unit tests inside an isolated sandbox subprocess.
4. Catch failures and feed stderr tracebacks back into the agent's observation loop.
5. Apply non-destructive, targeted diff patches until 100% of test assertions pass.

- **Estimated Time**: 90 Minutes
- **Starter Script**: [`starter_sdd_harness.py`](file:///c:/dev/Course-Content-Agentic-Template/modules/agentic-software-engineering/units/unit_01_vibe_coding_vs_agentic_sdlc/starter_sdd_harness.py)
- **Grading Weight**: 100 Points (See [`rubric.md`](file:///c:/dev/Course-Content-Agentic-Template/modules/agentic-software-engineering/units/unit_01_vibe_coding_vs_agentic_sdlc/rubric.md))

---

## 2. Environment Setup & Dual-Backend Configuration

This lab is engineered for complete flexibility and zero required expenditure. You can run using either **Google Gemini Flash** (cloud) or **Ollama with Qwen 2.5 Coder** (100% offline, local).

### Option A: Local Ollama (Recommended for Offline / Zero-Cost)
1. Ensure Ollama is installed and running (`ollama serve`).
2. Pull the optimized coding model:
   ```bash
   ollama pull qwen2.5-coder:7b
   ```
3. Run the harness with the `--backend ollama` flag:
   ```bash
   python starter_sdd_harness.py --backend ollama
   ```

### Option B: Google Gemini Flash API (Cloud Free Tier)
1. Obtain a free API key from [Google AI Studio](https://aistudio.google.com/).
2. Set the environment variable in your terminal:
   - **PowerShell (Windows)**:
     ```powershell
     $env:GEMINI_API_KEY="your-api-key-here"
     ```
   - **Bash (macOS/Linux)**:
     ```bash
     export GEMINI_API_KEY="your-api-key-here"
     ```
3. Run the harness with the `--backend gemini` flag:
   ```bash
   python starter_sdd_harness.py --backend gemini
   ```

### Option C: Deterministic Simulation Mock (Zero Tokens / Automated Testing)
If you are working in an environment without GPU acceleration or internet access:
```bash
python starter_sdd_harness.py --backend mock
```

---

## 3. Step-by-Step Implementation Instructions

### Step 1: Ingest & Categorize EARS Requirements
Inspect `SpecParser.parse_ears_spec()`. Complete the categorization logic so that requirements are extracted into:
- `ubiquitous`: Statements containing `shall` without conditional keywords.
- `event_driven`: Statements triggered by `WHEN`.
- `state_driven`: Statements active `WHILE`.
- `unwanted`: Negative/error conditions triggered by `IF ... THEN`.
- `optional`: Feature toggles governed by `WHERE`.

### Step 2: Implement the Poka-Yoke Diff Patcher
Inspect `DiffPatcher.apply_targeted_patch()`. 
- Ensure that the patcher checks `target_chunk in original_content`.
- Ensure it rejects ambiguous replacements if `original_content.count(target_chunk) > 1`.
- Replace exactly one instance using `original_content.replace(target_chunk, replacement_chunk, 1)`.

### Step 3: Implement the Sandboxed Pytest Runner
Inspect `SDDHarnessEngine._run_pytest()`. 
- Ensure it executes `sys.executable -m pytest test_candidate.py -q` within the temporary directory (`temp_dir`).
- Capture both `stdout` and `stderr` to feed back into the agent's observation scratchpad when tests fail.

### Step 4: Induce a Test Failure & Verify Self-Healing
Modify the candidate code generation prompt to deliberately induce an edge-case failure (e.g., omitting whitespace stripping in `reverse_words`).
- Run the harness.
- Observe how Attempt 1 fails, the traceback is extracted in Stage 5, and Attempt 2 applies a targeted fix resulting in `PASSED (100% Tests Green)`.

---

## 4. Verification & Submission

Run the automated test suite to ensure all unit assertions pass:
```bash
python -m pytest test_sdd_harness.py -v
```

### Submission Deliverables:
1. Your completed `starter_sdd_harness.py` file.
2. A terminal transcript (`execution_trace.txt`) demonstrating:
   - Spec parsing output.
   - At least one test failure followed by an automated self-healing patch.
   - Final green test run.
