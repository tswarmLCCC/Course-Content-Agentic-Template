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

## 3. DesignPLUS Banner Ribbon Scaffolding

```html
<div id="dp-wrapper" class="dp-wrapper dp-hdg-i-cp-brdr-h2-dp-primary dp-hdg-txt-h3-dp-primary dp-hdg-txt-h4-dp-primary dp-hdg-txt-h5-dp-primary dp-hdg-i-cp-brdr-h5-dp-primary dp-hdg-b-h2-brdr-b dp-hdg-txt-h6-dp-primary dp-hdg-i-cp-brdr-h6-dp-primary dp-hdg-i-styl-h2-pill dp-hdg-i-styl-h3-pill dp-hdg-cp-brdr-h3-dp-secondary dp-hdg-cp-brdr-h2-dp-secondary dp-hdg-brdr-h2-1 dp-hdg-brdr-h3-1 dp-hdg-brdr-h4-1 dp-hdg-brdr-h5-1 dp-hdg-brdr-h6-1 dp-hdg-i-sz-h2-fill dp-hdg-i-sz-h3-fill dp-hdg-i-sz-h5-fill dp-hdg-i-sz-h6-fill dp-hdg-i-brdr-h5-2 dp-hdg-i-brdr-h6-2 dp-hdg-b-h3-brdr-b dp-hdg-txt-h2-dp-primary dp-hdg-i-brdr-h2-1 dp-hdg-i-brdr-h3-1 dp-hdg-i-sz-h4-fill dp-hdg-i-cp-brdr-h3-dp-primary dp-hdg-i-brdr-h4-1 dp-hdg-i-bg-h2-dp-primary dp-hdg-i-bg-h3-dp-primary dp-hdg-b-h4-brdr-b dp-hdg-d-h4-table-l dp-hdg-i-styl-h4-pill dp-hdg-i-cp-brdr-h4-dp-primary">
  <div class="dp-content-block">
    <header class="dp-header dp-basic-bar dp-header-s-brdr-l dp-header-brdr-w-4 dp-header-out-dp-secondary dp-header-pre-s-brdr-r dp-header-pre-font-sm dp-header-pre-out-dp-secondary dp-header-sub-brdr-w-0 dp-header-desc-txt-dp-primary dp-header-desc-out-dp-primary dp-header-sub-bg-dp-white dp-header-sub-txt-dp-primary dp-header-sub-out-dp-primary">
      <h2 class="dp-heading dp-locked"><span class="dp-header-title">Page Title Here</span></h2>
    </header>
    <div class="dp-lead-paragraph" style="font-size: 1.1em; line-height: 1.6; color: #1e293b; margin-bottom: 1.5rem;">
      <p>Introductory lead text goes here.</p>
    </div>
  </div>
  
  <!-- Accordion Section -->
  <div class="dp-content-block">
    <h3 class="dp-has-icon dp-locked"><i class="far fa-folder-open"><span class="dp-icon-content" style="display: none;">&nbsp;</span></i> <span>Section Title</span></h3>
    <div class="dp-panel-body" style="padding-left: 1rem; border-left: 2px solid #e2e8f0; margin-bottom: 1.5rem;">
      <p>Panel contents...</p>
    </div>
  </div>
</div>
```

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
