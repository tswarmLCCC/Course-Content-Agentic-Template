#!/usr/bin/env python3
"""
Institutional Word (.docx) Syllabus Generator & Cloner
Clones the official LCCC Master Syllabus Word template (`LCCC_Master_Syllabus_Template.docx`)
preserving 100% of Word styles, customXml schemas, table borders, and college policies,
and injects course-specific metadata, description, outcomes, and grading components.
"""

import os
import zipfile
import html
from typing import List, Optional


def _find_template_docx() -> Optional[str]:
    """Locates LCCC_Master_Syllabus_Template.docx in the repository."""
    script_dir = os.path.dirname(os.path.abspath(__file__))
    candidates = [
        os.path.abspath(os.path.join(script_dir, "..", "..", "syllabus-docx-cloner", "templates", "LCCC_Master_Syllabus_Template.docx")),
        os.path.abspath(os.path.join(script_dir, "..", "templates", "LCCC_Master_Syllabus_Template.docx")),
        os.path.abspath(os.path.join(script_dir, "..", "..", "..", "..", "specs", "_templates", "syllabi", "LCCC_Master_Syllabus_Template.docx")),
    ]
    for path in candidates:
        if os.path.exists(path):
            return path
    return None


def create_syllabus_docx(
    output_path: str,
    course_code: str,
    course_title: str,
    term_str: str,
    institution: str,
    credits_str: str,
    description: str,
    outcomes: List[str],
    grading_breakdown: List[str],
    grading_scale: str = "A: 90 - 100% | B: 80 - 89% | C: 70 - 79% | D: 60 - 69% | F: 0 - 59%"
):
    """Generates an accreditation-compliant .docx syllabus by cloning the LCCC master template."""
    os.makedirs(os.path.dirname(os.path.abspath(output_path)), exist_ok=True)
    tpl_path = _find_template_docx()

    if tpl_path and os.path.exists(tpl_path):
        with zipfile.ZipFile(tpl_path, "r") as zin:
            doc_xml = zin.read("word/document.xml").decode("utf-8")

            # 1. Replace Course Number & Title
            doc_xml = doc_xml.replace(
                " Introduction to Modern SQL",
                f" {html.escape(course_code)}: {html.escape(course_title)}"
            )

            # 2. Replace Course Description
            clean_desc = description.strip().rstrip(".")
            doc_xml = doc_xml.replace(
                "This course provides comprehensive instruction in relational database querying, schema design, transactional integrity, and query performance optimization using modern PostgreSQL 16.",
                html.escape(clean_desc)
            )

            # 3. Replace Zybook reference with GitHub Codespaces labs
            doc_xml = doc_xml.replace(
                "Zybook guided learning, programming and application assignments, and a project based final",
                "asynchronous preparation drills, hands-on GitHub Codespaces engineering labs, unit knowledge checks, and an end-to-end capstone defense"
            )

            # 4. Replace Course Content Outline items
            outline_replacements = [
                ("Demystifying AI:", "Relational & Columnar Foundations:"),
                ("\xa0Defining AI, its history, and its impact on society.", " Building leak-free supervised learning feature matrices with DuckDB, Parquet, and point-in-time ASOF joins."),
                ("The Fundamentals:", "High-Throughput DataFrames & Anomaly Detection:"),
                ("\xa0Exploring core concepts like intelligent agents, problem-solving techniques, and search algorithms.", " Processing multi-million-row telemetry streams using Polars lazy evaluation, Apache Arrow, and Z-score scaling."),
                ("Learning Like a Machine:", "Multimodal Vision & Unstructured Text (RAG):"),
                ("\xa0Understanding machine learning, its different paradigms (supervised, unsupervised, etc.), and its applications.", " Normalizing image tensors with OpenCV and building semantic vector search indices with ChromaDB."),
                ("Thinking Like a Human:", "Data as a Service (REST APIs & Pydantic):"),
                ("\xa0Diving into knowledge representation, reasoning methods, and natural language processing.", " Serving validated, low-latency analytical data products over HTTP using FastAPI and Pydantic v2 data contracts."),
                ("Seeing and Acting:", "Agentic Interfaces (Model Context Protocol):"),
                ("\xa0Introducing computer vision, robotics, and the challenges of perception and action in AI.", " Exposing read-only enterprise data tools to AI agents via the Model Context Protocol (MCP)."),
                ("The Future of AI:", "Pipeline Orchestration & Containerized Deployment:"),
                ("\xa0Discussing ethical considerations, potential benefits and risks of advanced AI, and its future directions.", " Automating asset DAGs with Dagster, GitHub Actions CI/CD, and hardened multi-stage Docker containers."),
            ]
            for old_s, new_s in outline_replacements:
                doc_xml = doc_xml.replace(old_s, html.escape(new_s))

            # 5. Replace Course Notes
            doc_xml = doc_xml.replace(
                "Can include lecture slides, readings, summaries of key concepts, and links to relevant resources.",
                "All required readings, interactive Jupyter notebooks, starter scripts, and datasets are pre-configured in your free GitHub Codespaces Student Sandbox."
            )
            doc_xml = doc_xml.replace(
                "Consider incorporating interactive elements, case studies, and real-world examples of AI applications.",
                "Every unit includes guided active-learning coding clinics, Socratic AI review drills, and hands-on engineering labs."
            )

            # 6. Replace Course Competencies (up to 5 slots in template)
            old_competencies = [
                "Compare and contrast different machine learning approaches, identifying strengths and weaknesses for specific tasks.",
                "Develop a basic framework for applying machine learning or search algorithms to solve a simple problem.",
                "Explain the social, ethical, and economic implications of AI in a clear and concise manner.",
                "Explain AI concepts and their applications to a non-technical audience, using clear and concise language.",
                "<w:t>Design a basic AI </w:t></w:r><w:r w:rsidR=\"00A06AA6\"><w:rPr><w:rFonts w:ascii=\"Calibri\" w:hAnsi=\"Calibri\" w:cs=\"Calibri\"/><w:color w:val=\"000000\"/></w:rPr><w:t>solution to a chosen problem, outlining the chosen approach and reasoning behind it.</w:t>",
            ]
            padded_outcomes = list(outcomes) if outcomes else ["Demonstrate course competencies."]
            while len(padded_outcomes) < 5:
                padded_outcomes.append(padded_outcomes[-1])
            # Merge any extra outcomes (6..8) into the 5th slot so all 8 outcomes appear cleanly
            if len(outcomes) > 5:
                fifth_text = " | ".join(outcomes[4:])
            else:
                fifth_text = padded_outcomes[4]

            for idx in range(4):
                doc_xml = doc_xml.replace(old_competencies[idx], html.escape(padded_outcomes[idx]))
            doc_xml = doc_xml.replace(
                "Design a basic AI ",
                html.escape(fifth_text)
            ).replace(
                "solution to a chosen problem, outlining the chosen approach and reasoning behind it.",
                ""
            )

            # 7. Replace Grading Components
            doc_xml = doc_xml.replace(
                "Weekly Quizzes (25% of final grade):",
                "Hands-on Data Engineering Labs (40% of final grade) & Unit Quizzes (20% of final grade):"
            ).replace(
                " These short quizzes, taken at the end of each week, will assess your understanding of the foundational concepts covered in the weekly slide decks.",
                " Weekly applied engineering labs (40%) evaluate your ability to build working data pipelines in Python and SQL, while unit knowledge checks (20%, 3 attempts allowed) verify conceptual mastery."
            )
            doc_xml = doc_xml.replace(
                "<w:t>Weekly Topic</w:t>",
                "<w:t>Comprehensive Capstone Defense</w:t>"
            ).replace(
                "<w:t xml:space=\"preserve\"> Presentations (50% of final grade):</w:t>",
                "<w:t xml:space=\"preserve\"> (30% of final grade):</w:t>"
            )
            doc_xml = doc_xml.replace(
                "Class Discussions / Participation (25% of final grade):",
                "Asynchronous Preparation & Flipped Drills (10% of final grade):"
            )

            with zipfile.ZipFile(output_path, "w", zipfile.ZIP_DEFLATED) as zout:
                for item in zin.infolist():
                    if item.filename == "word/document.xml":
                        zout.writestr(item, doc_xml.encode("utf-8"))
                    else:
                        zout.writestr(item, zin.read(item.filename))
        return

    # Fallback standalone generator if template is unavailable
    content_types = (
        '<?xml version="1.0" encoding="UTF-8" standalone="yes"?>\n'
        '<Types xmlns="http://schemas.openxmlformats.org/package/2006/content-types">\n'
        '  <Default Extension="rels" ContentType="application/vnd.openxmlformats-package.relationships+xml"/>\n'
        '  <Default Extension="xml" ContentType="application/xml"/>\n'
        '  <Override PartName="/word/document.xml" ContentType="application/vnd.openxmlformats-officedocument.wordprocessingml.document.main+xml"/>\n'
        '</Types>'
    )
    rels = (
        '<?xml version="1.0" encoding="UTF-8" standalone="yes"?>\n'
        '<Relationships xmlns="http://schemas.openxmlformats.org/package/2006/relationships">\n'
        '  <Relationship Id="rId1" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/officeDocument" Target="word/document.xml"/>\n'
        '</Relationships>'
    )
    p_elements = [
        f'<w:p><w:r><w:rPr><w:b/><w:sz w:val="36"/></w:rPr><w:t>{html.escape(course_code)}: {html.escape(course_title)}</w:t></w:r></w:p>',
        f'<w:p><w:r><w:rPr><w:b/><w:sz w:val="28"/></w:rPr><w:t>Master Course Syllabus ({html.escape(term_str)})</w:t></w:r></w:p>',
        f'<w:p><w:r><w:t>Institution: {html.escape(institution)}</w:t></w:r></w:p>',
        f'<w:p><w:r><w:t>Course Credits: {html.escape(credits_str)}</w:t></w:r></w:p>',
        '<w:p><w:r><w:rPr><w:b/></w:rPr><w:t>Course Description:</w:t></w:r></w:p>',
        f'<w:p><w:r><w:t>{html.escape(description)}</w:t></w:r></w:p>',
    ]
    for idx, clo in enumerate(outcomes, 1):
        p_elements.append(f'<w:p><w:r><w:t>{idx}. {html.escape(clo)}</w:t></w:r></w:p>')
    for item in grading_breakdown:
        p_elements.append(f'<w:p><w:r><w:t>- {html.escape(item)}</w:t></w:r></w:p>')
    p_elements.append(f'<w:p><w:r><w:t>{html.escape(grading_scale)}</w:t></w:r></w:p>')
    doc_xml = (
        '<?xml version="1.0" encoding="UTF-8" standalone="yes"?>\n'
        '<w:document xmlns:w="http://schemas.openxmlformats.org/wordprocessingml/2006/main">\n'
        '  <w:body>\n    ' + "\n    ".join(p_elements) + '\n  </w:body>\n'
        '</w:document>'
    )
    with zipfile.ZipFile(output_path, "w", zipfile.ZIP_DEFLATED) as z:
        z.writestr("[Content_Types].xml", content_types)
        z.writestr("_rels/.rels", rels)
        z.writestr("word/document.xml", doc_xml)
