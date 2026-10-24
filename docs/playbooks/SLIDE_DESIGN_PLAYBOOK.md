# Universal Course Slide Design Playbook: Layouts, Code Hygiene & Visual Styling
**Institutional Presentation Specification for Higher Education & Enterprise Training**  
**Applies to All Modernized Courses in this Repository**

---

## 1. Executive Visual Philosophy

Presentations in high-stakes higher education and enterprise workforce programs must project authority, visual elegance, and pedagogical clarity. Generic white-background slides with unstyled black bullet points look amateur and disengage learners.

### The 5 Visual Principles:
1. **Assertion-Evidence Architecture:** Slide titles must make a complete declarative technical claim (e.g., *"Circuit Breakers Prevent Cascading Infrastructure Collapse"*), never a vague topic label (e.g., *"Circuit Breakers"*).
2. **Visual Card Encapsulation:** Content must be housed inside rounded rectangle containers with subtle color fills and contrasting borders.
3. **Strict Left-Aligned Code:** Code snippets must NEVER be centered or center-justified. Every paragraph must explicitly enforce `PP_ALIGN.LEFT` in a monospaced font.
4. **WCAG 2.1 AAA Color Contrast:** Text must exceed a 7:1 contrast ratio against card backgrounds; titles must exceed 11:1. Never use light yellow or light cyan text on white backgrounds.
5. **100% Speaker Notes Coverage:** Slides are visual anchors for students; deep instructional narratives, live-coding prompts, and common misconceptions belong in the embedded speaker notes.

### Pedagogical Cadence: The 4-Step Scaffolding Progression
Slides must not simply present syntax or isolated algorithms. Every technical capability must follow a 4-step pedagogical sequence:
1. **The Context:** Why are students studying this? (Real-world motivation and ecosystem relevance).
2. **The Problem Without It:** What breaks, fails, or scales terribly without this solution? (Dramatize the pain point/bottleneck).
3. **How It Works:** What is the conceptual/architectural mechanism? (Intuition, visual diagrams, cards).
4. **How to Use It:** How do we implement, measure, and tune it in modern code?

> [!TIP]
> **Calibrated Volume (Avoid Slide Bloat):** Use legacy decks as a benchmark for depth of instruction, but do not arbitrarily bloat slide counts. Aim for concise, high-impact cards with visual breathing room rather than 100+ repetitive slides.

---

## 2. The 5 Universal Slide Archetypes

Every presentation is built using a combination of these 5 proven layout archetypes:

```
┌─────────────────────────┐  ┌─────────────────────────┐  ┌─────────────────────────┐
│       [ 1. TITLE ]      │  │     [ 2. DIVIDER ]      │  │   [ 3. TWO-COLUMN ]     │
│ ┌─────┐ ┌─────────────┐ │  │ ┌─────────────────────┐ │  │ ┌─────────┐ ┌─────────┐ │
│ │ NAVY│ │ Main Title  │ │  │ │ NAVY / GOLD ACCENT  │ │  │ │ Card A   │ │ Card B   │ │
│ │ HERO│ │ Subtitle    │ │  │ │ SECTION 02          │ │  │ │ (Option A)│ │ (Option B)│ │
│ │ LCCC│ │ Meta Info   │ │  │ │ High-Contrast Hero  │ │  │ │ Anchor:  │ │ Anchor:  │ │
│ └─────┘ └─────────────┘ │  │ └─────────────────────┘ │  │ └─────────┘ └─────────┘ │
└─────────────────────────┘  └─────────────────────────┘  └─────────────────────────┘
┌─────────────────────────┐  ┌─────────────────────────┐
│       [ 4. NORMAL ]     │  │       [ 5. CODE ]       │
│ ┌─────────────────────┐ │  │ ┌─────────┐ ┌─────────┐ │
│ │ Full-Width Card     │ │  │ │ Concept │ │ Consolas│ │
│ │ Sequential Flow /   │ │  │ │ Spec    │ │ Code    │ │
│ │ Framework Checklist │ │  │ │ Points  │ │ (LEFT)  │ │
│ └─────────────────────┘ │  │ └─────────┘ └─────────┘ │
└─────────────────────────┘  └─────────────────────────┘
```

