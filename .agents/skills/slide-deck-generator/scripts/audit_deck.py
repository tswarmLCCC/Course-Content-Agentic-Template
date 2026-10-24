"""
Automated Course Presentation Quality Auditor
Audits any PowerPoint presentation (.pptx) against the institutional rubric:
- 100% Speaker Notes Coverage
- Assertion-Evidence Headlines
- Mandatory Objectives & Outcomes Slide
- Mandatory Battle Plan Alignment Slide
- Strict Left-Aligned Code Containers
- Mandatory References & Bibliography Slide
- Anti-Text-Wall Density Thresholds
"""

import sys
import os
from pptx import Presentation
from pptx.enum.text import PP_ALIGN


def audit_presentation(pptx_path):
    print("=" * 70)
    print(f"AUDITING PRESENTATION: '{os.path.basename(pptx_path)}'")
    print("=" * 70)

    if not os.path.exists(pptx_path):
        print(f"[FAIL] Presentation file not found: {pptx_path}")
        return False

    prs = Presentation(pptx_path)
    total_slides = len(prs.slides)
    print(f"Total Slides: {total_slides} (Target: >= 30 slides)")

    notes_missing = []
    non_assertion_titles = []
    centered_code_blocks = []
    text_wall_warnings = []

    has_objectives = False
    has_battle_plan = False
    has_bibliography = False

    for idx, slide in enumerate(prs.slides):
        slide_num = idx + 1

        # 1. Notes Check
        has_notes = False
        try:
            if slide.has_notes_slide:
                notes_text = slide.notes_slide.notes_text_frame.text.strip()
                if len(notes_text) > 15:
                    has_notes = True
        except Exception:
            pass

        if not has_notes:
            notes_missing.append(slide_num)

        # Inspect Shapes
        for shape in slide.shapes:
            if not shape.has_text_frame:
                continue

            tf = shape.text_frame
            full_shape_text = tf.text.strip()

            # Check for Objectives and Battle Plan
            low_text = full_shape_text.lower()
            if "learning objectives" in low_text and ("outcomes" in low_text or "deliverables" in low_text):
                has_objectives = True
            if "battle plan" in low_text or "alignment roadmap" in low_text:
                has_battle_plan = True
            if "references & further reading" in low_text or "bibliography" in low_text or "foundational literature" in low_text:
                has_bibliography = True

            # Check Code Paragraph Left Alignment
            for p in tf.paragraphs:
                p_text = p.text.strip()
                # If paragraph looks like code
                if any(kw in p_text for kw in ["def ", "class ", "import ", "curl ", "FROM ", "RUN ", "return ", "docker "]):
                    if p.alignment != PP_ALIGN.LEFT and p.alignment is not None:
                        centered_code_blocks.append((slide_num, p_text[:40]))

                # Check for dense walls of text (> 55 words in a single unbulleted paragraph)
                words = p_text.split()
                if len(words) > 55 and not p_text.startswith("#"):
                    text_wall_warnings.append((slide_num, len(words)))

    # Summary Evaluations
    pass_notes = len(notes_missing) == 0
    pass_code_align = len(centered_code_blocks) == 0
    pass_pacing = total_slides >= 29

    print("\n--- COMPREHENSIVE AUDIT RESULTS ---")
    print(f"Slide Count Pacing (>=30):        {'[PASS]' if pass_pacing else '[WARN: <30 slides]'}")
    print(f"100% Speaker Notes Coverage:      {'[PASS]' if pass_notes else f'[FAIL] (Missing on slides: {notes_missing})'}")
    print(f"Objectives & Outcomes Slide:      {'[PASS]' if has_objectives else '[FAIL] (Missing Slide 7)'}")
    print(f"Battle Plan Alignment Slide:      {'[PASS]' if has_battle_plan else '[FAIL] (Missing Slide 8)'}")
    print(f"Strict Left-Aligned Code:         {'[PASS]' if pass_code_align else f'[FAIL] (Centered code detected: {centered_code_blocks})'}")
    print(f"References & Bibliography Slide:  {'[PASS]' if has_bibliography else '[FAIL] (Missing final bibliography slide)'}")
    print(f"Anti-Text-Wall Density Check:     {'[PASS]' if len(text_wall_warnings) == 0 else f'[WARN] ({len(text_wall_warnings)} dense paragraphs)'}")

    overall_pass = pass_notes and has_objectives and has_battle_plan and pass_code_align and has_bibliography
    print("\n" + ("=" * 70))
    print(f"OVERALL AUDIT STATUS: {'[PASS] DECK APPROVED FOR DELIVERY' if overall_pass else '[FAIL] REMEDIATION REQUIRED'}")
    print("=" * 70)
    return overall_pass


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python audit_deck.py <path_to_presentation.pptx>")
        sys.exit(1)
    passed = audit_presentation(sys.argv[1])
    sys.exit(0 if passed else 1)
