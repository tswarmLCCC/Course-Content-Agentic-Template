---
name: syllabus-docx-cloner
description: >-
  Clones and transforms institutional Microsoft Word (.docx) syllabus documents
  preserving 100% style fidelity, customXml schemas, table borders, and college formatting.
---

# Institutional Syllabus Word Document Cloner Skill

This skill allows agents to produce institutional `.docx` syllabi that pass strict college accreditation reviews by cloning approved master templates.

## Workflow
1. **Template Source:** Uses `templates/syllabi/LCCC_Master_Syllabus_Template.docx`.
2. **ZIP Deconstruction:** Unpacks `word/document.xml` from the `.docx` archive.
3. **Regex / XML Transformation:** Updates course prefix (`CMAP 1815`), title, credit hours, prerequisites, textbook policies, module schedule, and grading breakdowns without disturbing Word XML namespaces or styles.
4. **Repackaging:** Re-archives the XML payload into the production `.docx` container.
5. **Canvas Deployment:** Places the document into `web_resources/syllabi/` and links it in Canvas LMS.
