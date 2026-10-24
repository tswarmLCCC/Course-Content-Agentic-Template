#!/usr/bin/env python3
"""
QTI 1.2 Quiz Builder for Canvas LMS
Converts human-readable Markdown quiz files into Canvas-compliant QTI 1.2 XML packages.

Features:
- Pure Python 3 standard library (no pip dependencies).
- Parses Markdown with questions (A-D options) and an Answer Key table with rationales.
- Emits Canvas QTI 1.2 XML (`assessment_qti.xml`), metadata (`assessment_meta.xml`),
  and `non_cc_assessments` payload.
"""

import os
import re
import html
import hashlib
from typing import List, Dict, Tuple, Optional


def make_canvas_id(seed: str) -> str:
    """Generate a deterministic 32-character hex ID matching Canvas format."""
    return "g" + hashlib.md5(seed.encode("utf-8")).hexdigest()[1:]


def parse_quiz_md(filepath: str) -> List[Dict]:
    """
    Parses a markdown quiz file into structured question objects.
    
    Expected format:
      ### Question 1
      What is the output of ...?
      * A) First option
      * B) Second option
      * C) Third option
      * D) Fourth option
      ...
      ## Answer Key
      | Question # | Correct Answer | Concept Tested & Rationale |
      | :--- | :--- | :--- |
      | **1** | **B** | Rationale text... |
    """
    if not os.path.exists(filepath):
        raise FileNotFoundError(f"Quiz file not found: {filepath}")

    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()

    # Split into questions section and answer key section
    parts = re.split(r"#+\s*Answer Key", content, flags=re.IGNORECASE)
    questions_part = parts[0]
    key_part = parts[1] if len(parts) > 1 else ""

    # Parse answer key table
    key_map: Dict[int, Tuple[str, str]] = {}
    for line in key_part.splitlines():
        line = line.strip()
        if not line.startswith("|"):
            continue
        cells = [c.strip() for c in line.split("|")[1:-1]]
        if len(cells) >= 3:
            q_num_match = re.search(r"\d+", cells[0])
            ans_match = re.search(r"[A-D]", cells[1], re.IGNORECASE)
            if q_num_match and ans_match:
                q_num = int(q_num_match.group(0))
                ans = ans_match.group(0).upper()
                rationale = cells[2]
                key_map[q_num] = (ans, rationale)

    # Parse question blocks
    q_blocks = re.split(r"###\s*Question\s+(\d+)", questions_part)
    questions = []
    for i in range(1, len(q_blocks), 2):
        q_num = int(q_blocks[i])
        block_text = q_blocks[i + 1].strip()

        # Extract options (A, B, C, D)
        opt_matches = list(re.finditer(r"^\s*[*•-]\s*([A-D])\)\s*(.+)$", block_text, flags=re.MULTILINE))
        if opt_matches:
            prompt_end = opt_matches[0].start()
            prompt = block_text[:prompt_end].strip()
            options = []
            for m in opt_matches:
                opt_letter = m.group(1).upper()
                opt_text = m.group(2).strip()
                options.append((opt_letter, opt_text))
        else:
            prompt = block_text
            options = []

        correct_ans, rationale = key_map.get(q_num, ("A", ""))
        questions.append({
            "num": q_num,
            "prompt": prompt,
            "options": options,
            "correct_answer": correct_ans,
            "rationale": rationale
        })

    return questions


