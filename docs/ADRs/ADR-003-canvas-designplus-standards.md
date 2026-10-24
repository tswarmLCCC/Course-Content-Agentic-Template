# ADR-003: Canvas Common Cartridge Packaging & DesignPLUS Theme Invariants

- **Status**: Accepted
- **Date**: 2026-10-24
- **Deciders**: Workspace Team & AI Assistant
- **Cross-References**: [ADR-001 (Accessibility)](./ADR-001-accessibility.md), [ADR-002 (Spec-Driven Development)](./ADR-002-spec-driven-development.md), [DesignPLUS Guide](../../.agents/skills/canvas-course-builder/references/designplus_guide.md), [Canvas Cartridge Architecture](../../.agents/skills/canvas-course-builder/references/canvas_cc_architecture.md)

---

## Context
When packaging courses into Canvas LMS via Common Cartridge (`.imscc`), subtle deviations in HTML metadata, CSS classes, DOM hierarchy, and title punctuation cause severe visual and behavioral regressions in Canvas:

1. **"HTML File Attachment / Sandboxed Iframe Bug"**: Canvas imports `.html` files as static file attachments in "Files" and embeds them inside an iframe with a disruptive "Download filename.html" banner, rather than rendering them as native Rich Content Editor (RCE) WikiPages.
2. **"Conflicting Inline CSS / Ballooning Accent Bar Bug"**: Hand-coding inline styles (`background: #1e3a8a`, `border-left`, hardcoded padding, inline font colors) onto DesignPLUS components (`dp-header`, `dp-link-grid`, `dp-module-list`, `dp-panel-group`) clobbers the institution's DesignPLUS theme. In Canvas, this causes nested boxes, disjointed fonts, and distorts the gold accent border into a massive block.
3. **"Detached Icon Dividers in Navigation Grids"**: Forcing `display: block` and background fills on `<a>` tags inside `<nav class="dp-link-grid">` breaks DesignPLUS flexbox, detaching the gold vertical icon divider into a floating `|` character.
4. **"DesignPLUS Accordion Title Truncation Bug"**: DesignPLUS's client-side JavaScript accordion parser (`dp-quick-links-panels-accordion-plus`) splits module titles on a colon (`:`). When modules are titled `Unit 01: Relational Foundations`, DesignPLUS parses `Unit 01:` as a module number and strips `Relational Foundations` entirely from the accordion header bar.
5. **"Missing Course Banner Image"**: Canvas home pages look barren and incomplete when omitting the standardized 1100x220 course hero banner.

---

## Decision
All course authoring tools, compilation scripts, and cartridge builders in this repository **shall strictly enforce the following six architectural invariants**:

### Invariant 1: Mandatory Native WikiPage `<head>` Metadata Contract
Every HTML page in `wiki_content/` must contain the exact Canvas RCE WikiPage metadata in `<head>`:
```html
<head>
<meta http-equiv="Content-Type" content="text/html; charset=utf-8"/>
<title>Page Title Here</title>
<meta name="identifier" content="{page_id}"/>
<meta name="editing_roles" content="teachers"/>
<meta name="workflow_state" content="active"/>   <!-- or "unpublished" for instructor guides -->
<meta name="front_page" content="true"/>        <!-- ONLY on home-page.html -->
<meta name="editor_type" content="rce"/>
</head>
```
- In `imsmanifest.xml`, declare as `<resource identifier="{page_id}" type="webcontent" href="wiki_content/{filename}"><file href="wiki_content/{filename}"/></resource>`.
- In `course_settings/module_meta.xml`, declare `<content_type>WikiPage</content_type>` with matching `<identifierref>{page_id}</identifierref>`.
- **Violation consequence:** Omitting `<meta name="identifier">` or `<meta name="editor_type" content="rce"/>` causes Canvas to sandbox the page in an iframe with a "Download" banner.

