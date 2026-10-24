# Zero-Cost Infrastructure Guide: Teaching High-Tech on a $0.00 Cloud Budget

## The Reality of Educational AI Budgets

The single greatest barrier to launching modern AI, data science, and agentic engineering courses in secondary, post-secondary, and vocational classrooms is **cloud computing cost and billing friction**.

Traditional cloud AI tutorials assume every student can enter a personal credit card for OpenAI, Anthropic, or AWS Bedrock APIs. In real-world educational institutions:
1. **Minors cannot enter credit cards.**
2. **Institutions take months to approve vendor POs and cloud billing accounts.**
3. **Unexpected billing spikes** (e.g., infinite loops in student agent while loops) can drain thousands of dollars overnight.
4. **Campus Wi-Fi firewall restrictions** frequently block live external WebSockets or streaming API connections.

This guide provides a tested blueprint for running hands-on, enterprise-grade AI courses with **exactly $0.00 in cloud bills**, zero credit card requirements, and zero risk of unexpected financial liability.

---

## The Three Pillars of Free Classroom Infrastructure

```
                      +---------------------------------------+
                      |   ZERO-COST CLASSROOM ARCHITECTURE    |
                      +---------------------------------------+
                                          |
        +---------------------------------+---------------------------------+
        |                                 |                                 |
        v                                 v                                 v
+-----------------------+     +-----------------------+     +-----------------------+
|  1. SOVEREIGN LOCAL   |     |  2. ZERO-CARD CLOUD   |     |  3. DETERMINISTIC CI  |
|       COMPUTE         |     |       FREE TIERS      |     |     & MOCK RUNNERS    |
+-----------------------+     +-----------------------+     +-----------------------+
| - Ollama / llama.cpp  |     | - Google AI Studio    |     | - Standard Lib Mock   |
| - Qwen2.5-Coder       |     |   (Gemini 1.5/2.0)    |     | - Golden JSON fixtures|
| - Llama 3.2 / Phi-3.5 |     | - GroqCloud LPUs      |     | - Offline grading     |
| - Air-gapped / No Net |     | - No credit card req  |     | - 100% test reliability|
+-----------------------+     +-----------------------+     +-----------------------+
```

---

## Pillar 1: Sovereign Local Compute (Ollama & llama.cpp)

Local inference provides complete pedagogical sovereignty. Once downloaded to student laptops or classroom lab machines, models run offline without internet connectivity, without rate limits, and without data egress.

### Recommended Educational Models (4-bit / 8-bit Quantized)

| Model Name | VRAM / RAM Req | Target Machine | Best Use Case |
| :--- | :--- | :--- | :--- |
| **Qwen2.5-Coder (1.5B)** | ~1.5 GB RAM | Chromebook / Older Laptop | Fast syntax generation, unit tests |
| **Llama 3.2 (3B)** | ~2.8 GB RAM | Standard MacBook Air / 8GB PC | Reasoning, conversation, tool use |
| **Qwen2.5-Coder (7B)** | ~5.5 GB RAM | 16GB RAM Laptop or M1/M2 Mac | Production-grade code generation |
| **Phi-3.5-mini (3.8B)** | ~3.0 GB RAM | Standard Student Laptop | Logical reasoning, structured JSON |

### Quickstart Setup for Students

