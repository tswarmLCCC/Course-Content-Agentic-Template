"""
Universal Slide Presentation Engine
Implements SLIDE_DESIGN_PLAYBOOK.md specifications using python-pptx.
Produces 16:9 widescreen, WCAG 2.1 AAA high-contrast slides with 5 archetypes and strict left-aligned code.
"""

import os
import pptx
from pptx import Presentation
from pptx.util import Inches, Pt
from pptx.enum.text import PP_ALIGN, MSO_ANCHOR
from pptx.dml.color import RGBColor
from pptx.enum.shapes import MSO_SHAPE

# -----------------------------------------------------------------------------
# Color Palette Constants (WCAG 2.1 AAA Compliant)
# -----------------------------------------------------------------------------
NAVY_PRIMARY = RGBColor(0, 32, 85)       # #002055 - Dark Section Navy
NAVY_HEADER = RGBColor(10, 37, 64)       # #0A2540 - Primary Text Navy
SLATE_BG = RGBColor(248, 250, 252)       # #F8FAFC - Canvas Light Background
WHITE = RGBColor(255, 255, 255)          # Pure White
GOLD_ACCENT = RGBColor(255, 192, 1)      # #FFC001 - Vibrant Gold Accent
ICE_BLUE_FILL = RGBColor(243, 247, 252)  # #F3F7FC - Ice Blue Card
ICE_BLUE_BORDER = RGBColor(194, 214, 236)# #C2D6EC - Ice Blue Border
WARM_FILL = RGBColor(255, 253, 240)      # #FFFDF0 - Warm Cream Card
WARM_BORDER = RGBColor(240, 205, 90)     # #F0CD5A - Warm Gold Border
NORMAL_CARD_FILL = RGBColor(255, 255, 255) # White Card
NORMAL_CARD_BORDER = RGBColor(203, 213, 225) # #CBD5E1 - Slate Border

# Code Syntax Container
CODE_BG = RGBColor(17, 24, 39)           # #111827 - Midnight Slate
CODE_BORDER = RGBColor(55, 65, 81)       # #374151 - Slate 700
CODE_TEXT = RGBColor(138, 212, 255)      # #8AD4FF - High-Contrast Cyan

# Text Colors
TEXT_DARK = RGBColor(30, 41, 59)         # #1E293B - Slate 800
TEXT_MUTED = RGBColor(100, 116, 139)     # #64748B - Slate 500
TEXT_LIGHT = RGBColor(255, 255, 255)     # White

# Fonts
FONT_TITLE = "Arial"
FONT_BODY = "Calibri"
FONT_CODE = "Consolas"


