# DesignPLUS & Institutional Styling Reference Guide

This document captures the visual design standards, color palettes, CSS classes, and HTML scaffolding used to create Canvas courses with DesignPLUS styling and college branding.

---

## 1. Color Palette Tokens

| Semantic Role | Hex Value | Application |
| :--- | :--- | :--- |
| **Primary Navy** | `#1e3a8a` | Main page titles (`<h1>`), section headings (`<h2>`), table headers (`<th>`), callout left borders |
| **Dark Slate** | `#0f172a` | Syntax-highlighted code block backgrounds, terminal boxes, primary text accents |
| **Accent Royal Blue** | `#2563eb` | Action buttons, external links, primary interactive highlights |
| **Light Slate Background** | `#f8fafc` | Card callouts, alternating table zebra rows, instructor notes backgrounds |
| **Borders & Dividers** | `#cbd5e1` / `#e2e8f0` | Table cell borders, horizontal rules, accordion borders |
| **Success Alert** | `#16a34a` (text: `#15803d`, bg: `#f0fdf4`) | Tip callouts, sandbox launch alerts |
| **Danger Alert** | `#ef4444` (text: `#991b1b`, bg: `#fef2f2`) | Data deletion warnings, disaster recovery boxes |

---

## 2. Selective Banner Ribbon Policy

> [!IMPORTANT]
> To prevent visual fatigue, **never** apply heavy DesignPLUS banner ribbons to every single subpage in a module.
>
> **Apply the DesignPLUS Ribbon Header ONLY to:**
> - `Home Page` (Front Page)
> - `Start Here` / Orientation
> - `Unit XX Overview` (Weekly Module Launchers)
> - `Course Syllabus`
>
> **Use the Clean Standard Layout on all Inner Subpages:**
> - Readings & Video Lectures
> - Asynchronous Drills
> - Lab Guides & Submission pages
> - Supplemental AI Drills
> - Instructor Guides

---

## 3. Production Scaffolding Standards

