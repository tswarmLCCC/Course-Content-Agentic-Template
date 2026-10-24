#!/usr/bin/env python3
"""
=============================================================================
Portable Canvas Course Cartridge Compiler (build_course.py)
=============================================================================
Zero-dependency CLI tool that compiles a production-grade, DesignPLUS-styled
Canvas Common Cartridge (.imscc) package from standard Markdown files and a JSON config.

Solves the Common Canvas Cartridge Import Bugs Once and For All:
1. "HTML File Links / Sandboxed Iframes": Fixes the bug where Canvas imports
   pages as raw file attachments in "Files" and embeds them inside an iframe with
   a 'Download filename.html' banner. (Enforces complete Canvas WikiPage <head>
   metadata: identifier, editing_roles, workflow_state, and editor_type).
2. "Home Page & Interactive Accordions": Generates the Canvas Front Page (home-page.html)
   with <meta name="front_page" content="true"/>, Quick Navigation cards, and the
   official DesignPLUS module accordion (dp-quick-links-panels-accordion-plus)
   linking directly to every course module ($CANVAS_OBJECT_REFERENCE$/modules/{id}).
3. "Unit Overviews with Collapsible Panels": Renders DesignPLUS ribbon banners and
   interactive accordion panels (dp-panels-wrapper dp-accordion-plus) for Objectives,
   Roadmap, and Contact Hours.
4. "Orientation Module": Generates the comprehensive 'Getting Started - Course Orientation'
   module with Start Here, Learn with AI guidelines, and Syllabus policies.
5. "Un-graded Quizzes": Compiles native QTI 1.2 XML with Canvas assessment_meta.xml
   settings directly from clean Markdown files.
6. "Generic Assignments": Packages native Canvas Assignments with SpeedGrader
   file upload filters (.sql, .py, .parquet, .txt, .pdf) and weighted gradebook groups.
7. "Automated Cartridge Backups": Automatically preserves previous .imscc builds
   with timestamps in archive/cartridge_backups/ before generating new packages.

Usage:
  python build_course.py --config course_config.json --units-dir units --output Course_Export.imscc
=============================================================================
"""

import os
import sys
import re
import json
import argparse
import html
import shutil
import datetime
from typing import Dict, List, Any, Optional

# Add scripts directory to module path
SCRIPT_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "scripts")
sys.path.insert(0, SCRIPT_DIR)

from build_cartridge import CanvasCourseBuilder
from html_styler import (
    render_designplus_html,
    render_standard_page_html,
    render_ribbon_sections_page_html,
    parse_markdown_to_html,
    parse_markdown_sections
)
from qti_builder import parse_quiz_md, make_canvas_id
from docx_syllabus import create_syllabus_docx


def load_config(config_path: str) -> Dict[str, Any]:
    """Loads course configuration JSON."""
    if not os.path.exists(config_path):
        raise FileNotFoundError(f"Configuration file not found: {config_path}")
    with open(config_path, "r", encoding="utf-8") as f:
        return json.load(f)


def find_file(directory: str, patterns: List[str]) -> Optional[str]:
    """Finds first file in directory matching any pattern in patterns."""
    if not os.path.exists(directory):
        return None
    for root, _, files in os.walk(directory):
        for f in sorted(files):
            for pat in patterns:
                if re.search(pat, f, re.IGNORECASE):
                    return os.path.join(root, f)
    return None


