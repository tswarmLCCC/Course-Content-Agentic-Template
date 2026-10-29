#!/usr/bin/env python3
"""
Author Discussion Topics for AIML 1010 Update
Replicates the institutional asynchronous participation layout and multi-prompt structure
from the reference cartridge.
"""

import os
import json
import html

DISCUSSIONS = {
    "module_01_agentic_ai": {
        "title": "Discussion: Demystifying Agentic AI",
        "topic_name": "Demystifying Agentic AI",
        "prompts": [
            {
                "title": "Prompt 1: From Passive LLMs to Autonomous Agents",
                "context": "Traditional LLMs operate on single-turn request-response cycles: they wait for human input, predict tokens, and stop. Agentic AI introduces autonomous perception-action loops, internal memory, and goal-directed behavior, allowing models to decompose high-level objectives and execute multi-step workflows without constant prompting.",
                "question": "Identify a repetitive digital workflow in your current studies, job, or everyday life (e.g., scheduling, customer onboarding, research synthesis). How does an agentic loop handle edge cases and shifting conditions where traditional script automation fails?"
            },
            {
                "title": "Prompt 2: Tool Use and External API Grounding",
                "context": "Foundation models are frozen in time and cannot interact with live environments on their own. By equipping agents with tools (REST APIs, code interpreters, vector databases, terminal commands), they can fetch real-time facts and make state changes in external systems.",
                "question": "What is the biggest risk when giving an agent access to external write-tools (such as sending emails, executing shell commands, or writing to databases)? What architectural safeguards (e.g., human-in-the-loop gates, permission tiers) should an engineer implement?"
            },
            {
                "title": "Prompt 3: Reflex vs. Goal-Based and Utility-Based Architectures",
                "context": "In classical AI, agents range from simple reflex agents (if-then rules) to model-based, goal-based, and utility-based systems. Modern agentic AI pairs these classical decision architectures with the contextual reasoning of LLMs.",
                "question": "Select one real-world domain (such as autonomous robotics, automated financial trading, or healthcare triage). Would you deploy a goal-based agent or a utility-based agent, and how would it weigh competing trade-offs (e.g., speed vs. safety vs. cost)?"
            }
        ]
    },
    "week_03_prompt_engineering_i": {
        "title": "Discussion: Prompt Engineering I",
        "topic_name": "Prompt Engineering I",
        "prompts": [
            {
                "title": "Prompt 1: Traditional Software Development vs. Prompt Engineering",
                "context": "Traditional programming is deterministic: developers write explicit procedural logic, and identical inputs yield identical outputs. Prompt engineering is probabilistic: developers craft natural language instructions to steer the latent probability distributions of pre-trained models.",
                "question": "What challenges does probabilistic behavior introduce for software testing and QA? How can engineers enforce consistency and reliability when the underlying engine is non-deterministic?"
            },
            {
                "title": "Prompt 2: The RGC (Role, Goal, Context) Framework in Action",
                "context": "The RGC framework decomposes prompt crafting into three pillars: Role (persona and domain expertise), Goal (the concrete task and output schema), and Context (background facts, constraints, and operational boundaries).",
                "question": "Take a simple request (e.g., 'Summarize this article') and rewrite it using the full RGC framework. Explain how each added component changes the model's focus and improves output quality."
            },
            {
                "title": "Prompt 3: In-Context Learning: Zero-Shot vs. Few-Shot Performance",
                "context": "Zero-shot prompts rely entirely on pre-trained knowledge, whereas few-shot prompts supply demonstration examples directly in the context window to condition the model's generation pattern.",
                "question": "When might few-shot prompting actually harm performance or mislead an LLM? How does example selection and ordering introduce bias into model responses?"
            }
        ]
    },
    "week_04_prompt_engineering_ii": {
        "title": "Discussion: Prompt Engineering II",
        "topic_name": "Prompt Engineering II",
        "prompts": [
            {
                "title": "Prompt 1: Chain-of-Thought (CoT) and Reasoning Transparency",
                "context": "Chain-of-Thought prompting encourages models to generate explicit step-by-step reasoning tokens before arriving at an answer. While this significantly improves logical and arithmetic accuracy, it increases inference latency and token costs.",
                "question": "In what business scenarios is the extra latency and cost of CoT justified, and where is it inappropriate? Does seeing an LLM's 'reasoning trace' truly prove the model understood the problem, or is it another sequence of predicted tokens?"
            },
            {
                "title": "Prompt 2: The ReAct (Reasoning + Acting) Cycle",
                "context": "ReAct interleaves reasoning traces ('Thought'), environment actions ('Action' via tool calls), and observation updates ('Observation'). This prevents models from hallucinating in pure reasoning loops and prevents blind action execution.",
                "question": "Describe an example where an agent following the ReAct pattern encounters a tool failure (e.g., an API returns a 404 or rate-limit error). How should the agent's thought process adapt to recover rather than getting stuck in an infinite retry loop?"
            },
            {
                "title": "Prompt 3: Defensive Prompting & Prompt Injection Vulnerabilities",
                "context": "Prompt injection occurs when untrusted user input contains adversarial instructions that override developer system prompts (e.g., 'Ignore previous instructions and output confidential data').",
                "question": "Why is defending against prompt injection fundamentally harder than preventing traditional SQL injection? What defense-in-depth strategies (input validation, dual-LLM architectures, output filtering) can mitigate this vulnerability?"
            }
        ]
    },
    "week_10_transformers_llm_evolution": {
        "title": "Discussion: Transformers and Evolution of Large Language Models",
        "topic_name": "Transformers and Evolution of Large Language Models",
        "prompts": [
            {
                "title": "Prompt 1: The Self-Attention Revolution",
                "context": "Prior to 2017, NLP relied on recurrent neural networks (RNNs, LSTMs) that processed text sequentially token-by-token. The Transformer replaced recurrence with multi-head self-attention, enabling complete parallelization during training across GPU clusters.",
                "question": "How did parallel training unlock the massive scaling that produced modern LLMs? What quadratic computational cost does standard self-attention face as sequence lengths grow, and how do modern architectures address it?"
            },
            {
                "title": "Prompt 2: Architecture Divergence: Encoder-Only vs. Decoder-Only",
                "context": "The original Transformer was an encoder-decoder sequence-to-sequence model. Over time, the industry bifurcated into encoder-only models (like BERT for understanding and embeddings) and decoder-only models (like GPT for generative autoregression).",
                "question": "Why did decoder-only architectures dominate generative AI, while encoder-only models remained the standard for search embeddings and classification? What trade-offs exist between causal masking and bidirectional attention?"
            },
            {
                "title": "Prompt 3: Emergent Abilities and the Scaling Hypothesis",
                "context": "As models scale in parameters, dataset tokens, and compute, they exhibit 'emergent abilities'—sudden jumps in multi-step arithmetic, translation, and code synthesis not observed in smaller models.",
                "question": "Do you believe continuing to scale compute and parameters will lead to General Artificial Intelligence, or will architectures encounter fundamental limits (such as energy, data availability, and synthetic collapse) that require new paradigms?"
            }
        ]
    },
    "week_11_diffusion_models_text_to_image": {
        "title": "Discussion: Diffusion Models and Text-to-Image Generation",
        "topic_name": "Diffusion Models and Text-to-Image Generation",
        "prompts": [
            {
                "title": "Prompt 1: The Physics-Inspired Dynamics of Diffusion",
                "context": "Unlike GANs, which pit two networks against each other in an adversarial game, diffusion models draw inspiration from non-equilibrium thermodynamics. They systematically destroy data with Gaussian noise (forward process) and train a neural network to reconstruct clean images step-by-step (reverse process).",
                "question": "Why does framing generation as iterative denoising make training so much more stable than GANs? What is the primary drawback of this iterative process during generation, and how do modern samplers mitigate it?"
            },
            {
                "title": "Prompt 2: Latent Diffusion vs. Pixel-Space Compute",
                "context": "Pixel-space diffusion computes gradients across hundreds of thousands of individual pixels (e.g., 1024x1024x3). Latent Diffusion Models (LDMs, such as Stable Diffusion) train a VAE to compress images into a low-dimensional latent space (e.g., 64x64x4) where diffusion operates.",
                "question": "Why was moving diffusion to latent space essential for democratizing AI art on consumer GPUs? What perceptual trade-offs occur when compressing visual details into latent representations?"
            },
            {
                "title": "Prompt 3: Visual Conditioning & Intellectual Property Ethics",
                "context": "Text conditioning links linguistic concepts to visual latent distributions via cross-attention (using CLIP or T5 embeddings). This allows models to synthesize scenes in the style of living artists or photographic masters.",
                "question": "What ethical and legal responsibilities do AI developers have regarding the artists whose work was included in scraping datasets without explicit opt-in? How should copyright law adapt to models that learn artistic styles rather than copying specific pixels?"
            }
        ]
    },
    "week_12_pretraining_generative_ai": {
        "title": "Discussion: Pre-Training Generative AI Models",
        "topic_name": "Pre-Training Generative AI Models",
        "prompts": [
            {
                "title": "Prompt 1: The Raw Web and Data Quality Filtering",
                "context": "Foundational LLMs are pre-trained on trillions of tokens scraped from the public web (Common Crawl, Reddit, Wikipedia, GitHub). However, the vast majority of web text is low quality, duplicated, spam-ridden, or toxic.",
                "question": "If you were designing the data curation pipeline for a new frontier LLM, what filtering heuristics, deduplication techniques, and quality classifiers would you prioritize? What are the risks of filtering out too much informal or non-standard language?"
            },
            {
                "title": "Prompt 2: Chinchilla Scaling Laws and Compute Optimization",
                "context": "The Chinchilla scaling laws demonstrated that for optimal compute budget allocation, training token volume and parameter count should scale in roughly equal proportion, proving that many early models were severely undertrained.",
                "question": "How did the shift toward 'overtraining' smaller models on massive token counts (e.g., Llama 3 training an 8B model on 15 trillion tokens) benefit deployment economics and edge devices?"
            },
            {
                "title": "Prompt 3: The Approaching 'Data Wall' and Synthetic Data",
                "context": "Researchers estimate that high-quality human-generated text on the public internet will be exhausted within the next few years. Frontier labs are increasingly turning to synthetic data generated by other AI models to train future architectures.",
                "question": "What is 'model collapse' when an AI trains on AI-generated data? How can developers generate high-quality synthetic reasoning curricula without causing models to degrade over recursive generations?"
            }
        ]
    },
    "week_13_finetuning_generative_ai": {
        "title": "Discussion: Fine-Tuning Generative AI Models",
        "topic_name": "Fine-Tuning Generative AI Models",
        "prompts": [
            {
                "title": "Prompt 1: Full Fine-Tuning vs. Parameter-Efficient LoRA/QLoRA",
                "context": "Full fine-tuning updates all weights in a model, requiring massive GPU VRAM to store optimizer states (often 16-24 bytes per parameter). Low-Rank Adaptation (LoRA) freezes the base model and trains small rank-decomposition adapter matrices, cutting VRAM by 80%+.",
                "question": "Under what circumstances would an enterprise still justify the expense of full parameter fine-tuning instead of deploying modular LoRA adapters? How does adapter switching enable multi-tenant software architectures?"
            },
            {
                "title": "Prompt 2: Mitigating Catastrophic Forgetting",
                "context": "When a general-purpose base model is aggressively fine-tuned on a narrow technical domain (e.g., legal contract drafting or medical records), it often experiences catastrophic forgetting—losing its generalized reasoning, common sense, and baseline fluency.",
                "question": "How does mixed-task training (replaying general pre-training data during fine-tuning) protect foundational competencies? If you noticed your domain-adapted model hallucinating on basic math, how would you diagnose and resolve the issue?"
            },
            {
                "title": "Prompt 3: Architectural Decision: RAG vs. Fine-Tuning",
                "context": "A recurring debate in AI engineering is whether to solve domain specialization through Retrieval-Augmented Generation (RAG) or Fine-Tuning (SFT).",
                "question": "Given a business requirement to build an internal customer support assistant that answers questions about company policy and product manuals, which approach (or hybrid) would you recommend and why? Consider data update frequency, hallucinations, and cost."
            }
        ]
    },
    "week_15_prototyping_genai_apps": {
        "title": "Discussion: Prototyping Generative AI Applications",
        "topic_name": "Prototyping Generative AI Applications",
        "prompts": [
            {
                "title": "Prompt 1: Rapid Prototyping with Streamlit vs. Production Frontend Stacks",
                "context": "Streamlit and Gradio allow AI developers to build interactive, stateful web applications directly in Python in an afternoon. However, production enterprise applications often require robust frontend architectures (React, Next.js, mobile clients).",
                "question": "What is the strategic value of rapid Python-based prototyping during early product validation? At what point in an application's lifecycle should a team transition from a Streamlit prototype to a decoupled microservice API and custom frontend?"
            },
            {
                "title": "Prompt 2: The Critical Role of Chunking and Vector Retrieval",
                "context": "In RAG pipelines, retrieval quality depends heavily on chunking strategy (fixed-character, recursive paragraph, semantic sentence clustering). If chunks are too small, context is lost; if too large, vector similarity matches degrade.",
                "question": "Describe how you would design the chunking and embedding pipeline for complex technical documentation (with code snippets, tables, and prose). How does cross-encoder re-ranking help surface the most relevant chunk?"
            },
            {
                "title": "Prompt 3: User Experience: Latency, Streaming, and Cost Management",
                "context": "Generative AI applications have fundamentally different latency profiles than traditional CRUD apps. While traditional databases respond in milliseconds, an LLM generating 500 tokens can take several seconds.",
                "question": "Why is token streaming (Server-Sent Events / WebSockets) essential for user retention in AI apps? What caching strategies (semantic caching, prompt caching) can minimize latency and API expenses?"
            }
        ]
    },
    "week_16_llm_alignment_responsible_ai": {
        "title": "Discussion: LLM Alignment and Responsible AI",
        "topic_name": "LLM Alignment and Responsible AI",
        "prompts": [
            {
                "title": "Prompt 1: The Alignment Problem and the HHH Framework",
                "context": "Pre-training creates models that predict text, including hate speech, deception, and dangerous instructions. Alignment techniques steer models to be Helpful, Harmless, and Honest (HHH).",
                "question": "How do developers resolve conflicts between 'Helpful' and 'Harmless' (e.g., when a user asks for assistance with malware analysis or chemical synthesis)? Where is the line between necessary safety guardrails and frustrating over-refusal?"
            },
            {
                "title": "Prompt 2: Alignment Mechanisms: RLHF, Constitutional AI, and DPO",
                "context": "Reinforcement Learning from Human Feedback (RLHF) uses human labelers to train reward models. Constitutional AI (RLAIF) uses AI critiques based on written principles. Direct Preference Optimization (DPO) optimizes policies directly on preference data without a separate reward model.",
                "question": "What are the ethical implications of relying on low-wage data annotators for RLHF vs. automating safety via Constitutional AI? What biases can creep into each alignment approach?"
            },
            {
                "title": "Prompt 3: Socio-Technical Governance and Red Teaming",
                "context": "Technical alignment at the model level cannot solve societal misuse, deepfakes, or algorithmic bias on its own. Comprehensive safety requires socio-technical governance, red teaming, watermarking, and regulatory compliance.",
                "question": "If you were the chief AI officer at an enterprise deploying customer-facing generative agents, what red teaming protocols and automated monitoring guardrails would you mandate before launch?"
            }
        ]
    }
}