### A. Front Page (`home-page.html`) Architecture (CMAP 1815 Gold Standard)
```html
<div id="dp-wrapper" class="dp-wrapper dp-hdg-i-cp-brdr-h2-dp-primary dp-hdg-txt-h3-dp-primary dp-hdg-txt-h4-dp-primary dp-hdg-txt-h5-dp-primary dp-hdg-i-cp-brdr-h5-dp-primary dp-hdg-b-h2-brdr-b dp-hdg-txt-h6-dp-primary dp-hdg-i-cp-brdr-h6-dp-primary dp-hdg-i-styl-h2-pill dp-hdg-i-styl-h3-pill dp-hdg-cp-brdr-h3-dp-secondary dp-hdg-cp-brdr-h2-dp-secondary dp-hdg-brdr-h2-1 dp-hdg-brdr-h3-1 dp-hdg-brdr-h4-1 dp-hdg-brdr-h5-1 dp-hdg-brdr-h6-1 dp-hdg-i-sz-h2-fill dp-hdg-i-sz-h3-fill dp-hdg-i-sz-h5-fill dp-hdg-i-sz-h6-fill dp-hdg-i-brdr-h5-2 dp-hdg-i-brdr-h6-2 dp-hdg-b-h3-brdr-b dp-hdg-txt-h2-dp-primary dp-hdg-i-brdr-h2-1 dp-hdg-i-brdr-h3-1 dp-hdg-i-sz-h4-fill dp-hdg-i-cp-brdr-h3-dp-primary dp-hdg-i-brdr-h4-1 dp-hdg-i-bg-h2-dp-primary dp-hdg-i-bg-h3-dp-primary dp-hdg-b-h4-brdr-b dp-hdg-d-h4-table-l dp-hdg-i-styl-h4-pill dp-hdg-i-cp-brdr-h4-dp-primary">
  
  <!-- QM Standards Note -->
  <div class="dp-action-item dp-action-item-block dp-action-item-note dp-locked" style="display: none;" aria-hidden="true">
    <p><em>Welcome to your Home Page! This page was designed with the guidance of QM Standards: <strong>SRS1.1, SRS7.1, SRS7.2, SRS7.3, SRS7.4</strong>.</em></p>
  </div>

  <!-- 1. DesignPLUS Banner Ribbon (Pure classes, zero inline styles) -->
  <div id="dp-wrapper_1" class="dp-header dp-basic-bar dp-header-s-brdr-l dp-header-brdr-w-4 dp-header-out-dp-secondary dp-header-pre-s-brdr-r dp-header-pre-font-sm dp-header-pre-out-dp-secondary dp-header-sub-brdr-w-0 dp-header-desc-txt-dp-primary dp-header-desc-out-dp-primary dp-header-sub-bg-dp-white dp-header-sub-txt-dp-primary dp-header-sub-out-dp-primary" data-header-class="dp-header dp-basic-bar variation-2" data-nav-class="container-fluid dp-link-grid">
    <header class="dp-header dp-basic-bar dp-header-s-brdr-l dp-header-brdr-w-4 dp-header-out-dp-secondary dp-header-pre-s-brdr-r dp-header-pre-font-sm dp-header-pre-out-dp-secondary dp-header-sub-brdr-w-0 dp-header-desc-txt-dp-primary dp-header-desc-out-dp-primary dp-header-sub-bg-dp-white dp-header-sub-txt-dp-primary dp-header-sub-out-dp-primary">
      <h1 class="dp-heading"><span class="dp-header-pre"><span class="dp-header-pre-1">COURSE 1010</span></span><span class="dp-header-title">Full Course Title Here</span></h1>
    </header>
  </div>

  <!-- 2. Centered 1100x220 Course Banner Image -->
  <div class="dp-banner-image" style="text-align: center; margin: 1rem 0;">
    <img role="presentation" src="$IMS-CC-FILEBASE$/images/course_banner.jpg" alt="Course Banner" width="1100" height="220" style="max-width: 100%; height: auto; border-radius: 6px; box-shadow: 0 4px 6px -1px rgba(0,0,0,0.1);" loading="lazy">
  </div>

  <!-- 3. Quick Links Navigation Grid (Pure classes, clean semantic list) -->
  <nav class="dp-link-grid container-fluid dp-link-grid-item-s-rounded dp-link-grid-item-bg-dp-primary dp-link-grid-hover-dp-accent dp-link-grid-icon-s-brdr-r dp-link-grid-icon-brdr-dp-secondary dp-link-grid-icon-brdr-w-2">
    <ul class="row">
      <li class="col-sm-12 col-md-4 col-lg-4"><a title="Course Overview" href="$WIKI_REFERENCE$/pages/page_start_here_id" data-course-type="wikiPages"><i class="fas fa-flag" aria-hidden="true"></i> Start Here: Course Overview</a></li>
      <li class="col-sm-12 col-md-4 col-lg-4"><a title="Syllabus" href="$CANVAS_COURSE_REFERENCE$/assignments/syllabus" data-course-type="navigation"><i class="fas fa-file-alt" aria-hidden="true"></i> Syllabus &amp; Policies</a></li>
      <li class="col-sm-12 col-md-4 col-lg-4"><a class="dp-has-icon" href="https://lcccwy.sharepoint.com/sites/StudentSuccessResources" target="_blank" rel="noopener"><i class="fas fa-external-link-alt" aria-hidden="true"></i> Student Resources</a></li>
    </ul>
  </nav>

  <!-- 4. Clean Welcome Block -->
  <div class="dp-content-block">
    <p style="text-align: left;"><strong>Welcome to COURSE 1010: Course Title! Please review the Course Overview, Syllabus, and Student Resources above to get started.</strong></p>
  </div>

  <!-- 5. Interactive Module List Accordion (Hyphenated titles, zero inline styles) -->
  <div class="dp-module-list dp-module-list-flag-completed dp-module-list-show-locked dp-quick-links-panels-accordion-plus dp-auto-update dp-panel-color-dp-primary dp-panel-active-color-dp-accent dp-panel-hover-color-dp-accent dp-quick-links-all dp-module-list-current-none">
    <nav class="dp-module-list-item-group">
      <ul class="fa-ul list-group">
        <li><a class="list-group-item list-group-item-action" href="$CANVAS_OBJECT_REFERENCE$/modules/mod_orient_id"><i class="fas fa-map-marker-alt"></i> Getting Started - Course Orientation</a></li>
        <li><a class="list-group-item list-group-item-action" href="$CANVAS_OBJECT_REFERENCE$/modules/mod_unit_1_id"><i class="fas fa-map-marker-alt"></i> Unit 01 - Relational Foundations</a></li>
      </ul>
    </nav>
  </div>
</div>
```

