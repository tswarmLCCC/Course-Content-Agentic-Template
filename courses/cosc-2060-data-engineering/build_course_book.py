#!/usr/bin/env python3
"""
Compiles the complete COSC 2060 Course Textbook & Lab Manual into a print-ready
HTML book and renders it to PDF via headless Google Chrome.
"""

import html
import os
import pathlib
import re
import subprocess
import sys

ROOT = pathlib.Path(__file__).resolve().parent
SKILL_SCRIPTS = ROOT.parent.parent / ".agents" / "skills" / "canvas-course-builder" / "scripts"
sys.path.insert(0, str(SKILL_SCRIPTS))
import html_styler  # noqa: E402

CHROME_PATHS = [
    r"C:\Program Files\Google\Chrome\Application\chrome.exe",
    r"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe",
    r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe",
]


def find_browser() -> str:
    for p in CHROME_PATHS:
        if os.path.exists(p):
            return p
    raise FileNotFoundError("Could not find Chrome or Edge for headless PDF generation.")


def transform_for_print(html_fragment: str) -> str:
    """Adapts Canvas web HTML (iframes, <details>, Canvas placeholders) for print PDF."""
    # 1. Replace YouTube iframe embeds with clean print-friendly Video Reference boxes
    iframe_pattern = re.compile(
        r'<div class="dp-embed-wrapper"[^>]*>\s*<iframe[^>]*title="([^"]*)"[^>]*src="https://www\.youtube\.com/embed/([^"?]+)[^"]*"[^>]*></iframe>\s*</div>\s*(?:<p[^>]*><a[^>]*>.*?</a></p>)?',
        re.DOTALL | re.IGNORECASE,
    )

    def _video_card(match: re.Match) -> str:
        title = match.group(1) or "Video Lecture"
        vid_id = match.group(2)
        watch_url = f"https://www.youtube.com/watch?v={vid_id}"
        return (
            '<div class="print-video-card">'
            f'<div class="print-video-title">&#9654; Video Lecture: {html.escape(title)}</div>'
            f'<div class="print-video-url">Watch online: <a href="{watch_url}">{watch_url}</a></div>'
            "</div>"
        )

    out = iframe_pattern.sub(_video_card, html_fragment)

    # 2. Convert <details>/<summary> into always-open print-friendly answer boxes
    out = re.sub(
        r"<details[^>]*>\s*<summary[^>]*>(.*?)</summary>",
        r'<div class="print-drill-box"><div class="print-drill-title">\1</div>',
        out,
        flags=re.DOTALL | re.IGNORECASE,
    )
    out = re.sub(r"</details>", "</div>", out, flags=re.IGNORECASE)

    # 3. Clean up Canvas-specific filebase links for print readability
    out = out.replace("$IMS-CC-FILEBASE$/", "")
    out = re.sub(r'href="\$CANVAS_OBJECT_REFERENCE\$/[^"]*"', 'href="#toc"', out)

    # 4. Remove empty institutional video dashed placeholders or make them compact
    out = re.sub(
        r'<div style="background: #f8fafc; border-radius: 6px; padding: 1\.5rem;[^"]*">.*?Campus Faculty Announcements.*?</div>',
        '<div class="print-note-box"><strong>Campus Faculty Recordings:</strong> Check your Canvas course site for campus-specific lecture recordings and office-hour walkthroughs.</div>',
        out,
        flags=re.DOTALL | re.IGNORECASE,
    )
    return out


def md_to_print_html(md_text: str) -> str:
    """Converts markdown to clean semantic HTML for textbook printing."""
    # Strip top-level H1 if we supply our own chapter/section header
    lines = md_text.splitlines()
    if lines and lines[0].startswith("# "):
        lines = lines[1:]
    body_md = "\n".join(lines).strip()
    raw_html = html_styler.parse_markdown_to_html(body_md)
    return transform_for_print(raw_html)