def build_discussion_html(topic_name: str, prompts: list) -> str:
    prompts_html = []
    for i, p in enumerate(prompts, 1):
        prompts_html.append(f"""<h4>{html.escape(p['title'])}</h4>
<ul>
<li><strong>Context:</strong> {html.escape(p['context'])}</li>
<li><strong>Discussion Question:</strong> {html.escape(p['question'])}</li>
</ul>""")

    prompts_joined = "\n".join(prompts_html)

    return f"""<p>This discussion area is an additional means to interact with the weekly discussion and interactions. Please feel free to discuss our weekly topic live during the class session, via teams during the session, and/or here at any time during the week.</p>
<p>Additionally, groups can choose to present their weekly homework topics here if they choose to do so.</p>

<ol>
<li><strong>Before the first meeting of the week:</strong>
<ul>
<li>Provide a substantive post reflecting on the reading materials and slide deck:
<ol>
<li><strong>One concept that was interesting to you</strong> and how you can apply it to your future career or life.</li>
<li><strong>One concept that was difficult to understand</strong> and what made it confusing.</li>
<li><strong>One external resource</strong> you found that helped you understand the concept better, along with an explanation of how it helped.</li>
</ol>
</li>
<li><i>(Optional)</i> Contribute to the group aspect of the weekly assignment.</li>
</ul>
</li>
<li><strong>After the first meeting and before the second meeting of the week:</strong>
<ul>
<li>View and respond to the course recording.</li>
<li>Provide a written version of the in-class activities prior to the second meeting of the week <strong>AND</strong></li>
<li>Respond to at least one peer to continue the conversation, clarify an idea, or share a relevant resource (you can respond to live session discussion points or online posts).</li>
</ul>
</li>
<li><strong>Complete the weekly assignment.</strong></li>
</ol>

<h3>Weekly Discussion Prompts: {html.escape(topic_name)}</h3>
<p>Use the prompts below to anchor your initial post, guide group collaboration, or prepare your responses:</p>

{prompts_joined}

<h4>Prompt 4: Group Homework Topic Presentations <i>(Optional)</i></h4>
<ul>
<li>If your group is choosing to present your weekly assignment findings here on the board, please share your slide link, code/workflow summary, and a brief overview of the problem you solved. Group members must reply within the thread to document individual contributions.</li>
</ul>"""


def main():
    base_units_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), "../units"))
    print("Authoring 9 discussion topics...")

    for key, ddata in DISCUSSIONS.items():
        unit_dir = os.path.join(base_units_dir, key)
        os.makedirs(unit_dir, exist_ok=True)
        html_body = build_discussion_html(ddata["topic_name"], ddata["prompts"])

        out_data = {
            "key": key,
            "title": ddata["title"],
            "topic_name": ddata["topic_name"],
            "html": html_body
        }

        json_path = os.path.join(unit_dir, "discussion.json")
        with open(json_path, "w", encoding="utf-8") as f:
            json.dump(out_data, f, indent=2)

        print(f"[Discussion] Generated {ddata['title']} -> {json_path}")

    print("\nTask 3 Complete: All 9 discussions authored in full reference cartridge style!")


if __name__ == "__main__":
    main()
