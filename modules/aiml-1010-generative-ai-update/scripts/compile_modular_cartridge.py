#!/usr/bin/env python3
"""
Modular Canvas Common Cartridge (.imscc) Compiler for AIML 1010 Update
Compiles all 9 modular units into a standalone import package for existing course shells.
Integrates Reading Pages, Slide PDFs, Native Assignments, QTI 1.2 Quizzes, and Discussion Topics.
"""

import os
import sys
import re
import json
import shutil
import html
import hashlib
import zipfile
import xml.etree.ElementTree as ET

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
MODULE_ROOT = os.path.abspath(os.path.join(SCRIPT_DIR, ".."))
REPO_ROOT = os.path.abspath(os.path.join(MODULE_ROOT, "../.."))
CCB_SCRIPTS = os.path.join(REPO_ROOT, ".agents/skills/canvas-course-builder/scripts")
sys.path.insert(0, CCB_SCRIPTS)

from qti_builder import make_canvas_id

# 9 Unit definitions in canonical order
MODULE_SPECS = [
    {
        "key": "module_01_agentic_ai",
        "module_title": "Module 01 - Demystifying Agentic AI",
        "reading_title": "Reading - Demystifying Agentic AI",
        "reading_file": "reading-demystifying-agentic-ai.html",
        "pdf_name": "[Slides] Module 01 - Agentic AI Notes.pdf",
        "assign_title": "Module 01 Applied Lab: Exploring the Rise of Agentic AI",
        "quiz_title": "Module 01 Knowledge Check: Demystifying Agentic AI",
        "disc_title": "Discussion: Demystifying Agentic AI"
    },
    {
        "key": "week_03_prompt_engineering_i",
        "module_title": "Week 03 - Prompt Engineering I",
        "reading_title": "Reading - Prompt Engineering I",
        "reading_file": "reading-prompt-engineering-i.html",
        "pdf_name": "[Slides] Week 3 - GAI Prompt 1.pdf",
        "assign_title": "Week 03 Applied Lab: Controlled Generation with the RGC Framework",
        "quiz_title": "Week 03 Knowledge Check: Prompt Engineering I",
        "disc_title": "Discussion: Prompt Engineering I"
    },
    {
        "key": "week_04_prompt_engineering_ii",
        "module_title": "Week 04 - Prompt Engineering II",
        "reading_title": "Reading - Prompt Engineering II",
        "reading_file": "reading-prompt-engineering-ii.html",
        "pdf_name": "[Slides] Week 4 - GAI Prompt 2.pdf",
        "assign_title": "Week 04 Applied Lab: Sequential Prompt Chaining & Multimodal Storytelling",
        "quiz_title": "Week 04 Knowledge Check: Prompt Engineering II",
        "disc_title": "Discussion: Prompt Engineering II"
    },
    {
        "key": "week_10_transformers_llm_evolution",
        "module_title": "Week 10 - Transformers and Evolution of Large Language Models",
        "reading_title": "Reading - Transformers and Evolution of Large Language Models",
        "reading_file": "reading-transformers-and-evolution-of-large-language-models.html",
        "pdf_name": "[Slides] Week 10 - GAI Notes.pdf",
        "assign_title": "Week 10 Applied Lab: Hugging Face Transformer Pipeline Architecture",
        "quiz_title": "Week 10 Knowledge Check: Transformers and Evolution of Large Language Models",
        "disc_title": "Discussion: Transformers and Evolution of Large Language Models"
    },
    {
        "key": "week_11_diffusion_models_text_to_image",
        "module_title": "Week 11 - Diffusion Models and the Evolution of Text-to-Image Generation",
        "reading_title": "Reading - Diffusion Models and Text-to-Image Generation",
        "reading_file": "reading-diffusion-models-and-text-to-image-generation.html",
        "pdf_name": "[Slides] Week 11 - GAI Notes.pdf",
        "assign_title": "Week 11 Applied Lab: Cross-Modal Generative AI & Image Synthesis",
        "quiz_title": "Week 11 Knowledge Check: Diffusion Models and Text-to-Image Generation",
        "disc_title": "Discussion: Diffusion Models and Text-to-Image Generation"
    },
    {
        "key": "week_12_pretraining_generative_ai",
        "module_title": "Week 12 - Pre-Training Generative AI Models",
        "reading_title": "Reading - Pre-Training Generative AI Models",
        "reading_file": "reading-pre-training-generative-ai-models.html",
        "pdf_name": "[Slides] Week 12 - GAI Notes.pdf",
        "assign_title": "Week 12 Applied Lab: Domain-Specific LLM Architecture & Pre-Training Case Study",
        "quiz_title": "Week 12 Knowledge Check: Pre-Training Generative AI Models",
        "disc_title": "Discussion: Pre-Training Generative AI Models"
    },
    {
        "key": "week_13_finetuning_generative_ai",
        "module_title": "Week 13 - Fine-Tuning Generative AI Models",
        "reading_title": "Reading - Fine-Tuning Generative AI Models",
        "reading_file": "reading-fine-tuning-generative-ai-models.html",
        "pdf_name": "[Slides] Week 13 - GAI Notes.pdf",
        "assign_title": "Week 13 Applied Lab: Curating Instruction Datasets & PEFT Fine-Tuning Strategy",
        "quiz_title": "Week 13 Knowledge Check: Fine-Tuning Generative AI Models",
        "disc_title": "Discussion: Fine-Tuning Generative AI Models"
    },
    {
        "key": "week_15_prototyping_genai_apps",
        "module_title": "Week 15 - Prototyping Generative AI Applications",
        "reading_title": "Reading - Prototyping Generative AI Applications",
        "reading_file": "reading-prototyping-generative-ai-applications.html",
        "pdf_name": "[Slides] Week 15 - GAI Notes.pdf",
        "assign_title": "Week 15 Applied Lab: Prototyping an Interactive Generative AI Application",
        "quiz_title": "Week 15 Knowledge Check: Prototyping Generative AI Applications",
        "disc_title": "Discussion: Prototyping Generative AI Applications"
    },
    {
        "key": "week_16_llm_alignment_responsible_ai",
        "module_title": "Week 16 - LLM Alignment and the Responsible Use of Generative AI",
        "reading_title": "Reading - LLM Alignment and the Responsible Use of Generative AI",
        "reading_file": "reading-llm-alignment-and-the-responsible-use-of-generative-ai.html",
        "pdf_name": "[Slides] Week 16 - GAI Notes.pdf",
        "assign_title": "Week 16 Applied Lab: Auditing LLM Bias, Hallucination, and Safety Guardrails",
        "quiz_title": "Week 16 Knowledge Check: LLM Alignment and Responsible AI",
        "disc_title": "Discussion: LLM Alignment and Responsible AI"
    }
]