def extract_body_from_html_file(path: pathlib.Path) -> str:
    text = path.read_text(encoding="utf-8")
    m = re.search(r"<body[^>]*>(.*)</body>", text, flags=re.DOTALL | re.IGNORECASE)
    inner = m.group(1) if m else text
    return transform_for_print(inner)


def build_book():
    units_dir = ROOT / "units"
    unit_folders = sorted(units_dir.glob("unit_*"))

    toc_entries = [
        ("syllabus", "Course Syllabus & 16-Week Schedule"),
        ("getting-started", "Orientation A — Getting Started with the Lab Environment"),
        ("shapes-of-ai-data", "Orientation B — The Shapes of AI Data (Companion Guide)"),
    ]

    unit_sections = []
    for idx, udir in enumerate(unit_folders, 1):
        overview_md = (udir / "overview.md").read_text(encoding="utf-8")
        # Extract unit title from first line of overview.md
        first_line = overview_md.splitlines()[0] if overview_md.splitlines() else f"Unit {idx}"
        unit_title = re.sub(r"^#\s*", "", first_line).strip()
        anchor = f"unit-{idx:02d}"
        toc_entries.append((anchor, unit_title))

        reading_md = (udir / "reading.md").read_text(encoding="utf-8")
        drills_md = (udir / "drills.md").read_text(encoding="utf-8")
        lab_md = (udir / "lab_guide.md").read_text(encoding="utf-8")

        unit_html = f"""
        <section class="unit-chapter" id="{anchor}">
          <div class="chapter-banner">
            <div class="chapter-kicker">UNIT {idx:02d}</div>
            <h1 class="chapter-title">{html.escape(unit_title)}</h1>
          </div>

          <div class="subchapter">
            <h2 class="subchapter-banner">Part 1 &mdash; Unit Overview &amp; Roadmap</h2>
            {md_to_print_html(overview_md)}
          </div>

          <div class="subchapter">
            <h2 class="subchapter-banner">Part 2 &mdash; Core Readings, Concepts &amp; Code Walkthroughs</h2>
            {md_to_print_html(reading_md)}
          </div>

          <div class="subchapter">
            <h2 class="subchapter-banner">Part 3 &mdash; Asynchronous Preparation &amp; Self-Check Drills</h2>
            {md_to_print_html(drills_md)}
          </div>

          <div class="subchapter">
            <h2 class="subchapter-banner">Part 4 &mdash; Applied Laboratory Guide &amp; Rubric</h2>
            {md_to_print_html(lab_md)}
          </div>
        </section>
        """
        unit_sections.append(unit_html)

    syllabus_md = (ROOT / "syllabus.md").read_text(encoding="utf-8")
    getting_started_md = (ROOT / "content" / "getting_started_lab.md").read_text(encoding="utf-8")
    shapes_html = extract_body_from_html_file(ROOT / "content" / "ai_data_shapes_guide.html")

    toc_list_html = "\n".join(
        f'<li><a href="#{anchor}">{html.escape(label)}</a></li>'
        for anchor, label in toc_entries
    )

    banner_path = ROOT / "build" / "web_resources" / "images" / "course_banner.jpg"
    banner_img_html = ""
    if banner_path.exists():
        banner_uri = banner_path.as_uri()
        banner_img_html = f'<img class="cover-banner" src="{banner_uri}" alt="COSC 2060 Course Banner"/>'

    full_html = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8"/>