def build_qti_xml(quiz_id: str, quiz_title: str, questions: List[Dict], max_attempts: int = 3) -> str:
    """Generates standard QTI 1.2 XML matching the exact Canvas Common Cartridge profile."""
    items_xml = []
    for q in questions:
        q_num = q["num"]
        item_id = make_canvas_id(f"{quiz_id}_q_{q_num}")

        opt_labels = []
        cond_elements = []
        for opt_letter, opt_text in q["options"]:
            opt_id = make_canvas_id(f"{item_id}_opt_{opt_letter}")
            opt_labels.append(f"""              <response_label ident="{opt_id}">
                <material>
                  <mattext texttype="text/plain">{html.escape(opt_text)}</mattext>
                </material>
              </response_label>""")

            if opt_letter == q["correct_answer"]:
                cond_elements.append(f"""                <varequal respident="response1">{opt_id}</varequal>""")
            else:
                cond_elements.append(f"""                <not>
                  <varequal respident="response1">{opt_id}</varequal>
                </not>""")

        options_block = "\n".join(opt_labels)
        condition_block = "\n".join(cond_elements)
        prompt_clean = html.escape(q["prompt"]).replace("\n", "<br/>")

        items_xml.append(f"""      <item ident="{item_id}" title="Question {q_num}">
        <itemmetadata>
          <qtimetadata>
            <qtimetadatafield>
              <fieldlabel>cc_profile</fieldlabel>
              <fieldentry>cc.multiple_response.v0p1</fieldentry>
            </qtimetadatafield>
          </qtimetadata>
        </itemmetadata>
        <presentation>
          <material>
            <mattext texttype="text/html">&lt;div&gt;{prompt_clean}&lt;/div&gt;</mattext>
          </material>
          <response_lid ident="response1" rcardinality="Multiple">
            <render_choice>
{options_block}
            </render_choice>
          </response_lid>
        </presentation>
        <resprocessing>
          <outcomes>
            <decvar maxvalue="100" minvalue="0" varname="SCORE" vartype="Decimal"/>
          </outcomes>
          <respcondition continue="No">
            <conditionvar>
              <and>
{condition_block}
              </and>
            </conditionvar>
            <setvar action="Set" varname="SCORE">100</setvar>
          </respcondition>
        </resprocessing>
      </item>""")

    items_joined = "\n".join(items_xml)

    return f"""<?xml version="1.0" encoding="UTF-8"?>
<questestinterop xmlns="http://www.imsglobal.org/xsd/ims_qtiasiv1p2" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:schemaLocation="http://www.imsglobal.org/xsd/ims_qtiasiv1p2 http://www.imsglobal.org/profile/cc/ccv1p1/ccv1p1_qtiasiv1p2p1_v1p0.xsd">
  <assessment ident="{quiz_id}" title="{html.escape(quiz_title)}">
    <qtimetadata>
      <qtimetadatafield>
        <fieldlabel>cc_profile</fieldlabel>
        <fieldentry>cc.exam.v0p1</fieldentry>
      </qtimetadatafield>
      <qtimetadatafield>
        <fieldlabel>qmd_assessmenttype</fieldlabel>
        <fieldentry>Examination</fieldentry>
      </qtimetadatafield>
      <qtimetadatafield>
        <fieldlabel>qmd_scoretype</fieldlabel>
        <fieldentry>Percentage</fieldentry>
      </qtimetadatafield>
      <qtimetadatafield>
        <fieldlabel>cc_maxattempts</fieldlabel>
        <fieldentry>{max_attempts}</fieldentry>
      </qtimetadatafield>
    </qtimetadata>
    <section ident="root_section">
{items_joined}
    </section>
  </assessment>
</questestinterop>
"""


