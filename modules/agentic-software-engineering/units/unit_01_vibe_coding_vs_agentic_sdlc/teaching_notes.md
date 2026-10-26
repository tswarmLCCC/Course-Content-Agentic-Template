# [Instructor Guide] Unit 01 Teaching Notes & Solutions

> **Status:** Unpublished Instructor Guide  
> **Target Course:** AENG 2100 — Agentic Software Engineering & The New SDLC  
> **Unit:** Unit 01 — Vibe Coding vs. Agentic SDLC & The 10/90 Harness Rule  

---

## 1. Pedagogical Intent & Faculty Overview

The purpose of Unit 01 is to administer a healthy "reality check" to computer science and engineering students who have grown accustomed to using ChatGPT or Claude as a casual copy-paste oracle.

Most undergraduate students currently operate in the **Vibe Coding** mindset:
1. They type a loose prompt.
2. The AI generates 300 lines of code.
3. They paste it into their IDE. If it fails, they paste the error message back into the chatbot.
4. They repeat until it appears to work, without understanding the boundary conditions, state lifecycle, or technical debt incurred.

This unit breaks that cycle by introducing **The 10/90 Harness Rule** codified in Google's *The New SDLC With Vibe Coding* whitepaper (Addy Osmani, Shubham Saboo, & Sokratis Kartakis, 2026). Students learn that the AI model itself is merely an autoregressive token predictor (accounting for only ~10% of agent reliability). The true engineering achievement is the **Harness (the 90%)**—the repository rules, machine-actionable specifications, Poka-Yoke tools, and closed-loop test runners that govern agent behavior.

---

## 2. 150-Minute Synchronous Active Learning Timeline

```
========================================================================================
150 TOTAL SYNCHRONOUS MINUTES
├── Part 1: Deconstructing the "80% Trap" & The 10/90 Rule (35 min)
├── Part 2: Paired Sparring Challenge: Rewriting Vague Prompts into EARS (30 min)
├── Part 3: Guided Hands-on Engineering Clinic: Lab 01 Harness (70 min)
└── Part 4: Code Review, Rubric Alignment & Debrief (15 min)
========================================================================================
```

### Part 1: Deconstructing the "80% Trap" (Minutes 0–35)
- **Live Demo (The Vibe Coding Crash)**:
  - Open a fresh chat window. Give the LLM a loose prompt: *"Build me a Python string processing library with caching."*
  - Show how the model generates plausible code, but silently fails on Unicode edge cases, case-insensitivity, and memory leaks.
  - Explain the **CapEx vs. OpEx debt curve**: generating code took 10 seconds (CapEx: $0.01), but debugging it in production takes 4 hours (OpEx: $200+).
- **The 10/90 Rule Discussion**:
  - Show why upgrading from an open-source 7B/70B model to a 400B frontier model does not fix missing repository rules or unconstrained file writes.

### Part 2: Paired Sparring Challenge (Minutes 35–65)
- Pair students into **Conductors** and **Orchestrators**.
- Give each pair 3 unstructured client prompts (e.g., *"Make our checkout fast and secure"*).
- Challenge them to reformulate the prompts into formal **EARS syntax** (Ubiquitous, Event, State, and If-Then Unwanted requirements).
- Have pairs swap requirements and test if their partner's EARS spec contains any ambiguities.

### Part 3: Guided Applied Lab Clinic (Minutes 65–135)
- Walk through `starter_sdd_harness.py`.
- Guide students through:
  1. The regex mechanics of `SpecParser.parse_ears_spec`.
  2. The string-matching safeguards of `DiffPatcher.apply_targeted_patch`.
  3. Running pytest inside `tempfile.TemporaryDirectory()`.
  4. Inducing an intentional defect and watching the model read the traceback in Stage 5 to auto-correct the code.
- Provide live debugging assistance for students running either local Ollama or Google Gemini Flash.

