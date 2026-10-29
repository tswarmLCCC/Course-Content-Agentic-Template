#!/usr/bin/env python3
"""
Author DesignPLUS-Compliant Reading Pages for AIML 1010 Update
Synthesizes reading briefing notes from the slide decks and facilitator guides,
incorporating unit objectives, active PDF links, and student exercise callouts.
"""

import os
import json
import html

READING_PAGES = {
    "module_01_agentic_ai": {
        "page_title": "Reading - Demystifying Agentic AI",
        "header_title": "Module 01: Demystifying Agentic AI",
        "icon": "fa-robot",
        "pdf_filename": "[Slides] Module 01 - Agentic AI Notes.pdf",
        "pdf_display_title": "Briefing Slide Deck & Speaker Notes: Module 01 Demystifying Agentic AI",
        "objectives": [
            "Define Agentic AI and distinguish it from automation, conventional AI, and standalone Generative AI.",
            "Identify and explain the core perception-action loop and traits of autonomous agent systems.",
            "Differentiate between Simple Reflex, Model-based, Goal-based, and Utility-based agent architectures.",
            "Analyze the strategic value and implementation patterns of tool use and function calling.",
            "Understand the emerging paradigm of Human-in-the-Loop (HITL) collaboration in modern workplaces."
        ],
        "problem_statement": "Traditional software and script automation follow rigid, deterministic decision trees. While early machine learning allowed computers to make statistical predictions, traditional large language models remain passive conversationalists waiting for single-turn user prompts. They cannot interact with live databases, dynamically recover from tool errors, or independently execute complex multi-step objectives. Agentic AI bridges this fundamental gap by enabling software entities to perceive dynamic environments, formulate multi-step plans, invoke external tools, reflect on intermediate outputs, and autonomously iterate until a goal is achieved.",
        "theoretical_framework": """<p><strong>The Evolution toward Agentic Autonomy:</strong> In classical artificial intelligence, agents are defined by their capacity to perceive an environment through sensors, reason internally, and act upon the environment through actuators. Agentic AI combines this foundational perception-action cycle with the rich semantic reasoning and world knowledge of Large Language Models.</p>
<p><strong>Agent Architectural Taxonomy:</strong></p>
<ul>
<li><strong>Simple Reflex Agents:</strong> Select actions based solely on current percepts using hardcoded condition-action rules. They fail in partially observable environments.</li>
<li><strong>Model-Based Reflex Agents:</strong> Maintain an internal state to track unobserved aspects of the world, allowing them to make informed decisions despite incomplete information.</li>
<li><strong>Goal-Based Agents:</strong> Combine state tracking with explicit goal representations, evaluating how candidate actions bring the system closer to a target state.</li>
<li><strong>Utility-Based Agents:</strong> Use a continuous utility function to evaluate trade-offs between competing outcomes, enabling optimal decision-making under uncertainty.</li>
</ul>
<p><strong>The Anatomy of Modern Agentic Systems:</strong> A modern agent comprises four core modules: (1) <em>Planning</em> (decomposing goals into sub-tasks and reflecting on intermediate errors), (2) <em>Memory</em> (short-term context window buffer and long-term vector database persistence), (3) <em>Tools</em> (REST APIs, calculators, code interpreters, and file systems), and (4) <em>Action Execution</em> (generating structured function calls and ingesting environment observations).</p>""",
        "implementation_guide": """<p>To implement an effective agentic workflow in enterprise software, developers adhere to a standard five-phase execution loop:</p>
<ol>
<li><strong>Perception & Ingestion:</strong> The agent receives an input percept (user objective, webhook, or system event) and parses it into structured context.</li>
<li><strong>Decomposition & Planning:</strong> The agent outlines a sequence of necessary operations, assessing tool requirements and prerequisite dependencies.</li>
<li><strong>Tool Invocation (Acting):</strong> The agent outputs a structured JSON schema function call to query an external service or execute an operation.</li>
<li><strong>Observation & Evaluation:</strong> The agent receives the tool output, checks for errors or rate limits, and validates the response against its sub-goal.</li>
<li><strong>Reflection & Iteration:</strong> The agent updates its internal trajectory. If errors occurred, it re-plans; if the goal is satisfied, it delivers the finalized synthesis to the user.</li>
</ol>""",
        "exercises": [
            "Map an existing multi-step administrative or data pipeline in your organization into an Agentic Perception-Action loop.",
            "Contrast the failure modes of a Simple Reflex agent versus a Goal-Based agent in handling sudden API downtime.",
            "Draft a Human-in-the-Loop (HITL) approval policy specifying which agent actions require manual human sign-off."
        ]
    },
    "week_03_prompt_engineering_i": {
        "page_title": "Reading - Prompt Engineering I",
        "header_title": "Week 03: Foundations of Prompt Engineering",
        "icon": "fa-terminal",
        "pdf_filename": "[Slides] Week 3 - GAI Prompt 1.pdf",
        "pdf_display_title": "Briefing Slide Deck & Speaker Notes: Week 03 Prompt Engineering I",
        "objectives": [
            "Explain the technical mechanisms of in-context learning and probabilistic token prediction.",
            "Master the Role-Goal-Context (RGC) framework to steer foundation model outputs.",
            "Distinguish between Zero-Shot, One-Shot, and Few-Shot prompting paradigms.",
            "Implement structural delimiters and explicit output constraints (JSON, Markdown) to eliminate formatting drift.",
            "Identify common prompting anti-patterns and apply defensive constraints against ambiguity."
        ],
        "problem_statement": "Pre-trained foundation models contain vast latent representations of human knowledge and language, but raw generation without structural steering produces verbose, unfocused, or hallucinated responses. Traditional software developers often struggle with the non-deterministic nature of language models. Prompt engineering provides the systematic discipline, architectural frameworks, and syntactic controls required to transform frozen neural networks into reliable, deterministic software components for production applications.",
        "theoretical_framework": """<p><strong>Probabilistic Token Prediction & In-Context Steering:</strong> Transformers compute conditional probability distributions P(w_t | w_1, ..., w_{t-1}). Every word in a prompt actively shifts the attention weights across the model's layers. Prompt engineering is the practice of shaping the context window so that the highest-probability continuation tokens coincide with the user's intended objective.</p>
<p><strong>The RGC Operational Framework:</strong></p>
<ul>
<li><strong>Role (Persona & Tone):</strong> Establishes domain authority and vocabulary constraints (e.g., 'Act as an expert data architect specializing in Apache Spark performance tuning').</li>
<li><strong>Goal (Task & Schema):</strong> Clearly specifies the exact deliverable, operational bounds, and output structure (e.g., 'Extract all date entities and format them as an ISO-8601 JSON array').</li>
<li><strong>Context (Grounding & Boundary):</strong> Provides the necessary source documentation, operational constraints, and edge-case instructions to minimize speculation.</li>
</ul>
<p><strong>In-Context Learning Spectrum:</strong> Zero-shot prompts test the model's generalized pre-trained distribution. Few-shot prompts introduce demonstration examples into the prompt, creating strong in-context attentional priors that guide both format and reasoning style without updating weights.</p>""",
        "implementation_guide": """<p>Follow these industry best practices when crafting production-grade prompts:</p>
<ol>
<li><strong>Use Explicit Structural Delimiters:</strong> Wrap source text and instructions in triple backticks (```), XML tags (&lt;context&gt;...&lt;/context&gt;), or Markdown headers to separate data from instructions and mitigate prompt injection.</li>
<li><strong>State What to Do (Avoid Negative Only):</strong> LLMs attend strongly to concepts mentioned in prompts. Positive instructions ('Write in active voice using under 100 words') outperform negative prohibitions ('Do not write long text').</li>
<li><strong>Enforce Schema Contracts:</strong> When integrating with APIs, demand JSON schemas and specify fallback values for missing entities.</li>
<li><strong>Iterative Prompt Refinement:</strong> Treat prompts like code: version control prompt templates, benchmark across diverse test cases, and evaluate error variance.</li>
</ol>""",
        "exercises": [
            "Take an unstructured customer support email and write an RGC prompt that extracts customer name, issue category, sentiment, and recommended routing queue into JSON.",
            "Construct a 3-shot few-shot prompt that teaches a model an invented company acronym taxonomy.",
            "Benchmark the consistency of zero-shot versus few-shot outputs across 10 temperature variations."
        ]
    },
    "week_04_prompt_engineering_ii": {
        "page_title": "Reading - Prompt Engineering II",
        "header_title": "Week 04: Advanced Prompt Engineering & Reasoning Frameworks",
        "icon": "fa-brain",
        "pdf_filename": "[Slides] Week 4 - GAI Prompt 2.pdf",
        "pdf_display_title": "Briefing Slide Deck & Speaker Notes: Week 04 Prompt Engineering II",
        "objectives": [
            "Deconstruct complex problem spaces using Chain-of-Thought (CoT) and Least-to-Most prompting.",
            "Analyze and implement the ReAct (Reasoning + Acting) pattern for interactive tool use.",
            "Understand Directional Stimulus Prompting to guide output focus dynamically.",
            "Architect multi-stage Prompt Chains to break complex business logic into verifiable sub-tasks.",
            "Examine prompt injection vulnerabilities and implement defense-in-depth safety guardrails."
        ],
        "problem_statement": "Single-turn prompt engineering reaches hard limits when applied to complex, multi-step symbolic reasoning, arithmetic calculations, or long-form workflows. Standard zero-shot prompting forces models to jump directly from question to conclusion without intermediate computation. Furthermore, enterprise pipelines face adversarial attacks such as prompt injection and context poisoning. Advanced prompting frameworks provide structured cognitive scaffolding (such as CoT and ReAct) and modular prompt chaining to solve complex problems reliably while reinforcing security posture.",
        "theoretical_framework": """<p><strong>Cognitive Scaffolding & Computation via Tokens:</strong> Because autoregressive Transformers generate tokens sequentially, allocating 'thinking tokens' allows the self-attention mechanism to perform multi-step computational hops. Chain-of-Thought (CoT) prompting prompts the model to generate explicit intermediate deduction steps, radically improving accuracy on math and logic benchmarks.</p>
<p><strong>Advanced Framework Taxonomy:</strong></p>
<ul>
<li><strong>Zero-Shot / Few-Shot CoT:</strong> Prompting with 'Let's think step by step' or providing demonstrated reasoning trajectories to unlock latent reasoning capabilities.</li>
<li><strong>Self-Consistency:</strong> Sampling multiple reasoning trajectories at non-zero temperature and selecting the majority answer via consensus voting.</li>
<li><strong>Tree of Thoughts (ToT):</strong> Allowing models to explore branching reasoning trees, self-evaluate intermediate thoughts, and backtrack from dead ends.</li>
<li><strong>ReAct (Reasoning + Acting):</strong> Interleaving internal thoughts with external tool calls and environment observations to ground reasoning in factual reality.</li>
<li><strong>Prompt Chaining:</strong> Modularizing a workflow into a directed acyclic graph (DAG) where output tokens of sub-task A are validated, parsed, and fed as input to sub-task B.</li>
</ul>""",
        "implementation_guide": """<p>Guidelines for engineering enterprise prompt chains and defensive guardrails:</p>
<ol>
<li><strong>Decompose Monolithic Tasks:</strong> Never ask a single prompt to extract data, validate compliance, perform translation, and write a summary simultaneously. Split into four discrete chained prompts.</li>
<li><strong>Incorporate Defensive System Enclaves:</strong> Clearly isolate user-submitted inputs inside quarantined XML data blocks and instruct the model to treat content inside the enclave strictly as untrusted data.</li>
<li><strong>Implement Post-Generation Validation:</strong> Use lightweight programmatic parsers (e.g., Pydantic schema validation) to catch formatting errors before responses reach user applications.</li>
<li><strong>Combine ReAct with Fallback Mechanisms:</strong> When an agent tool call fails, prompt the model with the exact error payload to trigger self-correction rather than terminating the workflow.</li>
</ol>""",
        "exercises": [
            "Design a 3-step prompt chain that: (1) extracts facts from an earnings report, (2) calculates financial ratios with CoT arithmetic, and (3) drafts an investor briefing.",
            "Implement a self-consistency prompt test on a challenging logic puzzle by comparing 5 independent runs.",
            "Formulate an adversarial prompt injection attack and design a defensive prompt template that neutralizes it."
        ]
    },
    "week_10_transformers_llm_evolution": {
        "page_title": "Reading - Transformers and Evolution of Large Language Models",
        "header_title": "Week 10: Transformers and Evolution of Large Language Models",
        "icon": "fa-network-wired",
        "pdf_filename": "[Slides] Week 10 - GAI Notes.pdf",
        "pdf_display_title": "Briefing Slide Deck & Speaker Notes: Week 10 Transformers and LLM Evolution",
        "objectives": [
            "Understand the fundamental limitations of Recurrent Neural Networks (RNNs) and LSTMs that led to the Transformer.",
            "Dissect the Multi-Head Self-Attention mechanism, Scaled Dot-Product Attention, and Positional Encodings.",
            "Compare Encoder-Only (BERT), Decoder-Only (GPT), and Encoder-Decoder (T5) architectural archetypes.",
            "Trace the evolution of foundation models from initial word embeddings to billion-parameter generative LLMs.",
            "Analyze the computational economics and quadratic scaling bottlenecks of self-attention mechanisms."
        ],
        "problem_statement": "Prior to 2017, natural language processing relied on sequential recurrent architectures (RNNs and LSTMs). These networks processed text word by word, creating severe sequential computational bottlenecks that prohibited efficient GPU parallelization. Furthermore, RNNs suffered from vanishing gradients, limiting their ability to retain long-range context across long documents. The Transformer architecture revolutionized artificial intelligence by replacing recurrent loops with multi-head self-attention, unlocking massive distributed training scalability and laying the foundation for modern generative AI.",
        "theoretical_framework": """<p><strong>The Mechanics of Multi-Head Self-Attention:</strong> In self-attention, each input token is linearly projected into three vectors: Query (Q), Key (K), and Value (V). The relationship between tokens is calculated using the Scaled Dot-Product Attention formula:</p>
<div style="background: #0f172a; color: #f8fafc; padding: 1rem; border-radius: 6px; font-family: Consolas, monospace; text-align: center; margin: 1rem 0;">
Attention(Q, K, V) = softmax( (Q * K^T) / sqrt(d_k) ) * V
</div>
<p>Dividing by the square root of the key dimension (sqrt(d_k)) prevents dot products from growing excessively large in high dimensions, which would cause the softmax gradient to vanish. Multi-head attention repeats this projection across multiple representation subspaces, allowing the model to simultaneously attend to syntax, coreference, semantics, and factual associations.</p>
<p><strong>Positional Encodings:</strong> Because self-attention is permutation-invariant (it treats input as an unordered set of tokens), positional encodings (sinusoidal functions or learned embeddings) are added directly to token vectors to encode sequence order.</p>
<p><strong>Architectural Branches:</strong></p>
<ul>
<li><strong>Encoder-Only (e.g., BERT, RoBERTa):</strong> Uses bidirectional attention to encode rich representations for classification, entity recognition, and dense search embeddings.</li>
<li><strong>Decoder-Only (e.g., GPT-4, Llama, Mistral):</strong> Uses causal (unidirectional) masking to prevent attending to future tokens, optimized for autoregressive text generation.</li>
<li><strong>Encoder-Decoder (e.g., T5, BART):</strong> Combines bidirectional encoding with autoregressive decoding, ideal for translation, summarization, and sequence transformation.</li>
</ul>""",
        "implementation_guide": """<p>Key considerations when navigating Transformer architectures in code:</p>
<ol>
<li><strong>Tokenization Pipeline:</strong> Raw text is split into subword units (e.g. Byte-Pair Encoding or WordPiece) and mapped to integer IDs before entering embedding lookup tables.</li>
<li><strong>Quadratic Attention Bottleneck:</strong> Standard self-attention scales at O(N^2) with sequence length N. Modern long-context architectures employ FlashAttention (IO-aware tiling), Grouped-Query Attention (GQA), and sliding-window attention to manage memory.</li>
<li><strong>Causal Masking in Generative Decoders:</strong> Generative models apply an upper-triangular mask with -infinity values to ensure token t can only attend to tokens &lt;= t during training.</li>
<li><strong>Residual Connections & LayerNorm:</strong> Add & Norm steps stabilize gradient flow across dozens of stacked Transformer layers, enabling deep networks (e.g., 32-128 layers) to train reliably.</li>
</ol>""",
        "exercises": [
            "Manually compute a 3x3 self-attention matrix for a three-word sequence given simplified Q and K vectors.",
            "Compare the parameter counts and memory footprints of an Encoder-only model versus a Decoder-only model of equal depth.",
            "Explain why FlashAttention achieves 2-4x speedups without changing the underlying mathematical output of attention."
        ]
    },
    "week_11_diffusion_models_text_to_image": {
        "page_title": "Reading - Diffusion Models and Text-to-Image Generation",
        "header_title": "Week 11: Diffusion Models and the Evolution of Text-to-Image Generation",
        "icon": "fa-palette",
        "pdf_filename": "[Slides] Week 11 - GAI Notes.pdf",
        "pdf_display_title": "Briefing Slide Deck & Speaker Notes: Week 11 Diffusion Models and Image Synthesis",
        "objectives": [
            "Contrast diffusion models with Generative Adversarial Networks (GANs) and Variational Autoencoders (VAEs).",
            "Dissect the mathematical mechanics of Forward Diffusion (noise addition) and Reverse Diffusion (iterative denoising).",
            "Examine Latent Diffusion Models (LDMs) and the computational role of the VAE latent space.",
            "Analyze cross-attention text conditioning using vision-language embeddings (CLIP/T5).",
            "Evaluate advanced image manipulation techniques: Inpainting, Outpainting, and Classifier-Free Guidance (CFG)."
        ],
        "problem_statement": "Early generative computer vision was dominated by Generative Adversarial Networks (GANs). While capable of generating sharp images, GANs suffered from notorious training instability, hyperparameter sensitivity, and mode collapse (generating only a narrow subset of training data). Furthermore, conditioning GANs on complex, nuanced natural language descriptions proved brittle. Diffusion models solved these foundational challenges by reformulating image synthesis as a continuous physical process of iterative denoising, establishing a new paradigm for high-fidelity, controllable multimodal generation.",
        "theoretical_framework": """<p><strong>The Denoising Diffusion Framework (DDPM):</strong> Diffusion models operate across two mirrored processes:</p>
<ul>
<li><strong>Forward Process (q):</strong> A fixed Markov chain that gradually corrupts a clean image x_0 by adding Gaussian noise over T discrete timesteps according to a variance schedule beta_1, ..., beta_T. At timestep T, the image is indistinguishable from isotropic Gaussian noise.</li>
<li><strong>Reverse Process (p_theta):</strong> A learned neural network (traditionally a U-Net with attention layers, or a Diffusion Transformer / DiT) trained to predict the exact noise vector added at timestep t, allowing the algorithm to subtract the noise and reconstruct a clean sample.</li>
</ul>
<p><strong>Latent Diffusion Models (LDMs):</strong> Running diffusion directly in high-resolution pixel space (e.g. 1024x1024x3 = 3.1 million values) requires immense computational power. Stable Diffusion revolutionized the field by first training a Variational Autoencoder (VAE) to compress images 8x into a compact latent space (128x128x4), performing the iterative diffusion process entirely within this lower-dimensional manifold, and decoding the final latent back into pixels.</p>
<p><strong>Text Conditioning via Cross-Attention:</strong> A pre-trained text encoder (such as CLIP ViT-L or T5) converts text prompts into embedding vectors. Inside the diffusion U-Net, cross-attention layers allow intermediate visual latent features to attend to text tokens, steering the generated content to match the text prompt.</p>""",
        "implementation_guide": """<p>Key parameters and workflows when generating and editing images via diffusion:</p>
<ol>
<li><strong>Classifier-Free Guidance (CFG Scale):</strong> Balances prompt adherence against image diversity. Low CFG (3-5) produces creative, diverse images; moderate CFG (7-9) balances quality and prompt adherence; high CFG (15+) creates oversaturated, hyper-literal renders.</li>
<li><strong>Denoising Sampling Schedulers:</strong> Algorithms like DDIM, Euler Ancestral, and DPM++ Solve the reverse diffusion differential equations in 20-30 steps rather than 1,000 steps, cutting generation latency by 97%.</li>
<li><strong>Inpainting & Outpainting:</strong> By masking specific pixels in latent space and conditioning the reverse process on unmasked boundaries, models can seamlessly fill in missing elements or expand canvas boundaries.</li>
<li><strong>Negative Prompting:</strong> Implemented by calculating guidance away from unwanted terms during classifier-free guidance, suppressing artifacts, blurry details, and undesirable visual motifs.</li>
</ol>""",
        "exercises": [
            "Explain why adding Gaussian noise in the forward process can be computed analytically in a single step at any arbitrary timestep t without calculating all preceding steps.",
            "Compare the computational footprint of pixel-space diffusion vs. latent-space diffusion for generating a 1024x1024 image.",
            "Analyze the ethical and copyright implications of training vision-language models on web-scraped artwork without artist attribution."
        ]
    },
    "week_12_pretraining_generative_ai": {
        "page_title": "Reading - Pre-Training Generative AI Models",
        "header_title": "Week 12: Pre-Training Generative AI Models",
        "icon": "fa-server",
        "pdf_filename": "[Slides] Week 12 - GAI Notes.pdf",
        "pdf_display_title": "Briefing Slide Deck & Speaker Notes: Week 12 Pre-Training Generative AI",
        "objectives": [
            "Deconstruct the end-to-end data engineering pipeline for pre-training trillion-token foundation models.",
            "Evaluate data extraction, heuristic filtering, MinHash deduplication, and quality classification methods.",
            "Analyze tokenization algorithms (Byte-Pair Encoding, WordPiece) and vocabulary trade-offs.",
            "Understand compute-optimal scaling laws (Chinchilla) and GPU cluster infrastructure requirements.",
            "Explore the strategic transition from raw web scraping to curated synthetic data curricula."
        ],
        "problem_statement": "Pre-training is the most compute-intensive, expensive, and critical phase of the generative AI lifecycle, consuming over 95% of the total budget required to create foundation models. While consumer perception focuses on model architectures, empirical research has repeatedly demonstrated that data quality, volume, and curation rigor dictate downstream capabilities. Uncleaned web scrapes lead to biased, toxic, and hallucination-prone models. Understanding the data engineering, tokenization mechanics, and distributed scaling laws of pre-training is essential for modern AI engineering.",
        "theoretical_framework": """<p><strong>The Pre-Training Paradigm:</strong> Pre-training uses self-supervised learning on massive unlabeled corpora (trillions of tokens) to learn general linguistic structure, factual knowledge, and world models. The model learns by predicting the next token across billions of passages:</p>
<div style="background: #0f172a; color: #f8fafc; padding: 1rem; border-radius: 6px; font-family: Consolas, monospace; text-align: center; margin: 1rem 0;">
Loss(theta) = - sum_{i} log P(x_i | x_{&lt;i}; theta)
</div>
<p><strong>The Data Engineering Pipeline:</strong></p>
<ul>
<li><strong>Web Scraping & Text Extraction:</strong> Ingesting petabytes of raw HTML from Common Crawl, extracting clean text while stripping boilerplate, markup, and navigation menus.</li>
<li><strong>Heuristic & Quality Filtering:</strong> Applying statistical filters (document length, symbol-to-word ratio, stopword distribution) and training lightweight classifiers (e.g., FastText trained on Wikipedia) to score text quality.</li>
<li><strong>Deduplication (MinHash & Exact Match):</strong> Removing near-duplicate documents across trillions of tokens to prevent rote memorization, improve diversity, and stabilize gradient descent.</li>
<li><strong>Safety & PII Redaction:</strong> Scrubbing personally identifiable information (emails, phone numbers, addresses) and filtering toxic text.</li>
</ul>
<p><strong>Compute-Optimal Scaling Laws (Chinchilla):</strong> Hoffmann et al. demonstrated that for optimal compute allocation, parameter count and training tokens should scale in equal 1:1 proportion. Under-training massive models wastes compute; training smaller models (e.g. 8B) on massive token counts (15T tokens) yields faster, cheaper inference in production.</p>""",
        "implementation_guide": """<p>Architectural considerations when engineering pre-training runs:</p>
<ol>
<li><strong>Subword Tokenizer Construction:</strong> Train a Byte-Pair Encoding (BPE) tokenizer on the clean corpus. Ensure the vocabulary size (e.g., 32k to 128k tokens) balances compression efficiency against embedding parameter size.</li>
<li><strong>Distributed Hardware Parallelism:</strong> Massive models exceed single GPU VRAM. Training requires combining:
   <ul>
   <li><strong>Data Parallelism (DDP / FSDP):</strong> Sharding data batches and optimizer states across nodes.</li>
   <li><strong>Tensor Parallelism:</strong> Splitting individual weight matrices across GPUs within a node.</li>
   <li><strong>Pipeline Parallelism:</strong> Partitioning layers sequentially across nodes.</li>
   </ul>
</li>
<li><strong>Synthetic Data Integration:</strong> Augment raw web text with textbook-quality synthetic reasoning data generated by frontier models to bypass web data exhaustion.</li>
</ol>""",
        "exercises": [
            "Given a 100-billion token raw web scrape, outline the step-by-step filtering criteria you would use to yield a 15-billion token high-quality corpus.",
            "Calculate compute-optimal token requirements for a 13-billion parameter model according to Chinchilla scaling laws.",
            "Explain why Byte-Pair Encoding (BPE) handles multilingual text and code more effectively than character-level tokenizers."
        ]
    },
    "week_13_finetuning_generative_ai": {
        "page_title": "Reading - Fine-Tuning Generative AI Models",
        "header_title": "Week 13: Fine-Tuning Generative AI Models",
        "icon": "fa-sliders-h",
        "pdf_filename": "[Slides] Week 13 - GAI Notes.pdf",
        "pdf_display_title": "Briefing Slide Deck & Speaker Notes: Week 13 Fine-Tuning Generative AI",
        "objectives": [
            "Distinguish between Supervised Fine-Tuning (SFT), Continued Pre-training, and In-Context Learning (RAG).",
            "Examine the mathematical mechanics of Parameter-Efficient Fine-Tuning (PEFT) and Low-Rank Adaptation (LoRA).",
            "Understand Quantized LoRA (QLoRA) and 4-bit NormalFloat (NF4) memory optimizations.",
            "Diagnose and mitigate Catastrophic Forgetting during domain adaptation.",
            "Master instruction dataset formatting, conversational chat templates, and loss masking."
        ],
        "problem_statement": "A raw pre-trained base model is an unguided autocomplete engine: if prompted with 'What is the capital of France?', it might simply continue with 'What is the capital of Germany?'. Supervised Fine-Tuning (SFT) transforms base models into conversational, instruction-following assistants. However, full-parameter fine-tuning of multi-billion parameter models requires prohibitive GPU compute and storage. Parameter-Efficient Fine-Tuning (PEFT), particularly LoRA and QLoRA, solves this barrier by freezing base model weights and training lightweight adapter matrices, democratizing model customization.",
        "theoretical_framework": """<p><strong>The Fine-Tuning Spectrum:</strong></p>
<ul>
<li><strong>Continued Pre-Training:</strong> Unsupervised training on domain text (legal, medical) using standard next-token prediction to instill vocabulary and background knowledge.</li>
<li><strong>Supervised Fine-Tuning (SFT):</strong> Training on paired instruction-response examples to teach turn-taking format, tone, and structured output adherence.</li>
<li><strong>Parameter-Efficient Fine-Tuning (LoRA):</strong> Based on the hypothesis that weight updates during adaptation have a low intrinsic dimension. LoRA freezes original weights W_0 (d x k) and injects trainable low-rank matrices B (d x r) and A (r x k), where rank r &lt;&lt; min(d, k):</li>
</ul>
<div style="background: #0f172a; color: #f8fafc; padding: 1rem; border-radius: 6px; font-family: Consolas, monospace; text-align: center; margin: 1rem 0;">
h = W_0 * x + (alpha / r) * (B * A) * x
</div>
<p>Only matrices A and B receive gradient updates during training, reducing trainable parameters and optimizer memory by 99%.</p>
<p><strong>QLoRA Innovations:</strong> Quantizes the frozen base model to 4-bit NormalFloat (NF4), applies double quantization to compress quantization constants, and utilizes paged optimizers to manage memory spikes, allowing fine-tuning of 70B models on a single consumer GPU.</p>
<p><strong>Catastrophic Forgetting:</strong> Occurs when gradient updates on a narrow dataset overwrite neural circuits responsible for general reasoning and commonsense. Mitigated by mixing general instruction data into the domain dataset (co-training).</p>""",
        "implementation_guide": """<p>Production workflow for fine-tuning instruction models:</p>
<ol>
<li><strong>Format Instruction Datasets:</strong> Structure training data into conversational roles (system, user, assistant) and apply the model's exact Chat Template (e.g., Llama-3, ChatML) with special delimiter tokens.</li>
<li><strong>Apply Loss Masking:</strong> Calculate cross-entropy loss exclusively on the assistant's response tokens, masking out user prompt tokens so the model is not penalized for user phrasing.</li>
<li><strong>Configure LoRA Hyperparameters:</strong> Target all linear projection layers (q_proj, k_proj, v_proj, o_proj, gate_proj, up_proj, down_proj). Set rank r=16 or 32, alpha=2*r, and learning rate ~2e-4.</li>
<li><strong>Evaluate with Benchmarks:</strong> Monitor validation loss and evaluate on both domain-specific test sets and general reasoning benchmarks (MMLU, GSM8K) to ensure general capability retention.</li>
</ol>""",
        "exercises": [
            "Calculate the number of trainable parameters in a LoRA adapter for a model with hidden dimension d=4096 and rank r=16 applied to query and value projections.",
            "Contrast when an enterprise should deploy a RAG pipeline versus fine-tuning a custom LoRA adapter.",
            "Draft an instruction example in ShareGPT conversational JSON format with proper system, user, and assistant roles."
        ]
    },
    "week_15_prototyping_genai_apps": {
        "page_title": "Reading - Prototyping Generative AI Applications",
        "header_title": "Week 15: Prototyping Generative AI Applications",
        "icon": "fa-cubes",
        "pdf_filename": "[Slides] Week 15 - GAI Notes.pdf",
        "pdf_display_title": "Briefing Slide Deck & Speaker Notes: Week 15 Prototyping Generative AI",
        "objectives": [
            "Master rapid web application prototyping for generative AI using Streamlit and Gradio.",
            "Architect modular application pipelines using frameworks like LangChain and LlamaIndex.",
            "Design robust Vector Database ingestion, chunking, and similarity retrieval workflows.",
            "Implement enterprise LLMOps: experiment tracking, latency management, streaming, and cost monitoring.",
            "Evaluate production user experience paradigms: Time to First Token (TTFT) and graceful error recovery."
        ],
        "problem_statement": "Developing a successful generative AI application requires bridging the gap between raw model endpoints and interactive user experiences. While training and prompting produce functional outputs, enterprise software requires authentication, state management, persistent memory, retrieval across proprietary documents, low latency, and intuitive interfaces. Without rapid prototyping tools, engineering teams waste weeks building boilerplate infrastructure before validating core product hypotheses. Fast prototyping enables iterative experimentation and rapid user feedback.",
        "theoretical_framework": """<p><strong>The Generative AI Application Stack:</strong></p>
<ul>
<li><strong>Presentation Layer (UI):</strong> Rapid interactive interfaces built with Streamlit, Gradio, or Next.js that support streaming text, file uploads, parameter sliders, and chat message history.</li>
<li><strong>Orchestration Layer:</strong> Frameworks (LangChain, LlamaIndex) that manage prompt templating, multi-turn conversational memory, output parsing, and dynamic tool routing.</li>
<li><strong>Retrieval & Knowledge Layer (RAG):</strong> Document parsers (PyPDF, Unstructured), semantic chunking algorithms, embedding models, and vector databases (Pinecone, Chroma, Qdrant) that surface relevant context.</li>
<li><strong>Foundation Model Layer:</strong> Commercial API endpoints (Google Gemini, OpenAI) or self-hosted open-weights inference engines (vLLM, Ollama, TGI).</li>
<li><strong>LLMOps & Observability:</strong> Tracking platforms (Weights & Biases, LangSmith, Arize) that monitor prompt versions, token consumption, latency, and hallucination rates.</li>
</ul>
<p><strong>The Mechanics of Chunking & Dense Retrieval:</strong> Unstructured documents are broken into chunks (e.g. 500 tokens with 50-token overlap). An embedding model maps chunks to dense vectors in high-dimensional space. User queries are embedded with the same model, and Approximate Nearest Neighbor (ANN) search retrieves top-k chunks based on cosine similarity.</p>""",
        "implementation_guide": """<p>Best practices for building responsive AI prototypes in Streamlit:</p>
<ol>
<li><strong>Stream Token Outputs:</strong> Never make users wait for complete 1,000-token generations. Use generator functions and Streamlit's `st.write_stream` to stream tokens in real time, minimizing perceived latency.</li>
<li><strong>Leverage Session State:</strong> Manage conversation history and tool states persistently using `st.session_state` across component reruns.</li>
<li><strong>Implement Defensive Error Trapping:</strong> Wrap API calls in retry loops with exponential backoff to handle rate limits and network dropouts gracefully.</li>
<li><strong>Optimize Chunking Strategies:</strong> Use recursive character text splitters that prioritize semantic boundaries (paragraphs, code blocks) over arbitrary character counts.</li>
</ol>""",
        "exercises": [
            "Build a minimal Streamlit app that accepts user input, queries a mock vector store, and streams an LLM response.",
            "Evaluate the latency and cost trade-offs between dense vector retrieval alone versus vector retrieval followed by cross-encoder re-ranking.",
            "Formulate an LLMOps monitoring dashboard specification tracking token throughput, user ratings, and latency percentiles (p50, p95, p99)."
        ]
    },
    "week_16_llm_alignment_responsible_ai": {
        "page_title": "Reading - LLM Alignment and the Responsible Use of Generative AI",
        "header_title": "Week 16: LLM Alignment and the Responsible Use of Generative AI",
        "icon": "fa-balance-scale",
        "pdf_filename": "[Slides] Week 16 - GAI Notes.pdf",
        "pdf_display_title": "Briefing Slide Deck & Speaker Notes: Week 16 LLM Alignment and Responsible AI",
        "objectives": [
            "Define the Alignment Problem and analyze the tensions within the Helpful, Harmless, and Honest (HHH) framework.",
            "Examine Reinforcement Learning from Human Feedback (RLHF) and Proximal Policy Optimization (PPO).",
            "Understand Constitutional AI (RLAIF) and automated self-critique mechanisms.",
            "Analyze Direct Preference Optimization (DPO) and reference-free preference modeling.",
            "Examine adversarial vulnerabilities: prompt injection, jailbreaking, data poisoning, and enterprise red teaming."
        ],
        "problem_statement": "Pre-training language models on raw internet text teaches them to predict human language, including hate speech, biological weapon synthesis, malicious code, and deceptive propaganda. An unaligned model has raw capability without human values. As AI systems become more autonomous and integrated into critical infrastructure, technical alignment and responsible deployment frameworks are essential to ensure models remain beneficial, trustworthy, safe, and accountable to human society.",
        "theoretical_framework": """<p><strong>The Alignment Problem & The HHH Taxonomy:</strong> Alignment is the technical discipline of ensuring an AI's behavior conforms to intended human objectives and ethical standards. The industry standard framework evaluates three axes:</p>
<ul>
<li><strong>Helpful:</strong> The model accurately understands and fulfills user instructions.</li>
<li><strong>Harmless:</strong> The model refuses to generate illegal, dangerous, hateful, or abusive content.</li>
<li><strong>Honest:</strong> The model conveys accurate information and expresses calibrated confidence, avoiding deception and hallucination.</li>
</ul>
<p><strong>The Alignment Methodology Continuum:</strong></p>
<ol>
<li><strong>Reinforcement Learning from Human Feedback (RLHF):</strong> Human annotators rank candidate model completions. A reward model is trained on these pairwise preferences. Then, Proximal Policy Optimization (PPO) fine-tunes the generative policy to maximize predicted reward while penalizing drift from the base model via KL-divergence.</li>
<li><strong>Constitutional AI (RLAIF):</strong> Replaces human preference labeling with AI self-critique guided by a written 'constitution' of safety and fairness principles.</li>
<li><strong>Direct Preference Optimization (DPO):</strong> Solves the RLHF objective directly using cross-entropy loss over preferred vs dispreferred completions, eliminating the complexity and instability of training separate reward models and RL policy networks.</li>
</ol>""",
        "implementation_guide": """<p>Enterprise guardrails and responsible deployment protocols:</p>
<ol>
<li><strong>Structured Red Teaming:</strong> Systematically subject models to adversarial attacks (hypothetical framing, roleplay jailbreaks, encoding obfuscation) before public release.</li>
<li><strong>Input and Output Guardrails:</strong> Deploy lightweight secondary classifiers (e.g., Llama-Guard, NeMo Guardrails) to scan user queries and model outputs for policy violations in real time.</li>
<li><strong>Calibrated Refusals:</strong> Train models to refuse harmful requests neutrally without preachiness, patronizing tone, or false positives on benign educational queries.</li>
<li><strong>Socio-Technical Governance:</strong> Pair technical alignment with institutional governance: human auditing, transparent model cards, and clear escalation pathways for automated mistakes.</li>
</ol>""",
        "exercises": [
            "Analyze a refusal dilemma where being helpful directly conflicts with being harmless, and formulate the model's ideal response.",
            "Compare the operational complexity, cost, and bias profiles of RLHF with human annotators versus Constitutional AI with model self-critique.",
            "Design a 5-point red teaming test suite targeting demographic bias in an automated hiring screening assistant."
        ]
    }
}


