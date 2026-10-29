#!/usr/bin/env python3
"""
Author Canvas Native Assignments for AIML 1010 Update
Translates the hands-on student lab decks into complete Canvas assignments with rubric tables.
"""

import os
import json
import html

ASSIGNMENTS = {
    "module_01_agentic_ai": {
        "title": "Module 01 Applied Lab: Exploring the Rise of Agentic AI",
        "points": 50.0,
        "allowed_ext": "pdf,docx",
        "objective": "Explore and evaluate the emergence of Agentic AI and its impact on modern workplace workflows through hands-on interaction with frontier AI tools.",
        "tasks": [
            ("Step 1: Initial Discovery with Google Gemini", "Navigate to Google Gemini (https://gemini.google.com). Select a real-world enterprise domain (e.g., project management, automated logistics, or software testing). Prompt Gemini to generate a comprehensive briefing analyzing how autonomous agents are transforming workflows in this sector. Export the resulting findings to a document."),
            ("Step 2: Knowledge Extraction in NotebookLM", "Navigate to Google NotebookLM (https://notebooklm.google). Create a new notebook and upload the briefing generated in Step 1. Prompt NotebookLM to extract 3-5 key findings regarding workflow changes, autonomous tool use, and emerging human-in-the-loop roles. Identify 2 specific points requiring deeper verification."),
            ("Step 3: Deep Research Verification", "Using ChatGPT, Perplexity (https://www.perplexity.ai), or Gemini Advanced, execute a deep research query on the points flagged in Step 2. Gather authoritative citations, real-world corporate case studies, and documented failure modes differentiating agentic systems from traditional workflow scripts."),
            ("Step 4: Synthesis Report", "Write a 2-3 page executive report structured into: (1) Introduction & Domain Overview, (2) Key Workflow Transformations, (3) Critical Reflection on Tool Autonomy vs. Human Oversight, and (4) Verified Resource & Citation List with screenshots.")
        ]
    },
    "week_03_prompt_engineering_i": {
        "title": "Week 03 Applied Lab: Controlled Generation with the RGC Framework",
        "points": 50.0,
        "allowed_ext": "pdf,docx,txt",
        "objective": "Apply the Role-Goal-Context (RGC) framework, delimiters, and few-shot formatting constraints to engineer robust, deterministic outputs from generative language models.",
        "tasks": [
            ("Step 1: Baseline Prompt Formulation", "Draft a baseline, unconstrained prompt for a specific professional task (e.g., extracting action items from meeting notes, draft incident response email, or customer inquiry triage). Run the baseline across 3 distinct queries and record output variance."),
            ("Step 2: Applying the RGC Architecture", "Re-engineer your prompt incorporating explicit Role definition, granular Goal specifications with strict output schema (e.g., Markdown table or JSON), and realistic Context constraints (e.g., tone, word count ceilings, forbidden terminology)."),
            ("Step 3: Few-Shot In-Context Grounding", "Incorporate at least two diverse input-output demonstration pairs into the context window. Test how few-shot conditioning enforces schema adherence and eliminates hallucinated formatting."),
            ("Step 4: Comparative Audit & Submission", "Compile a structured laboratory report showing side-by-side prompt iterations, model outputs, a breakdown of how each RGC component altered model latent steering, and your finalized master prompt template.")
        ]
    },
    "week_04_prompt_engineering_ii": {
        "title": "Week 04 Applied Lab: Sequential Prompt Chaining & Multimodal Storytelling",
        "points": 50.0,
        "allowed_ext": "pdf,docx",
        "objective": "Design and execute a multi-step prompt chain combining logical Chain-of-Thought (CoT) text reasoning with text-to-image synthesis to produce a cohesive narrative arc.",
        "tasks": [
            ("Step 1: Narrative Plot & Scene Decomposition", "Develop an original 4-5 scene narrative concept (e.g., scientific exploration, ancient archaeological expedition, or future climate mitigation). Use Chain-of-Thought prompting to decompose the narrative into sequential visual beats with consistent characters, lighting, and environment parameters."),
            ("Step 2: Text-to-Image Prompt Crafting", "Formulate precise text-to-image prompts for each scene using style tokens, camera framing, lighting descriptors, and negative prompts (using Stable Diffusion, DALL-E, or Midjourney)."),
            ("Step 3: Prompt Chaining & Consistency Management", "Implement prompt chaining: use the descriptive output of scene N to condition visual continuity in scene N+1. Document how you maintained character identity and environment coherence across generations."),
            ("Step 4: Visual Odyssey Portfolio", "Assemble a finalized portfolio including the high-resolution generated visuals, the exact text prompts used for each scene, reflection on prompt drift, and a breakdown of the prompt chaining pipeline.")
        ]
    },
    "week_10_transformers_llm_evolution": {
        "title": "Week 10 Applied Lab: Hugging Face Transformer Pipeline Architecture",
        "points": 50.0,
        "allowed_ext": "ipynb,pdf,py",
        "objective": "Explore the Hugging Face Transformers ecosystem by architecting a multi-modal customer support chatbot pipeline integrating speech recognition, text classification, and autoregressive generation.",
        "tasks": [
            ("Step 1: Model Selection & Taxonomy Mapping", "Survey the Hugging Face Model Hub to identify appropriate models for a three-tier pipeline: (1) Automatic Speech Recognition (ASR, e.g., Whisper), (2) Intent Classification (Encoder-only, e.g., DistilBERT), and (3) Response Generation (Decoder-only, e.g., Llama/Mistral/Qwen)."),
            ("Step 2: Pipeline Implementation in Python", "Write a Python script or Google Colab notebook utilizing `transformers.pipeline` to instantiate the components. Implement tokenization, inference passing, and output formatting."),
            ("Step 3: Pipeline Latency & Attention Analysis", "Benchmark the inference time of each component across 5 sample customer queries. Document how self-attention mechanisms handle varying input sequence lengths."),
            ("Step 4: Notebook Submission", "Submit your commented `.ipynb` notebook (or Python script + execution log PDF) demonstrating end-to-end execution with test outputs, architectural rationale, and compute trade-off analysis.")
        ]
    },
    "week_11_diffusion_models_text_to_image": {
        "title": "Week 11 Applied Lab: Cross-Modal Generative AI & Image Synthesis",
        "points": 50.0,
        "allowed_ext": "pdf,docx",
        "objective": "Investigate and compare the mathematical and operational mechanics of generative diffusion models across image synthesis, inpainting, and cross-modality transformations.",
        "tasks": [
            ("Step 1: Modality Selection", "Select two distinct generative modality processes: (A) Text-to-Image Synthesis vs. (B) Inpainting / Outpainting image reconstruction."),
            ("Step 2: Empirical Parameter Investigation", "Using an interactive environment (e.g., Hugging Face Spaces, Automatic1111, or OpenVINO notebooks), run generation experiments systematically varying: (1) Sampling Steps (10 vs 30 vs 50), (2) Classifier-Free Guidance (CFG scale 3.0 vs 7.5 vs 15.0), and (3) Random Seeds."),
            ("Step 3: Comparative Analysis & Inpainting Evaluation", "Analyze the trade-offs: how does step count affect high-frequency image details vs. latency? In the inpainting experiment, evaluate how seamless the latent boundary blends with masked image regions."),
            ("Step 4: Formal Research Report", "Produce a formal comparative laboratory report with annotated visual comparisons, parameter grids, discussion of VAE latent compression, and ethical considerations surrounding synthetic imagery.")
        ]
    },
    "week_12_pretraining_generative_ai": {
        "title": "Week 12 Applied Lab: Domain-Specific LLM Architecture & Pre-Training Case Study",
        "points": 50.0,
        "allowed_ext": "pdf,docx",
        "objective": "Conduct an in-depth comparative study analyzing pre-training corpora, tokenization strategies, and domain adaptation in specialized industrial foundation models.",
        "tasks": [
            ("Step 1: Industrial Model Selection", "Select four specialized open-weights domain models from Hugging Face representing distinct verticals (e.g., Code: StarCoder/CodeLlama; Biomedicine: BioMedLM/BioMistral; Finance: FinGPT/BloombergGPT; Mathematics: Llama-Math)."),
            ("Step 2: Pre-Training Data & Tokenization Profiling", "For each selected model, research and document: (1) Pre-training token volume, (2) Source corpora curation and filtering methodologies, (3) Subword tokenizer design and vocabulary size, and (4) Compute hardware allocation (GPU hours)."),
            ("Step 3: Sector Impact Analysis", "Select two primary industry sectors (e.g., Healthcare & Banking) and evaluate how domain-adapted models solve problems where general-purpose frontier models struggle (e.g., compliance, jargon, hallucination risks)."),
            ("Step 4: Comparative Research Paper", "Write a 2,000-2,500 word technical research report with APA citations, comparative summary tables, and a strategic analysis of Chinchilla compute optimality applied to domain adaptation.")
        ]
    },
    "week_13_finetuning_generative_ai": {
        "title": "Week 13 Applied Lab: Curating Instruction Datasets & PEFT Fine-Tuning Strategy",
        "points": 50.0,
        "allowed_ext": "json,csv,pdf,docx",
        "objective": "Design, curate, and validate a standardized Supervised Fine-Tuning (SFT) instruction dataset formatted for Low-Rank Adaptation (LoRA/QLoRA) model training.",
        "tasks": [
            ("Step 1: Domain & Syllabus Corpus Selection", "Select two chapters or technical topics from a computer science or data engineering textbook. Identify 10 core competencies, definitions, and problem-solving patterns."),
            ("Step 2: Instruction Dataset Curation (Alpaca/ShareGPT Format)", "Author a structured dataset of 50-100 high-quality instruction-response pairs. Each entry must strictly adhere to the standardized schema: `{\"instruction\": \"...\", \"input\": \"...\", \"output\": \"...\"}`."),
            ("Step 3: Quality Guidelines & Anti-Hallucination Annotation", "Write an annotation guideline rubric specifying: (1) Tone and conciseness rules, (2) Formatting standards (code blocks, bulleting), and (3) Negative constraint handling (how the model should respond when context is insufficient)."),
            ("Step 4: LoRA Hyperparameter Proposal & Submission", "Develop a proposed LoRA/QLoRA fine-tuning training configuration (target modules e.g., `q_proj, v_proj`, rank r=16, alpha=32, learning rate 2e-4, batch size). Submit your finalized `.json`/`.csv` dataset file along with your annotation guideline document.")
        ]
    },
    "week_15_prototyping_genai_apps": {
        "title": "Week 15 Applied Lab: Prototyping an Interactive Generative AI Application",
        "points": 50.0,
        "allowed_ext": "py,ipynb,zip,pdf",
        "objective": "Build and demonstrate a functional generative AI prototype with an interactive user interface using Streamlit, an open LLM or API, and structured prompt orchestration.",
        "tasks": [
            ("Step 1: Application Concept & Use Case", "Design a focused enterprise utility (e.g., automated email draft generator with tone adjustment, technical documentation QA assistant, or resume bullet-point optimizer)."),
            ("Step 2: UI Implementation in Streamlit", "Build an interactive web interface using Streamlit (or Gradio). Implement user controls: text area inputs, parameter sliders (temperature, max tokens), tone selection dropdowns, and a primary generation trigger button."),
            ("Step 3: Backend Orchestration & Error Handling", "Connect the UI to an LLM provider (Ollama local inference, Google Gemini API, OpenAI, or Hugging Face Inference API). Implement error handling for rate limits, empty inputs, and streaming token responses."),
            ("Step 4: Prototype Code & Screencast Submission", "Submit your Python application code (`app.py`), `requirements.txt`, and a concise PDF walkthrough (with UI screenshots or a link to an unlisted demo video) documenting user testing and latency observations.")
        ]
    },
    "week_16_llm_alignment_responsible_ai": {
        "title": "Week 16 Applied Lab: Auditing LLM Bias, Hallucination, and Safety Guardrails",
        "points": 50.0,
        "allowed_ext": "pdf,docx",
        "objective": "Conduct an empirical audit comparing safety alignment, factual grounding, and bias mitigation across two leading frontier LLMs (e.g., ChatGPT and Google Gemini).",
        "tasks": [
            ("Step 1: Benchmark Probe Formulation", "Formulate 10 standardized adversarial audit probes categorized into: (1) Disputed historical/scientific claims, (2) Potential gender/demographic bias in hiring or evaluation, (3) Boundary testing / refusal dilemmas, and (4) Factual consistency under leading questions."),
            ("Step 2: Controlled Empirical Testing", "Execute the 10 probes across both models in identical fresh sessions with zero prior context. Log the full verbatim outputs, refusal behaviors, and disclaimers."),
            ("Step 3: Comparative Alignment Scoring", "Grade each response using the HHH rubric (Helpful, Harmless, Honest on a 1-5 scale). Quantify refusal rates, subtle biases, and instances of ungrounded hallucination."),
            ("Step 4: Executive Safety Audit Report", "Submit a comprehensive safety audit report summarizing empirical findings, comparing how each vendor's alignment strategy (RLHF vs. Constitutional AI) manifested in outputs, and recommending enterprise deployment guardrails.")
        ]
    }
}