### B. Unit Overview Page (`unit-XX-overview.html`) Architecture
```html
<div id="dp-wrapper" class="dp-wrapper ...">
  <header class="dp-header dp-basic-bar dp-header-s-brdr-l dp-header-brdr-w-4 dp-header-out-dp-secondary dp-header-pre-s-brdr-r dp-header-pre-font-sm dp-header-pre-out-dp-secondary dp-header-sub-brdr-w-0 dp-header-desc-txt-dp-primary dp-header-desc-out-dp-primary dp-header-sub-bg-dp-white dp-header-sub-txt-dp-primary dp-header-sub-out-dp-primary">
    <h2 class="dp-heading dp-locked"><span class="dp-header-title">Unit 01 Overview: Relational Foundations</span></h2>
    <p>&nbsp;</p>
  </header>
  <div class="dp-content-block">
    <p>Welcome to Unit 01...</p>
  </div>
  <div class="dp-panels-wrapper dp-accordion-plus dp-panel-color-dp-primary dp-panel-active-color-dp-accent dp-panel-hover-color-dp-accent">
    <div class="dp-panel-group">
      <h2 class="dp-panel-heading ">Measurable Learning Objectives</h2>
      <div class="dp-panel-content ">
        <p>By the end of this unit, you will be able to...</p>
      </div>
    </div>
  </div>
</div>
```

### C. Strict Styling Anti-Patterns (NEVER DO)
1. **NEVER inject inline `style="background: #1e3a8a; color: #ffffff; ..."` on `<header>`, `<h1>`, `<h2>`, or `<span>`.**  
   *Result:* Destroys DesignPLUS theme variables, creates nested rectangles, and balloons the gold accent border into an oversized block.
2. **NEVER inject inline styles on `<ul>`, `<li>`, or `<a>` inside `<nav class="dp-link-grid">`.**  
   *Result:* Breaks the flex grid and detaches the gold icon divider into a floating `|` character.
3. **NEVER use colons (`:`) in module titles (e.g. `Unit 01: Foundations`).**  
   *Result:* DesignPLUS's client-side accordion splits on colons and strips everything after it, displaying only `Unit 01`. Always use hyphens (`Unit 01 - Foundations`).
4. **NEVER inject custom header divs (`<div>Course Modules</div>`) inside `.dp-module-list`.**  
   *Result:* Breaks DesignPLUS's DOM tree expectations and corrupts the accordion script.

---

## 4. Native Content Element Patterns

### A. Styled Data Tables (Zebra Rows & Navy Headers)
```html
<div style="overflow-x: auto; margin: 1.25rem 0;">
  <table style="width: 100%; border-collapse: collapse; border: 1px solid #cbd5e1; font-size: 0.95em;">
    <thead>
      <tr style="background-color: #1e3a8a; color: #ffffff;">
        <th style="padding: 10px 14px; border: 1px solid #94a3b8; font-weight: 600;">Criterion</th>
        <th style="padding: 10px 14px; border: 1px solid #94a3b8; font-weight: 600;">Points</th>
      </tr>
    </thead>
    <tbody>
      <tr style="background-color: #f8fafc;">
        <td style="padding: 8px 14px; border: 1px solid #cbd5e1;">Query Syntax &amp; Correctness</td>
        <td style="padding: 8px 14px; border: 1px solid #cbd5e1;">30 pts</td>
      </tr>
      <tr style="background-color: #ffffff;">
        <td style="padding: 8px 14px; border: 1px solid #cbd5e1;">Formatting &amp; Uppercase Keywords</td>
        <td style="padding: 8px 14px; border: 1px solid #cbd5e1;">20 pts</td>
      </tr>
    </tbody>
  </table>
</div>
```

### B. Dark Consolas Code Box
```html
<div style="background: #0f172a; color: #f8fafc; padding: 1rem 1.25rem; border-radius: 6px; overflow-x: auto; margin: 1.25rem 0; font-family: Consolas, Monaco, monospace; font-size: 0.9em; line-height: 1.5;">
  <pre style="margin: 0; background: transparent; color: inherit;"><code>SELECT employee_id, first_name, salary
FROM employees
WHERE salary &gt; 75000;</code></pre>
</div>
```

### C. Expandable Formative Drill (<details><summary>)
```html
<details style="background: #f8fafc; border: 1px solid #cbd5e1; border-radius: 6px; padding: 0.75rem 1.25rem; margin: 1rem 0;">
  <summary style="font-weight: 600; color: #1e3a8a; cursor: pointer; padding: 0.25rem 0;">Check Your Answer &amp; Explanation</summary>
  <div style="padding-top: 0.75rem; border-top: 1px solid #e2e8f0; margin-top: 0.5rem; line-height: 1.6;">
    <p>Detailed explanation and reasoning here.</p>
  </div>
</details>
```