def build_reading_html(page_data: dict) -> str:
    objectives_li = "\n".join([f"<li>{html.escape(obj)}</li>" for obj in page_data["objectives"]])
    exercises_li = "\n".join([f"<li>{html.escape(ex)}</li>" for ex in page_data["exercises"]])
    
    # URL encode the PDF filename for the link href
    pdf_href = f"$IMS-CC-FILEBASE$/slides/{html.escape(page_data['pdf_filename']).replace(' ', '%20')}?canvas_=1&amp;canvas_qs_wrap=1"

    return f"""<html>
<head>
<meta http-equiv="Content-Type" content="text/html; charset=utf-8"/>
<title>{html.escape(page_data['page_title'])}</title>
<meta name="editing_roles" content="teachers"/>
<meta name="workflow_state" content="active"/>
<meta name="editor_type" content="rce"/>
</head>
<body>
<div id="dp-wrapper" class="dp-wrapper dp-hdg-txt-h4-dp-primary dp-hdg-txt-h5-dp-primary dp-hdg-txt-h6-dp-primary dp-hdg-brdr-h3-1 dp-hdg-brdr-h5-1 dp-hdg-brdr-h6-1 dp-hdg-i-txt-h5-dp-primary dp-hdg-i-txt-h6-dp-primary dp-hdg-i-txt-h4-dp-primary dp-hdg-d-h4-table-l dp-hdg-d-h5-table-l dp-hdg-d-h6-table-l dp-hdg-i-bg-h2-dp-primary dp-hdg-i-sz-h2-in dp-hdg-i-sz-h3-in dp-hdg-i-sz-h5-in dp-hdg-i-sz-h6-in dp-hdg-i-styl-h2-brdr-b dp-hdg-i-cp-brdr-h2-dp-secondary dp-hdg-i-cp-brdr-h3-dp-secondary dp-hdg-i-cp-brdr-h4-dp-secondary dp-hdg-i-cp-brdr-h5-dp-secondary dp-hdg-i-brdr-h2-4 dp-hdg-i-brdr-h5-4 dp-hdg-i-brdr-h6-4 dp-hdg-i-cp-brdr-h6-dp-secondary dp-hdg-txt-h2-dp-primary dp-hdg-txt-h3-dp-primary dp-hdg-i-styl-h3-brdr-b dp-hdg-i-brdr-h3-2 dp-hdg-b-h2-brdr-b dp-hdg-brdr-h2-1 dp-hdg-cp-brdr-h2-dp-gray dp-hdg-b-h3-brdr-b dp-hdg-cp-brdr-h3-dp-gray dp-hdg-i-bg-h3-dp-primary dp-hdg-i-sz-h4-in dp-hdg-b-h4-brdr-b dp-hdg-cp-brdr-h4-dp-gray dp-hdg-i-styl-h4-brdr-b dp-hdg-i-brdr-h4-4" data-header-class="dp-header dp-basic-color dp-header-out-dp-secondary dp-header-s-brdr-b dp-header-title-txt-tl dp-header-pre-out-dp-secondary dp-header-sub-bg-dp-primary dp-header-desc-bg-dp-white dp-header-brdr-w-2 cp-bg-dp-primary">
<header class="dp-header dp-badge"></header>
<header class="dp-header dp-basic-color dp-header-out-dp-secondary dp-header-s-brdr-b dp-header-title-txt-tl dp-header-pre-out-dp-secondary dp-header-sub-bg-dp-primary dp-header-desc-bg-dp-white dp-header-brdr-w-2 cp-bg-dp-primary">
<h2 class="dp-heading dp-has-icon"><i class="dp-icon fas {page_data['icon']}" aria-hidden="true"><span class="dp-icon-content" style="display: none;">&nbsp;</span></i> <span class="dp-header-title">{html.escape(page_data['header_title'])}</span></h2>
</header>
<div class="dp-column-container container-fluid">
<div class="row">
<div class="col-12">
<div style="float: right; width: 35%; min-width: 280px; margin-left: 20px; margin-bottom: 20px;">
<div class="dp-card card dp-shadow-b6 cp-bg-dp-primary">
<h4 class="dp-has-icon dp-locked"><i class="dp-icon fas fa-bullseye cp-bg-dp-primary" aria-hidden="true"><span class="dp-icon-content" style="display: none;">&nbsp;</span></i> <span style="color: #ffffff;"><strong>Unit Objectives</strong></span></h4>
<div class="card-body">
<ul>
{objectives_li}
</ul>
</div>
</div>
</div>

<h3 class="dp-has-icon"><i class="dp-icon fas fa-link" aria-hidden="true"><span class="dp-icon-content" style="display: none;">&nbsp;</span></i> <strong><span class="selected">Required Reading &amp; Slide Deck</span></strong></h3>
<p><a class="instructure_file_link inline_disabled" href="{pdf_href}" target="_blank"><strong>{html.escape(page_data['pdf_display_title'])}</strong></a></p>

<h3 class="dp-has-icon"><i class="dp-icon fas fa-cogs" aria-hidden="true"><span class="dp-icon-content" style="display: none;">&nbsp;</span></i> <strong><span class="selected">The Problem Statement</span></strong></h3>
<p>{page_data['problem_statement']}</p>
<hr class="dp-hr-color-dp-primary w-100 dp-hr-pill">

<h3 class="dp-has-icon"><i class="dp-icon fas fa-sitemap" aria-hidden="true"><span class="dp-icon-content" style="display: none;">&nbsp;</span></i> <strong><span class="selected">Theoretical Framework</span></strong></h3>
{page_data['theoretical_framework']}

<h3 class="dp-has-icon"><i class="dp-icon fas fa-laptop-code" aria-hidden="true"><span class="dp-icon-content" style="display: none;">&nbsp;</span></i> <strong><span class="selected">Implementation Guide</span></strong></h3>
{page_data['implementation_guide']}
<hr class="dp-hr-color-dp-primary w-100 dp-hr-pill">

<div class="dp-callout dp-callout-placeholder card dp-callout-position-default dp-shadow-r2 dp-callout-color-dp-primary dp-callout-type-info rounded-0 dp-callout-pos-default w-100">
<div class="dp-callout-side-emphasis"><i class="fas fa-terminal dp-default-icon dp-locked"><span class="dp-icon-content" style="display: none;">&nbsp;</span></i></div>
<div class="card-body">
<h4 class="card-title dp-font-oswald">Conceptual Exercises &amp; Applications</h4>
<hr class="dp-hr-pill dp-hr-color-dp-secondary float-clear dp-margin-direction-all w-50 dp-locked" style="margin: 5px;">
<p>To deepen your comprehension of this unit's concepts and prepare for the weekly discussion board and hands-on lab, reflect on the following exploratory challenges:</p>
<ul>
{exercises_li}
</ul>
</div>
</div>

</div>
</div>
</div>
<p>&nbsp;</p>
</div>
</body>
</html>"""


def main():
    base_units_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), "../units"))
    print("Authoring 9 DesignPLUS-compliant reading pages...")

    for key, pdata in READING_PAGES.items():
        unit_dir = os.path.join(base_units_dir, key)
        os.makedirs(unit_dir, exist_ok=True)

        full_html = build_reading_html(pdata)
        html_path = os.path.join(unit_dir, "reading.html")
        with open(html_path, "w", encoding="utf-8") as f:
            f.write(full_html)

        print(f"[Reading Page] Generated {pdata['page_title']} -> {html_path}")

    print("\nTask 5 Complete: All 9 reading pages authored with DesignPLUS styling and PDF links!")


if __name__ == "__main__":
    main()