### Part 4: Rubric Alignment & Debrief (Minutes 135–150)
- Review the 100-point rubric in `rubric.md`.
- Ensure students verify all assertions using `python -m pytest test_sdd_harness.py -v`.

---

## 3. Common Student Misconceptions & Pitfalls

| Misconception | What the Student Believes | The Engineering Reality |
|---|---|---|
| **"Bigger Model = Fewer Regressions"** | If my agent breaks code, I just need to switch to Claude 3.5 Sonnet or GPT-4o. | Without an automated test harness and negative rules (`AGENTS.md`), larger models hallucinate with greater eloquence and break code just as frequently. |
| **"Prompt Stuffing"** | I should paste my entire 500-page API documentation into the system prompt. | Context degrades rapidly ("lost-in-the-middle"). Production harnesses use **progressive disclosure** (dynamic skills). |
| **"AI Ground Truth"** | If the AI says 'All tests pass and the code is optimal', I can trust it. | LLMs have no internal concept of ground truth. Ground truth only exists when an external compiler or unit test suite exits with code 0. |

---

## 4. Master Solution Code: `starter_sdd_harness.py`

Below is the reference solution implementation for the key student lab methods:

```python
# Reference Solution: SpecParser.parse_ears_spec
@staticmethod
def parse_ears_spec(spec_text: str) -> Dict[str, List[str]]:
    categories = {
        "ubiquitous": [],
        "event_driven": [],
        "state_driven": [],
        "unwanted": [],
        "optional": []
    }
    for line in spec_text.strip().splitlines():
        line = line.strip()
        if not line or not line.startswith("- "):
            continue
        cleaned = line.lstrip("- ").strip()
        upper = cleaned.upper()
        if upper.startswith("WHEN "):
            categories["event_driven"].append(cleaned)
        elif upper.startswith("WHILE "):
            categories["state_driven"].append(cleaned)
        elif upper.startswith("IF "):
            categories["unwanted"].append(cleaned)
        elif upper.startswith("WHERE "):
            categories["optional"].append(cleaned)
        elif "SHALL" in upper:
            categories["ubiquitous"].append(cleaned)
    return categories


# Reference Solution: DiffPatcher.apply_targeted_patch
@staticmethod
def apply_targeted_patch(original_content: str, target_chunk: str, replacement_chunk: str) -> Tuple[bool, str]:
    if target_chunk not in original_content:
        return False, f"Target chunk not found in original content: '{target_chunk[:40]}...'"
    
    occurrences = original_content.count(target_chunk)
    if occurrences > 1:
        return False, f"Target chunk is ambiguous ({occurrences} occurrences found)."
        
    updated = original_content.replace(target_chunk, replacement_chunk, 1)
    return True, updated


# Reference Solution: SDDHarnessEngine._run_pytest
@staticmethod
def _run_pytest(cwd: str) -> Tuple[bool, str, str]:
    cmd = [sys.executable, "-m", "pytest", "test_candidate.py", "-q"]
    proc = subprocess.run(
        cmd,
        cwd=cwd,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True
    )
    return proc.returncode == 0, proc.stdout, proc.stderr
```

---

## 5. Grading Checklist (100 Points Total)
- [ ] **EARS Parser (20 pts)**: Passes `test_spec_parser_ears` with all 5 patterns parsed.
- [ ] **Diff Patcher (25 pts)**: Passes `test_diff_patcher_success`, `test_diff_patcher_not_found`, and `test_diff_patcher_ambiguous`.
- [ ] **Sandboxed Pytest Runner (25 pts)**: Test runner executes in isolated tempdir; stdout and stderr captured.
- [ ] **Self-Healing Loop (20 pts)**: Passes `test_sdd_engine_mock_success` and cleanly enforces `test_sdd_engine_retry_limit`.
- [ ] **Code Quality & Typing (10 pts)**: Passes `test_dual_backend_fallback_on_unreachable` with clean type annotations and no crashes.
