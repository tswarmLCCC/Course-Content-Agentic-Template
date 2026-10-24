# Canvas Course Builder Skill (`canvas-course-builder`)

A complete, self-contained, portable AI agent skill and Python automation toolkit for building production-grade, DesignPLUS-compliant **Canvas LMS Common Cartridges (`.imscc`)**.

---

## 🌟 What This Skill Does

This package gives AI coding agents (and human course developers) everything needed to author, format, package, and deploy complete college courses into Canvas LMS:

1. **Deterministic Common Cartridge Compilation:** Compiles pages, assignments, quizzes, syllabi, and modules into a single 1-click importable `.imscc` package.
2. **Native QTI 1.2 Quizzes:** Converts clean, human-readable Markdown quiz files (with answer keys and rationales) directly into Canvas-native QTI 1.2 assessments.
3. **DesignPLUS Visual Styling:** Applies institutional Navy (`#1e3a8a`), Dark Slate (`#0f172a`), and Royal Blue (`#2563eb`) styling with selective top banner ribbons, responsive embedded videos, dark Consolas syntax boxes, and expandable formative accordions (`<details><summary>`).
4. **Institutional Syllabus Generator:** Produces accreditation-compliant Microsoft Word (`.docx`) course syllabi using zero-dependency OpenXML packaging and links them seamlessly inside the Canvas Syllabus tab.
5. **Proven 8-Item Weekly Unit Sequence:** Standardizes module taxonomy across college courses for consistent student experience and QM (Quality Matters) compliance.

---

## 📁 Repository & Skill Directory Structure

```text
canvas-course-builder/
├── SKILL.md                          # Antigravity Agent Skill Blueprint & Instructions
├── README.md                         # Human-readable guide (this file)
├── scripts/                          # Zero-dependency Python CLI tools
│   ├── build_cartridge.py            # Master Common Cartridge compiler class
│   ├── qti_builder.py                # Markdown to QTI 1.2 XML quiz generator
│   ├── html_styler.py                # DesignPLUS ribbons & clean inner page styler
│   └── docx_syllabus.py              # Pure-Python Word (.docx) syllabus generator
├── templates/                        # Reusable course scaffolding templates
│   ├── course_config.example.json    # Full course configuration metadata template
│   └── unit_quiz_template.md         # 15-question Markdown quiz starter template
└── references/                       # Technical architecture & design standards
    ├── canvas_cc_architecture.md     # XML schemas, manifests, IDs & Canvas quirks
    └── designplus_guide.md           # CSS class tokens, palettes & responsive layout
```

---

## 🚀 How to Use in Any Project

### Method 1: Git Submodule (Recommended for Course Repositories)

Using Git submodules is the cleanest way to reference this skill across multiple course repositories. It keeps the skill centrally version-controlled while ensuring each course tracks a specific, stable version.

#### Step 1: Add Submodule to Your Course Repository
In the root directory of your target course project:
```bash
git submodule add https://github.com/tswarmLCCC/canvas-course-builder.git .agents/skills/canvas-course-builder
git commit -m "Add canvas-course-builder skill as submodule"
```

#### Step 2: Cloning Repositories That Use This Submodule
When cloning a course repository on a new machine or for another instructor:
```bash
# Clone and initialize submodules in one step:
git clone --recurse-submodules <course-repo-url>

# Or if the repo was already cloned normally:
git submodule update --init --recursive
```

#### Step 3: Updating the Skill to the Latest Version
When you push enhancements or bug fixes to this skill repository, update it inside your course repo:
```bash
# Pull the latest changes from the skill repo's main branch:
git submodule update --remote --merge

# Commit the submodule pointer update:
git commit -am "Update canvas-course-builder submodule to latest version"
```

---

### 📦 Initial Setup: Creating the Standalone Skill Repository

To publish this skill into its own dedicated GitHub repository:

1. **Create a clean directory outside your course repo:**
   ```bash
   mkdir c:\dev\canvas-course-builder
   ```
2. **Copy the skill contents into the new folder:**
   ```powershell
   Copy-Item -Recurse c:\dev\CMAP_1815_Autogen\.agents\skills\canvas-course-builder\* c:\dev\canvas-course-builder\
   ```
3. **Initialize Git and push to GitHub:**
   ```bash
   cd c:\dev\canvas-course-builder
   git init
   git add .
   git commit -m "Initial release: Canvas Course Builder skill and automation tools"
   git branch -M main
   git remote add origin https://github.com/tswarmLCCC/canvas-course-builder.git
   git push -u origin main
   ```

---

### Method 2: Global Configuration (Machine-Wide)

To make this skill automatically active in **all** projects on your computer without adding submodules or copying files:
```powershell
# Windows (PowerShell)
Copy-Item -Recurse c:\dev\canvas-course-builder "$HOME\.gemini\config\skills\canvas-course-builder"

# macOS / Linux
cp -r canvas-course-builder ~/.gemini/config/skills/canvas-course-builder
```

---

### Method 3: Command-Line Execution

You can also run the standalone Python utilities directly from your terminal:
```bash
# Convert a Markdown quiz to Canvas QTI 1.2 XML:
python scripts/qti_builder.py path/to/unit_quiz.md --out ./dist_quiz --title "Unit 1 Quiz"

# Generate an accredited Word Syllabus (.docx):
python scripts/docx_syllabus.py --code "CS 1010" --title "Intro to Computer Science" --out ./Syllabus.docx
```

---

## 📋 The Standard 8-Item Module Sequence

Each weekly unit follows this sequence:
1. `Unit X Overview: [Topic]` *(DesignPLUS Banner Ribbon)*
2. `Unit X: Required Readings & Video Lectures` *(Responsive 16:9 Video Chapters)*
3. `Unit X: Asynchronous Preparation & Drills` *(Interactive Expandable Self-Checks)*
4. `Unit X: Applied Lab Guide` *(Scenario, Instructions, HTML Rubric Table)*
5. `Unit X Applied Lab Assignment` *(Canvas Assignment, 50 pts, SpeedGrader)*
6. `Unit X: Learn with AI — Supplemental Practice Drill` *(Socratic Role-play Drill)*
7. `Unit X Knowledge Check: [Topic]` *(Native QTI 1.2 Quiz, 15 Questions, 30 pts)*
8. `[Instructor Guide] Unit X Teaching Notes & Solutions` *(Unpublished/Hidden)*

---

## 🛠️ Zero Dependencies
All scripts require **only standard Python 3.8+** (`xml.etree.ElementTree`, `zipfile`, `hashlib`, `html`, `re`, `json`). No `pip install` required!