def compile_course(config_path: str, units_dir: str, output_imscc: str, build_dir: Optional[str] = None):
    print("=" * 70)
    print("Portable Canvas Course Cartridge Compiler (DesignPLUS & Native WikiPages)")
    print("=" * 70)

    config = load_config(config_path)
    c_code = config.get("course_code", "COURSE 1010")
    c_title = config.get("course_title", "Sample Course")
    institution = config.get("institution", "Laramie County Community College")
    print(f"Target Course: {c_code} - {c_title}")
    print(f"Units Folder:  {units_dir}")
    print(f"Output File:   {output_imscc}\n")

    builder = CanvasCourseBuilder(config, output_imscc, build_dir=build_dir)
    builder.prepare_directories()

    # 1. Assignment Groups (Gradebook Weighting)
    group_map = builder.build_assignment_groups()
    labs_gid = group_map.get("labs", list(group_map.values())[0])
    quizzes_gid = group_map.get("quizzes", list(group_map.values())[0])

    # 2. Core Settings
    builder.build_core_settings()

    # 3. Native Syllabus Page & Word Document
    syllabus_md_file = find_file(os.path.dirname(config_path), ["syllabus\\.md"])
    syllabus_body = "<p>Welcome to modern online coursework.</p>"
    if syllabus_md_file:
        with open(syllabus_md_file, "r", encoding="utf-8") as sf:
            syllabus_body = parse_markdown_to_html(sf.read())

    # Build Word Syllabus .docx
    docx_filename = f"{c_code.replace(' ', '_')}_Master_Syllabus.docx"
    docx_path = os.path.join(builder.syllabi_dir, docx_filename)
    try:
        breakdown = [f"{g.get('name', 'Assignment')}: {g.get('weight', 0)}%" for g in config.get("assignment_groups", [])]
        create_syllabus_docx(
            output_path=docx_path,
            course_code=c_code,
            course_title=c_title,
            term_str=config.get("term", "Fall 2026"),
            institution=institution,
            credits_str=config.get("credits", "3.0 Credit Hours"),
            description=config.get("description", ""),
            outcomes=config.get("learning_outcomes", []),
            grading_breakdown=breakdown,
            grading_scale=config.get("grading_scale", "A: 90 - 100% | B: 80 - 89% | C: 70 - 79% | D: 60 - 69% | F: 0 - 59%")
        )
        print(f"  [+] Generated Master Syllabus (.docx): {docx_filename}")
    except Exception as e:
        print(f"  [!] Note: docx syllabus generation skipped: {e}")

    # Build Native Syllabus HTML
    docx_rel = os.path.relpath(docx_path, builder.web_res_dir).replace(os.sep, "/")
    syllabus_html = f"""<div class="dp-header dp-basic-bar" style="background: #1e3a8a; color: #ffffff; padding: 1.5rem; border-radius: 6px; margin-bottom: 1.5rem;">
  <h1 style="margin: 0; color: #ffffff; font-size: 1.8rem;">{html.escape(c_code)}: {html.escape(c_title)}</h1>
  <p style="margin: 0.5rem 0 0 0; opacity: 0.9;">Institutional Course Syllabus &amp; Policies</p>
</div>
<div style="background: #eff6ff; border-left: 4px solid #2563eb; padding: 1rem 1.25rem; margin-bottom: 1.5rem; border-radius: 0 4px 4px 0;">
  <p style="margin: 0; font-weight: 600;">Download Official Word Document Syllabus:</p>
  <p style="margin: 0.25rem 0 0 0;"><a class="instructure_file_link" title="{docx_filename}" href="$IMS-CC-FILEBASE$/{docx_rel}?canvas_=1&amp;canvas_qs_wrap=1" target="_blank" rel="noopener" style="color: #2563eb; font-weight: 600; text-decoration: underline;">&#128196; {docx_filename}</a></p>
</div>
{syllabus_body}
"""
    with open(os.path.join(builder.settings_dir, "syllabus.html"), "w", encoding="utf-8") as f:
        f.write(syllabus_html)

    # 4. Discover Weekly Units & Pre-generate Module IDs
    unit_folders = []
    if os.path.exists(units_dir):
        unit_folders = [f for f in sorted(os.listdir(units_dir)) if os.path.isdir(os.path.join(units_dir, f))]

    print(f"  [*] Discovered {len(unit_folders)} unit folders under {units_dir}/")

    mod_orient_id = make_canvas_id("module_orientation")
    unit_mod_ids = {u_idx: make_canvas_id(f"mod_unit_{u_idx}") for u_idx in range(1, len(unit_folders) + 1)}

    # 5. Generate Front Page (home-page.html) with DesignPLUS Quick-Links Module Accordion
    p_home_id = make_canvas_id("page_home_front")
    p_start_here_id = make_canvas_id("page_start_here")
    p_orient_syl_id = make_canvas_id("page_orient_syllabus")

    mod_links_lis = [
        f'<li style="border-bottom: 1px solid #e2e8f0; background: #ffffff;"><a class="list-group-item list-group-item-action" href="$CANVAS_OBJECT_REFERENCE$/modules/{mod_orient_id}" style="display: flex; align-items: center; gap: 0.75rem; padding: 0.85rem 1.25rem; color: #1e293b; text-decoration: none; font-weight: 600; font-size: 1.05em;"><i class="fas fa-map-marker-alt" style="color: #2563eb;"></i> Getting Started - Course Orientation</a></li>'
    ]

    for u_idx, u_folder in enumerate(unit_folders, 1):
        u_title = u_folder.replace("_", " ").title()
        u_title_clean = re.sub(r"^Unit\s*\d+\s*", "", u_title, flags=re.IGNORECASE).strip()
        u_display_title = f"Unit {u_idx:02d}: {u_title_clean}" if u_title_clean else f"Unit {u_idx:02d}"
        m_id = unit_mod_ids[u_idx]
        mod_links_lis.append(f'<li style="border-bottom: 1px solid #e2e8f0; background: #ffffff;"><a class="list-group-item list-group-item-action" href="$CANVAS_OBJECT_REFERENCE$/modules/{m_id}" style="display: flex; align-items: center; gap: 0.75rem; padding: 0.85rem 1.25rem; color: #1e293b; text-decoration: none; font-weight: 600; font-size: 1.05em;"><i class="fas fa-map-marker-alt" style="color: #2563eb;"></i> {html.escape(u_display_title)}</a></li>')

    mod_links_joined = "\n".join(mod_links_lis)

    home_html = f"""<html>
<head>
<meta http-equiv="Content-Type" content="text/html; charset=utf-8"/>
<title>Home Page</title>
<meta name="identifier" content="{p_home_id}"/>
<meta name="editing_roles" content="teachers"/>
<meta name="workflow_state" content="active"/>
<meta name="front_page" content="true"/>
<meta name="editor_type" content="rce"/>
</head>
<body>
<div id="dp-wrapper" class="dp-wrapper dp-hdg-i-cp-brdr-h2-dp-primary dp-hdg-txt-h3-dp-primary dp-hdg-txt-h4-dp-primary dp-hdg-txt-h5-dp-primary dp-hdg-i-cp-brdr-h5-dp-primary dp-hdg-b-h2-brdr-b dp-hdg-txt-h6-dp-primary dp-hdg-i-cp-brdr-h6-dp-primary dp-hdg-i-styl-h2-pill dp-hdg-i-styl-h3-pill dp-hdg-cp-brdr-h3-dp-secondary dp-hdg-cp-brdr-h2-dp-secondary dp-hdg-brdr-h2-1 dp-hdg-brdr-h3-1 dp-hdg-brdr-h4-1 dp-hdg-brdr-h5-1 dp-hdg-brdr-h6-1 dp-hdg-i-sz-h2-fill dp-hdg-i-sz-h3-fill dp-hdg-i-sz-h5-fill dp-hdg-i-sz-h6-fill dp-hdg-i-brdr-h5-2 dp-hdg-i-brdr-h6-2 dp-hdg-b-h3-brdr-b dp-hdg-txt-h2-dp-primary dp-hdg-i-brdr-h2-1 dp-hdg-i-brdr-h3-1 dp-hdg-i-sz-h4-fill dp-hdg-i-cp-brdr-h3-dp-primary dp-hdg-i-brdr-h4-1 dp-hdg-i-bg-h2-dp-primary dp-hdg-i-bg-h3-dp-primary dp-hdg-b-h4-brdr-b dp-hdg-d-h4-table-l dp-hdg-i-styl-h4-pill dp-hdg-i-cp-brdr-h4-dp-primary">
  <div class="dp-action-item dp-action-item-block dp-action-item-note dp-locked" style="display: none;" aria-hidden="true">
    <p><em>Welcome to your Home Page! This page was designed with the guidance of QM Standards: <strong>SRS1.1, SRS7.1, SRS7.2, SRS7.3, SRS7.4</strong>.</em></p>
  </div>
  <div id="dp-wrapper_1" class="dp-header dp-basic-bar dp-header-s-brdr-l dp-header-brdr-w-4 dp-header-out-dp-secondary dp-header-pre-s-brdr-r dp-header-pre-font-sm dp-header-pre-out-dp-secondary dp-header-sub-brdr-w-0 dp-header-desc-txt-dp-primary dp-header-desc-out-dp-primary dp-header-sub-bg-dp-white dp-header-sub-txt-dp-primary dp-header-sub-out-dp-primary" style="margin-bottom: 1.5rem;">
    <header class="dp-header dp-basic-bar dp-header-s-brdr-l dp-header-brdr-w-4 dp-header-out-dp-secondary dp-header-pre-s-brdr-r dp-header-pre-font-sm dp-header-pre-out-dp-secondary dp-header-sub-brdr-w-0 dp-header-desc-txt-dp-primary dp-header-desc-out-dp-primary dp-header-sub-bg-dp-white dp-header-sub-txt-dp-primary dp-header-sub-out-dp-primary" style="background: #1e3a8a; color: #ffffff; padding: 1.75rem 2rem; border-radius: 6px; border-left: 6px solid #2563eb; box-shadow: 0 4px 6px -1px rgba(0,0,0,0.1);">
      <h1 class="dp-heading" style="margin: 0; color: #ffffff;"><span class="dp-header-pre"><span class="dp-header-pre-1" style="color: #93c5fd; font-size: 0.9em; text-transform: uppercase; letter-spacing: 0.05em; display: block; margin-bottom: 0.25rem;">{html.escape(c_code)}</span></span><span class="dp-header-title" style="color: #ffffff; font-size: 1.9rem; font-weight: 700; line-height: 1.2;">{html.escape(c_title)}</span></h1>
      <p style="margin: 0.5rem 0 0 0; color: #e2e8f0; font-size: 1.05em; opacity: 0.95;">Institutional Course Hub &amp; Weekly Learning Modules</p>
    </header>
  </div>
  <nav class="dp-link-grid container-fluid dp-link-grid-item-s-rounded dp-link-grid-item-bg-dp-primary dp-link-grid-hover-dp-accent dp-link-grid-icon-s-brdr-r dp-link-grid-icon-brdr-dp-secondary dp-link-grid-icon-brdr-w-2" style="margin: 1.5rem 0;">
    <ul class="row" style="list-style: none; padding: 0; display: flex; flex-wrap: wrap; gap: 1rem;">
      <li class="col-sm-12 col-md-4 col-lg-4" style="flex: 1; min-width: 220px;"><a title="Course Overview" href="$WIKI_REFERENCE$/pages/{p_start_here_id}" data-course-type="wikiPages" style="display: block; background: #1e3a8a; color: #ffffff; padding: 0.85rem 1.25rem; border-radius: 6px; text-decoration: none; font-weight: 600; text-align: center; box-shadow: 0 2px 4px rgba(0,0,0,0.1);"><i class="fas fa-flag" aria-hidden="true"></i> Start Here: Course Overview</a></li>
      <li class="col-sm-12 col-md-4 col-lg-4" style="flex: 1; min-width: 220px;"><a title="Syllabus" href="$WIKI_REFERENCE$/pages/{p_orient_syl_id}" data-course-type="wikiPages" style="display: block; background: #1e3a8a; color: #ffffff; padding: 0.85rem 1.25rem; border-radius: 6px; text-decoration: none; font-weight: 600; text-align: center; box-shadow: 0 2px 4px rgba(0,0,0,0.1);"><i class="fas fa-file-alt" aria-hidden="true"></i> Syllabus &amp; Policies</a></li>
      <li class="col-sm-12 col-md-4 col-lg-4" style="flex: 1; min-width: 220px;"><a class="dp-has-icon" href="https://lcccwy.sharepoint.com/sites/StudentSuccessResources" target="_blank" rel="noopener" style="display: block; background: #1e3a8a; color: #ffffff; padding: 0.85rem 1.25rem; border-radius: 6px; text-decoration: none; font-weight: 600; text-align: center; box-shadow: 0 2px 4px rgba(0,0,0,0.1);"><i class="fas fa-external-link-alt" aria-hidden="true"></i> Student Resources</a></li>
    </ul>
  </nav>
  <div class="dp-content-block" style="background: #f8fafc; border-left: 4px solid #1e3a8a; padding: 1.25rem 1.5rem; margin-bottom: 2rem; border-radius: 0 6px 6px 0;">
    <p style="margin: 0; font-size: 1.05em; line-height: 1.6; color: #334155;"><strong>Welcome to {html.escape(c_code)}: {html.escape(c_title)}!</strong> This asynchronous coursework emphasizes production-grade engineering, verifiable technical implementations, and hands-on laboratory mastery. Select any unit below to access readings, lecture deep dives, preparatory exercises, and lab assignments.</p>
  </div>
  <div class="dp-module-list dp-module-list-flag-completed dp-module-list-show-locked dp-quick-links-panels-accordion-plus dp-auto-update dp-panel-color-dp-primary dp-panel-active-color-dp-accent dp-panel-hover-color-dp-accent dp-quick-links-all dp-module-list-current-none" style="margin-top: 2rem;">
    <div style="background: #f1f5f9; padding: 0.85rem 1.25rem; border-radius: 6px 6px 0 0; border: 1px solid #cbd5e1; border-bottom: none; font-weight: 700; color: #1e3a8a; font-size: 1.1em;">
      <i class="fas fa-layer-group" style="color: #2563eb; margin-right: 0.5rem;"></i> Course Modules &amp; Weekly Roadmap
    </div>
    <nav class="dp-module-list-item-group">
      <ul class="fa-ul list-group" style="list-style: none; padding: 0; margin: 0; border: 1px solid #cbd5e1; border-radius: 0 0 6px 6px; overflow: hidden;">
{mod_links_joined}
      </ul>
    </nav>
  </div>
</div>
</body>
</html>"""
    builder.add_wiki_page(p_home_id, "home-page.html", "Home Page", home_html, is_front_page=True)
    print("  [+] Generated Native Canvas Front Page (home-page.html) with DesignPLUS Quick-Links Module Accordion")

    # 6. Generate Orientation Module ("Getting Started - Course Orientation")
    orient_items = []

    # Page: Start Here: Course Overview & Orientation
    start_here_panels = [
        ("How to Navigate this Course",
         """<ul>
  <li><strong>Home Page:</strong> Displays your central course dashboard with the interactive module accordion and quick navigation links.</li>
  <li><strong>Modules:</strong> The primary roadmap where all units, readings, labs, and assessments are organized in chronological order.</li>
  <li><strong>Syllabus:</strong> Access the institutional course policies, contact hour budgets, and download your official Word (.docx) syllabus.</li>
  <li><strong>Grades &amp; SpeedGrader:</strong> View real-time evaluation rubrics, automated check-in results, and detailed instructor feedback.</li>
</ul>"""),
        ("Required Resources (Zero-Cost Educational Model)",
         """<p>This course follows a strict <strong>Zero-Cost / Open-Educational Resource (OER)</strong> philosophy. You are NOT required to purchase proprietary textbooks:</p>
<ul>
  <li><strong>Cloud &amp; Local Runtimes:</strong> Python 3.10+, DuckDB CLI, Polars, Docker, and GitHub Codespaces.</li>
  <li><strong>Authoritative Documentation:</strong> Official engineering specifications and open-access industry guides.</li>
  <li><strong>Embedded Micro-Lectures:</strong> Verified video walk-throughs embedded directly inside each module.</li>
</ul>"""),
        ("Hands-on Technical Labs & Submission Workflow",
         """<p>Each weekly module culminates in a hands-on applied laboratory assignment:</p>
<ol>
  <li><strong>Read the Lab Guide:</strong> Review scenario constraints, architecture diagrams, and rubric expectations.</li>
  <li><strong>Implement &amp; Test Locally:</strong> Write and verify your code in your terminal or cloud sandbox.</li>
  <li><strong>Submit to Canvas:</strong> Upload your completed code files (.py, .sql, .parquet) or project repository links for grading.</li>
</ol>"""),
        ("Communication Expectations & Support",
         """<p>We are dedicated to your technical growth and success. For questions and technical assistance:</p>
<ul>
  <li><strong>Canvas Inbox:</strong> Recommended for personal questions, grade reviews, and direct 1-on-1 communication.</li>
  <li><strong>Unit Discussion Boards:</strong> Recommended for debugging shared syntax hurdles, architecture trade-offs, and conceptual sparring.</li>
  <li><strong>Instructor Office Hours:</strong> Virtual open-door lab sessions are hosted weekly via Microsoft Teams / Zoom.</li>
</ul>""")
    ]
    start_here_html = render_designplus_html(
        "Start Here: Course Overview & Orientation",
        f"<p>Welcome to <strong>{c_code}: {c_title}</strong>. Please review the navigation rules, open-access resources, and technical lab workflow below before beginning Unit 01.</p>",
        start_here_panels,
        p_start_here_id,
        header_subtitle="Institutional Course Overview & Getting Started Guide"
    )
    builder.add_wiki_page(p_start_here_id, "start-here.html", "Start Here: Course Overview & Orientation", start_here_html)
    orient_items.append({"type": "WikiPage", "title": "Start Here: Course Overview & Orientation", "ref": p_start_here_id, "indent": 0, "state": "active"})

    # Page: Orientation - Learn with AI Guidelines
    p_orient_ai_id = make_canvas_id("page_orient_learn_with_ai")
    orient_ai_panels = [
        ("The AI Pair Programmer Philosophy",
         """<p>In this course, Artificial Intelligence is treated as an interactive technical co-pilot, code reviewer, and Socratic sparring partner—<strong>not a shortcut to bypass critical engineering reasoning</strong>.</p>
<p>Blindly copying and pasting unverified AI code into production pipelines causes silent data corruption, security breaches, and catastrophic performance degradation. In this course, you will practice <strong>Active Socratic Learning with AI</strong>: assigning AI models specialized reviewer roles to challenge your architecture and uncover edge cases.</p>"""),
        ("The Big Four 100% Free AI Platforms",
         """<p>Every AI exercise in this course is designed for <strong>100% free web chat tiers</strong>. You do NOT need paid subscriptions or private API keys:</p>
<ul>
  <li><strong>ChatGPT Free:</strong> <a href="https://chatgpt.com" target="_blank" rel="noopener">chatgpt.com</a> (GPT-4o-mini / Free tier).</li>
  <li><strong>Claude Free:</strong> <a href="https://claude.ai" target="_blank" rel="noopener">claude.ai</a> (Anthropic Claude 3.5 Sonnet / Haiku web interface).</li>
  <li><strong>Google Gemini Free:</strong> <a href="https://gemini.google.com" target="_blank" rel="noopener">gemini.google.com</a> (Free with any Google account).</li>
  <li><strong>Microsoft Copilot Free:</strong> <a href="https://copilot.microsoft.com" target="_blank" rel="noopener">copilot.microsoft.com</a> (Free web chat).</li>
</ul>"""),
        ("The Golden Rule: Verification Protocol",
         """<p>Never submit AI-generated code without empirical proof of correctness! The foundational rule of this course:</p>
<div style="background: #eff6ff; border-left: 4px solid #2563eb; padding: 1rem 1.25rem; margin: 1rem 0; border-radius: 0 4px 4px 0;">
  <strong>Empirical Verification Mandate:</strong> Every single query, Python transform, schema migration, or pipeline script must be executed and verified against a live local or cloud container environment prior to Canvas submission.
</div>""")
    ]
    orient_ai_html = render_designplus_html(
        "Orientation: Learn with AI — Course Guidelines & Free Tools",
        "<p>Guidelines on using conversational AI co-pilots effectively and ethically as an engineering student.</p>",
        orient_ai_panels,
        p_orient_ai_id,
        header_subtitle="AI Co-pilot Guidelines & Ethical Use Standards"
    )
    builder.add_wiki_page(p_orient_ai_id, "orientation-learn-with-ai.html", "Orientation: Learn with AI — Course Guidelines & Free Tools", orient_ai_html)
    orient_items.append({"type": "WikiPage", "title": "Orientation: Learn with AI — Course Guidelines & Free Tools", "ref": p_orient_ai_id, "indent": 1, "state": "active"})

    # Page: Course Syllabus & Policies Page
    p_orient_syl_id = make_canvas_id("page_orient_syllabus")
    orient_syl_panels = [
        ("Institutional Master Syllabus (.docx)",
         f"""<p>Review the full institutional syllabus including course outcomes, ADA compliance, and grading scale:</p>
<p><a class="instructure_file_link" title="{docx_filename}" href="$IMS-CC-FILEBASE$/{docx_rel}?canvas_=1&amp;canvas_qs_wrap=1" target="_blank" rel="noopener" style="color: #2563eb; font-weight: 600; text-decoration: underline;">&#128196; Download {docx_filename}</a></p>"""),
        ("Gradebook Weights & Evaluation Criteria",
         """<table style="width: 100%; border-collapse: collapse; border: 1px solid #cbd5e1; font-size: 0.95em;">
  <thead>
    <tr style="background: #1e3a8a; color: #ffffff;">
      <th style="padding: 10px 14px; text-align: left; border: 1px solid #94a3b8;">Evaluation Category</th>
      <th style="padding: 10px 14px; text-align: center; border: 1px solid #94a3b8; width: 140px;">Percentage</th>
    </tr>
  </thead>
  <tbody>
    <tr style="background: #ffffff;"><td style="padding: 8px 14px; border: 1px solid #cbd5e1;">Hands-on Applied Labs</td><td style="padding: 8px 14px; border: 1px solid #cbd5e1; text-align: center; font-weight: 600;">40%</td></tr>
    <tr style="background: #f8fafc;"><td style="padding: 8px 14px; border: 1px solid #cbd5e1;">Unit Knowledge Checks &amp; Quizzes</td><td style="padding: 8px 14px; border: 1px solid #cbd5e1; text-align: center; font-weight: 600;">20%</td></tr>
    <tr style="background: #ffffff;"><td style="padding: 8px 14px; border: 1px solid #cbd5e1;">Asynchronous Preparation &amp; Drills</td><td style="padding: 8px 14px; border: 1px solid #cbd5e1; text-align: center; font-weight: 600;">10%</td></tr>
    <tr style="background: #f8fafc;"><td style="padding: 8px 14px; border: 1px solid #cbd5e1;">Comprehensive Course Capstone</td><td style="padding: 8px 14px; border: 1px solid #cbd5e1; text-align: center; font-weight: 600;">30%</td></tr>
  </tbody>
</table>""")
    ]
    orient_syl_html = render_designplus_html(
        "Course Syllabus & Institutional Policies",
        "<p>Review institutional course expectations, contact hours, and grading policies.</p>",
        orient_syl_panels,
        p_orient_syl_id,
        header_subtitle="Policies, Grading Scale & Master Document Download"
    )
    builder.add_wiki_page(p_orient_syl_id, "course-orientation-and-syllabus.html", "Course Syllabus & Institutional Policies", orient_syl_html)
    orient_items.append({"type": "WikiPage", "title": "Course Syllabus & Institutional Policies", "ref": p_orient_syl_id, "indent": 1, "state": "active"})

    # Register Orientation Module
    builder.add_module(mod_orient_id, "Getting Started - Course Orientation", orient_items)
    print("  [+] Generated Getting Started - Course Orientation Module (3 Native Pages)")

    # 7. Process Weekly Units
    for u_idx, u_folder in enumerate(unit_folders, 1):
        u_dir = os.path.join(units_dir, u_folder)
        u_title = u_folder.replace("_", " ").title()
        u_title_clean = re.sub(r"^Unit\s*\d+\s*", "", u_title, flags=re.IGNORECASE).strip()
        u_display_title = f"Unit {u_idx:02d}: {u_title_clean}" if u_title_clean else f"Unit {u_idx:02d}"

        print(f"  [+] Processing Unit {u_idx:02d}: {u_folder}")
        module_items = []
        mod_id = unit_mod_ids[u_idx]

        # Item 1: Unit Overview (WikiPage) - Uses DesignPLUS Banner + Accordions
        ov_file = find_file(u_dir, ["overview.*\\.md$", "^overview\\.md$"])
        ov_id = make_canvas_id(f"page_u{u_idx}_overview")
        ov_html_file = f"unit-{u_idx:02d}-overview.html"

        if ov_file:
            with open(ov_file, "r", encoding="utf-8") as of:
                ov_raw_md = of.read()
            ov_extracted_title, ov_lead_html, ov_sections = parse_markdown_sections(ov_raw_md)
            ov_panels = ov_sections if ov_sections else [
                ("Measurable Learning Objectives", parse_markdown_to_html(ov_raw_md)),
                ("Weekly Roadmap & Contact Hours", "<p>Review weekly instructional readings, complete self-check drills, and submit your technical lab.</p>")
            ]
            ov_page_content = render_designplus_html(
                ov_extracted_title or f"Unit {u_idx:02d} Overview: {u_title_clean}",
                ov_lead_html,
                ov_panels,
                ov_id,
                header_subtitle="Weekly Roadmap, Learning Objectives & Schedule"
            )
        else:
            default_panels = [
                ("Measurable Learning Objectives", f"<p>Complete weekly technical competencies in {u_title_clean}.</p>"),
                ("Weekly Roadmap & Contact Hours", "<p>Review readings (150 min), complete drills (60 min), and execute engineering lab (90 min).</p>")
            ]
            ov_page_content = render_designplus_html(
                f"Unit {u_idx:02d} Overview: {u_title_clean}",
                f"<p>Welcome to {u_display_title}. Review the weekly readings and complete all applied labs.</p>",
                default_panels,
                ov_id,
                header_subtitle="Weekly Roadmap, Learning Objectives & Schedule"
            )

        builder.add_wiki_page(ov_id, ov_html_file, f"Unit {u_idx:02d} Overview: {u_title_clean}", ov_page_content)
        module_items.append({"type": "WikiPage", "title": f"Unit {u_idx:02d} Overview: {u_title_clean}", "ref": ov_id, "indent": 0, "state": "active"})

        # Item 2: Required Readings & Lectures (WikiPage)
        readings_file = find_file(u_dir, ["reading", "lecture.*notes", "slides"])
        if readings_file:
            r_id = make_canvas_id(f"page_u{u_idx}_readings")
            r_html_file = f"unit-{u_idx:02d}-readings.html"
            with open(readings_file, "r", encoding="utf-8") as rf:
                r_raw_md = rf.read()
            r_title_extracted, r_lead_html, r_sections = parse_markdown_sections(r_raw_md)

            if len(r_sections) >= 2:
                r_page_content = render_designplus_html(
                    f"Unit {u_idx:02d}: Required Readings, Concepts & Video Lectures",
                    r_lead_html or "<p>Review all instructional lecture materials and conceptual deep dives below.</p>",
                    r_sections,
                    r_id,
                    header_subtitle="Required Readings, Concepts & Video Lectures"
                )
            else:
                r_panels = [("Core Reading & Conceptual Deep Dive", parse_markdown_to_html(r_raw_md))]
                r_page_content = render_standard_page_html(
                    f"Unit {u_idx:02d}: Required Readings & Lectures",
                    "<p>Review all instructional materials and concepts.</p>",
                    r_panels,
                    r_id
                )
            builder.add_wiki_page(r_id, r_html_file, f"Unit {u_idx:02d}: Required Readings, Concepts & Video Lectures", r_page_content)
            module_items.append({"type": "WikiPage", "title": f"Unit {u_idx:02d}: Required Readings, Concepts & Video Lectures", "ref": r_id, "indent": 1, "state": "active"})

        # Item 3: Asynchronous Preparation & Drills (WikiPage)
        drills_file = find_file(u_dir, ["study_guide", "drill", "self_check", "prep"])
        if drills_file:
            d_id = make_canvas_id(f"page_u{u_idx}_drills")
            d_html_file = f"unit-{u_idx:02d}-drills.html"
            with open(drills_file, "r", encoding="utf-8") as df:
                d_body = parse_markdown_to_html(df.read())
            d_panels = [("Formative Self-Check Drills & Exercises", d_body)]
            d_page_content = render_standard_page_html(
                f"Unit {u_idx:02d}: Asynchronous Preparation & Drills",
                "<p>Formative self-check exercises and diagnostic execution order drills with expandable answer keys.</p>",
                d_panels,
                d_id
            )
            builder.add_wiki_page(d_id, d_html_file, f"Unit {u_idx:02d}: Asynchronous Preparation & Drills", d_page_content)
            module_items.append({"type": "WikiPage", "title": f"Unit {u_idx:02d}: Asynchronous Preparation & Drills", "ref": d_id, "indent": 1, "state": "active"})

        # Item 4: Applied Lab Guide (WikiPage)
        lab_file = find_file(u_dir, ["lab_guide", "student_lab", "project_guide"])
        if lab_file:
            lg_id = make_canvas_id(f"page_u{u_idx}_lab_guide")
            lg_html_file = f"unit-{u_idx:02d}-applied-lab-guide.html"
            with open(lab_file, "r", encoding="utf-8") as lf:
                lg_body = parse_markdown_to_html(lf.read())

            rubric_file = find_file(u_dir, ["rubric"])
            rubric_html = ""
            if rubric_file:
                with open(rubric_file, "r", encoding="utf-8") as rf:
                    rubric_html = parse_markdown_to_html(rf.read())

            lg_panels = [("Laboratory Scenario & Task Specifications", lg_body)]
            if rubric_html:
                lg_panels.append(("Grading Rubric & Scoring Criteria", rubric_html))

            lg_page_content = render_standard_page_html(
                f"Unit {u_idx:02d}: Applied Lab Guide",
                "<p>Hands-on technical scenario, tasks, starter code specifications, and rubric criteria.</p>",
                lg_panels,
                lg_id
            )
            builder.add_wiki_page(lg_id, lg_html_file, f"Unit {u_idx:02d}: Applied Lab Guide", lg_page_content)
            module_items.append({"type": "WikiPage", "title": f"Unit {u_idx:02d}: Applied Lab Guide", "ref": lg_id, "indent": 1, "state": "active"})

        # Item 5: Native Canvas Assignment (Assignment)
        assign_id = make_canvas_id(f"assignment_u{u_idx}")
        assign_title = f"Unit {u_idx:02d} Applied Lab Assignment"
        assign_desc = f"""<html>
<head><meta http-equiv="Content-Type" content="text/html; charset=utf-8"/><title>{html.escape(assign_title)}</title></head>
<body style="font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif; line-height: 1.6; color: #1e293b; padding: 1rem; max-width: 900px;">
  <h2 style="color: #1e3a8a; border-bottom: 2px solid #1e3a8a; padding-bottom: 0.3rem;">{html.escape(assign_title)} (50 Points)</h2>
  <div style="background: #f8fafc; border-left: 4px solid #1e3a8a; padding: 0.75rem 1.25rem; margin: 1rem 0; border-radius: 0 4px 4px 0;">
    <p style="margin: 0;">Complete the engineering exercises outlined in the <strong>Unit {u_idx:02d}: Applied Lab Guide</strong> and upload your completed solution files below for evaluation.</p>
  </div>
  <h3 style="color: #0f172a; margin-top: 1.5rem;">Submission Instructions</h3>
  <ol style="padding-left: 1.5rem; line-height: 1.8;">
    <li>Write and test your code locally in your development sandbox or container environment.</li>
    <li>Verify that your solution meets all technical requirements and passes all automated test cases.</li>
    <li>Upload your final solution file(s) (.py, .sql, .parquet, .txt, or .pdf) to this assignment.</li>
  </ol>
</body>
</html>"""
        builder.build_assignment(assign_id, assign_title, labs_gid, assign_desc, points=50.0, allowed_ext="py,sql,parquet,csv,txt,pdf")
        module_items.append({"type": "Assignment", "title": assign_title, "ref": assign_id, "indent": 1, "state": "active"})

        # Item 6: Knowledge Check (Quiz) via QTI 1.2
        quiz_file = find_file(u_dir, ["quiz.*\\.md$", "^quiz\\.md$"])
        if quiz_file:
            q_id = make_canvas_id(f"quiz_u{u_idx}")
            q_title = f"Unit {u_idx:02d} Knowledge Check: {u_title_clean}"
            try:
                questions = parse_quiz_md(quiz_file)
                if questions:
                    builder.build_quiz(q_id, q_title, quizzes_gid, questions)
                    module_items.append({"type": "Quizzes::Quiz", "title": q_title, "ref": q_id, "indent": 1, "state": "active"})
                    print(f"     [>] Compiled QTI Quiz: {len(questions)} questions")
            except Exception as e:
                print(f"     [!] Warning: Quiz compilation skipped for {quiz_file}: {e}")

        # Item 7: Instructor Notes & Solutions (Unpublished WikiPage)
        sol_file = find_file(u_dir, ["instructor.*solution", "teaching.*notes", "solution.*\\.sql$", "solution.*\\.py$"])
        if sol_file:
            t_id = make_canvas_id(f"page_u{u_idx}_instructor_guide")
            t_html_file = f"unit-{u_idx:02d}-instructor-guide.html"
            with open(sol_file, "r", encoding="utf-8") as sf:
                sol_code = sf.read()
            if sol_file.endswith((".md", ".markdown")):
                t_body = parse_markdown_to_html(sol_code)
                t_panels = [("Instructor Flipped Classroom Guide & Video Walkthrough Scripts", t_body)]
            else:
                sol_box = f"<div style='background: #0f172a; color: #f8fafc; padding: 1rem 1.25rem; border-radius: 6px; overflow-x: auto; font-family: Consolas, Monaco, monospace; font-size: 0.9em; line-height: 1.5;'><pre style='margin: 0; background: transparent; color: inherit;'><code>{html.escape(sol_code.strip())}</code></pre></div>"
                t_panels = [("Instructor Master Solution Key & Answer Code", sol_box)]
            t_page_content = render_standard_page_html(
                f"[Instructor Guide] Unit {u_idx:02d} Teaching Notes & Solutions",
                "<p><strong>[FOR INSTRUCTORS ONLY — UNPUBLISHED]</strong> Flipped classroom walkthrough scripts, pedagogical timing, and master answer keys.</p>",
                t_panels,
                t_id,
                workflow_state="unpublished"
            )
            builder.add_wiki_page(t_id, t_html_file, f"[Instructor Guide] Unit {u_idx:02d} Teaching Notes & Solutions", t_page_content, workflow_state="unpublished")
            module_items.append({"type": "WikiPage", "title": f"[Instructor Guide] Unit {u_idx:02d} Teaching Notes & Solutions", "ref": t_id, "indent": 1, "state": "unpublished"})

        # Register Unit Module
        builder.add_module(mod_id, u_display_title, module_items)

    # 8. Generate Manifest and Synchronized Module Meta
    print("\n--- Generating Synchronized Canvas Manifest & Module Meta ---")
    builder.build_module_meta_and_manifest()

    # 9. Validate XML Files
    print("--- Running XML Validation Suite ---")
    xml_count = builder.validate_xml_files()
    print(f"SUCCESS: Verified {xml_count} XML files. Zero syntax errors!")

    # 10. Package into .imscc
    print(f"\n--- Compressing into Common Cartridge Package: {output_imscc} ---")
    total_files = builder.package_imscc()
    size_mb = os.path.getsize(output_imscc) / (1024 * 1024)
    print(f"SUCCESS: Created {output_imscc} ({total_files} files, {size_mb:.2f} MB)")
    print("\n[SUCCESS] Canvas Native Course Export Package build complete!\n")


def main():
    parser = argparse.ArgumentParser(description="Compile Canvas Common Cartridge (.imscc) with DesignPLUS formatting and QTI quizzes.")
    parser.add_argument("--config", default="course_config.json", help="Path to course configuration JSON file.")
    parser.add_argument("--units-dir", default="units", help="Directory containing unit subdirectories.")
    parser.add_argument("--output", default="", help="Path for output .imscc file (defaults to [code]_Complete.imscc).")
    parser.add_argument("--build-dir", default=None, help="Temporary staging build directory.")

    args = parser.parse_args()

    output_imscc = args.output
    if not output_imscc:
        try:
            cfg = load_config(args.config)
            c_code = cfg.get("course_code", "Course").replace(" ", "_")
            output_imscc = f"{c_code}_Complete.imscc"
        except Exception:
            output_imscc = "Canvas_Course_Package.imscc"

    compile_course(args.config, args.units_dir, output_imscc, build_dir=args.build_dir)


if __name__ == "__main__":
    main()