def assemble_cartridge():
    build_dir = os.path.join(MODULE_ROOT, "_cartridge_build")
    output_imscc = os.path.join(MODULE_ROOT, "AIML_1010_Generative_AI_Update_Modules_Import.imscc")

    if os.path.exists(build_dir):
        shutil.rmtree(build_dir)
    os.makedirs(build_dir, exist_ok=True)

    # Core subdirectories
    wiki_dir = os.path.join(build_dir, "wiki_content")
    settings_dir = os.path.join(build_dir, "course_settings")
    non_cc_dir = os.path.join(build_dir, "non_cc_assessments")
    slides_res_dir = os.path.join(build_dir, "web_resources", "slides")

    for d in [wiki_dir, settings_dir, non_cc_dir, slides_res_dir]:
        os.makedirs(d, exist_ok=True)

    # 1. Assignment Groups (standardized weights)
    labs_group_id = make_canvas_id("group_labs")
    quizzes_group_id = make_canvas_id("group_quizzes")
    prep_group_id = make_canvas_id("group_prep")
    disc_group_id = make_canvas_id("group_discussions")

    assign_groups_xml = f"""<?xml version="1.0" encoding="UTF-8"?>
<assignmentGroups xmlns="http://canvas.instructure.com/xsd/cccv1p0" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:schemaLocation="http://canvas.instructure.com/xsd/cccv1p0 https://canvas.instructure.com/xsd/cccv1p0.xsd">
  <assignmentGroup identifier="{labs_group_id}">
    <title>Hands-on Applied Labs</title>
    <position>1</position>
    <group_weight>40.0</group_weight>
  </assignmentGroup>
  <assignmentGroup identifier="{quizzes_group_id}">
    <title>Unit Knowledge Checks &amp; Quizzes</title>
    <position>2</position>
    <group_weight>20.0</group_weight>
  </assignmentGroup>
  <assignmentGroup identifier="{prep_group_id}">
    <title>Asynchronous Preparation &amp; Drills</title>
    <position>3</position>
    <group_weight>20.0</group_weight>
  </assignmentGroup>
  <assignmentGroup identifier="{disc_group_id}">
    <title>Weekly Collaborative Discussions</title>
    <position>4</position>
    <group_weight>20.0</group_weight>
  </assignmentGroup>
</assignmentGroups>
"""
    with open(os.path.join(settings_dir, "assignment_groups.xml"), "w", encoding="utf-8") as f:
        f.write(assign_groups_xml)

    # 2. Context & Course Settings (Modular Import Mode)
    course_id = make_canvas_id("AIML_1010_GAI_UPDATE")
    with open(os.path.join(settings_dir, "canvas_export.txt"), "w", encoding="utf-8") as f:
        f.write("AIML 1010 Generative AI & Agentic Curriculum Modular Update\n")

    with open(os.path.join(settings_dir, "context.xml"), "w", encoding="utf-8") as f:
        f.write(f"""<?xml version="1.0" encoding="UTF-8"?>
<context_info xmlns="http://canvas.instructure.com/xsd/cccv1p0" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:schemaLocation="http://canvas.instructure.com/xsd/cccv1p0 https://canvas.instructure.com/xsd/cccv1p0.xsd">
  <course_id>21632</course_id>
  <course_name>AIML 1010: Introduction to Artificial Intelligence</course_name>
  <root_account_id>100000000000001</root_account_id>
  <root_account_name>Laramie County Community College</root_account_name>
  <canvas_domain>lccc-wy.instructure.com</canvas_domain>
</context_info>
""")

    with open(os.path.join(settings_dir, "files_meta.xml"), "w", encoding="utf-8") as f:
        f.write("""<?xml version="1.0" encoding="UTF-8"?>
<fileMeta xmlns="http://canvas.instructure.com/xsd/cccv1p0" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:schemaLocation="http://canvas.instructure.com/xsd/cccv1p0 https://canvas.instructure.com/xsd/cccv1p0.xsd">
  <folders></folders>
  <files></files>
</fileMeta>
""")

    with open(os.path.join(settings_dir, "course_settings.xml"), "w", encoding="utf-8") as f:
        f.write(f"""<?xml version="1.0" encoding="UTF-8"?>
<course identifier="{course_id}" xmlns="http://canvas.instructure.com/xsd/cccv1p0" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:schemaLocation="http://canvas.instructure.com/xsd/cccv1p0 https://canvas.instructure.com/xsd/cccv1p0.xsd">
  <title>AIML 1010: Generative AI &amp; Agentic Curriculum Update</title>
  <course_code>AIML 1010</course_code>
  <is_public>false</is_public>
  <default_view>modules</default_view>
  <license>private</license>
  <grading_standard_enabled>true</grading_standard_enabled>
</course>
""")

    # Tracking manifests
    pages_manifest = []       # (filename, title, page_id)
    assign_manifest = []      # (assign_id, filename, title)
    quiz_manifest = []        # (quiz_id, quiz_meta_id, title)
    disc_manifest = []        # (topic_id, meta_id, title)
    slides_manifest = []      # (rel_path, res_id)
    modules_structure = []    # list of module objects

    units_dir = os.path.join(MODULE_ROOT, "units")
    qti_build_dir = os.path.join(MODULE_ROOT, "_qti_build")

    for mod_pos, spec in enumerate(MODULE_SPECS, 1):
        key = spec["key"]
        mod_dir = os.path.join(units_dir, key)
        mod_id = make_canvas_id(f"module_{key}")
        mod_items = []

        # --- A. Reading Page ---
        page_id = make_canvas_id(f"page_{key}")
        reading_src = os.path.join(mod_dir, "reading.html")
        with open(reading_src, "r", encoding="utf-8") as rf:
            reading_html = rf.read()

        # Ensure identifier meta tag matches page_id
        if 'name="identifier"' in reading_html:
            reading_html = re.sub(r'<meta\s+name=["\']identifier["\']\s+content=["\'][^"\']*["\']\s*/?>', f'<meta name="identifier" content="{page_id}"/>', reading_html, flags=re.IGNORECASE)
        else:
            reading_html = reading_html.replace("<head>", f'<head>\n<meta name="identifier" content="{page_id}"/>')

        with open(os.path.join(wiki_dir, spec["reading_file"]), "w", encoding="utf-8") as wf:
            wf.write(reading_html)

        pages_manifest.append((spec["reading_file"], spec["reading_title"], page_id))
        mod_items.append({
            "type": "WikiPage",
            "title": spec["reading_title"],
            "ref": page_id,
            "indent": 0
        })

        # --- B. Slide PDF Web Resource ---
        pdf_src = os.path.join(mod_dir, "slides", spec["pdf_name"])
        pdf_dest = os.path.join(slides_res_dir, spec["pdf_name"])
        shutil.copy2(pdf_src, pdf_dest)
        rel_pdf_path = f"web_resources/slides/{spec['pdf_name']}"
        pdf_res_id = make_canvas_id(f"res_{rel_pdf_path}")
        slides_manifest.append((rel_pdf_path, pdf_res_id))

        # --- C. Applied Assignment ---
        assign_id = make_canvas_id(f"assign_{key}")
        assign_folder = os.path.join(build_dir, assign_id)
        os.makedirs(assign_folder, exist_ok=True)

        with open(os.path.join(mod_dir, "assignment.json"), "r", encoding="utf-8") as af:
            adata = json.load(af)

        assign_settings_xml = f"""<?xml version="1.0" encoding="UTF-8"?>
<assignment identifier="{assign_id}" xmlns="http://canvas.instructure.com/xsd/cccv1p0" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:schemaLocation="http://canvas.instructure.com/xsd/cccv1p0 https://canvas.instructure.com/xsd/cccv1p0.xsd">
  <title>{html.escape(spec['assign_title'])}</title>
  <time_zone_edited>Mountain Time (US &amp; Canada)</time_zone_edited>
  <module_locked>false</module_locked>
  <assignment_group_identifierref>{labs_group_id}</assignment_group_identifierref>
  <workflow_state>published</workflow_state>
  <assignment_overrides></assignment_overrides>
  <allowed_extensions>{adata['allowed_ext']}</allowed_extensions>
  <has_group_category>false</has_group_category>
  <points_possible>{adata['points']:.1f}</points_possible>
  <grading_type>points</grading_type>
  <submission_types>online_text_entry,online_upload</submission_types>
  <turnitin_enabled>false</turnitin_enabled>
  <peer_reviews>false</peer_reviews>
  <post_policy><post_manually>false</post_manually></post_policy>
</assignment>
"""
        with open(os.path.join(assign_folder, "assignment_settings.xml"), "w", encoding="utf-8") as asf:
            asf.write(assign_settings_xml)

        with open(os.path.join(assign_folder, f"{assign_id}.html"), "w", encoding="utf-8") as ahf:
            ahf.write(adata["html"])

        assign_manifest.append((assign_id, f"{assign_id}.html", spec["assign_title"]))
        mod_items.append({
            "type": "Assignment",
            "title": spec["assign_title"],
            "ref": assign_id,
            "indent": 1
        })

        # --- D. QTI 1.2 Knowledge Check Quiz ---
        quiz_id = make_canvas_id(f"quiz_{key}")
        quiz_meta_id = make_canvas_id(f"meta_{quiz_id}")
        quiz_src_dir = os.path.join(qti_build_dir, quiz_id)
        quiz_dest_dir = os.path.join(build_dir, quiz_id)
        os.makedirs(quiz_dest_dir, exist_ok=True)

        shutil.copy2(os.path.join(quiz_src_dir, "assessment_qti.xml"), os.path.join(quiz_dest_dir, "assessment_qti.xml"))
        shutil.copy2(os.path.join(quiz_src_dir, "assessment_meta.xml"), os.path.join(quiz_dest_dir, "assessment_meta.xml"))
        shutil.copy2(os.path.join(qti_build_dir, "non_cc_assessments", f"{quiz_id}.xml.qti"), os.path.join(non_cc_dir, f"{quiz_id}.xml.qti"))

        quiz_manifest.append((quiz_id, quiz_meta_id, spec["quiz_title"]))
        mod_items.append({
            "type": "Quizzes::Quiz",
            "title": spec["quiz_title"],
            "ref": quiz_id,
            "indent": 1
        })

        # --- E. Native Discussion Topic ---
        topic_id = make_canvas_id(f"topic_{key}")
        disc_meta_id = make_canvas_id(f"meta_topic_{key}")

        with open(os.path.join(mod_dir, "discussion.json"), "r", encoding="utf-8") as df:
            ddata = json.load(df)

        topic_xml = f"""<?xml version="1.0" encoding="UTF-8"?>
<topic xmlns="http://www.imsglobal.org/xsd/imsccv1p1/imsdt_v1p1" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:schemaLocation="http://www.imsglobal.org/xsd/imsccv1p1/imsdt_v1p1 http://www.imsglobal.org/profile/cc/ccv1p1/ccv1p1_imsdt_v1p1.xsd">
  <title>{html.escape(spec['disc_title'])}</title>
  <text texttype="text/html">{html.escape(ddata['html'])}</text>
</topic>
"""
        with open(os.path.join(build_dir, f"{topic_id}.xml"), "w", encoding="utf-8") as tf:
            tf.write(topic_xml)

        disc_meta_xml = f"""<?xml version="1.0" encoding="UTF-8"?>
<topicMeta identifier="{disc_meta_id}" xmlns="http://canvas.instructure.com/xsd/cccv1p0" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:schemaLocation="http://canvas.instructure.com/xsd/cccv1p0 https://canvas.instructure.com/xsd/cccv1p0.xsd">
  <topic_id>{topic_id}</topic_id>
  <title>{html.escape(spec['disc_title'])}</title>
  <position/>
  <type>topic</type>
  <discussion_type>threaded</discussion_type>
  <has_group_category>false</has_group_category>
  <workflow_state>active</workflow_state>
  <module_locked>false</module_locked>
  <allow_rating>false</allow_rating>
  <only_graders_can_rate>false</only_graders_can_rate>
  <sort_by_rating>false</sort_by_rating>
  <sort_order>desc</sort_order>
  <sort_order_locked>false</sort_order_locked>
  <expanded>false</expanded>
  <expanded_locked>false</expanded_locked>
  <todo_date/>
</topicMeta>
"""
        with open(os.path.join(build_dir, f"{disc_meta_id}.xml"), "w", encoding="utf-8") as dmf:
            dmf.write(disc_meta_xml)

        disc_manifest.append((topic_id, disc_meta_id, spec["disc_title"]))
        mod_items.append({
            "type": "DiscussionTopic",
            "title": spec["disc_title"],
            "ref": topic_id,
            "indent": 1
        })

        modules_structure.append({
            "id": mod_id,
            "title": spec["module_title"],
            "items": mod_items
        })

    # 3. Generate module_meta.xml
    modules_xml_items = []
    org_items = []

    for pos, mod in enumerate(modules_structure, 1):
        mod_id = mod["id"]
        mod_title = mod["title"]
        m_items_xml = []
        m_man_items = []

        for i_pos, item in enumerate(mod["items"], 1):
            shared_item_id = make_canvas_id(f"item_{mod_id}_{item['ref']}")
            m_items_xml.append(f"""      <item identifier="{shared_item_id}">
        <content_type>{item['type']}</content_type>
        <workflow_state>active</workflow_state>
        <title>{html.escape(item['title'])}</title>
        <identifierref>{item['ref']}</identifierref>
        <position>{i_pos}</position>
        <new_tab>false</new_tab>
        <indent>{item['indent']}</indent>
        <link_settings_json>null</link_settings_json>
      </item>""")

            m_man_items.append(f"""          <item identifier="{shared_item_id}" identifierref="{item['ref']}">
            <title>{html.escape(item['title'])}</title>
          </item>""")

        modules_xml_items.append(f"""  <module identifier="{mod_id}">
    <title>{html.escape(mod_title)}</title>
    <workflow_state>active</workflow_state>
    <position>{pos}</position>
    <items>
{chr(10).join(m_items_xml)}
    </items>
  </module>""")

        org_items.append(f"""        <item identifier="{mod_id}">
          <title>{html.escape(mod_title)}</title>
{chr(10).join(m_man_items)}
        </item>""")

    mod_meta_xml = f"""<?xml version="1.0" encoding="UTF-8"?>
<modules xmlns="http://canvas.instructure.com/xsd/cccv1p0" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:schemaLocation="http://canvas.instructure.com/xsd/cccv1p0 https://canvas.instructure.com/xsd/cccv1p0.xsd">
{chr(10).join(modules_xml_items)}
</modules>
"""
    with open(os.path.join(settings_dir, "module_meta.xml"), "w", encoding="utf-8") as f:
        f.write(mod_meta_xml)

    # 4. Generate imsmanifest.xml
    resources_xml = []

    # Sentinel & Course Settings
    resources_xml.append(f"""    <resource identifier="{course_id}" type="associatedcontent/imscc_xmlv1p1/learning-application-resource" href="course_settings/canvas_export.txt">
      <file href="course_settings/course_settings.xml"/>
      <file href="course_settings/module_meta.xml"/>
      <file href="course_settings/assignment_groups.xml"/>
      <file href="course_settings/context.xml"/>
      <file href="course_settings/canvas_export.txt"/>
      <file href="course_settings/files_meta.xml"/>
    </resource>""")

    # Wiki Pages
    for filename, title, page_id in pages_manifest:
        resources_xml.append(f"""    <resource identifier="{page_id}" type="webcontent" href="wiki_content/{filename}">
      <file href="wiki_content/{filename}"/>
    </resource>""")

    # Assignments
    for assign_id, html_name, assign_title in assign_manifest:
        resources_xml.append(f"""    <resource identifier="{assign_id}" type="associatedcontent/imscc_xmlv1p1/learning-application-resource" href="{assign_id}/{assign_id}.html">
      <file href="{assign_id}/{assign_id}.html"/>
      <file href="{assign_id}/assignment_settings.xml"/>
    </resource>""")

    # Quizzes
    for quiz_id, quiz_meta_id, quiz_title in quiz_manifest:
        resources_xml.append(f"""    <resource identifier="{quiz_id}" type="imsqti_xmlv1p2/imscc_xmlv1p1/assessment">
      <file href="{quiz_id}/assessment_qti.xml"/>
      <dependency identifierref="{quiz_meta_id}"/>
    </resource>
    <resource identifier="{quiz_meta_id}" type="associatedcontent/imscc_xmlv1p1/learning-application-resource" href="{quiz_id}/assessment_meta.xml">
      <file href="{quiz_id}/assessment_meta.xml"/>
      <file href="non_cc_assessments/{quiz_id}.xml.qti"/>
    </resource>""")

    # Discussions
    for topic_id, meta_id, disc_title in disc_manifest:
        resources_xml.append(f"""    <resource identifier="{topic_id}" type="imsdt_xmlv1p1">
      <file href="{topic_id}.xml"/>
      <dependency identifierref="{meta_id}"/>
    </resource>
    <resource identifier="{meta_id}" type="associatedcontent/imscc_xmlv1p1/learning-application-resource" href="{meta_id}.xml">
      <file href="{meta_id}.xml"/>
    </resource>""")

    # Slide PDFs
    for rel_path, res_id in slides_manifest:
        resources_xml.append(f"""    <resource identifier="{res_id}" type="webcontent" href="{rel_path}">
      <file href="{rel_path}"/>
    </resource>""")

    imsmanifest_xml = f"""<?xml version="1.0" encoding="UTF-8"?>
<manifest identifier="{make_canvas_id('root_manifest')}" xmlns="http://www.imsglobal.org/xsd/imsccv1p1/imscp_v1p1" xmlns:lom="http://ltsc.ieee.org/xsd/imsccv1p1/LOM/resource" xmlns:lomimscc="http://ltsc.ieee.org/xsd/imsccv1p1/LOM/manifest" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:schemaLocation="http://www.imsglobal.org/xsd/imsccv1p1/imscp_v1p1 http://www.imsglobal.org/profile/cc/ccv1p1/ccv1p1_imscp_v1p2_v1p0.xsd http://ltsc.ieee.org/xsd/imsccv1p1/LOM/resource http://www.imsglobal.org/profile/cc/ccv1p1/LOM/ccv1p1_lomresource_v1p0.xsd http://ltsc.ieee.org/xsd/imsccv1p1/LOM/manifest http://www.imsglobal.org/profile/cc/ccv1p1/LOM/ccv1p1_lommanifest_v1p0.xsd">
  <metadata>
    <schema>IMS Common Cartridge</schema>
    <schemaversion>1.1.0</schemaversion>
    <lomimscc:lom>
      <lomimscc:general>
        <lomimscc:title>
          <lomimscc:string>AIML 1010: Generative AI &amp; Agentic Curriculum Update</lomimscc:string>
        </lomimscc:title>
      </lomimscc:general>
    </lomimscc:lom>
  </metadata>
  <organizations>
    <organization identifier="org_1" structure="rooted-hierarchy">
      <item identifier="LearningModules">
{chr(10).join(org_items)}
      </item>
    </organization>
  </organizations>
  <resources>
{chr(10).join(resources_xml)}
  </resources>
</manifest>
"""
    with open(os.path.join(build_dir, "imsmanifest.xml"), "w", encoding="utf-8") as f:
        f.write(imsmanifest_xml)

    # 5. Schema Validation on all XML & QTI files
    print("\nValidating XML syntax on all generated files...")
    xml_count = 0
    for root, _, files in os.walk(build_dir):
        for file in files:
            if file.endswith(".xml") or file.endswith(".qti"):
                fpath = os.path.join(root, file)
                try:
                    ET.parse(fpath)
                    xml_count += 1
                except ET.ParseError as e:
                    raise ValueError(f"XML Validation Failed on {fpath}: {e}")
    print(f"SUCCESS: {xml_count} XML documents validated with 0 syntax errors.")

    # 6. Compress into .imscc
    print(f"\nCompressing build directory into {output_imscc}...")
    file_count = 0
    with zipfile.ZipFile(output_imscc, "w", zipfile.ZIP_DEFLATED) as z:
        for root, _, files in os.walk(build_dir):
            for file in files:
                full_path = os.path.join(root, file)
                rel_path = os.path.relpath(full_path, build_dir)
                z.write(full_path, rel_path)
                file_count += 1

    cartridge_size = os.path.getsize(output_imscc)
    print(f"SUCCESS: Packed {file_count} files into {output_imscc} ({cartridge_size:,} bytes).")

    return {
        "output_imscc": output_imscc,
        "size_bytes": cartridge_size,
        "xml_count": xml_count,
        "modules_count": len(modules_structure)
    }


if __name__ == "__main__":
    res = assemble_cartridge()
    print("\nModular cartridge compilation finished successfully!")