### Invariant 2: Pure DesignPLUS Theme Classes (Zero Conflicting Inline CSS)
Never inject hardcoded background colors, borders, or font colors into DesignPLUS structural elements. Allow the institution's theme CSS classes to govern typography, spacing, and brand colors natively:
- **Banner Ribbons:** Use `<header class="dp-header dp-basic-bar dp-header-s-brdr-l dp-header-brdr-w-4 dp-header-out-dp-secondary ...">` without inline background or border overrides.
- **Header Text:** Use `<h1 class="dp-heading"><span class="dp-header-pre"><span class="dp-header-pre-1">{c_code}</span></span><span class="dp-header-title">{c_title}</span></h1>`.
- **Panel Groups:** Use clean `<div class="dp-panel-group"><h2 class="dp-panel-heading ">{title}</h2><div class="dp-panel-content ">{content}</div></div>` without inline background fills or border styles.
- **Violation consequence:** Inline CSS causes visual glitches, double borders, broken contrast, and theme clashing inside Canvas.

### Invariant 3: Standard 1100x220 Centered Banner Image
Every course home page (`home-page.html`) must feature a centered, rounded 1100x220 banner image directly below the header ribbon:
```html
<div class="dp-banner-image" style="text-align: center; margin: 1rem 0;">
  <img role="presentation" 
       src="$IMS-CC-FILEBASE$/images/course_banner.jpg" 
       alt="{c_code}: {c_title} Course Banner" 
       width="1100" 
       height="220" 
       style="max-width: 100%; height: auto; border-radius: 6px; box-shadow: 0 4px 6px -1px rgba(0,0,0,0.1);" 
       loading="lazy">
</div>
```
- Cartridge compilation scripts must bundle the banner into `web_resources/images/course_banner.jpg` and register it in `imsmanifest.xml` as a `webcontent` resource.

### Invariant 4: Hyphenated Module Titles (No Colons)
All unit module titles across `imsmanifest.xml`, `module_meta.xml`, and `home-page.html` must use **hyphens (` - `)** instead of colons:
- **Correct:** `Unit 01 - Relational Foundations & Vectorized Ingestion`
- **Forbidden:** `Unit 01: Relational Foundations & Vectorized Ingestion`
- **Rationale:** DesignPLUS client-side accordion scripts split on colons. Hyphens prevent the accordion parser from truncating the module subtitle.

### Invariant 5: Clean Semantic DOM for Navigation Grids and Module Lists
- **Quick Links:** Use clean `<nav class="dp-link-grid container-fluid ..."><ul class="row"><li class="col-sm-12 col-md-4 col-lg-4"><a ...><i class="fas fa-..."></i> Label</a></li></ul></nav>` with zero inline styles on `<ul>`, `<li>`, or `<a>`.
- **Module Accordion:** Use clean `<div class="dp-module-list ..."><nav class="dp-module-list-item-group"><ul class="fa-ul list-group"><li><a class="list-group-item list-group-item-action" href="$CANVAS_OBJECT_REFERENCE$/modules/{m_id}"><i class="fas fa-map-marker-alt"></i> Unit XX - Title</a></li></ul></nav></div>`.
- **Forbidden:** Never insert custom header divs (`<div>Course Modules</div>`) or custom inline flexbox styling inside `.dp-module-list` or `.dp-link-grid`.

### Invariant 6: Automated XML Validation and Cartridge Backups
1. Every cartridge build must parse all generated XML and QTI files with `xml.etree.ElementTree.parse()` to guarantee zero XML syntax errors before packaging.
2. The compiler must automatically preserve prior `.imscc` builds with ISO timestamps in `archive/cartridge_backups/` before writing a new package.

---

## Consequences
- Guarantees 100% style and behavioral fidelity upon Canvas import across all courses in the monorepo.
- Eliminates manual post-import patching, iframe debugging, and accordion title repair.
- Any future cartridge compiler script or course automation tool must pass these six invariant checks.
