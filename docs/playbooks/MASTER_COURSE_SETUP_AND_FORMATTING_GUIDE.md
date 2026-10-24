# Master Course Setup & Formatting Playbook
## The Complete Blueprint for Building Production-Grade Canvas LMS Courses

This guide packages all architectural standards, DesignPLUS styling components, HTML formatting engines, Socratic AI prompts, pedagogical models, and automation scripts used in **CMAP 1815: Modern SQL**. 

Bring this document and the accompanying tools in `agent_tools_catalog/` into any new course repository to immediately generate stunning, institutional-grade Canvas Common Cartridges (`.imscc`).

---

## 1. Why Other Canvas Pages Look Bad (And The Solution)

### The Three Common Failure Modes in Agent-Built Courses
1. **Raw Markdown Dumping:** An agent outputs markdown (`### Header`, `- bullet`, ````sql`) directly into Canvas WikiPages or `<pre><code>` wrappers. Canvas renders raw markdown as unstyled plain text or awkward browser defaults.
2. **Generic, Cluttered Visuals:** Use of default browser colors (plain blue links, generic gray borders) or repetitive, giant banner ribbons on every single subpage that force students to scroll before reading content.
3. **Broken Assessment Plumbing:** Using text files instead of native Canvas Assignments, unlinked gradebook categories, or manual quiz entry instead of programmatic QTI 1.2 XML.

### The Production Design System
To make pages feel executive, modern, and state-of-the-art:
- **Curated Color Palette:**
  - **Primary Brand Navy:** `#1e3a8a` (Deep institutional blue for major headers, table title bars, and active badges).
  - **Dark Code Container:** `#0f172a` (Sleek slate dark-mode background for SQL and code blocks).
  - **Accent / Alert Blue:** `#2563eb` / `#3b82f6` (Vibrant accent for due dates, key metrics, and hover states).
  - **Neutral Background Card:** `#f8fafc` (Ultra-light slate for lead cards, study callouts, and zebra stripes).
  - **Structural Borders:** `#cbd5e1` (Table and card borders) & `#e2e8f0` (Section divider lines).
- **Typography Stack:**
  `-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif`
- **Selective Ribbon Policy:**
  - **Use DesignPLUS Banner Ribbons ONLY on:** Course Home Page, Start Here Orientation, Weekly Unit Overviews, and the Master Syllabus page.
  - **Use Clean Standard Layout on all Inner Pages:** Reading pages, lab guides, study drills, and AI practice use clean typography with styled section headers and lead cards—never repetitive banner ribbons.

---

## 2. The Universal 8-Item Weekly Module Taxonomy

Every weekly unit follows this strict, proven sequence inside Canvas Modules:

| Seq | Item Title Convention | Canvas Item Type | State | Pedagogical Role |
| :---: | :--- | :--- | :---: | :--- |
| **1** | `Unit X Overview: [Topic]` | `WikiPage` | Published | Roadmap, contact-hour budget (150m study / 150m lab), learning outcomes. Uses DesignPLUS ribbon. |
| **2** | `Unit X: Required Readings, Concepts & Video Lectures` | `WikiPage` | Published | Curated instructor lecture deep-dive, official documentation links, 16:9 embedded video chapters, and campus video slot. |
| **3** | `Unit X: Asynchronous Preparation & Drills` | `WikiPage` | Published | Conceptual focus questions and formative self-check drills with interactive `<details>/<summary>` answer keys. |
| **4** | `Unit X: Applied Lab Guide` | `WikiPage` | Published | Business scenario, step-by-step challenges, and full native HTML grading rubric table. |
| **5** | `Unit X Applied Lab Assignment` | `Assignment` | Published | Native Canvas Assignment (50 pts) for SpeedGrader file upload (`.sql`, `.py`, `.txt`), official deadline, and rubric. |
| **6** | `Unit X: Learn with AI — Supplemental Practice Drill` | `WikiPage` | Published | Socratic roleplay scenario, free tools guide, copy-paste master prompt, and weekly discussion debrief task. |
| **7** | `Unit X Knowledge Check: [Topic]` | `Quizzes::Quiz` | Published | Native QTI 1.2 assessment (15 questions, 30 pts, 3 attempts, highest score kept). |
| **8** | `[Instructor Guide] Unit X Teaching Notes & Solutions` | `WikiPage` | **Unpublished** | Hidden from students. Synchronous delivery agenda, lecture notes, demo contingency runbooks, and solution keys. |

---

## 3. Master HTML Component Library (Copy-Paste Ready)

When generating Canvas page HTML, use these pre-styled semantic components:

### A. Lead Card / Summary Callout
```html
<div style="background: #f8fafc; border-left: 4px solid #1e3a8a; padding: 1rem 1.25rem; margin-bottom: 1.75rem; border-radius: 0 4px 4px 0; font-size: 1.05em; line-height: 1.5; color: #334155;">
  <p style="margin: 0;"><strong>Welcome to Unit 1!</strong> Complete the guided tutorials, embedded micro-video lectures, and hands-on laboratory exercises outlined below.</p>
</div>
```

### B. Due Date & Calendar Alert Box
```html
<div style="background: #eff6ff; border-left: 4px solid #2563eb; padding: 0.75rem 1.25rem; margin: 1rem 0; border-radius: 0 4px 4px 0;">
  <p style="margin: 0; font-weight: 600; color: #1e40af;"><i class="far fa-calendar-alt"></i> Due Date: Friday, October 23, 2026 at 11:59 PM MT</p>
</div>
```

### C. Native Styled Rubric & Data Table (Zebra Striped)
```html
<table style="width: 100%; border-collapse: collapse; border: 1px solid #cbd5e1; margin: 1.5rem 0; font-size: 0.95em;">
  <thead>
    <tr style="background: #1e3a8a; color: #ffffff;">
      <th style="padding: 0.75rem 1rem; text-align: left; border: 1px solid #cbd5e1;">Criteria</th>
      <th style="padding: 0.75rem 1rem; text-align: left; border: 1px solid #cbd5e1;">Exemplary (Full Points)</th>
      <th style="padding: 0.75rem 1rem; text-align: left; border: 1px solid #cbd5e1;">Developing (Partial)</th>
      <th style="padding: 0.75rem 1rem; text-align: center; border: 1px solid #cbd5e1;">Points</th>
    </tr>
  </thead>
  <tbody>
    <tr style="background: #ffffff;">
      <td style="padding: 0.65rem 1rem; font-weight: 600; border: 1px solid #cbd5e1;">1. Execution & Accuracy</td>
      <td style="padding: 0.65rem 1rem; border: 1px solid #cbd5e1;">All queries execute cleanly with zero syntax errors.</td>
      <td style="padding: 0.65rem 1rem; border: 1px solid #cbd5e1;">1–2 minor syntax or logic errors.</td>
      <td style="padding: 0.65rem 1rem; text-align: center; font-weight: bold; border: 1px solid #cbd5e1;">40</td>
    </tr>
    <tr style="background: #f8fafc;">
      <td style="padding: 0.65rem 1rem; font-weight: 600; border: 1px solid #cbd5e1;">2. Formatting Standards</td>
      <td style="padding: 0.65rem 1rem; border: 1px solid #cbd5e1;">Keywords uppercase, clauses on new lines.</td>
      <td style="padding: 0.65rem 1rem; border: 1px solid #cbd5e1;">Mixed casing or single-line run-ons.</td>
      <td style="padding: 0.65rem 1rem; text-align: center; font-weight: bold; border: 1px solid #cbd5e1;">20</td>
    </tr>
  </tbody>
</table>
```

### D. Dark Modern Syntax Box (Code & SQL Snippets)
```html
<div style="background: #0f172a; color: #f8fafc; padding: 1rem 1.25rem; border-radius: 6px; font-family: Consolas, Monaco, 'Courier New', monospace; font-size: 0.9em; margin: 1rem 0; overflow-x: auto;">
  <pre style="margin: 0; background: transparent; color: inherit;"><code>SELECT product_name, retail_price
FROM products
WHERE retail_price &gt; 100.00
ORDER BY retail_price DESC;</code></pre>
</div>
```

### E. Interactive Formative Drill Accordion (`<details>/<summary>`)
```html
<details style="background: #f8fafc; border: 1px solid #cbd5e1; border-radius: 6px; padding: 0.75rem 1.25rem; margin: 1rem 0;">
  <summary style="cursor: pointer; font-weight: 600; color: #1e3a8a; padding: 0.25rem 0;">
    🔍 Self-Check: Click to Reveal the Instructor Solution & Explanation
  </summary>
  <div style="margin-top: 0.75rem; padding-top: 0.5rem; border-top: 1px dashed #cbd5e1;">
    <p><strong>Correct Answer:</strong> In SQL, <code>salary + NULL</code> evaluates to <code>NULL</code> because NULL represents an unknown value.</p>
    <div style="background: #0f172a; color: #f8fafc; padding: 0.5rem 0.75rem; border-radius: 4px; font-family: Consolas, monospace;">
      <pre style="margin: 0; background: transparent; color: inherit;"><code>SELECT last_name, COALESCE(bonus, 0) AS safe_bonus FROM employees;</code></pre>
    </div>
  </div>
</details>
```

### F. Responsive 16:9 Video Embed Card
```html
<div style="margin: 1.5rem 0; background: #ffffff; border: 1px solid #cbd5e1; border-radius: 8px; overflow: hidden; box-shadow: 0 1px 3px rgba(0,0,0,0.05);">
  <div style="background: #1e3a8a; color: #ffffff; padding: 0.6rem 1rem; font-weight: 600; font-size: 0.95em;">
    <i class="fas fa-play-circle"></i> Video Chapter: Relational Foundations (0:05:17)
  </div>
  <div style="position: relative; padding-bottom: 56.25%; height: 0; overflow: hidden;">
    <iframe style="position: absolute; top: 0; left: 0; width: 100%; height: 100%; border: 0;" 
            src="https://www.youtube-nocookie.com/embed/qw--VYLpxG4?start=317" 
            title="Relational Foundations" 
            allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" 
            allowfullscreen></iframe>
  </div>
</div>
```

### G. Custom Campus / Institutional Video Placeholder
```html
<div style="background: #f8fafc; border: 2px dashed #94a3b8; border-radius: 6px; padding: 1.5rem; margin: 1rem 0; text-align: center;">
  <p style="font-size: 1.1em; font-weight: 600; color: #1e3a8a; margin-top: 0; margin-bottom: 0.5rem;">
    <i class="fas fa-video"></i> Custom Institutional Video Embed Slot
  </p>
  <p style="color: #475569; margin-bottom: 0.5rem; font-size: 0.95em;">
    This section is reserved for custom institutional lecture recordings (Canvas Studio, Panopto, Kaltura, or unlisted media embeds).
  </p>
  <p style="color: #64748b; font-size: 0.85em; margin-bottom: 0;">
    <em>[Instructor Notice: Use the Canvas Rich Content Editor to insert your campus video iframe directly into this placeholder.]</em>
  </p>
</div>
```

---

## 4. Master "Learn with AI" Prompts & Scenarios

Every unit features a graded **Learn with AI** drill. Rather than asking AI for answers, students engage in Socratic role-playing:

### The Golden Rule of AI Practice
> *"Never assume an AI's code is correct! Every single query or code snippet discussed with AI must be executed and verified against your live database environment before submitting."*

### Archetype 1: The Socratic Professor (Conceptual Reasoning)
```text
Act as a strict, Socratic computer science professor named Professor Codd. I am a student learning [TOPIC]. 
Do NOT give me direct answers or write the code for me.
Instead, ask me one challenging question at a time to test my understanding of:
1. [Core Concept 1]
2. [Underlying Mental Model 2]
3. [Common Industry Anti-Pattern 3]
Start by asking me your first question. Wait for my response before evaluating my reasoning and asking the next question.
```

### Archetype 2: The Pedantic QA Lead (Edge Cases & Traps)
```text
Act as a pedantic Senior Database QA Engineer. I am writing code using [SYNTAX/TOOLS].
Present me with 3 realistic code snippets that contain subtle logic bugs related to:
1. Edge cases and boundary conditions.
2. Silent data corruption or unexpected type conversions.
3. Operator precedence or missing parentheses.
Present the first buggy snippet and ask me to identify the exact trap and how to fix it. Do NOT reveal the fix until I attempt an answer.
```

### Archetype 3: The Non-Technical Stakeholder (Requirements Translation)
```text
Act as a stressed-out VP of Operations at an enterprise company. You do NOT know SQL or programming; you only understand business problems and revenue metrics.
Present me with a realistic business dilemma and ask me to pull the data you need to make a decision. 
Critique whether my technical questions help clarify your business requirements.
```

---

## 5. Course Setup & Packaging Automation

To build any course into a native Canvas Common Cartridge (`.imscc`):

### Directory Structure of a Course Repository
```text
my-course-repo/
├── .agents/skills/canvas-course-builder/   # Modular cartridge builder engine
├── course_specs/                          # Syllabus, rubrics, and media specs
├── units/
│   ├── unit_01_[topic]/
│   │   ├── lectures/                      # Lecture notes and slides
│   │   ├── async/                         # Study guide and self-check drills
│   │   ├── guides/                        # Student lab guide and solution keys
│   │   └── assessments/                   # Rubric and 15-question unit quiz
├── scripts/
│   └── build_canvas_cartridge.py          # Master compilation script
├── agent_tools_catalog/                   # Master catalog of shared assets
└── README.md
```

### How to Run the Build Engine:
```bash
python scripts/build_canvas_cartridge.py
```

### What the Engine Generates Automatically:
1. **Directory Tree:** Creates standard Canvas CC structures (`wiki_content/`, `course_settings/`, `non_cc_assessments/`, assignment folders, and quiz folders).
2. **Deterministic MD5 Hashing:** Ensures every page, assignment, and quiz has stable 32-character identifiers across builds.
3. **HTML Transformation:** Translates markdown tables into zebra-striped HTML, wraps code blocks, and builds interactive `<details>` tags.
4. **Weighted Gradebook:** Emits `assignment_groups.xml` with institutional 100% weighted distribution (Labs 40%, Capstone 30%, Quizzes 20%, Preparation 10%).
5. **Native QTI 1.2 Quizzes:** Parses markdown question sets into compliant QTI assessment XML with 3 attempts and highest score retained.
6. **Schema Validation:** Validates all 38+ generated XML files using `xml.etree.ElementTree` to guarantee zero syntax errors upon Canvas import.
7. **ZIP Compression:** Assembles all resources into a single `.imscc` file ready for Canvas import.

---

## 6. How to Deploy into Canvas in 60 Seconds

1. Open your Canvas course &rarr; click **Settings** (bottom left menu).
2. Click **Import Course Content** (right sidebar).
3. Under **Content Type**, select: **Common Cartridge 1.x Package**.
4. Click **Choose File** &rarr; select `[CourseName]_Complete.imscc`.
5. Select **All content**.
6. Click **Import**.
7. Once finished, verify that:
   - Front Page is automatically set to **Home Page** with the module accordion.
   - All modules display in the clean 8-item sequence.
   - Assignments accept `.sql` / file uploads in SpeedGrader.
   - Rubrics render as crisp, bordered HTML tables.
   - Quizzes are populated in the Quizzes tab with 3 attempts allowed.
