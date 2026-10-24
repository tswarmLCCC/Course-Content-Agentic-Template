# Canvas Common Cartridge Architecture & XML Standards

This document specifies the technical requirements and quirks of Canvas LMS Common Cartridge (`.imscc`) packages to ensure successful automated import without manual intervention.

---

## 1. Deterministic Identifiers (`make_canvas_id`)

Canvas expects 32-character hex identifiers starting with a letter (typically `g`):
```python
def make_canvas_id(seed: str) -> str:
    return "g" + hashlib.md5(seed.encode("utf-8")).hexdigest()[1:]
```
- **Crucial Rule:** The exact same ID must be referenced across `imsmanifest.xml`, `module_meta.xml`, and the file/directory name.
- Deterministic hashing guarantees idempotency across rebuilds.

---

## 2. Cartridge Directory Tree

```text
cartridge_root/
├── imsmanifest.xml                       # Master manifest of all resources & items
├── course_settings/
│   ├── course_settings.xml              # Course title, code, grading standard
│   ├── assignment_groups.xml            # Weighted assignment groups
│   ├── module_meta.xml                  # Canvas module item sequencing & indentation
│   ├── syllabus.html                    # Native syllabus page content
│   ├── context.xml                      # Account & institution metadata
│   ├── canvas_export.txt                # Canvas export signature ("panda" text)
│   └── files_meta.xml                   # File metadata
├── wiki_content/
│   ├── home-page.html
│   ├── start-here.html
│   └── unit-01-overview.html
├── [assign_id]/                         # One folder per native assignment
│   ├── assignment_settings.xml          # Points, submission types, extensions, rubric
│   └── [assign_id].html                 # Assignment description & instructions
├── [quiz_id]/                           # One folder per QTI assessment
│   ├── assessment_qti.xml               # Standard QTI 1.2 XML
│   └── assessment_meta.xml              # Canvas quiz settings (attempts, points, due date)
├── non_cc_assessments/
│   └── [quiz_id].xml.qti                # Duplicate QTI XML required by Canvas engine
└── web_resources/
    ├── syllabi/
    │   └── Master_Syllabus.docx         # Institutional Word document syllabus
    └── images/
        ├── course_banner.jpg
        └── course_thumbnail.jpg
```

---

## 3. Module Items Synchronization

Canvas determines module structure from two linked files:
1. `course_settings/module_meta.xml`:
   Specifies module title, workflow state, and child `<item>` tags with:
   - `<content_type>`: `WikiPage`, `Assignment`, `Quizzes::Quiz`, `DiscussionTopic`, or `ContextExternalTool`.
   - `<workflow_state>`: `active` (published) or `unpublished` (draft/instructor only).
   - `<indent>`: `0` (main header), `1` (sub-item), `2` (nested).
   - `<identifierref>`: Points to the resource ID in `imsmanifest.xml`.
2. `imsmanifest.xml`:
   Under `<organizations><organization>`, mirrors the module hierarchy using `<item identifier="..." identifierref="...">`.

---

## 4. Native Assignment Descriptors (`assignment_settings.xml`)

Controls Canvas SpeedGrader settings:
```xml
<assignment identifier="g1234567890abcdef1234567890abcdef" xmlns="http://canvas.instructure.com/xsd/cccv1p0">
  <title>Unit 1 Applied Lab Assignment</title>
  <assignment_group_identifierref>g_group_labs_id</assignment_group_identifierref>
  <workflow_state>published</workflow_state>
  <allowed_extensions>sql,txt,pdf</allowed_extensions>
  <points_possible>50.0</points_possible>
  <grading_type>points</grading_type>
  <submission_types>online_text_entry,online_upload</submission_types>
</assignment>
```

---

## 5. QTI 1.2 Quiz Profile for Canvas

Canvas imports multiple-choice questions cleanly when formatted under the `cc.multiple_response.v0p1` profile with single correct answers:
- Prompt wrapped in `<mattext texttype="text/html">&lt;div&gt;Prompt...&lt;/div&gt;</mattext>`.
- Choices wrapped in `<response_label>` with `<varequal>` scoring conditions.
- Maximum attempts and scoring policy set in `assessment_meta.xml`:
  ```xml
  <allowed_attempts>3</allowed_attempts>
  <scoring_policy>keep_highest</scoring_policy>
  <quiz_type>assignment</quiz_type>
  ```
- **Dual Placement Requirement:** The QTI XML must be written to **both** `[quiz_id]/assessment_qti.xml` and `non_cc_assessments/[quiz_id].xml.qti`.

---

## 6. Compression & Packaging

The final `.imscc` file is a standard ZIP archive compressed with `ZIP_DEFLATED`.
File extensions: `.imscc` (Common Cartridge).
All XML files inside must pass standard XML parser validation (`xml.etree.ElementTree.parse`).
