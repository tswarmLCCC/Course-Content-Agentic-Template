#!/usr/bin/env python3
"""
Portable Canvas Common Cartridge (.imscc) Builder
Compiles a complete, DesignPLUS-compliant Canvas course package from modular files or a JSON config.

Features:
- Pure Python standard library (no pip dependencies).
- Creates 100% compliant Canvas Common Cartridge 1.x (.imscc) zip packages.
- Generates synchronized imsmanifest.xml, module_meta.xml, assignment_groups.xml,
  assignment_settings.xml, and QTI 1.2 assessments.
- Integrates HTML styler and QTI builder modules.
- Performs schema validation using xml.etree.ElementTree on all generated XML files.
"""

import os
import sys
import re
import json
import hashlib
import zipfile
import html
import shutil
import datetime
import xml.etree.ElementTree as ET
from typing import Dict, List, Any, Optional

# Import local sibling modules
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, SCRIPT_DIR)
from qti_builder import parse_quiz_md, build_qti_xml, build_assessment_meta_xml, make_canvas_id
from html_styler import render_designplus_html, render_standard_page_html, parse_markdown_to_html
from docx_syllabus import create_syllabus_docx


class CanvasCourseBuilder:
    def __init__(self, config: Dict[str, Any], output_imscc: str, build_dir: Optional[str] = None):
        self.config = config
        self.output_imscc = os.path.abspath(output_imscc)
        self.build_dir = os.path.abspath(build_dir or os.path.join(os.path.dirname(output_imscc), "_cartridge_build"))
        
        self.course_id = make_canvas_id(config.get("course_code", "COURSE_1010"))
        self.wiki_dir = os.path.join(self.build_dir, "wiki_content")
        self.settings_dir = os.path.join(self.build_dir, "course_settings")
        self.non_cc_dir = os.path.join(self.build_dir, "non_cc_assessments")
        self.web_res_dir = os.path.join(self.build_dir, "web_resources")
        self.syllabi_dir = os.path.join(self.web_res_dir, "syllabi")
        self.images_dir = os.path.join(self.web_res_dir, "images")

        self.pages_manifest = []        # (filename, title, id)
        self.assignment_manifest = []   # (id, filename, title)
        self.quiz_manifest = []         # (quiz_id, quiz_meta_id, title)
        self.modules_data = []          # list of module definitions

    def prepare_directories(self):
        """Creates target directory structure."""
        for d in [self.wiki_dir, self.settings_dir, self.non_cc_dir, self.syllabi_dir, self.images_dir]:
            os.makedirs(d, exist_ok=True)

    def build_assignment_groups(self) -> Dict[str, str]:
        """Generates assignment_groups.xml with weighted percentages."""
        groups_conf = self.config.get("assignment_groups", [
            {"name": "Hands-on Applied Labs", "weight": 40.0, "key": "labs"},
            {"name": "Unit Knowledge Checks & Quizzes", "weight": 20.0, "key": "quizzes"},
            {"name": "Asynchronous Preparation & Drills", "weight": 10.0, "key": "prep"},
            {"name": "Comprehensive Course Capstone", "weight": 30.0, "key": "capstone"}
        ])

        group_map = {}
        items_xml = []
        for pos, g in enumerate(groups_conf, 1):
            gid = make_canvas_id(f"group_{g['key']}")
            group_map[g["key"]] = gid
            items_xml.append(f"""  <assignmentGroup identifier="{gid}">
    <title>{html.escape(g['name'])}</title>
    <position>{pos}</position>
    <group_weight>{float(g['weight']):.1f}</group_weight>
  </assignmentGroup>""")

        xml_str = f"""<?xml version="1.0" encoding="UTF-8"?>
<assignmentGroups xmlns="http://canvas.instructure.com/xsd/cccv1p0" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:schemaLocation="http://canvas.instructure.com/xsd/cccv1p0 https://canvas.instructure.com/xsd/cccv1p0.xsd">
{chr(10).join(items_xml)}
</assignmentGroups>
"""
        with open(os.path.join(self.settings_dir, "assignment_groups.xml"), "w", encoding="utf-8") as f:
            f.write(xml_str)
        return group_map

    def build_core_settings(self, is_modular: bool = False):
        """Generates context.xml, canvas_export.txt, files_meta.xml, and course_settings.xml."""
        c_code = self.config.get("course_code", "COURSE 1010")
        c_title = self.config.get("course_title", "Sample Course")
        institution = self.config.get("institution", "College")
        domain = self.config.get("domain", "canvas.institution.edu")

        with open(os.path.join(self.settings_dir, "canvas_export.txt"), "w", encoding="utf-8") as f:
            f.write("Q: What did the panda say when he was forced out of his natural habitat?\nA: This is un-BEAR-able\n")

        with open(os.path.join(self.settings_dir, "context.xml"), "w", encoding="utf-8") as f:
            f.write(f"""<?xml version="1.0" encoding="UTF-8"?>
<context_info xmlns="http://canvas.instructure.com/xsd/cccv1p0" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:schemaLocation="http://canvas.instructure.com/xsd/cccv1p0 https://canvas.instructure.com/xsd/cccv1p0.xsd">
  <course_id>1001</course_id>
  <course_name>{html.escape(c_code)}: {html.escape(c_title)}</course_name>
  <root_account_id>100000000000001</root_account_id>
  <root_account_name>{html.escape(institution)}</root_account_name>
  <canvas_domain>{html.escape(domain)}</canvas_domain>
</context_info>
""")

        with open(os.path.join(self.settings_dir, "files_meta.xml"), "w", encoding="utf-8") as f:
            f.write("""<?xml version="1.0" encoding="UTF-8"?>
<fileMeta xmlns="http://canvas.instructure.com/xsd/cccv1p0" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:schemaLocation="http://canvas.instructure.com/xsd/cccv1p0 https://canvas.instructure.com/xsd/cccv1p0.xsd">
  <folders></folders>
  <files></files>
</fileMeta>
""")

        default_view_tag = "<default_view>modules</default_view>" if is_modular else "<default_view>wiki</default_view>"
        with open(os.path.join(self.settings_dir, "course_settings.xml"), "w", encoding="utf-8") as f:
            f.write(f"""<?xml version="1.0" encoding="UTF-8"?>
<course identifier="{self.course_id}" xmlns="http://canvas.instructure.com/xsd/cccv1p0" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:schemaLocation="http://canvas.instructure.com/xsd/cccv1p0 https://canvas.instructure.com/xsd/cccv1p0.xsd">
  <title>{html.escape(c_code)}: {html.escape(c_title)}</title>
  <course_code>{html.escape(c_code)}</course_code>
  <is_public>false</is_public>
  {default_view_tag}
  <license>private</license>
  <grading_standard_enabled>true</grading_standard_enabled>
</course>
""")

    def build_assignment(self, assign_id: str, title: str, group_id: str, html_body: str, points: float = 50.0, allowed_ext: str = "sql,txt,pdf", due_iso: Optional[str] = None):
        """Builds assignment directory with assignment_settings.xml and assignment HTML."""
        folder = os.path.join(self.build_dir, assign_id)
        os.makedirs(folder, exist_ok=True)
        html_file = f"{assign_id}.html"

        due_block = f"  <due_at>{due_iso}</due_at>\n  <lock_at>{due_iso}</lock_at>\n" if due_iso else ""

        settings_xml = f"""<?xml version="1.0" encoding="UTF-8"?>
<assignment identifier="{assign_id}" xmlns="http://canvas.instructure.com/xsd/cccv1p0" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:schemaLocation="http://canvas.instructure.com/xsd/cccv1p0 https://canvas.instructure.com/xsd/cccv1p0.xsd">
  <title>{html.escape(title)}</title>
  <time_zone_edited>Mountain Time (US &amp; Canada)</time_zone_edited>
  <module_locked>false</module_locked>
  <assignment_group_identifierref>{group_id}</assignment_group_identifierref>
  <workflow_state>published</workflow_state>
{due_block}  <assignment_overrides></assignment_overrides>
  <allowed_extensions>{allowed_ext}</allowed_extensions>
  <has_group_category>false</has_group_category>
  <points_possible>{points:.1f}</points_possible>
  <grading_type>points</grading_type>
  <submission_types>online_text_entry,online_upload</submission_types>
  <turnitin_enabled>false</turnitin_enabled>
  <peer_reviews>false</peer_reviews>
  <post_policy><post_manually>false</post_manually></post_policy>
</assignment>
"""
        with open(os.path.join(folder, "assignment_settings.xml"), "w", encoding="utf-8") as f:
            f.write(settings_xml)

        with open(os.path.join(folder, html_file), "w", encoding="utf-8") as f:
            f.write(html_body)

        self.assignment_manifest.append((assign_id, html_file, title))

    def _ensure_wiki_metadata(self, html_content: str, page_id: str, title: str, is_front_page: bool = False, workflow_state: str = "active") -> str:
        """
        Defensive gate: Guarantees that any HTML page destined for wiki_content/ contains the
        mandatory Canvas WikiPage metadata in <head>.
        Without this metadata, Canvas does not register the file in wiki_pages and instead
        falls back to rendering a sandboxed <iframe> with a 'Download <file>.html' header!
        """
        # If not a full HTML document, wrap it completely
        if "<html" not in html_content.lower():
            front_meta = '\n<meta name="front_page" content="true"/>' if is_front_page else ''
            return f"""<html>
<head>
<meta http-equiv="Content-Type" content="text/html; charset=utf-8"/>
<title>{html.escape(title)}</title>
<meta name="identifier" content="{page_id}"/>
<meta name="editing_roles" content="teachers"/>
<meta name="workflow_state" content="{workflow_state}"/>
<meta name="editor_type" content="rce"/>{front_meta}
</head>
<body>
{html_content}
</body>
</html>"""

        # It is an HTML document. Ensure <head> contains the required tags
        head_match = re.search(r"<head\b[^>]*>", html_content, re.IGNORECASE)
        if not head_match:
            html_tag_match = re.search(r"<html\b[^>]*>", html_content, re.IGNORECASE)
            pos = html_tag_match.end() if html_tag_match else 0
            front_meta = '\n<meta name="front_page" content="true"/>' if is_front_page else ''
            head_block = f"""\n<head>\n<meta http-equiv="Content-Type" content="text/html; charset=utf-8"/>\n<title>{html.escape(title)}</title>\n<meta name="identifier" content="{page_id}"/>\n<meta name="editing_roles" content="teachers"/>\n<meta name="workflow_state" content="{workflow_state}"/>\n<meta name="editor_type" content="rce"/>{front_meta}\n</head>"""
            return html_content[:pos] + head_block + html_content[pos:]

        # Inject or update required meta tags inside existing <head>
        insert_pos = head_match.end()
        injections = []
        if 'name="identifier"' in html_content:
            html_content = re.sub(r'<meta\s+name=["\']identifier["\']\s+content=["\'][^"\']*["\']\s*/?>', f'<meta name="identifier" content="{page_id}"/>', html_content, flags=re.IGNORECASE)
        else:
            injections.append(f'<meta name="identifier" content="{page_id}"/>')

        if 'name="editing_roles"' not in html_content:
            injections.append('<meta name="editing_roles" content="teachers"/>')
        if 'name="workflow_state"' not in html_content:
            injections.append(f'<meta name="workflow_state" content="{workflow_state}"/>')
        if 'name="editor_type"' not in html_content:
            injections.append('<meta name="editor_type" content="rce"/>')
        if is_front_page and 'name="front_page"' not in html_content:
            injections.append('<meta name="front_page" content="true"/>')

        if injections:
            inject_str = "\n" + "\n".join(injections)
            return html_content[:insert_pos] + inject_str + html_content[insert_pos:]

        return html_content

    def add_wiki_page(self, page_id: str, filename: str, title: str, html_body: str, is_front_page: bool = False, workflow_state: str = "active"):
        """Writes wiki page HTML to wiki_content/ and records in pages manifest."""
        if filename in ("home-page.html", "front-page.html", "index.html"):
            is_front_page = True

        guaranteed_html = self._ensure_wiki_metadata(html_body, page_id, title, is_front_page=is_front_page, workflow_state=workflow_state)
        file_path = os.path.join(self.wiki_dir, filename)
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(guaranteed_html)
        self.pages_manifest.append((filename, title, page_id))

    def build_quiz(self, quiz_id: str, quiz_title: str, group_id: str, questions: List[Dict[str, Any]], due_iso: Optional[str] = None):
        """Compiles QTI 1.2 XML and Canvas assessment_meta.xml."""
        quiz_meta_id = make_canvas_id(f"meta_{quiz_id}")
        q_dir = os.path.join(self.build_dir, quiz_id)
        os.makedirs(q_dir, exist_ok=True)

        qti_xml_str = build_qti_xml(quiz_id, quiz_title, questions)
        with open(os.path.join(q_dir, "assessment_qti.xml"), "w", encoding="utf-8") as qf:
            qf.write(qti_xml_str)

        meta_xml_str = build_assessment_meta_xml(
            quiz_id, quiz_title, group_id,
            due_at=due_iso, lock_at=due_iso
        )
        with open(os.path.join(q_dir, "assessment_meta.xml"), "w", encoding="utf-8") as mf:
            mf.write(meta_xml_str)

        with open(os.path.join(self.non_cc_dir, f"{quiz_id}.xml.qti"), "w", encoding="utf-8") as ncf:
            ncf.write(qti_xml_str)

        self.quiz_manifest.append((quiz_id, quiz_meta_id, quiz_title))

    def add_module(self, mod_id: str, title: str, items: List[Dict[str, Any]]):
        """Adds a module structure with ordered items."""
        self.modules_data.append({
            "id": mod_id,
            "title": title,
            "items": items
        })

    def build_module_meta_and_manifest(self):
        """Generates synchronized module_meta.xml and imsmanifest.xml with deterministic IDs."""
        modules_xml_items = []
        org_items = []

        for pos, mod in enumerate(self.modules_data, 1):
            mod_id = mod["id"]
            mod_title = mod["title"]
            m_items_xml = []
            m_man_items = []

            for i_pos, item in enumerate(mod["items"], 1):
                shared_item_id = make_canvas_id(f"item_{mod_id}_{item['ref']}")
                item_state = item.get("state", "active")
                item_indent = item.get("indent", 0)

                m_items_xml.append(f"""      <item identifier="{shared_item_id}">
        <content_type>{item['type']}</content_type>
        <workflow_state>{item_state}</workflow_state>
        <title>{html.escape(item['title'])}</title>
        <identifierref>{item['ref']}</identifierref>
        <position>{i_pos}</position>
        <new_tab>false</new_tab>
        <indent>{item_indent}</indent>
        <link_settings_json>null</link_settings_json>
      </item>""")

                m_man_items.append(f"""          <item identifier="{shared_item_id}" identifierref="{item['ref']}">
            <title>{html.escape(item['title'])}</title>
          </item>""")

            items_joined = "\n".join(m_items_xml)
            modules_xml_items.append(f"""  <module identifier="{mod_id}">
    <title>{html.escape(mod_title)}</title>
    <workflow_state>active</workflow_state>
    <position>{pos}</position>
    <items>
{items_joined}
    </items>
  </module>""")

            man_items_joined = "\n".join(m_man_items)
            org_items.append(f"""        <item identifier="{mod_id}">
          <title>{html.escape(mod_title)}</title>
{man_items_joined}
        </item>""")

        mod_meta_xml = f"""<?xml version="1.0" encoding="UTF-8"?>
<modules xmlns="http://canvas.instructure.com/xsd/cccv1p0" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:schemaLocation="http://canvas.instructure.com/xsd/cccv1p0 https://canvas.instructure.com/xsd/cccv1p0.xsd">
{chr(10).join(modules_xml_items)}
</modules>
"""
        with open(os.path.join(self.settings_dir, "module_meta.xml"), "w", encoding="utf-8") as f:
            f.write(mod_meta_xml)

        # Build imsmanifest.xml resources
        resources_xml = []
        
        # 1. Primary Canvas Native Course Settings & Sentinel Resource (CRITICAL for Canvas native import)
        if os.path.exists(os.path.join(self.settings_dir, "syllabus.html")):
            resources_xml.append(f"""    <resource identifier="{self.course_id}_syllabus" type="associatedcontent/imscc_xmlv1p1/learning-application-resource" href="course_settings/syllabus.html" intendeduse="syllabus">
      <file href="course_settings/syllabus.html"/>
    </resource>""")
        resources_xml.append(f"""    <resource identifier="{self.course_id}" type="associatedcontent/imscc_xmlv1p1/learning-application-resource" href="course_settings/canvas_export.txt">
      <file href="course_settings/course_settings.xml"/>
      <file href="course_settings/module_meta.xml"/>
      <file href="course_settings/assignment_groups.xml"/>
      <file href="course_settings/context.xml"/>
      <file href="course_settings/canvas_export.txt"/>
      <file href="course_settings/files_meta.xml"/>
    </resource>""")

        for filename, title, page_id in self.pages_manifest:
            resources_xml.append(f"""    <resource identifier="{page_id}" type="webcontent" href="wiki_content/{filename}">
      <file href="wiki_content/{filename}"/>
    </resource>""")

        for assign_id, html_name, assign_title in self.assignment_manifest:
            resources_xml.append(f"""    <resource identifier="{assign_id}" type="associatedcontent/imscc_xmlv1p1/learning-application-resource" href="{assign_id}/{assign_id}.html">
      <file href="{assign_id}/{assign_id}.html"/>
      <file href="{assign_id}/assignment_settings.xml"/>
    </resource>""")

        for quiz_id, quiz_meta_id, quiz_title in self.quiz_manifest:
            resources_xml.append(f"""    <resource identifier="{quiz_id}" type="imsqti_xmlv1p2/imscc_xmlv1p1/assessment">
      <file href="{quiz_id}/assessment_qti.xml"/>
      <dependency identifierref="{quiz_meta_id}"/>
    </resource>
    <resource identifier="{quiz_meta_id}" type="associatedcontent/imscc_xmlv1p1/learning-application-resource" href="{quiz_id}/assessment_meta.xml">
      <file href="{quiz_id}/assessment_meta.xml"/>
      <file href="non_cc_assessments/{quiz_id}.xml.qti"/>
    </resource>""")

        # Add syllabi & web resources
        for root, _, files in os.walk(self.web_res_dir):
            for file in files:
                rel_path = os.path.relpath(os.path.join(root, file), self.build_dir).replace("\\", "/")
                res_id = make_canvas_id(f"res_{rel_path}")
                resources_xml.append(f"""    <resource identifier="{res_id}" type="webcontent" href="{rel_path}">
      <file href="{rel_path}"/>
    </resource>""")

        c_code = self.config.get("course_code", "COURSE 1010")
        c_title = self.config.get("course_title", "Sample Course")

        imsmanifest_xml = f"""<?xml version="1.0" encoding="UTF-8"?>
<manifest identifier="{make_canvas_id('root_manifest')}" xmlns="http://www.imsglobal.org/xsd/imsccv1p1/imscp_v1p1" xmlns:lom="http://ltsc.ieee.org/xsd/imsccv1p1/LOM/resource" xmlns:lomimscc="http://ltsc.ieee.org/xsd/imsccv1p1/LOM/manifest" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:schemaLocation="http://www.imsglobal.org/xsd/imsccv1p1/imscp_v1p1 http://www.imsglobal.org/profile/cc/ccv1p1/ccv1p1_imscp_v1p2_v1p0.xsd http://ltsc.ieee.org/xsd/imsccv1p1/LOM/resource http://www.imsglobal.org/profile/cc/ccv1p1/LOM/ccv1p1_lomresource_v1p0.xsd http://ltsc.ieee.org/xsd/imsccv1p1/LOM/manifest http://www.imsglobal.org/profile/cc/ccv1p1/LOM/ccv1p1_lommanifest_v1p0.xsd">
  <metadata>
    <schema>IMS Common Cartridge</schema>
    <schemaversion>1.1.0</schemaversion>
    <lomimscc:lom>
      <lomimscc:general>
        <lomimscc:title>
          <lomimscc:string>{html.escape(c_code)}: {html.escape(c_title)}</lomimscc:string>
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
        with open(os.path.join(self.build_dir, "imsmanifest.xml"), "w", encoding="utf-8") as f:
            f.write(imsmanifest_xml)

    def validate_xml_files(self) -> int:
        """Parses all generated XML files with ElementTree to verify zero syntax errors."""
        count = 0
        for root, _, files in os.walk(self.build_dir):
            for file in files:
                if file.endswith(".xml") or file.endswith(".qti"):
                    path = os.path.join(root, file)
                    try:
                        ET.parse(path)
                        count += 1
                    except ET.ParseError as e:
                        raise ValueError(f"XML Validation Failed on {path}: {e}")
        return count

    def package_imscc(self) -> int:
        """Compresses build directory into .imscc Common Cartridge package."""
        if os.path.exists(self.output_imscc):
            backup_dir = os.path.join(os.path.dirname(self.output_imscc), "archive", "cartridge_backups")
            os.makedirs(backup_dir, exist_ok=True)
            mtime = os.path.getmtime(self.output_imscc)
            mtime_str = datetime.datetime.fromtimestamp(mtime).strftime("%Y-%m-%d_%H%M%S")
            base_name = os.path.splitext(os.path.basename(self.output_imscc))[0]
            backup_path = os.path.join(backup_dir, f"{base_name}_{mtime_str}.imscc")
            if not os.path.exists(backup_path):
                shutil.copy2(self.output_imscc, backup_path)
                print(f"[Backup] Preserved previous cartridge to: {backup_path}")
            os.remove(self.output_imscc)

        file_count = 0
        with zipfile.ZipFile(self.output_imscc, "w", zipfile.ZIP_DEFLATED) as z:
            for root, _, files in os.walk(self.build_dir):
                for file in files:
                    full_path = os.path.join(root, file)
                    rel_path = os.path.relpath(full_path, self.build_dir)
                    z.write(full_path, rel_path)
                    file_count += 1
        return file_count


if __name__ == "__main__":
    print("CanvasCourseBuilder portable package module ready.")
