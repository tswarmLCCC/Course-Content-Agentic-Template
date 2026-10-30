# Unit 08: Open-Source Guide — Local Model Serving with Ollama & OpenVINO on Intel PCs

> **Course**: AIML 2050 — AI in the Workforce  
> **Toolchain**: Ollama, OpenVINO, Python 3.10+, SQLite / FAISS  
> **Cost**: $0.00 (Zero-cost, 100% offline local inference)

---

## 1. Overview
This guide provides the complete setup for running private, sovereign language models locally using **Ollama** and Python with zero cloud API keys and zero internet data transmission.

---

## 2. Installing and Running Ollama
1. Download and install Ollama from https://ollama.com.
2. Pull a lightweight, high-performance quantized model:
```powershell
ollama run llama3.2:1b
```
3. Verify that the local REST server is active on `http://localhost:11434`.

---

## 3. Python Local Sovereign Agent Script

Save as `local_agent.py`:
```python
import requests
import json
import sqlite3

OLLAMA_URL = "http://localhost:11434/api/generate"
MODEL_NAME = "llama3.2:1b"

def query_local_llm(prompt: str, system_prompt: str = "") -> str:
    # Queries local Ollama instance with zero external cloud transmission
    payload = {
        "model": MODEL_NAME,
        "prompt": prompt,
        "system": system_prompt,
        "stream": False,
        "options": {
            "temperature": 0.2
        }
    }
    try:
        response = requests.post(OLLAMA_URL, json=payload, timeout=60)
        response.raise_for_status()
        return response.json().get("response", "").strip()
    except Exception as e:
        return f"Local Inference Error: {e}"

if __name__ == "__main__":
    print(f"[*] Testing sovereign connection to local {MODEL_NAME}...")
    ans = query_local_llm("Explain data sovereignty in two concise sentences.")
    print("
[+] Local Model Output:
", ans)
```

---

## 4. The Standardized SKILL.md Pattern

Save as `SKILL.md`:
```yaml
---
name: sovereign-workforce-assistant
description: Private on-device assistant for processing sensitive workplace documentation with zero cloud leakage.
version: 1.0.0
author: LCCC AI Program
tools:
  - name: local_sqlite_query
    description: Queries local internal database records.
  - name: local_policy_lookup
    description: Performs cosine search over local offline text documents.
governance:
  cloud_transmission_allowed: false
  pii_sanitization_required: true
  max_iterations: 5
---

# Operational Instructions
You are a sovereign enterprise AI assistant operating entirely on local hardware. You have no connection to external cloud APIs. All company data must remain strictly isolated on this device.
```