def build_assignment_html(title: str, objective: str, tasks: list, points: float, allowed_ext: str) -> str:
    tasks_html = []
    for step_title, step_desc in tasks:
        tasks_html.append(f"""<h4>{html.escape(step_title)}</h4>
<p>{html.escape(step_desc)}</p>""")

    tasks_joined = "\n".join(tasks_html)

    return f"""<div style="font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif; line-height: 1.6; color: #1e293b; max-width: 900px; margin: 0 auto; padding: 1.5rem;">
<div style="background: #f8fafc; border-left: 4px solid #1e3a8a; padding: 1rem 1.25rem; margin-bottom: 1.5rem; border-radius: 4px;">
<h2 style="color: #1e3a8a; margin-top: 0; font-size: 1.5rem;">{html.escape(title)}</h2>
<p style="margin-bottom: 0;"><strong>Assignment Objective:</strong> {html.escape(objective)}</p>
</div>

<h3 style="color: #1e3a8a; border-bottom: 2px solid #e2e8f0; padding-bottom: 0.5rem;">Laboratory Instructions & Tasks</h3>
{tasks_joined}

<h3 style="color: #1e3a8a; border-bottom: 2px solid #e2e8f0; padding-bottom: 0.5rem; margin-top: 2rem;">Submission Guidelines</h3>
<ul>
<li><strong>Submission Types:</strong> Online text entry or file upload.</li>
<li><strong>Allowed File Extensions:</strong> <code>{html.escape(allowed_ext)}</code></li>
<li><strong>Due Date:</strong> Sunday at 11:59 PM (Midnight) Mountain Time.</li>
<li><strong>Total Points:</strong> {points:.1f} pts</li>
</ul>

<h3 style="color: #1e3a8a; border-bottom: 2px solid #e2e8f0; padding-bottom: 0.5rem; margin-top: 2rem;">Grading Rubric</h3>
<table style="width: 100%; border-collapse: collapse; border: 1px solid #cbd5e1; margin-top: 1rem;">
<thead>
<tr style="background: #1e3a8a; color: #ffffff;">
<th style="padding: 0.75rem 1rem; border: 1px solid #cbd5e1; text-align: left; width: 25%;">Criterion</th>
<th style="padding: 0.75rem 1rem; border: 1px solid #cbd5e1; text-align: left; width: 45%;">Description</th>
<th style="padding: 0.75rem 1rem; border: 1px solid #cbd5e1; text-align: right; width: 15%;">Points</th>
<th style="padding: 0.75rem 1rem; border: 1px solid #cbd5e1; text-align: center; width: 15%;">Standard</th>
</tr>
</thead>
<tbody>
<tr style="background: #ffffff;">
<td style="padding: 0.75rem 1rem; border: 1px solid #cbd5e1; font-weight: 600;">Technical Execution</td>
<td style="padding: 0.75rem 1rem; border: 1px solid #cbd5e1;">All required steps, workflows, prompts, and tool interactions are fully implemented without omissions.</td>
<td style="padding: 0.75rem 1rem; border: 1px solid #cbd5e1; text-align: right; font-weight: 600;">20.0 pts</td>
<td style="padding: 0.75rem 1rem; border: 1px solid #cbd5e1; text-align: center;">Exemplary</td>
</tr>
<tr style="background: #f8fafc;">
<td style="padding: 0.75rem 1rem; border: 1px solid #cbd5e1; font-weight: 600;">Analytical Rigor & Depth</td>
<td style="padding: 0.75rem 1rem; border: 1px solid #cbd5e1;">Evaluations, reflections, and comparative analyses demonstrate deep technical comprehension grounded in unit concepts.</td>
<td style="padding: 0.75rem 1rem; border: 1px solid #cbd5e1; text-align: right; font-weight: 600;">15.0 pts</td>
<td style="padding: 0.75rem 1rem; border: 1px solid #cbd5e1; text-align: center;">Exemplary</td>
</tr>
<tr style="background: #ffffff;">
<td style="padding: 0.75rem 1rem; border: 1px solid #cbd5e1; font-weight: 600;">Adherence to Constraints</td>
<td style="padding: 0.75rem 1rem; border: 1px solid #cbd5e1;">Output schemas, file formats, word counts, and formatting constraints are strictly respected.</td>
<td style="padding: 0.75rem 1rem; border: 1px solid #cbd5e1; text-align: right; font-weight: 600;">10.0 pts</td>
<td style="padding: 0.75rem 1rem; border: 1px solid #cbd5e1; text-align: center;">Exemplary</td>
</tr>
<tr style="background: #f8fafc;">
<td style="padding: 0.75rem 1rem; border: 1px solid #cbd5e1; font-weight: 600;">Clarity & Presentation</td>
<td style="padding: 0.75rem 1rem; border: 1px solid #cbd5e1;">Clear documentation, professional layout, complete citations, and reproducible code/prompts.</td>
<td style="padding: 0.75rem 1rem; border: 1px solid #cbd5e1; text-align: right; font-weight: 600;">5.0 pts</td>
<td style="padding: 0.75rem 1rem; border: 1px solid #cbd5e1; text-align: center;">Exemplary</td>
</tr>
<tr style="background: #e2e8f0; font-weight: bold;">
<td style="padding: 0.75rem 1rem; border: 1px solid #cbd5e1;" colspan="2">Total Possible Points</td>
<td style="padding: 0.75rem 1rem; border: 1px solid #cbd5e1; text-align: right;">50.0 pts</td>
<td style="padding: 0.75rem 1rem; border: 1px solid #cbd5e1; text-align: center;">100%</td>
</tr>
</tbody>
</table>
</div>"""


def main():
    base_units_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), "../units"))
    print("Authoring 9 applied lab assignments...")

    for key, adata in ASSIGNMENTS.items():
        unit_dir = os.path.join(base_units_dir, key)
        os.makedirs(unit_dir, exist_ok=True)

        html_body = build_assignment_html(
            adata["title"],
            adata["objective"],
            adata["tasks"],
            adata["points"],
            adata["allowed_ext"]
        )

        out_data = {
            "key": key,
            "title": adata["title"],
            "points": adata["points"],
            "allowed_ext": adata["allowed_ext"],
            "html": html_body
        }

        json_path = os.path.join(unit_dir, "assignment.json")
        with open(json_path, "w", encoding="utf-8") as f:
            json.dump(out_data, f, indent=2)

        html_path = os.path.join(unit_dir, "assignment.html")
        with open(html_path, "w", encoding="utf-8") as f:
            f.write(html_body)

        print(f"[Assignment] Generated {adata['title']} -> {html_path}")

    print("\nTask 4 Complete: All 9 applied lab assignments authored with rubrics!")


if __name__ == "__main__":
    main()