<title>COSC 2060 — Modern Data Engineering &amp; AI Infrastructure (Course Book)</title>
<style>
  @page {{
    size: letter;
    margin: 0.8in 0.75in 0.8in 0.75in;
    @top-left {{
      content: "COSC 2060: Modern Data Engineering & AI Infrastructure";
      font-family: "Segoe UI", Roboto, Helvetica, Arial, sans-serif;
      font-size: 8.5pt;
      color: #64748b;
    }}
    @bottom-center {{
      content: "Page " counter(page) " of " counter(pages);
      font-family: "Segoe UI", Roboto, Helvetica, Arial, sans-serif;
      font-size: 8.5pt;
      color: #64748b;
    }}
  }}
  @page :first {{
    margin: 0.75in;
    @top-left {{ content: none; }}
    @bottom-center {{ content: none; }}
  }}

  * {{ box-sizing: border-box; }}
  body {{
    font-family: "Segoe UI", -apple-system, BlinkMacSystemFont, Roboto, Helvetica, Arial, sans-serif;
    font-size: 10pt;
    line-height: 1.55;
    color: #1e293b;
    margin: 0;
    padding: 0;
  }}

  /* Cover Page */
  .cover-page {{
    page-break-after: always;
    display: flex;
    flex-direction: column;
    justify-content: space-between;
    min-height: 9.2in;
    border: 1px solid #cbd5e1;
    border-radius: 8px;
    padding: 2.2rem;
    background: linear-gradient(180deg, #f8fafc 0%, #ffffff 45%);
  }}
  .cover-kicker {{
    display: inline-block;
    background: #1e3a8a;
    color: #ffffff;
    font-weight: 700;
    font-size: 9pt;
    letter-spacing: 0.08em;
    padding: 0.35rem 0.75rem;
    border-radius: 4px;
    text-transform: uppercase;
  }}
  .cover-title {{
    font-size: 26pt;
    font-weight: 800;
    color: #0f172a;
    line-height: 1.15;
    margin: 1rem 0 0.5rem 0;
  }}
  .cover-subtitle {{
    font-size: 13pt;
    color: #334155;
    margin: 0 0 1.5rem 0;
  }}
  .cover-banner {{
    width: 100%;
    height: auto;
    border-radius: 6px;
    border: 1px solid #cbd5e1;
    margin: 1rem 0;
  }}
  .cover-meta {{
    border-top: 2px solid #1e3a8a;
    padding-top: 1rem;
    font-size: 9.5pt;
    color: #475569;
  }}

  /* Table of Contents */
  .toc-page {{
    page-break-after: always;
  }}
  .toc-title {{
    font-size: 18pt;
    color: #1e3a8a;
    border-bottom: 2px solid #1e3a8a;
    padding-bottom: 0.4rem;
    margin-bottom: 1rem;
  }}
  .toc-list {{
    list-style: none;
    padding: 0;
    margin: 0;
  }}
  .toc-list li {{
    padding: 0.45rem 0;
    border-bottom: 1px dashed #cbd5e1;
    font-size: 10.5pt;
  }}
  .toc-list a {{
    color: #0f172a;
    text-decoration: none;
    font-weight: 600;
  }}

  /* Chapter & Subchapter Headers */
  .unit-chapter {{
    page-break-before: always;
  }}
  .chapter-banner {{
    background: #1e3a8a;
    color: #ffffff;
    padding: 1.1rem 1.35rem;
    border-radius: 6px;
    margin-bottom: 1.25rem;
    border-left: 6px solid #f59e0b;
  }}
  .chapter-kicker {{
    font-size: 8.5pt;
    font-weight: 700;
    letter-spacing: 0.1em;
    color: #fde68a;
    text-transform: uppercase;
  }}
  .chapter-title {{
    font-size: 16pt;
    margin: 0.2rem 0 0 0;
    color: #ffffff;
    line-height: 1.25;
  }}
  .subchapter {{
    margin-bottom: 1.5rem;
  }}
  .subchapter-banner {{
    background: #f1f5f9;
    color: #1e3a8a;
    border-left: 4px solid #1e3a8a;
    padding: 0.5rem 0.85rem;
    font-size: 12.5pt;
    margin: 1.5rem 0 0.85rem 0;
    page-break-after: avoid;
  }}

  /* Headings & Prose */
  h1, h2, h3, h4 {{
    color: #0f172a;
    page-break-after: avoid;
    margin-top: 1.15rem;
    margin-bottom: 0.45rem;
  }}
  h2 {{
    font-size: 12pt;
    color: #1e3a8a;
    border-bottom: 1px solid #e2e8f0;
    padding-bottom: 0.25rem;
  }}
  h3 {{ font-size: 10.8pt; color: #1e293b; }}
  h4 {{ font-size: 10pt; color: #334155; }}
  p {{ margin: 0.45rem 0; }}
  ul, ol {{ margin: 0.4rem 0 0.6rem 0; padding-left: 1.4rem; }}
  li {{ margin-bottom: 0.25rem; }}
  hr {{ border: none; border-top: 1px solid #e2e8f0; margin: 1rem 0; }}

  /* Code Blocks & Inline Code */
  pre {{
    background: #0f172a !important;
    color: #f8fafc !important;
    padding: 0.75rem 0.9rem !important;
    border-radius: 5px;
    font-family: Consolas, "Cascadia Code", Monaco, monospace;
    font-size: 8.3pt;
    line-height: 1.4;
    white-space: pre-wrap;
    word-break: break-word;
    page-break-inside: avoid;
    margin: 0.65rem 0;
  }}
  pre code {{
    background: transparent !important;
    color: inherit !important;
    padding: 0 !important;
    font-weight: 400 !important;
  }}
  code {{
    font-family: Consolas, "Cascadia Code", Monaco, monospace;
    font-size: 8.8pt;
    background: #f1f5f9;
    color: #0369a1;
    padding: 0.1rem 0.3rem;
    border-radius: 3px;
  }}

  /* Tables */
  table {{
    width: 100%;
    border-collapse: collapse;
    margin: 0.75rem 0;
    font-size: 8.8pt;
    page-break-inside: avoid;
  }}
  th {{
    background: #1e3a8a !important;
    color: #ffffff !important;
    padding: 0.45rem 0.6rem;
    text-align: left;
    border: 1px solid #cbd5e1;
  }}
  td {{
    padding: 0.4rem 0.6rem;
    border: 1px solid #cbd5e1;
    vertical-align: top;
  }}
  tr:nth-child(even) td {{
    background: #f8fafc;
  }}

  /* Blockquotes & Print Cards */
  blockquote {{
    background: #f8fafc;
    border-left: 4px solid #2563eb;
    margin: 0.65rem 0;
    padding: 0.55rem 0.85rem;
    color: #334155;
    page-break-inside: avoid;
  }}
  .print-video-card {{
    background: #eff6ff;
    border: 1px solid #bfdbfe;
    border-left: 4px solid #2563eb;
    border-radius: 4px;
    padding: 0.55rem 0.85rem;
    margin: 0.6rem 0;
    page-break-inside: avoid;
  }}
  .print-video-title {{ font-weight: 700; color: #1e3a8a; font-size: 9.5pt; }}
  .print-video-url {{ font-size: 8.5pt; color: #334155; margin-top: 0.15rem; }}
  .print-drill-box {{
    background: #f8fafc;
    border: 1px solid #cbd5e1;
    border-left: 4px solid #059669;
    border-radius: 4px;
    padding: 0.6rem 0.85rem;
    margin: 0.65rem 0;
    page-break-inside: avoid;
  }}
  .print-drill-title {{
    font-weight: 700;
    color: #065f46;
    margin-bottom: 0.35rem;
    border-bottom: 1px dashed #cbd5e1;
    padding-bottom: 0.25rem;
  }}
  .print-note-box {{
    background: #f8fafc;
    border: 1px dashed #94a3b8;
    border-radius: 4px;
    padding: 0.55rem 0.85rem;
    font-size: 9pt;
    color: #475569;
    margin: 0.65rem 0;
  }}
  /* Ensure embedded orientation styles look crisp */
  .dp-panel-group {{ margin-bottom: 0.75rem; }}
  .dp-panel-heading {{
    background: #f1f5f9;
    color: #1e3a8a;
    padding: 0.35rem 0.65rem;
    border-left: 4px solid #1e3a8a;
    font-size: 11pt;
  }}
</style>
</head>
<body>

  <!-- COVER PAGE -->
  <div class="cover-page">
    <div>
      <span class="cover-kicker">Laramie County Community College &bull; COSC 2060</span>
      <h1 class="cover-title">Modern Data Engineering &amp; AI Infrastructure</h1>
      <p class="cover-subtitle">Complete Course Textbook, Bottom-Up Code Walkthroughs, Self-Check Drills &amp; Applied Laboratory Manual</p>
      {banner_img_html}
    </div>
    <div class="cover-meta">
      <p><strong>Course Structure:</strong> Course Orientation + 8 Applied Units (16-Week Semester)</p>
      <p><strong>Technology Stack:</strong> Python 3.11 &bull; DuckDB &bull; Apache Parquet &bull; Polars &bull; OpenCV &bull; SentenceTransformers &bull; ChromaDB &bull; FastAPI &bull; Pydantic v2 &bull; MCP &bull; Docker</p>
      <p><strong>Student Sandbox Repository:</strong> <a href="https://github.com/tswarmLCCC/COSC-2060-Student-Sandbox">https://github.com/tswarmLCCC/COSC-2060-Student-Sandbox</a></p>
    </div>
  </div>

  <!-- TABLE OF CONTENTS -->
  <div class="toc-page" id="toc">
    <h1 class="toc-title">Table of Contents</h1>
    <ul class="toc-list">
      {toc_list_html}
    </ul>
  </div>

  <!-- FRONT MATTER: SYLLABUS -->
  <section class="unit-chapter" id="syllabus">
    <div class="chapter-banner">
      <div class="chapter-kicker">COURSE SYLLABUS</div>
      <h1 class="chapter-title">COSC 2060 Master Syllabus &amp; 16-Week Schedule</h1>
    </div>
    {md_to_print_html(syllabus_md)}
  </section>

  <!-- FRONT MATTER: GETTING STARTED -->
  <section class="unit-chapter" id="getting-started">
    <div class="chapter-banner">
      <div class="chapter-kicker">ORIENTATION A</div>
      <h1 class="chapter-title">Getting Started with the Lab Environment</h1>
    </div>
    {md_to_print_html(getting_started_md)}
  </section>

  <!-- FRONT MATTER: THE SHAPES OF AI DATA -->
  <section class="unit-chapter" id="shapes-of-ai-data">
    <div class="chapter-banner">
      <div class="chapter-kicker">ORIENTATION B</div>
      <h1 class="chapter-title">The Shapes of AI Data — A Companion Guide</h1>
    </div>
    {shapes_html}
  </section>

  <!-- UNITS 1-8 -->
  {"".join(unit_sections)}

</body>
</html>
"""

    build_dir = ROOT / "build"
    build_dir.mkdir(parents=True, exist_ok=True)
    html_out = build_dir / "COSC_2060_Course_Book.html"
    pdf_out = ROOT / "COSC_2060_Course_Book.pdf"

    html_out.write_text(full_html, encoding="utf-8")
    print(f"[+] Wrote print-ready HTML book: {html_out} ({html_out.stat().st_size / 1024:.1f} KB)")

    browser = find_browser()
    cmd = [
        browser,
        "--headless",
        "--disable-gpu",
        "--no-sandbox",
        "--no-pdf-header-footer",
        f"--print-to-pdf={pdf_out}",
        html_out.as_uri(),
    ]
    res = subprocess.run(cmd, capture_output=True, text=True, check=False)
    if res.returncode != 0 or not pdf_out.exists():
        print("STDOUT:", res.stdout)
        print("STDERR:", res.stderr)
        raise RuntimeError(f"PDF generation failed (exit {res.returncode})")
    print(f"[SUCCESS] Generated PDF Course Book: {pdf_out} ({pdf_out.stat().st_size / (1024 * 1024):.2f} MB)")


if __name__ == "__main__":
    build_book()
