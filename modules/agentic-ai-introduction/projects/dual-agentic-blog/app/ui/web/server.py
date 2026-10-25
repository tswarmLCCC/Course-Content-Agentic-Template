"""Lightweight FastAPI server powering the local web dashboard."""

import json
import asyncio
import queue
import threading
from typing import Optional
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse, StreamingResponse
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

from ...config import AppConfig
from ...providers.mock_provider import MockProvider
from ...providers.ollama_provider import OllamaProvider
from ...providers.google_provider import GoogleProvider
from ...coordinator import PipelineCoordinator
from ...schemas import AgentTraceStep, PipelineRunState


class RunRequest(BaseModel):
    topic: str
    provider: str = "mock"
    model: Optional[str] = None
    max_iterations: int = 3


def get_html_content() -> str:
    """Returns the standalone HTML/CSS/JS dashboard UI."""
    return """<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Dual-Backend Multi-Agent Web Dashboard (ADK Equivalent)</title>
  <style>
    :root {
      --bg: #0f172a;
      --card-bg: #1e293b;
      --border: #334155;
      --text: #f8fafc;
      --text-muted: #94a3b8;
      --accent: #38bdf8;
      --green: #22c55e;
      --red: #ef4444;
      --yellow: #f59e0b;
      --purple: #a855f7;
    }
    * { box-sizing: border-box; margin: 0; padding: 0; }
    body {
      font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif;
      background: var(--bg);
      color: var(--text);
      line-height: 1.5;
      padding: 1.5rem;
    }
    header {
      display: flex;
      justify-content: space-between;
      align-items: center;
      padding-bottom: 1.5rem;
      border-bottom: 1px solid var(--border);
      margin-bottom: 1.5rem;
    }
    .badge {
      display: inline-block;
      padding: 0.25rem 0.6rem;
      border-radius: 9999px;
      font-size: 0.8rem;
      font-weight: 600;
      background: #0369a1;
      color: #e0f2fe;
    }
    .grid {
      display: grid;
      grid-template-columns: 340px 1fr;
      gap: 1.5rem;
    }
    .card {
      background: var(--card-bg);
      border: 1px solid var(--border);
      border-radius: 0.75rem;
      padding: 1.25rem;
      margin-bottom: 1.5rem;
    }
    h2 { font-size: 1.1rem; margin-bottom: 1rem; color: var(--accent); }
    label { display: block; font-size: 0.85rem; color: var(--text-muted); margin-bottom: 0.25rem; }
    input, select, button {
      width: 100%;
      padding: 0.6rem;
      margin-bottom: 0.8rem;
      border-radius: 0.5rem;
      border: 1px solid var(--border);
      background: #0f172a;
      color: var(--text);
      font-size: 0.9rem;
    }
    button {
      background: #0284c7;
      color: white;
      font-weight: 600;
      cursor: pointer;
      border: none;
      transition: background 0.2s;
    }
    button:hover { background: #0369a1; }
    button:disabled { opacity: 0.5; cursor: not-allowed; }

    /* Visual Graph Pipeline */
    .pipeline-graph {
      display: flex;
      justify-content: space-between;
      align-items: center;
      background: #0f172a;
      padding: 1rem;
      border-radius: 0.5rem;
      margin-bottom: 1.25rem;
      border: 1px solid var(--border);
    }
    .graph-node {
      padding: 0.6rem 1rem;
      border-radius: 0.5rem;
      background: #1e293b;
      border: 2px solid var(--border);
      font-weight: 600;
      font-size: 0.85rem;
      text-align: center;
      transition: all 0.3s;
    }
    .graph-node.active {
      border-color: var(--accent);
      box-shadow: 0 0 12px rgba(56, 189, 248, 0.4);
      transform: scale(1.05);
    }
    .graph-node.passed { border-color: var(--green); color: var(--green); }
    .graph-node.retry { border-color: var(--yellow); color: var(--yellow); }
    .graph-arrow { color: var(--text-muted); font-size: 1.2rem; }

    /* Traces Feed */
    .trace-list {
      max-height: 280px;
      overflow-y: auto;
      font-family: monospace;
      font-size: 0.82rem;
      background: #090d16;
      padding: 0.75rem;
      border-radius: 0.5rem;
    }
    .trace-item {
      padding: 0.35rem 0;
      border-bottom: 1px solid rgba(255, 255, 255, 0.05);
    }
    .trace-item .agent { font-weight: bold; }
    .trace-item .agent.PlannerAgent { color: var(--accent); }
    .trace-item .agent.WriterAgent { color: var(--yellow); }
    .trace-item .agent.ValidatorAgent { color: var(--purple); }

    /* Diff & Output */
    pre {
      background: #090d16;
      padding: 1rem;
      border-radius: 0.5rem;
      overflow-x: auto;
      font-size: 0.85rem;
      white-space: pre-wrap;
      max-height: 400px;
    }
    .tabs {
      display: flex;
      gap: 0.5rem;
      margin-bottom: 0.75rem;
    }
    .tab-btn {
      width: auto;
      padding: 0.4rem 0.8rem;
      background: #1e293b;
      border: 1px solid var(--border);
      color: var(--text-muted);
      border-radius: 0.35rem;
      font-size: 0.85rem;
    }
    .tab-btn.active {
      background: #0284c7;
      color: white;
      border-color: #0284c7;
    }
  </style>
</head>
<body>
  <header>
    <div>
      <h1>Multi-Agent Blog Pipeline</h1>
      <p style="color: var(--text-muted); font-size: 0.9rem;">
        Google ADK Equivalent &bull; ReAct Loops &bull; Evaluator-Optimizer
      </p>
    </div>
    <div style="display: flex; gap: 0.5rem; align-items: center;">
      <span class="badge" id="providerBadge">MOCK BACKEND</span>
      <span id="runStatus" style="font-weight: 600; font-size: 0.85rem; color: var(--green);">READY</span>
    </div>
  </header>

  <div class="grid">
    <!-- Controls Column -->
    <div>
      <div class="card">
        <h2>Pipeline Controls</h2>
        <label for="topicInput">Blog Post Topic</label>
        <input type="text" id="topicInput" value="Modern Vector Search & RAG Architectures">

        <label for="providerSelect">Execution Backend</label>
        <select id="providerSelect" onchange="updateProviderOptions()">
          <option value="mock" selected>Mock Simulation (Zero-Cost & Offline)</option>
          <option value="ollama">Ollama Local (llama3.1 / qwen2.5)</option>
          <option value="google">Google Cloud (Gemini 1.5 Flash)</option>
        </select>

        <label for="modelInput">Model Name</label>
        <input type="text" id="modelInput" value="mock-agent-v1">

        <label for="maxIterInput">Max Iteration Budget</label>
        <input type="number" id="maxIterInput" value="3" min="1" max="5">

        <button id="runBtn" onclick="startExecution()">Run Multi-Agent Pipeline</button>
      </div>

      <div class="card">
        <h2>Live Execution Traces</h2>
        <div class="trace-list" id="traceFeed">
          <div style="color: var(--text-muted);">Awaiting pipeline execution...</div>
        </div>
      </div>
    </div>

    <!-- Visualization Column -->
    <div>
      <div class="card">
        <h2>Agent Execution Graph (Evaluator-Optimizer)</h2>
        <div class="pipeline-graph">
          <div class="graph-node" id="nodePlanner">1. Planner Agent</div>
          <div class="graph-arrow">&rarr;</div>
          <div class="graph-node" id="nodeWriter">2. Writer Agent</div>
          <div class="graph-arrow">&rarr;</div>
          <div class="graph-node" id="nodeValidator">3. Validator Agent</div>
          <div class="graph-arrow">&#8644;</div>
          <div class="graph-node" id="nodeRetry">Loop / Gate</div>
          <div class="graph-arrow">&rarr;</div>
          <div class="graph-node" id="nodePublished">Published</div>
        </div>
      </div>

      <div class="card">
        <div class="tabs">
          <button class="tab-btn active" onclick="switchTab('article')">Published Article</button>
          <button class="tab-btn" onclick="switchTab('diff')">Self-Correction Diff</button>
          <button class="tab-btn" onclick="switchTab('plan')">Strategic Plan</button>
        </div>

        <div id="tabArticle">
          <pre id="articleContent">The final article will appear here once all validation gates pass.</pre>
        </div>

        <div id="tabDiff" style="display: none;">
          <pre id="diffContent">Side-by-side revision differences will appear here if the Validator triggers retries.</pre>
        </div>

        <div id="tabPlan" style="display: none;">
          <pre id="planContent">Structured JSON plan generated by the Planner Agent will appear here.</pre>
        </div>
      </div>
    </div>
  </div>

  <script>
    let activeDrafts = [];
    let activePlan = null;

    function updateProviderOptions() {
      const p = document.getElementById("providerSelect").value;
      const m = document.getElementById("modelInput");
      const b = document.getElementById("providerBadge");
      if (p === "mock") {
        m.value = "mock-agent-v1";
        b.innerText = "MOCK SIMULATION";
      } else if (p === "ollama") {
        m.value = "llama3.1:8b";
        b.innerText = "LOCAL OLLAMA";
      } else if (p === "google") {
        m.value = "gemini-1.5-flash";
        b.innerText = "GOOGLE GEMINI";
      }
    }

    function switchTab(name) {
      document.querySelectorAll(".tab-btn").forEach(b => b.classList.remove("active"));
      document.getElementById("tabArticle").style.display = name === "article" ? "block" : "none";
      document.getElementById("tabDiff").style.display = name === "diff" ? "block" : "none";
      document.getElementById("tabPlan").style.display = name === "plan" ? "block" : "none";
      event.target.classList.add("active");
    }

    function resetNodes() {
      ['nodePlanner', 'nodeWriter', 'nodeValidator', 'nodeRetry', 'nodePublished'].forEach(id => {
        const el = document.getElementById(id);
        el.className = 'graph-node';
      });
    }

    async function startExecution() {
      const btn = document.getElementById("runBtn");
      const statusEl = document.getElementById("runStatus");
      const feed = document.getElementById("traceFeed");
      btn.disabled = true;
      statusEl.innerText = "RUNNING";
      statusEl.style.color = "var(--yellow)";
      feed.innerHTML = "";
      resetNodes();
      activeDrafts = [];

      const payload = {
        topic: document.getElementById("topicInput").value,
        provider: document.getElementById("providerSelect").value,
        model: document.getElementById("modelInput").value,
        max_iterations: parseInt(document.getElementById("maxIterInput").value)
      };

      try {
        const res = await fetch("/api/run", {
          method: "POST",
          headers: { "Content-Type": "application/json" },
          body: JSON.stringify(payload)
        });
        const data = await res.json();

        // Render traces
        feed.innerHTML = "";
        data.trace_steps.forEach(s => {
          const div = document.createElement("div");
          div.className = "trace-item";
          div.innerHTML = `<span class="agent ${s.agent_name}">[${s.agent_name}]</span> (${s.phase} &bull; ${s.latency_ms}ms)<br>&rarr; ${s.content_snippet}`;
          feed.appendChild(div);
        });

        // Set node statuses
        document.getElementById("nodePlanner").classList.add("passed");
        document.getElementById("nodeWriter").classList.add("passed");
        document.getElementById("nodeValidator").classList.add("passed");
        if (data.total_iterations > 1) {
          document.getElementById("nodeRetry").classList.add("retry");
        }
        document.getElementById("nodePublished").classList.add(data.final_status === "PASSED" ? "passed" : "retry");

        // Display results
        document.getElementById("articleContent").innerText = data.current_draft;
        document.getElementById("planContent").innerText = JSON.stringify(data.plan, null, 2);

        if (data.draft_history.length > 1) {
          document.getElementById("diffContent").innerText =
            `=== DRAFT ITERATION 1 (${data.draft_history[0].split(/\\s+/).length} words) ===\\n\\n` +
            data.draft_history[0] +
            `\\n\\n==============================================\\n` +
            `=== REVISED DRAFT ITERATION 2 (${data.draft_history[1].split(/\\s+/).length} words) ===\\n\\n` +
            data.draft_history[1];
        } else {
          document.getElementById("diffContent").innerText = "No retries needed. Draft passed on iteration 1!";
        }

        statusEl.innerText = data.final_status;
        statusEl.style.color = data.final_status === "PASSED" ? "var(--green)" : "var(--red)";
      } catch (err) {
        statusEl.innerText = "ERROR";
        statusEl.style.color = "var(--red)";
        feed.innerHTML += `<div style="color: var(--red);">Error: ${err.message}</div>`;
      } finally {
        btn.disabled = false;
      }
    }
  </script>
</body>
</html>"""


def create_app() -> FastAPI:
    """Instantiates and configures the FastAPI application."""
    app = FastAPI(title="Dual-Agentic-Blog Dashboard", version="0.1.0")

    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    @app.get("/", response_class=HTMLResponse)
    def index():
        return get_html_content()

    @app.post("/api/run")
    def run_pipeline(req: RunRequest):
        config = AppConfig(
            provider=req.provider,
            model=req.model or ("llama3.1:8b" if req.provider == "ollama" else ("gemini-1.5-flash" if req.provider == "google" else "mock-agent-v1")),
            max_iterations=req.max_iterations,
        )

        if req.provider == "mock":
            provider = MockProvider(model_name=config.model)
        elif req.provider == "ollama":
            provider = OllamaProvider(model_name=config.model, host=config.ollama_host)
        elif req.provider == "google":
            provider = GoogleProvider(model_name=config.model, api_key=config.gemini_api_key)
        else:
            raise ValueError(f"Unknown provider: {req.provider}")

        coordinator = PipelineCoordinator(config=config, provider=provider)
        state = coordinator.run(topic=req.topic)
        return state.model_dump()

    return app
