# AIML 2050: AI in the Workforce

> **Course Silo**: Full 8-Week Accelerated Block (3.0 Credits)  
> **Institution**: Laramie County Community College (LCCC)  
> **Contact Hours**: 6.0 Contact Hours / Week (48 Contact Hours Total)  
> **Primary Source Curriculum**: Intel Agentic AI Curriculum (~16 Source Units @ ~4 Contact Hours)  
> **Pedagogical Framework**: Backward Design (Outcome & Project &rarr; Scaffolded Build-up &rarr; Knowledge Check)

---

## 1. Course Vision & Workforce Relevance

**AIML 2050: AI in the Workforce** prepares community college and workforce students to design, evaluate, deploy, and govern practical agentic AI workflows and tools across modern enterprise environments.

Unlike theoretical machine learning courses, this curriculum focuses on **applied workplace competence**:
- Integrating autonomous tools, APIs, and retrieval pipelines into real-world business processes.
- Structuring robust human-in-the-loop review points and safety guardrails.
- Specifying and implementing end-to-end multi-agent and tool-calling solutions.
- Defending business ROI, operational trade-offs, and ethical governance.

---

## 2. 8-Week Accelerated Contact Hour Architecture

### The 16 &rarr; 8 Synthesis Matrix
- **Raw Input**: ~16 Intel agentic curriculum units designed for ~4 hours each (~64 total hours).
- **Target Course**: 8-week accelerated block with **6.0 contact hours per week** (48 contact hours total).
- **Strategy**: Rather than simply cutting half the material or skimming 16 modules superficially, we systematically **pair and consolidate conceptually linked units into 8 coherent, weekly milestone modules**.
- In each paired week, low-level redundant exercises are pared back, and the contact time is concentrated into building a **unified weekly workforce project**.

### Weekly Contact-Hour Allocation (6 Hours Total)
| Component | Allocated Time | Pedagogical Phase | Canvas Deliverable |
|---|---|---|---|
| **Roadmap & Executive Overview** | 30 mins | Orientation | `Unit XX Overview: [Topic]` |
| **Conceptual Foundations & Lecture Chapters** | 90 mins | **Why** (Theory & Workforce Need) | `Unit XX: Required Readings, Concepts & Video Lectures` |
| **Formative Check & Socratic Drills** | 60 mins | **What** (Comprehension & AI Sparring) | `Unit XX: Asynchronous Preparation & Drills` + `Learn with AI Drill` |
| **Guided Lab Demonstration** | 60 mins | **How** (Scaffolding & Tool Harnessing) | `Unit XX: Applied Lab Guide` |
| **Applied Weekly Project Build** | 90 mins | **Produce** (Authentic Workplace Artifact) | `Unit XX Applied Lab Assignment` (SpeedGrader) |
| **Knowledge Check & Retrospective** | 30 mins | **Verify** (Mastery & Self-Audit) | `Unit XX Knowledge Check: [Topic]` (QTI 1.2 Quiz) |

---

## 3. Weekly Module Taxonomy (Standard 8-to-9 Item Sequence)

Each weekly module inside the Canvas Common Cartridge follows the verified DesignPLUS sequence, augmented with dedicated open-source guide pages where external tooling is used:

1. `Unit XX Overview: [Topic]` (*WikiPage, Published, DesignPLUS Banner*)
2. `Unit XX: Required Readings, Concepts & Video Lectures` (*WikiPage, Published, includes curated slide range study directives*)
3. `Unit XX: Open-Source [Tool] Setup & Reference Guide` (*WikiPage, Published — standalone page added whenever new open-source tooling is introduced*)
4. `Unit XX: Asynchronous Preparation & Drills` (*WikiPage, Published, `<details>` accordion drills*)
5. `Unit XX: Applied Lab Guide` (*WikiPage, Published, native rubric table*)
6. `Unit XX Applied Lab Assignment` (*Assignment, Published, 50 pts, SpeedGrader upload*)
7. `Unit XX: Learn with AI — Supplemental Practice Drill` (*WikiPage, Published, Socratic roleplay*)
8. `Unit XX Knowledge Check: [Topic]` (*Quizzes::Quiz, Published, QTI 1.2, 3 attempts*)
9. `[Instructor Guide] Unit XX Teaching Notes & Solutions` (*WikiPage, Unpublished*)

---

## 4. Course Invariants & Authoring Rules (ADR Alignment)

See [`COURSE_RULES.md`](file:///c:/dev/Course-Content-Agentic-Template/courses/aiml-2050-ai-in-the-workforce/COURSE_RULES.md) for full details:
1. **Rule 1: Unaltered Slide Decks with Curated Directives**: The vendor Intel slide decks (`.pptx` / `.pdf`) remain 100% unaltered. On reading pages, students receive explicit slide numbers and section guidance (e.g., *"Study Slides 12–28; skip 29–40"*).
2. **Rule 2: Standalone Open-Source Guides**: Whenever an open-source tool, runtime, or framework is introduced (Ollama, OpenVINO, SQLite, FAISS, LangChain, n8n), provide a dedicated separate WikiPage with installation commands, configuration, smoke tests, and troubleshooting.
3. **Rule 3: Backward Design Anchoring**: Every unit builds toward a single, authentic workplace project deliverable submitted through SpeedGrader.
4. **Rule 4: DesignPLUS & Accessibility**: WCAG 2.2 AA compliant, hyphenated module titles (no colons), ribbons only on overviews/syllabus.

---

## 4. Assessment & Gradebook Weights

```json
{
  "Weekly Applied Projects (Labs)": "40.0%",
  "Workforce AI Capstone Project & Live Defense": "30.0%",
  "Weekly Knowledge Checks (QTI 1.2 Quizzes)": "20.0%",
  "Asynchronous AI Drills & Interactive Debriefs": "10.0%"
}
```

---

## 5. Directory Silo Structure

```
courses/aiml-2050-ai-in-the-workforce/
├── README.md                          # This master course charter
├── course_config.json                 # Canvas Cartridge & gradebook configuration
├── syllabus.md                        # Master course syllabus & policies
├── intake/                            # Curriculum intake dropzone for Intel materials
│   └── INCOMING_INTEL_CONTENT_DROPZONE.md
├── specs/                             # Specification-Driven Development iterations
│   └── 001-course-scaffold-and-intake/
│       ├── spec.md                    # EARS requirements
│       ├── plan.md                    # Architectural & pedagogical plan
│       └── tasks.md                   # Verifiable checklist
└── units/                             # Weekly unit deliverables
    ├── unit-01/                       # Week 1
    ├── unit-02/                       # Week 2
    ├── unit-03/                       # Week 3
    ├── unit-04/                       # Week 4
    ├── unit-05/                       # Week 5
    ├── unit-06/                       # Week 6
    ├── unit-07/                       # Week 7
    └── unit-08/                       # Week 8
```

---

## 6. Next Steps & Active Workflow

1. **Curriculum Drop**: Receive the Intel table of contents, topic list, or slide decks in `intake/`.
2. **Synthesis & Alignment Matrix**: Map out the ~16 source units into the 8 weekly block modules.
3. **Outcome & Project Definition**: For each of the 8 weeks, establish:
   - 2–3 explicit, workforce-measurable Learning Outcomes.
   - An authentic weekly Project Deliverable that proves those outcomes.
   - The progressive scaffolding (Why &rarr; What &rarr; How) that guides students to success.
4. **Content Generation**: Author reading pages, interactive drills, applied lab guides, SpeedGrader assignments, and QTI 1.2 quizzes.
5. **Compilation**: Package into `AIML_2050_Complete.imscc` and verify XML compliance.
