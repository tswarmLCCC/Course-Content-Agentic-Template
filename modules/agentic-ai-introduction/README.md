# Agentic AI Introduction: Autonomous Agents & Tool Use

> **Standalone Modular Course Bundle for Canvas LMS**  
> *Designed to drop into any Computer Science, Software Engineering, Data Science, or Artificial Intelligence course.*

---

## 1. Module Overview & Value Proposition

- **Target Package**: Canvas Common Cartridge (`.imscc`) formatted with institutional DesignPLUS themes, accessible WikiPages, speed-graded labs, and native QTI 1.2 quizzes.
- **Import Strategy**: Non-destructive modular import. Does not alter host course homepage, host syllabus, or existing course navigation.
- **Target Deliverable**: `Agentic_AI_Introduction_Modules_Import.imscc`

---

## 2. Target Audience & Pedagogical Philosophy

- **Target Persona**: Undergraduate students (Computer Science, Data Science, IT, Software Engineering).
- **Prior Background**: Foundational Python programming (functions, loops, dictionaries, basic API requests).
- **Core Problem Solved**: Moving students beyond passive "chatting with an LLM" to understanding **agentic loops, structured function calling (tool use), ReAct reasoning patterns, and autonomous multi-step execution**.
- **Pedagogical Model**: "I Do, We Do, You Do" gradual release, paired with the 8-cell Transition progression and strict empirical verification (zero ungrounded hallucination).

---

## 3. Modular Taxonomy

Each unit in this standalone module follows the standardized 8-item Canvas sequence:
1. `Unit X Overview: [Topic]` (`WikiPage`, Published)
2. `Unit X: Required Readings, Concepts & Video Lectures` (`WikiPage`, Published)
3. `Unit X: Asynchronous Preparation & Drills` (`WikiPage`, Published)
4. `Unit X: Applied Lab Guide` (`WikiPage`, Published)
5. `Unit X Applied Lab Assignment` (`Assignment`, Published)
6. `Unit X: Learn with AI — Supplemental Practice Drill` (`WikiPage`, Published)
7. `Unit X Knowledge Check: [Topic]` (`Quizzes::Quiz`, Published)
8. `[Instructor Guide] Unit X Teaching Notes & Solutions` (`WikiPage`, Unpublished)

---

## 4. Directory Structure

```
modules/agentic-ai-introduction/
├── README.md                                 # This module overview & specs
├── module_config.json                        # Modular cartridge configuration
├── Agentic_AI_Introduction_Modules_Import.imscc # Generated Canvas Cartridge
├── specs/                                    # SDD iteration specifications
└── units/                                    # Unit source files
```

---

## 5. Compilation Command

```bash
python .agents/skills/canvas-course-builder/build_course.py \
  --modular \
  --config modules/agentic-ai-introduction/module_config.json \
  --units-dir modules/agentic-ai-introduction/units \
  --output modules/agentic-ai-introduction/Agentic_AI_Introduction_Modules_Import.imscc
```
