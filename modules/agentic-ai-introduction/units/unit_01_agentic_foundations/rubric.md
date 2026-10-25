# Grading Rubric: Unit 01 Auto-Correcting Multi-Agent Pipeline

| Evaluation Criteria | Maximum Points | Description |
| :--- | :---: | :--- |
| **Architectural Separation of Roles** | 25 | Planner, Writer, and Validator agents are cleanly separated into dedicated classes with isolated system prompts and schema-validated interfaces. |
| **Self-Correcting Critique Loop** | 30 | The Writer agent dynamically absorbs the Validator's structured critique, repairs missing sections, adjusts word count, and achieves a passing score within 2–3 turns. |
| **Defensive Stopping & Loop Controls** | 25 | The pipeline enforces a strict `max_iterations = 3` cap, tracks execution history, and avoids runaway infinite loops or token exhaustion. |
| **Poka-Yoke Tool Design & Validation** | 20 | Code utilizes structured JSON schemas, comprehensive error trapping, and outputs an informative execution trace. |
| **Total Points** | **100** | Scaled to 50 Points in Canvas SpeedGrader. |
