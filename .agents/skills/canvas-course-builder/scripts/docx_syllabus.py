#!/usr/bin/env python3
"""
Institutional Word (.docx) Syllabus Generator
Creates Microsoft Word (.docx) course syllabi conforming to college accreditation standards.

Features:
- Pure Python 3 standard library (no python-docx or pip dependencies).
- Direct OpenXML zip packaging.
- Supports Course Title, Subtitle, Credits, Description, Outcomes, and Grading Distribution.
"""

import os
import zipfile
import html
from typing import List, Dict, Optional


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
    """Generates a standard accreditation-compliant .docx syllabus."""
    os.makedirs(os.path.dirname(os.path.abspath(output_path)), exist_ok=True)

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

    # Build paragraph elements
    p_elements = []

    # Title
    p_elements.append(
        f'<w:p><w:r><w:rPr><w:b/><w:sz w:val="36"/></w:rPr><w:t>{html.escape(course_code)}: {html.escape(course_title)}</w:t></w:r></w:p>'
    )
    # Term
    p_elements.append(
        f'<w:p><w:r><w:rPr><w:b/><w:sz w:val="28"/></w:rPr><w:t>Master Course Syllabus ({html.escape(term_str)})</w:t></w:r></w:p>'
    )
    # Metadata
    p_elements.append(f'<w:p><w:r><w:t>Institution: {html.escape(institution)}</w:t></w:r></w:p>')
    p_elements.append(f'<w:p><w:r><w:t>Course Credits: {html.escape(credits_str)}</w:t></w:r></w:p>')

    # Description
    p_elements.append('<w:p><w:r><w:rPr><w:b/></w:rPr><w:t>Course Description:</w:t></w:r></w:p>')
    p_elements.append(f'<w:p><w:r><w:t>{html.escape(description)}</w:t></w:r></w:p>')

    # Learning Outcomes
    p_elements.append('<w:p><w:r><w:rPr><w:b/></w:rPr><w:t>Course Learning Outcomes (CLOs):</w:t></w:r></w:p>')
    for idx, clo in enumerate(outcomes, 1):
        p_elements.append(f'<w:p><w:r><w:t>{idx}. {html.escape(clo)}</w:t></w:r></w:p>')

    # Grading Breakdown
    p_elements.append('<w:p><w:r><w:rPr><w:b/></w:rPr><w:t>Grading Policy &amp; Weighting:</w:t></w:r></w:p>')
    for item in grading_breakdown:
        p_elements.append(f'<w:p><w:r><w:t>- {html.escape(item)}</w:t></w:r></w:p>')

    # Grade Scale
    p_elements.append('<w:p><w:r><w:rPr><w:b/></w:rPr><w:t>Grade Scale:</w:t></w:r></w:p>')
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


if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description="Generate Word (.docx) Course Syllabus")
    parser.add_argument("--out", "-o", default="./Master_Syllabus.docx", help="Output file path")
    parser.add_argument("--code", default="COURSE 1010", help="Course Code")
    parser.add_argument("--title", default="Course Title", help="Course Title")
    args = parser.parse_args()

    create_syllabus_docx(
        output_path=args.out,
        course_code=args.code,
        course_title=args.title,
        term_str="Fall 2026",
        institution="Laramie County Community College (LCCC)",
        credits_str="3.0 Credit Hours (Asynchronous Online)",
        description="Comprehensive course instruction.",
        outcomes=["Demonstrate foundational competencies.", "Execute applied problem solving."],
        grading_breakdown=["Applied Labs (40%)", "Quizzes (20%)", "Capstone (30%)", "Participation (10%)"]
    )
    print(f"Generated {args.out}")