def build_assessment_meta_xml(
    quiz_id: str,
    quiz_title: str,
    quiz_group_id: str,
    points_possible: float = 30.0,
    allowed_attempts: int = 3,
    description: str = "",
    due_at: Optional[str] = None,
    lock_at: Optional[str] = None
) -> str:
    """Builds Canvas assessment_meta.xml linking the quiz to an assignment group."""
    assign_id = make_canvas_id(f"assign_{quiz_id}")
    due_block = f"  <due_at>{due_at}</due_at>\n  <lock_at>{lock_at}</lock_at>\n" if due_at else ""
    assign_due_block = f"    <due_at>{due_at}</due_at>\n    <lock_at>{lock_at}</lock_at>\n" if due_at else ""
    desc_clean = description or f"<p>This assessment evaluates student mastery of key concepts and query patterns. Allowed attempts: {allowed_attempts}. Highest score kept.</p>"

    return f"""<?xml version="1.0" encoding="UTF-8"?>
<quiz xmlns="http://canvas.instructure.com/xsd/cccv1p0" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:schemaLocation="http://canvas.instructure.com/xsd/cccv1p0 https://canvas.instructure.com/xsd/cccv1p0.xsd" identifier="{quiz_id}">
  <title>{html.escape(quiz_title)}</title>
  <description>{html.escape(desc_clean)}</description>
{due_block}  <shuffle_questions>false</shuffle_questions>
  <shuffle_answers>false</shuffle_answers>
  <scoring_policy>keep_highest</scoring_policy>
  <quiz_type>assignment</quiz_type>
  <points_possible>{points_possible:.1f}</points_possible>
  <allowed_attempts>{allowed_attempts}</allowed_attempts>
  <show_correct_answers>true</show_correct_answers>
  <assignment identifier="{assign_id}">
    <title>{html.escape(quiz_title)}</title>
{assign_due_block}    <workflow_state>published</workflow_state>
    <quiz_identifierref>{quiz_id}</quiz_identifierref>
    <points_possible>{points_possible:.1f}</points_possible>
    <grading_type>points</grading_type>
    <submission_types>online_quiz</submission_types>
    <assignment_group_identifierref>{quiz_group_id}</assignment_group_identifierref>
  </assignment>
</quiz>
"""


def package_quiz(
    quiz_md_path: str,
    output_cartridge_dir: str,
    quiz_id: str,
    quiz_title: str,
    quiz_group_id: str,
    points_possible: float = 30.0,
    allowed_attempts: int = 3,
    due_at: Optional[str] = None
) -> Dict[str, str]:
    """
    End-to-end quiz packaging into a cartridge directory.
    Creates:
      - [output_cartridge_dir]/[quiz_id]/assessment_qti.xml
      - [output_cartridge_dir]/[quiz_id]/assessment_meta.xml
      - [output_cartridge_dir]/non_cc_assessments/[quiz_id].xml.qti
    """
    questions = parse_quiz_md(quiz_md_path)
    qti_xml = build_qti_xml(quiz_id, quiz_title, questions, max_attempts=allowed_attempts)
    meta_xml = build_assessment_meta_xml(
        quiz_id, quiz_title, quiz_group_id,
        points_possible=points_possible,
        allowed_attempts=allowed_attempts,
        due_at=due_at, lock_at=due_at
    )

    q_dir = os.path.join(output_cartridge_dir, quiz_id)
    non_cc_dir = os.path.join(output_cartridge_dir, "non_cc_assessments")
    os.makedirs(q_dir, exist_ok=True)
    os.makedirs(non_cc_dir, exist_ok=True)

    with open(os.path.join(q_dir, "assessment_qti.xml"), "w", encoding="utf-8") as f:
        f.write(qti_xml)
    with open(os.path.join(q_dir, "assessment_meta.xml"), "w", encoding="utf-8") as f:
        f.write(meta_xml)
    with open(os.path.join(non_cc_dir, f"{quiz_id}.xml.qti"), "w", encoding="utf-8") as f:
        f.write(qti_xml)

    return {
        "quiz_id": quiz_id,
        "question_count": str(len(questions)),
        "qti_path": os.path.join(q_dir, "assessment_qti.xml")
    }


if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description="Convert Markdown quiz to Canvas QTI 1.2 XML")
    parser.add_argument("quiz_md", help="Path to Markdown quiz file")
    parser.add_argument("--out", "-o", default="./dist_quiz", help="Output directory")
    parser.add_argument("--title", "-t", default="Unit Knowledge Check", help="Quiz Title")
    args = parser.parse_args()

    qid = make_canvas_id(args.title)
    gid = make_canvas_id("quizzes_group")
    res = package_quiz(args.quiz_md, args.out, qid, args.title, gid)
    print(f"Successfully compiled {res['question_count']} questions into {args.out}")
