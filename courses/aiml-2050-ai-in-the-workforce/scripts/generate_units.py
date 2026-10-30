#!/usr/bin/env python3
"""
Unit Content Generator for AIML 2050: AI in the Workforce
Compiles the 8 synthesized course units adhering to DesignPLUS styling,
ADR-001 (Accessibility), and ADR-003 (Canvas Cartridge Theme Invariants).
"""

import os
import sys
import re
import zipfile
import xml.etree.ElementTree as ET
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
UNITS_DIR = BASE_DIR / "units"
INTEL_DIR = Path(r"C:\Users\tswar.KAIASCOMPUTER\OneDrive - Laramie County Community College\Intel Curriculum\AIML 2050 - Agentic Version")

def extract_quiz_questions(xlsx_path):
    """Extracts multiple choice questions from Intel quiz excel files."""
    if not xlsx_path.exists():
        return []
    with zipfile.ZipFile(xlsx_path) as z:
        strings = []
        if 'xl/sharedStrings.xml' in z.namelist():
            with z.open('xl/sharedStrings.xml') as s:
                tree = ET.parse(s)
                for elem in tree.iter('{http://schemas.openxmlformats.org/spreadsheetml/2006/main}si'):
                    t_elems = elem.findall('.//{http://schemas.openxmlformats.org/spreadsheetml/2006/main}t')
                    strings.append(''.join([t.text for t in t_elems if t.text]))
        
        with z.open('xl/worksheets/sheet1.xml') as sh:
            tree = ET.parse(sh)
            rows = []
            for row in tree.iter('{http://schemas.openxmlformats.org/spreadsheetml/2006/main}row'):
                c_dict = {}
                for c in row.iter('{http://schemas.openxmlformats.org/spreadsheetml/2006/main}c'):
                    r_ref = c.get('r')
                    col_letter = re.match(r'([A-Z]+)', r_ref).group(1) if r_ref else ''
                    v = c.find('{http://schemas.openxmlformats.org/spreadsheetml/2006/main}v')
                    val = v.text if v is not None and v.text is not None else ''
                    if c.get('t') == 's' and val.isdigit() and int(val) < len(strings):
                        val = strings[int(val)]
                    c_dict[col_letter] = val
                rows.append(c_dict)
    
    questions = []
    opt_map = {'option 1': 'A', 'option 2': 'B', 'option 3': 'C', 'option 4': 'D',
               '1': 'A', '2': 'B', '3': 'C', '4': 'D', 'a': 'A', 'b': 'B', 'c': 'C', 'd': 'D'}
    
    for r in rows:
        q_text = r.get('B', '').strip()
        o1 = r.get('D', '').strip()
        o2 = r.get('E', '').strip()
        o3 = r.get('F', '').strip()
        o4 = r.get('G', '').strip()
        ans_raw = r.get('I', r.get('H', '')).strip().lower()
        ans = opt_map.get(ans_raw, 'A')
        
        if q_text and o1 and o2 and q_text.lower() not in ['question', 'module']:
            questions.append({
                'question': q_text,
                'options': {'A': o1, 'B': o2, 'C': o3 or 'N/A', 'D': o4 or 'N/A'},
                'answer': ans,
                'rationale': f"Core concept check: {q_text[:60]}..."
            })
    return questions

def format_quiz_markdown(unit_num, unit_title, questions):
    """Renders QTI 1.2 compatible Markdown quiz."""
    md = [f"# Unit {unit_num:02d} Knowledge Check: {unit_title}\n"]
    md.append(f"This assessment evaluates your conceptual understanding of Unit {unit_num:02d} competencies, enterprise workflows, and tool architectures.\n")
    md.append("---\n")
    
    for idx, q in enumerate(questions, 1):
        md.append(f"### Question {idx}")
        md.append(f"{q['question']}")
        md.append(f"* A) {q['options']['A']}")
        md.append(f"* B) {q['options']['B']}")
        md.append(f"* C) {q['options']['C']}")
        md.append(f"* D) {q['options']['D']}\n")
    
    md.append("---\n")
    md.append("## Answer Key\n")
    md.append("| Question # | Correct Answer | Concept Tested & Rationale |")
    md.append("| :--- | :--- | :--- |")
    for idx, q in enumerate(questions, 1):
        md.append(f"| **{idx}** | **{q['answer']}** | {q['rationale']} |")
    
    return "\n".join(md)

print("Helper functions defined successfully.")
