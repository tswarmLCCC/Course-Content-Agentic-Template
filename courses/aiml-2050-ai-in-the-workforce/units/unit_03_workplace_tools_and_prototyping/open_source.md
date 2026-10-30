# Unit 03: Open-Source Guide — Streamlit & Gradio Rapid Agent Prototyping

> **Course**: AIML 2050 — AI in the Workforce  
> **Toolchain**: Streamlit, Gradio, SQLite3, Python 3.10+  
> **Cost**: $0.00 (Zero-cost local infrastructure)

---

## 1. Overview
This guide provides complete, production-ready starter templates for building interactive workplace AI prototypes using **Streamlit** and Python's built-in **sqlite3** engine.

---

## 2. Installation Commands

In your active virtual environment (`aiml_env`), install the prototyping packages:
```powershell
pip install streamlit gradio pandas requests
```

---

## 3. Complete Working Prototype: Streamlit + SQLite Database

Save the following code as `app.py`:

```python
import streamlit as st
import sqlite3
import datetime
import os

# 1. Initialize Persistent SQLite Database
DB_FILE = "prototype_records.db"

def init_db():
    conn = sqlite3.connect(DB_FILE)
    c = conn.cursor()
    c.execute('''
        CREATE TABLE IF NOT EXISTS interactions (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            timestamp TEXT,
            department TEXT,
            user_prompt TEXT,
            agent_response TEXT,
            rating TEXT
        )
    ''')
    conn.commit()
    conn.close()

def save_interaction(dept, prompt, response):
    conn = sqlite3.connect(DB_FILE)
    c = conn.cursor()
    ts = datetime.datetime.now().isoformat()
    c.execute('''
        INSERT INTO interactions (timestamp, department, user_prompt, agent_response, rating)
        VALUES (?, ?, ?, ?, ?)
    ''', (ts, dept, prompt, response, "Unrated"))
    conn.commit()
    conn.close()

init_db()

# 2. UI Layout
st.set_page_config(page_title="Workforce Assistant Prototype", layout="wide")
st.title("Enterprise Operations Assistant Prototype")
st.markdown("Rapid prototype demonstrating prompt engineering and persistent database logging.")

col1, col2 = st.columns([2, 1])

with col1:
    st.subheader("Interactive Workplace Assistant")
    dept = st.selectbox("Select Target Department", ["Human Resources", "Finance & Accounting", "IT Helpdesk", "Customer Support"])
    user_prompt = st.text_area("Enter your workplace request or query:", height=120)
    
    if st.button("Generate Agent Response"):
        if user_prompt.strip():
            # Mock or Live LLM reasoning logic
            agent_output = f"[MOCK AGENT RESPONSE for {dept}]: Analyzed request '{user_prompt[:40]}...'. Action planned: Triage ticket, verify compliance against SOP-2026, and notify manager."
            st.success("Response Generated!")
            st.markdown(f"**Agent Output:**

{agent_output}")
            
            # Persist to SQLite
            save_interaction(dept, user_prompt, agent_output)
            st.info("Record logged to SQLite database.")
        else:
            st.warning("Please enter a valid request.")

with col2:
    st.subheader("Audit & Telemetry Database")
    conn = sqlite3.connect(DB_FILE)
    import pandas as pd
    df = pd.read_sql_query("SELECT id, timestamp, department, user_prompt FROM interactions ORDER BY id DESC LIMIT 5", conn)
    conn.close()
    st.dataframe(df, use_container_width=True)
```

---

## 4. Running and Verifying the Prototype
Execute:
```powershell
streamlit run app.py
```
Open your browser to `http://localhost:8501`. Enter test prompts, verify that records appear in the live telemetry table, and verify that restarting the server retains the stored records in `prototype_records.db`.
