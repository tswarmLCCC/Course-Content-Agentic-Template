import os
import glob
import zipfile
import xml.etree.ElementTree as ET
import json

base_ref = r"ref/AIML 1010 Update/New Modules"
folders = sorted([d for d in os.listdir(base_ref) if os.path.isdir(os.path.join(base_ref, d))])

all_quizzes = {}

for folder in folders:
    fpath = os.path.join(base_ref, folder)
    xlsx_files = [f for f in os.listdir(fpath) if f.endswith(".xlsx") and "Quiz" in f]
    if not xlsx_files:
        continue
    xlsx_path = os.path.join(fpath, xlsx_files[0])
    
    # Read xlsx zip
    with zipfile.ZipFile(xlsx_path, 'r') as z:
        # shared strings
        ss_tree = ET.fromstring(z.read("xl/sharedStrings.xml"))
        # namespace
        ns = {'x': 'http://schemas.openxmlformats.org/spreadsheetml/2006/main'}
        strings = []
        for si in ss_tree.findall(".//x:si", ns):
            t_node = si.find("./x:t", ns)
            if t_node is not None and t_node.text:
                strings.append(t_node.text)
            else:
                r_texts = [r.text for r in si.findall(".//x:t", ns) if r.text]
                strings.append("".join(r_texts))
                
        # sheet1
        sheet_tree = ET.fromstring(z.read("xl/worksheets/sheet1.xml"))
        rows = sheet_tree.findall(".//x:row", ns)
        
        parsed_rows = []
        for r in rows:
            row_data = {}
            for c in r.findall("./x:c", ns):
                cell_ref = c.attrib.get('r', '')
                col = ''.join([ch for ch in cell_ref if ch.isalpha()])
                t_attr = c.attrib.get('t', '')
                v_node = c.find("./x:v", ns)
                if v_node is not None and v_node.text is not None:
                    raw_val = v_node.text
                    if t_attr == 's':
                        idx = int(raw_val)
                        val = strings[idx] if idx < len(strings) else raw_val
                    else:
                        val = raw_val
                    row_data[col] = val
            if row_data:
                parsed_rows.append(row_data)
                
    all_quizzes[folder] = {
        "file": xlsx_files[0],
        "rows": parsed_rows
    }

print(f"Extracted {len(all_quizzes)} quizzes.")
with open("modules/aiml-1010-generative-ai-update/scripts/raw_quizzes.json", "w", encoding="utf-8") as f:
    json.dump(all_quizzes, f, indent=2)

for name, q in all_quizzes.items():
    print(f"\n--- {name} ({len(q['rows'])} rows) ---")
    for r in q['rows'][:3]:
        print("  ", list(r.values()))