### Archetype 1: Split-Hero Title Slide
- **Left Hero Container (Width: 4.8", Height: 7.5"):** Dark institutional navy (`#002055`) with high-impact organization acronym (e.g., `AI4W`, `LCCC`, `INTEL`) in 64pt bold white, followed by program name and warm gold accent band (`#FFC001`, 0.18" width).
- **Right Container (Width: 7.3", Height: 5.5"):** Department eyebrow tag (14pt accent blue), main course title (40pt bold primary navy), horizontal gold divider rule, unit subtitle (20pt bold charcoal), and academic corequisite metadata (13pt muted text).

### Archetype 2: High-Contrast Section Divider Slide
- **Full Slide Background:** Rich dark section navy (`#002055`).
- **Vertical Gold Accent Bar (Width: 0.2", Height: 2.6"):** Anchored at left margin (`left=1.0", top=2.2"`).
- **Typography:** Section number in 14pt bold gold (`#FFC001`), section title in 36pt bold white, and descriptive subtitle in 18pt light ice blue (`#C8E1FA`).

### Archetype 3: Two-Column Comparison Cards
- **Use Cases:** Trade-off analysis, Theory vs Practice, Good vs Bad, Dual-Course Synchronization, Learning Objectives vs Unit Outcomes.
- **Left Card (Width: 5.6", Height: 4.9", Fill: Ice Blue `#F3F7FC`, Border: `#C2D6EC`):** Card title in 21pt bold navy; 2–4 bold anchor bullet items (`Anchor: `, body text).
- **Right Card (Width: 5.6", Height: 4.9", Fill: Warm Cream/Gold `#FFFDF0`, Border: `#F0CD5A`):** Matching structural hierarchy in warm contrast palette.

### Archetype 4: Normal Full-Width Content Card
- **Use Cases:** Sequential 4-step processes, course trajectory roadmaps, failure mode anatomies, or lab instruction checklists.
- **Dimensions:** Width: 11.7", Height: 4.9", Left: 0.8", Top: 1.8".
- **Container Styling:** Rounded rectangle with 1.5pt border, 0.4" internal padding, 3–4 scannable bold anchor items.

### Archetype 5: The Usable Code & Runbook Slide (Strictly Left-Aligned)
- **Use Cases:** Software algorithms, API requests, Dockerfile syntax, terminal commands, or structured configuration files.
- **Left Specification Card (Width: 5.2"):** Explains the architectural logic, mathematical model, or security parameters in 3–4 bold anchor points.
- **Right Code Card (Width: 6.2", Height: 4.9", Fill: Midnight Slate `#111827`, Border: `#374151`):** Dark syntax container displaying 10–20 lines of realistic code.

---

## 3. Strict Left-Aligned Code Formatting Specification

### 3.1 The PowerPoint Centering Trap
> [!WARNING]
> In `python-pptx`, any shape created via `shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE)` or `MSO_SHAPE.RECTANGLE` **DEFAULTS TO CENTER-JUSTIFIED TEXT**.
> If you add paragraphs without explicitly setting alignment, your code will render center-justified, destroying indentation and rendering code completely unreadable.

### 3.2 The Exact Python-PPTX Automation Recipe
To guarantee strictly left-aligned, production-quality code formatting, you must execute this loop for every line in the code block:

```python
from pptx.util import Inches, Pt
from pptx.enum.shapes import MSO_SHAPE
from pptx.enum.text import PP_ALIGN
from pptx.dml.color import RGBColor

# 1. Define Visual Midnight Container
CODE_BG = RGBColor(17, 24, 39)       # #111827 (Deep Slate)
CODE_LINE = RGBColor(55, 65, 81)     # #374151 (Border Slate)
CODE_TEXT = RGBColor(138, 212, 255)  # #8AD4FF (High-Contrast Cyan/Ice Blue)

code_card = slide.shapes.add_shape(
    MSO_SHAPE.ROUNDED_RECTANGLE, Inches(6.3), Inches(1.8), Inches(6.2), Inches(4.9)
)
code_card.fill.solid()
code_card.fill.fore_color.rgb = CODE_BG
code_card.line.color.rgb = CODE_LINE
code_card.line.width = Pt(1.5)

tf = code_card.text_frame
tf.word_wrap = True
tf.margin_left = Inches(0.25)
tf.margin_top = Inches(0.25)

# 2. Iterate Line-by-Line with STRICT Left Alignment
lines = raw_code_snippet.strip().split("\n")
for l_idx, line in enumerate(lines):
    p = tf.paragraphs[0] if l_idx == 0 else tf.add_paragraph()
    p.text = line if line else " "
    p.font.name = "Consolas"         # Clean monospaced font
    p.font.size = Pt(10.5)            # Readable 10.5pt size
    p.font.color.rgb = CODE_TEXT
    p.alignment = PP_ALIGN.LEFT       # <--- CRITICAL: ENFORCES LEFT ALIGNMENT
    p.space_after = Pt(1.5)
```

### 3.3 Code Usability Rules
- **Realistic & Functional:** Use real library calls (`import re, json, time`), sensible variable names, and production logic.
- **Never Use Trivial Pseudocode:** Avoid `<do magic here>` or abstract placeholders that leave students confused.
- **Enforce Indentation:** 4-space indentation must be strictly preserved.

---

## 4. Master Layout Cleaning (Stripping Third-Party Logos)

When modernizing legacy course decks, old vendor or institutional logos often linger in the slide master layouts, bleeding into new slides.

### The Automated Logo Stripper:
```python
# Programmatically clean legacy logos from slide masters
for master in prs.slide_masters:
    for layout in master.slide_layouts:
        for shp in list(layout.shapes):
            # Shape Type 13 = Picture; also check name for logo strings
            if shp.shape_type == 13 or "Picture" in shp.name or "Logo" in shp.name:
                sp_elem = shp._element
                sp_elem.getparent().remove(sp_elem)
```

---

## 5. Mandatory Academic Bibliography Slide Standard

Every unit presentation must conclude with a formal `References & Further Reading` slide formatted with academic rigor:
- **Left Column:** Foundational peer-reviewed academic papers or books (APA style, including authors, publication year, title, and journal/publisher).
- **Right Column:** Recognized industry standards, engineering whitepapers, regulatory frameworks (NIST, OWASP, ISO, IEEE, Intel Whitepapers, OpenVINO Docs, Google SRE).
- **Instructor Note Requirement:** Notes must explain how students can cite these sources in their project dossiers.
