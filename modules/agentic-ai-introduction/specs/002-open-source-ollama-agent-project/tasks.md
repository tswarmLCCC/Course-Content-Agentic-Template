# Task Checklist: Dual-Backend Agentic Blog Pipeline (Google Gemini + Local Ollama)

- **Spec Reference**: [`spec.md`](file:///c:/dev/Course-Content-Agentic-Template/modules/agentic-ai-introduction/specs/002-open-source-ollama-agent-project/spec.md)
- **Plan Reference**: [`plan.md`](file:///c:/dev/Course-Content-Agentic-Template/modules/agentic-ai-introduction/specs/002-open-source-ollama-agent-project/plan.md)
- **Target Directory**: `modules/agentic-ai-introduction/projects/dual-agentic-blog/`

---

## Task Execution Sequence

- [x] **Task 1: Project Scaffolding, Configuration & Pydantic Data Contracts**
  - **Action**: Create `pyproject.toml`, `app/config.py`, and `app/schemas.py` defining `BlogPlan`, `SectionPlan`, `ValidationReport`, `AgentTrace`, and `PipelineRunState`.
  - **Check**: Run Python script importing all schemas and verifying valid JSON schema generation via Pydantic (`.model_json_schema()`). *(PASSED - verified schemas and AppConfig)*

- [x] **Task 2: Dual-Backend Provider Strategy Layer**
  - **Action**: Create `app/providers/base.py`, `app/providers/mock_provider.py`, `app/providers/ollama_provider.py`, and `app/providers/google_provider.py` implementing unified structured output and tool-calling interfaces.
  - **Check**: Execute test script asserting that all providers implement `BaseLLMProvider` and mock provider returns valid `BlogPlan` and `ValidationReport`. *(PASSED - verified inheritance and mock self-correcting loop)*

- [x] **Task 3: ReAct Environmental Tools**
  - **Action**: Create `app/tools.py` implementing `calculate_reading_metrics`, `verify_code_syntax`, and `local_grounding_search` with strict type annotations, docstrings, and error handling.
  - **Check**: Run standalone unit tests on tools asserting valid dictionary responses and handling of malformed inputs. *(PASSED - all 3 tools verified with unit tests)*

- [x] **Task 4: Specialized Agent Nodes (Planner, Writer, Validator)**
  - **Action**: Create `app/agents/planner.py`, `app/agents/writer.py`, and `app/agents/validator.py` with rigorous system prompts, structured schema enforcement, and revision feedback handling.
  - **Check**: Run isolated agent tests with mock provider asserting valid plan generation, drafting, and rubric grading. *(PASSED - Planner, Writer, and Validator unit tests passed)*

- [x] **Task 5: Evaluator-Optimizer Coordinator State Machine**
  - **Action**: Create `app/coordinator.py` implementing the Planner $\to$ Writer $\to$ Validator self-correcting loop, enforcing a hard `max_iterations = 3` runaway guard, state deduplication, and execution trace history.
  - **Check**: Run coordinator end-to-end with mock provider, asserting auto-correction on iteration 2 and successful completion. *(PASSED - verified completion at iteration 2, status=PASSED)*

- [x] **Task 6: Rich Terminal Interface with Live Diffs**
  - **Action**: Create `app/ui/terminal.py` using Python `rich` to render colored agent thought boxes, tool execution badges, validator scorecards, and git-style revision diffs between iterations.
  - **Check**: Run CLI in terminal mode verifying rich formatting and clean output without errors. *(PASSED - verified cp1252-safe Rich terminal rendering)*

- [x] **Task 7: Standalone Local Web Dashboard (ADK Web UI Equivalent)**
  - **Action**: Create `app/ui/web/` containing a lightweight FastAPI server with Server-Sent Events (SSE) streaming and a zero-dependency HTML5/CSS3/Vanilla JS single-page app displaying the live agent graph, thought traces, and side-by-side markdown diff viewer.
  - **Check**: Spin up web server test, verify HTTP 200 on `GET /` and valid SSE streaming endpoint. *(PASSED - verified HTTP 200 and /api/run endpoint)*

- [x] **Task 8: Unified CLI Entrypoint & Automated Test Suite**
  - **Action**: Create `app/main.py` accepting `--provider [google|ollama|mock]`, `--topic`, `--max-iterations`, and `--web/--cli` flags. Author comprehensive test suite in `tests/`.
  - **Check**: Run `pytest` or standalone test runner verifying 100% test pass rate across schemas, mock pipeline, and CLI args. *(PASSED - 6/6 pytest tests passed)*

- [x] **Task 9: Content Hygiene, EARS Retrospective & Git Commit**
  - **Action**: Verify zero dead links, write `retrospective.md` auditing all 14 EARS requirements, update `CURRENT.md`, and commit all code cleanly to git.
  - **Check**: `git status` clean and retrospective PASS. *(PASSED)*

---

## Definition of Done
- [x] Runnable project located at `modules/agentic-ai-introduction/projects/dual-agentic-blog/`.
- [x] Tested and verified with both local mock and Ollama/Google interfaces.
- [x] Working tree clean in git.