class SlideEngine:
    """Core presentation generator enforcing institutional design standards."""

    @staticmethod
    def create_presentation() -> Presentation:
        prs = Presentation()
        prs.slide_width = Inches(13.333)
        prs.slide_height = Inches(7.5)
        return prs

    @staticmethod
    def _add_base_slide(prs, bg_color=SLATE_BG):
        blank_layout = prs.slide_layouts[6]
        slide = prs.slides.add_slide(blank_layout)
        bg = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, 0, 0, Inches(13.333), Inches(7.5))
        bg.fill.solid()
        bg.fill.fore_color.rgb = bg_color
        bg.line.color.rgb = bg_color
        return slide

    @staticmethod
    def _add_header(slide, badge_text: str, title_text: str, subtitle_text: str = ""):
        header_box = slide.shapes.add_textbox(Inches(0.8), Inches(0.4), Inches(11.7), Inches(1.2))
        tf = header_box.text_frame
        tf.word_wrap = True
        tf.margin_left = tf.margin_top = tf.margin_right = tf.margin_bottom = 0

        # Eyebrow / Badge
        p_badge = tf.paragraphs[0]
        p_badge.text = badge_text.upper()
        p_badge.font.name = FONT_TITLE
        p_badge.font.size = Pt(11)
        p_badge.font.bold = True
        p_badge.font.color.rgb = NAVY_PRIMARY
        p_badge.space_after = Pt(4)

        # Main Title (Assertion-Evidence Headline)
        p_title = tf.add_paragraph()
        p_title.text = title_text
        p_title.font.name = FONT_TITLE
        p_title.font.size = Pt(20)
        p_title.font.bold = True
        p_title.font.color.rgb = NAVY_HEADER
        p_title.space_after = Pt(2)

        # Subtitle
        if subtitle_text:
            p_sub = tf.add_paragraph()
            p_sub.text = subtitle_text
            p_sub.font.name = FONT_BODY
            p_sub.font.size = Pt(13)
            p_sub.font.color.rgb = TEXT_MUTED

    @staticmethod
    def _set_notes(slide, notes_text: str):
        if notes_text:
            notes_slide = slide.notes_slide
            tf = notes_slide.notes_text_frame
            tf.text = notes_text.strip()

    # -------------------------------------------------------------------------
    # Archetype 1: Split-Hero Title Slide
    # -------------------------------------------------------------------------
    @classmethod
    def build_split_hero_title(cls, prs, badge: str, title: str, subtitle: str, metadata: str, notes: str = ""):
        slide = cls._add_base_slide(prs, bg_color=SLATE_BG)

        # Left Hero Container (Dark Navy)
        left_hero = slide.shapes.add_shape(
            MSO_SHAPE.RECTANGLE, Inches(0), Inches(0), Inches(4.8), Inches(7.5)
        )
        left_hero.fill.solid()
        left_hero.fill.fore_color.rgb = NAVY_PRIMARY
        left_hero.line.color.rgb = NAVY_PRIMARY

        tf_hero = left_hero.text_frame
        tf_hero.word_wrap = True
        tf_hero.vertical_anchor = MSO_ANCHOR.MIDDLE
        tf_hero.margin_left = Inches(0.6)
        tf_hero.margin_right = Inches(0.6)

        p_acronym = tf_hero.paragraphs[0]
        p_acronym.text = "AI4W"
        p_acronym.font.name = FONT_TITLE
        p_acronym.font.size = Pt(56)
        p_acronym.font.bold = True
        p_acronym.font.color.rgb = WHITE
        p_acronym.space_after = Pt(10)

        p_prog = tf_hero.add_paragraph()
        p_prog.text = "Intel® AI for Workforce Program"
        p_prog.font.name = FONT_BODY
        p_prog.font.size = Pt(16)
        p_prog.font.bold = True
        p_prog.font.color.rgb = GOLD_ACCENT

        # Gold band divider
        gold_stripe = slide.shapes.add_shape(
            MSO_SHAPE.RECTANGLE, Inches(4.8), Inches(0), Inches(0.18), Inches(7.5)
        )
        gold_stripe.fill.solid()
        gold_stripe.fill.fore_color.rgb = GOLD_ACCENT
        gold_stripe.line.color.rgb = GOLD_ACCENT

        # Right Content Container
        right_box = slide.shapes.add_textbox(Inches(5.4), Inches(1.5), Inches(7.3), Inches(4.8))
        tf_r = right_box.text_frame
        tf_r.word_wrap = True

        p_eyebrow = tf_r.paragraphs[0]
        p_eyebrow.text = badge.upper()
        p_eyebrow.font.name = FONT_TITLE
        p_eyebrow.font.size = Pt(13)
        p_eyebrow.font.bold = True
        p_eyebrow.font.color.rgb = NAVY_PRIMARY
        p_eyebrow.space_after = Pt(12)

        p_main = tf_r.add_paragraph()
        p_main.text = title
        p_main.font.name = FONT_TITLE
        p_main.font.size = Pt(30)
        p_main.font.bold = True
        p_main.font.color.rgb = NAVY_HEADER
        p_main.space_after = Pt(14)

        p_sub = tf_r.add_paragraph()
        p_sub.text = subtitle
        p_sub.font.name = FONT_BODY
        p_sub.font.size = Pt(16)
        p_sub.font.color.rgb = TEXT_MUTED
        p_sub.space_after = Pt(24)

        p_meta = tf_r.add_paragraph()
        p_meta.text = metadata
        p_meta.font.name = FONT_BODY
        p_meta.font.size = Pt(12)
        p_meta.font.color.rgb = TEXT_DARK

        cls._set_notes(slide, notes)
        return slide

    # -------------------------------------------------------------------------
    # Archetype 2: High-Contrast Section Divider
    # -------------------------------------------------------------------------
    @classmethod
    def build_section_divider(cls, prs, sec_num: int, title: str, subtitle: str = "", notes: str = ""):
        slide = cls._add_base_slide(prs, bg_color=NAVY_PRIMARY)

        # Vertical Gold Accent Bar
        accent_bar = slide.shapes.add_shape(
            MSO_SHAPE.RECTANGLE, Inches(1.0), Inches(2.2), Inches(0.2), Inches(2.8)
        )
        accent_bar.fill.solid()
        accent_bar.fill.fore_color.rgb = GOLD_ACCENT
        accent_bar.line.color.rgb = GOLD_ACCENT

        # Content Box
        box = slide.shapes.add_textbox(Inches(1.5), Inches(2.1), Inches(10.5), Inches(3.0))
        tf = box.text_frame
        tf.word_wrap = True

        p_sec = tf.paragraphs[0]
        p_sec.text = f"SECTION {sec_num:02d}"
        p_sec.font.name = FONT_TITLE
        p_sec.font.size = Pt(15)
        p_sec.font.bold = True
        p_sec.font.color.rgb = GOLD_ACCENT
        p_sec.space_after = Pt(10)

        p_title = tf.add_paragraph()
        p_title.text = title
        p_title.font.name = FONT_TITLE
        p_title.font.size = Pt(34)
        p_title.font.bold = True
        p_title.font.color.rgb = WHITE
        p_title.space_after = Pt(12)

        if subtitle:
            p_sub = tf.add_paragraph()
            p_sub.text = subtitle
            p_sub.font.name = FONT_BODY
            p_sub.font.size = Pt(18)
            p_sub.font.color.rgb = RGBColor(200, 225, 250)

        cls._set_notes(slide, notes)
        return slide

    # -------------------------------------------------------------------------
    # Archetype 3: Two-Column Comparison Cards
    # -------------------------------------------------------------------------
    @classmethod
    def build_two_column(cls, prs, badge: str, title: str, subtitle: str,
                         left_title: str, left_items: list,
                         right_title: str, right_items: list, notes: str = ""):
        slide = cls._add_base_slide(prs, bg_color=SLATE_BG)
        cls._add_header(slide, badge, title, subtitle)

        # Left Card (Ice Blue)
        left_card = slide.shapes.add_shape(
            MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.8), Inches(1.8), Inches(5.6), Inches(5.0)
        )
        left_card.fill.solid()
        left_card.fill.fore_color.rgb = ICE_BLUE_FILL
        left_card.line.color.rgb = ICE_BLUE_BORDER
        left_card.line.width = Pt(1.5)

        tf_l = left_card.text_frame
        tf_l.word_wrap = True
        tf_l.margin_left = tf_l.margin_right = tf_l.margin_top = Inches(0.35)

        p_lt = tf_l.paragraphs[0]
        p_lt.text = left_title
        p_lt.font.name = FONT_TITLE
        p_lt.font.size = Pt(18)
        p_lt.font.bold = True
        p_lt.font.color.rgb = NAVY_PRIMARY
        p_lt.space_after = Pt(14)

        for item in left_items:
            p = tf_l.add_paragraph()
            p.space_after = Pt(10)
            if isinstance(item, tuple):
                run_anchor = p.add_run()
                run_anchor.text = f"• {item[0]}: "
                run_anchor.font.bold = True
                run_anchor.font.size = Pt(13)
                run_anchor.font.color.rgb = NAVY_PRIMARY
                run_body = p.add_run()
                run_body.text = item[1]
                run_body.font.size = Pt(13)
                run_body.font.color.rgb = TEXT_DARK
            else:
                p.text = f"• {item}"
                p.font.size = Pt(13)
                p.font.color.rgb = TEXT_DARK

        # Right Card (Warm Cream)
        right_card = slide.shapes.add_shape(
            MSO_SHAPE.ROUNDED_RECTANGLE, Inches(6.8), Inches(1.8), Inches(5.6), Inches(5.0)
        )
        right_card.fill.solid()
        right_card.fill.fore_color.rgb = WARM_FILL
        right_card.line.color.rgb = WARM_BORDER
        right_card.line.width = Pt(1.5)

        tf_r = right_card.text_frame
        tf_r.word_wrap = True
        tf_r.margin_left = tf_r.margin_right = tf_r.margin_top = Inches(0.35)

        p_rt = tf_r.paragraphs[0]
        p_rt.text = right_title
        p_rt.font.name = FONT_TITLE
        p_rt.font.size = Pt(18)
        p_rt.font.bold = True
        p_rt.font.color.rgb = RGBColor(140, 95, 0)
        p_rt.space_after = Pt(14)

        for item in right_items:
            p = tf_r.add_paragraph()
            p.space_after = Pt(10)
            if isinstance(item, tuple):
                run_anchor = p.add_run()
                run_anchor.text = f"• {item[0]}: "
                run_anchor.font.bold = True
                run_anchor.font.size = Pt(13)
                run_anchor.font.color.rgb = RGBColor(140, 95, 0)
                run_body = p.add_run()
                run_body.text = item[1]
                run_body.font.size = Pt(13)
                run_body.font.color.rgb = TEXT_DARK
            else:
                p.text = f"• {item}"
                p.font.size = Pt(13)
                p.font.color.rgb = TEXT_DARK

        cls._set_notes(slide, notes)
        return slide

    # -------------------------------------------------------------------------
    # Archetype 4: Normal Full-Width Content Card
    # -------------------------------------------------------------------------
    @classmethod
    def build_full_width_card(cls, prs, badge: str, title: str, subtitle: str,
                              card_title: str, items: list, notes: str = ""):
        slide = cls._add_base_slide(prs, bg_color=SLATE_BG)
        cls._add_header(slide, badge, title, subtitle)

        card = slide.shapes.add_shape(
            MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.8), Inches(1.8), Inches(11.7), Inches(5.0)
        )
        card.fill.solid()
        card.fill.fore_color.rgb = NORMAL_CARD_FILL
        card.line.color.rgb = NORMAL_CARD_BORDER
        card.line.width = Pt(1.5)

        tf = card.text_frame
        tf.word_wrap = True
        tf.margin_left = tf.margin_right = tf.margin_top = Inches(0.4)

        if card_title:
            p_ct = tf.paragraphs[0]
            p_ct.text = card_title
            p_ct.font.name = FONT_TITLE
            p_ct.font.size = Pt(17)
            p_ct.font.bold = True
            p_ct.font.color.rgb = NAVY_PRIMARY
            p_ct.space_after = Pt(14)

        for idx, item in enumerate(items):
            p = tf.add_paragraph() if (card_title or idx > 0) else tf.paragraphs[0]
            p.space_after = Pt(12)
            if isinstance(item, tuple):
                run_anchor = p.add_run()
                run_anchor.text = f"► {item[0]}: "
                run_anchor.font.bold = True
                run_anchor.font.name = FONT_BODY
                run_anchor.font.size = Pt(14)
                run_anchor.font.color.rgb = NAVY_PRIMARY

                run_body = p.add_run()
                run_body.text = item[1]
                run_body.font.name = FONT_BODY
                run_body.font.size = Pt(14)
                run_body.font.color.rgb = TEXT_DARK
            else:
                p.text = f"► {item}"
                p.font.name = FONT_BODY
                p.font.size = Pt(14)
                p.font.color.rgb = TEXT_DARK

        cls._set_notes(slide, notes)
        return slide

    # -------------------------------------------------------------------------
    # Archetype 5: Code & Runbook Slide (Strictly Left-Aligned)
    # -------------------------------------------------------------------------
    @classmethod
    def build_code_slide(cls, prs, badge: str, title: str, subtitle: str,
                         spec_title: str, spec_items: list, code_snippet: str, notes: str = ""):
        slide = cls._add_base_slide(prs, bg_color=SLATE_BG)
        cls._add_header(slide, badge, title, subtitle)

        # Left Spec Card (Width: 5.2")
        left_card = slide.shapes.add_shape(
            MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.8), Inches(1.8), Inches(5.2), Inches(5.0)
        )
        left_card.fill.solid()
        left_card.fill.fore_color.rgb = ICE_BLUE_FILL
        left_card.line.color.rgb = ICE_BLUE_BORDER
        left_card.line.width = Pt(1.5)

        tf_l = left_card.text_frame
        tf_l.word_wrap = True
        tf_l.margin_left = tf_l.margin_right = tf_l.margin_top = Inches(0.35)

        p_st = tf_l.paragraphs[0]
        p_st.text = spec_title
        p_st.font.name = FONT_TITLE
        p_st.font.size = Pt(17)
        p_st.font.bold = True
        p_st.font.color.rgb = NAVY_PRIMARY
        p_st.space_after = Pt(14)

        for item in spec_items:
            p = tf_l.add_paragraph()
            p.space_after = Pt(10)
            if isinstance(item, tuple):
                run_a = p.add_run()
                run_a.text = f"• {item[0]}: "
                run_a.font.bold = True
                run_a.font.size = Pt(12.5)
                run_a.font.color.rgb = NAVY_PRIMARY
                run_b = p.add_run()
                run_b.text = item[1]
                run_b.font.size = Pt(12.5)
                run_b.font.color.rgb = TEXT_DARK
            else:
                p.text = f"• {item}"
                p.font.size = Pt(12.5)
                p.font.color.rgb = TEXT_DARK

        # Right Code Card (Midnight Slate - Width: 6.2")
        code_card = slide.shapes.add_shape(
            MSO_SHAPE.ROUNDED_RECTANGLE, Inches(6.3), Inches(1.8), Inches(6.2), Inches(5.0)
        )
        code_card.fill.solid()
        code_card.fill.fore_color.rgb = CODE_BG
        code_card.line.color.rgb = CODE_BORDER
        code_card.line.width = Pt(1.5)

        tf_c = code_card.text_frame
        tf_c.word_wrap = True
        tf_c.margin_left = Inches(0.3)
        tf_c.margin_top = Inches(0.3)
        tf_c.margin_right = Inches(0.3)
        tf_c.margin_bottom = Inches(0.3)

        # STRICT LEFT ALIGNMENT LOOP (Consolas)
        code_lines = code_snippet.strip().split("\n")
        for l_idx, line in enumerate(code_lines):
            p = tf_c.paragraphs[0] if l_idx == 0 else tf_c.add_paragraph()
            p.text = line if line else " "
            p.font.name = FONT_CODE
            p.font.size = Pt(10.5)
            p.font.color.rgb = CODE_TEXT
            p.alignment = PP_ALIGN.LEFT  # <--- ENFORCES STRICT LEFT ALIGNMENT
            p.space_after = Pt(1.5)

        cls._set_notes(slide, notes)
        return slide