1. **Install Ollama** (Windows, macOS, Linux):
   Visit [ollama.com](https://ollama.com) and install the native installer.

2. **Pull Classroom Target Model** (Terminal / Command Prompt):
   ```bash
   ollama pull llama3.2:3b
   ```

3. **Verify Local API**:
   Ollama runs an OpenAI-compatible REST API locally on port `11434`.
   ```bash
   curl http://localhost:11434/api/generate -d '{
     "model": "llama3.2:3b",
     "prompt": "Explain recursion in one sentence.",
     "stream": false
   }'
   ```

4. **Python Integration (Zero External SDKs Required)**:
   ```python
   import json
   import urllib.request

   def call_local_llm(prompt: str, model: str = "llama3.2:3b") -> str:
       url = "http://localhost:11434/api/generate"
       payload = json.dumps({"model": model, "prompt": prompt, "stream": False}).encode("utf-8")
       req = urllib.request.Request(url, data=payload, headers={"Content-Type": "application/json"})
       with urllib.request.urlopen(req) as resp:
           data = json.loads(resp.read().decode("utf-8"))
           return data.get("response", "")
   ```

---

## Pillar 2: Zero-Card Cloud Free Tiers

When local hardware is insufficient (e.g., student Chromebooks or tablets without local terminal access), use cloud providers that offer **free developer tiers without requiring a credit card**.

### 1. Google AI Studio (Gemini 1.5 Flash / Gemini 2.0 Flash)
- **Free Limit**: Up to 15 Requests Per Minute (RPM), 1,500 Requests Per Day (RPD), and 1,000,000 Tokens Per Minute (TPM).
- **Billing Requirements**: Absolutely **NO credit card required**. Log in with any Google account (personal or educational Google Workspace).
- **Best Use Case**: Long-context reasoning (up to 1M context window), document analysis, multi-turn dialogue, structured JSON output.

### 2. GroqCloud (Ultra-Fast LPUs)
- **Free Limit**: Generous token-per-minute limits across open models (Llama 3.3 70B, Llama 3.1 8B, Gemma 2 9B).
- **Billing Requirements**: **NO credit card required** for initial developer tier.
- **Speed**: 300 to 800 tokens per second, making real-time tool loops feel instantaneous for students.

### Unified Free-Tier Python Adapter

Students configure an `.env` file with whatever key they have, and the codebase adapts automatically:

```python
import os
import json
import urllib.request

def call_frontier_free(prompt: str) -> str:
    """
    Tries Google AI Studio or GroqCloud depending on environment variables.
    Falls back to local Ollama if no cloud keys are provided.
    """
    gemini_key = os.getenv("GEMINI_API_KEY")
    groq_key = os.getenv("GROQ_API_KEY")

    if groq_key:
        url = "https://api.groq.com/openai/v1/chat/completions"
        payload = json.dumps({
            "model": "llama-3.1-8b-instant",
            "messages": [{"role": "user", "content": prompt}],
            "temperature": 0.2
        }).encode("utf-8")
        headers = {
            "Authorization": f"Bearer {groq_key}",
            "Content-Type": "application/json"
        }
        req = urllib.request.Request(url, data=payload, headers=headers)
        with urllib.request.urlopen(req) as resp:
            data = json.loads(resp.read().decode("utf-8"))
            return data["choices"][0]["message"]["content"]

    elif gemini_key:
        url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash:generateContent?key={gemini_key}"
        payload = json.dumps({
            "contents": [{"parts": [{"text": prompt}]}]
        }).encode("utf-8")
        headers = {"Content-Type": "application/json"}
        req = urllib.request.Request(url, data=payload, headers=headers)
        with urllib.request.urlopen(req) as resp:
            data = json.loads(resp.read().decode("utf-8"))
            return data["candidates"][0]["content"]["parts"][0]["text"]

    else:
        # Fallback to local Ollama
        return call_local_llm(prompt)
```

---

## Pillar 3: Deterministic CI & Mock Runners (Grading at Scale)

In automated grading environments (such as GitHub Actions grading student lab submissions), calling live LLM APIs is an anti-pattern:
1. **Flakiness**: Network timeouts or rate limits cause false-negative grading failures.
2. **Cost & Secrets Exposure**: Pushing instructor API keys into automated PR runs exposes keys to extraction.
3. **Non-Determinism**: Slight differences in LLM token completions make strict assertion testing fragile.

### The Educational Solution: Golden JSON Fixtures

Require students to separate **prompt construction and output parsing** from the actual network call:

```python
# Lab implementation: student decouples parsing logic
class SentimentAgent:
    def __init__(self, llm_callable):
        self.llm = llm_callable

    def analyze(self, text: str) -> dict:
        prompt = f"Analyze sentiment of: '{text}'. Respond with JSON: {{\"label\": \"POS\"|\"NEG\", \"score\": 0.0-1.0}}"
        raw_output = self.llm(prompt)
        # Robust parsing handles code fences
        clean_json = raw_output.replace("```json", "").replace("```", "").strip()
        return json.loads(clean_json)

# In Student Lab Tests / GitHub CI (100% Offline, $0.00):
def test_sentiment_agent_parsing():
    mock_llm = lambda prompt: '{"label": "POS", "score": 0.98}'
    agent = SentimentAgent(mock_llm)
    result = agent.analyze("Great product!")
    assert result["label"] == "POS"
    assert result["score"] == 0.98
```

---

## The Golden Rule of Classroom Live Demos

> **Never tie a live student grade or classroom demonstration solely to live network calls during an exam or presentation.**

Always require students to implement the **Three-Tier Demo Contingency Plan** (provided in `templates/demo_contingency_runbook_template.md`):
1. **Tier 1 (Live Primary)**: Live inference call to cloud or local LLM.
2. **Tier 2 (Sovereign Local Fallback)**: One-click toggle to local 3B model if campus Wi-Fi drops.
3. **Tier 3 (Cached Golden Fixture)**: Offline pre-recorded JSON responses or synthetic outputs if the GPU/CPU crashes.
