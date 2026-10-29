#!/usr/bin/env python3
"""
Quiz Cleaner & QTI Builder for AIML 1010 Update
Audits, cleans, corrects, and compiles all 9 quizzes into standard Markdown and QTI 1.2 XML.
"""

import os
import sys
import json

# Ensure canvas-course-builder scripts are importable
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
REPO_ROOT = os.path.abspath(os.path.join(SCRIPT_DIR, "../../.."))
CCB_SCRIPTS = os.path.join(REPO_ROOT, ".agents/skills/canvas-course-builder/scripts")
sys.path.insert(0, CCB_SCRIPTS)

from qti_builder import parse_quiz_md, package_quiz, make_canvas_id

QUIZZES = {
    "module_01_agentic_ai": {
        "title": "Module 01 Knowledge Check: Demystifying Agentic AI",
        "questions": [
            {
                "num": 1,
                "prompt": "What is the most fundamental characteristic that defines any AI Agent?",
                "options": [
                    ("A", "Operates exclusively in a fully observable, deterministic, and static environment"),
                    ("B", "Relies strictly on hardcoded rules without learning or perceptual capabilities"),
                    ("C", "Possesses human-level consciousness and general artificial intelligence"),
                    ("D", "Perceives its environment through sensors/inputs and autonomously takes actions to achieve goals")
                ],
                "correct": "D",
                "rationale": "An AI agent is fundamentally defined by its perception-action cycle: perceiving an environment and executing actions autonomously toward a specific objective."
            },
            {
                "num": 2,
                "prompt": "What is the primary advantage of a Model-based Reflex Agent over a Simple Reflex Agent?",
                "options": [
                    ("A", "It evaluates sequences of actions based on a mathematical utility function"),
                    ("B", "It maintains an internal state to track unobserved aspects of the partially observable environment"),
                    ("C", "It guarantees selecting the globally optimal action by computing all future possibilities"),
                    ("D", "It directly maps immediate sensory inputs to actions using condition-action rules without memory")
                ],
                "correct": "B",
                "rationale": "Model-based reflex agents maintain internal state representing the world that cannot currently be seen, overcoming the limitation of simple reflex agents in partially observable worlds."
            },
            {
                "num": 3,
                "prompt": "What is the key differentiator between Agentic AI and conventional AI systems?",
                "options": [
                    ("A", "Agentic AI focuses solely on generating human-like creative writing, while conventional AI focuses on automation"),
                    ("B", "Agentic AI and conventional AI are identical terms used interchangeably in industry"),
                    ("C", "Agentic AI demonstrates autonomous goal decomposition, tool use, and multi-step iterative action, rather than just single-turn predictions"),
                    ("D", "Agentic AI is restricted to offline data processing without interacting with external environments")
                ],
                "correct": "C",
                "rationale": "Agentic AI moves beyond single-turn prompt-response interactions to systems that autonomously plan, call tools, reflect on intermediate outputs, and execute multi-step workflows."
            },
            {
                "num": 4,
                "prompt": "In the context of Agentic AI, what does the Tooling (or Function Calling) module primarily enable the agent to do?",
                "options": [
                    ("A", "Permanently fine-tune the base model weights on local user data"),
                    ("B", "Evaluate internal token logits against human preference benchmarks"),
                    ("C", "Convert natural language prompts into compressed vector embeddings"),
                    ("D", "Interact with external software, APIs, calculators, and databases to perform actions beyond internal reasoning")
                ],
                "correct": "D",
                "rationale": "Tool calling allows an LLM agent to bridge the gap between static model weights and dynamic external environments—querying APIs, querying databases, running code, and triggering actions."
            },
            {
                "num": 5,
                "prompt": "What is the primary focus of the Reflection phase in an agentic workflow?",
                "options": [
                    ("A", "Reviewing the outcome of past actions/plans and adjusting internal strategy for subsequent steps"),
                    ("B", "Tokenizing input prompts into subword integer arrays"),
                    ("C", "Compressing long context windows into fixed-size summary embeddings"),
                    ("D", "Generating random alternative responses to increase temperature")
                ],
                "correct": "A",
                "rationale": "Self-reflection allows agents to critique their own intermediate outputs, identify errors or failed tool calls, and refine their execution plans iteratively."
            },
            {
                "num": 6,
                "prompt": "Which two factors must a Goal-based Agent primarily consider when selecting an action?",
                "options": [
                    ("A", "The current system clock and total memory allocation"),
                    ("B", "The target goal state and the predicted outcomes of candidate actions"),
                    ("C", "The hardware GPU architecture and compiler optimization flags"),
                    ("D", "The length of historical user prompts and token budgets")
                ],
                "correct": "B",
                "rationale": "Goal-based agents combine knowledge of current states with goal descriptions and world models to evaluate how candidate actions bring the agent closer to the desired goal."
            },
            {
                "num": 7,
                "prompt": "Which characteristic best defines a Utility-based Agent?",
                "options": [
                    ("A", "It selects actions solely based on binary goal achievement, ignoring preferences or efficiency"),
                    ("B", "It reacts strictly to real-time inputs without tracking history or future consequences"),
                    ("C", "It follows an immutable hardcoded decision tree regardless of context"),
                    ("D", "It uses a continuous utility function to weigh trade-offs and choose the most desirable or optimal outcome among competing goals")
                ],
                "correct": "D",
                "rationale": "Utility-based agents map states to real numbers (utility), enabling principled trade-off analysis when multiple conflicting goals exist or when success is probabilistic."
            },
            {
                "num": 8,
                "prompt": "Which of the following is a key capability that differentiates Agentic AI from traditional standalone LLMs?",
                "options": [
                    ("A", "Ability to predict the next token in a static prompt"),
                    ("B", "Autonomous multi-step execution using external tools, error-checking, and memory without requiring human prompts at every sub-step"),
                    ("C", "Generation of grammatically correct English responses"),
                    ("D", "Processing inputs using Transformer self-attention mechanisms")
                ],
                "correct": "B",
                "rationale": "Traditional LLMs generate single responses to static prompts. Agentic AI loops autonomously: taking actions, receiving feedback from tools/environments, and continuing until the objective is achieved."
            },
            {
                "num": 9,
                "prompt": "In an Agentic AI architecture, what is a 'tool'?",
                "options": [
                    ("A", "The pre-training dataset used to train the base foundational model"),
                    ("B", "The GPU cluster executing tensor floating-point calculations"),
                    ("C", "The internal activation function inside multi-head attention layers"),
                    ("D", "An external function, API, script, or service that the model can invoke via structured schema to interact with the world")
                ],
                "correct": "D",
                "rationale": "A tool in agentic systems is an executable software interface (API, database connector, calculator, bash terminal) described by a schema that the agent calls to interact with reality."
            },
            {
                "num": 10,
                "prompt": "Which statement best characterizes modern Human-AI collaboration in Agentic AI systems?",
                "options": [
                    ("A", "Humans are entirely replaced across all enterprise decision loops"),
                    ("B", "Humans act as supervisors and collaborators (Human-in-the-Loop), providing high-level intent, guardrails, and approvals while agents handle execution"),
                    ("C", "AI agents operate with complete unmonitored autonomy in mission-critical legal and medical settings"),
                    ("D", "Humans only interact with agents during initial model weights compilation")
                ],
                "correct": "B",
                "rationale": "Effective agentic systems utilize Human-in-the-Loop (HITL) patterns: agents handle high-throughput discovery, synthesis, and execution, while humans steer strategy, review sensitive actions, and provide governance."
            }
        ]
    },
    "week_03_prompt_engineering_i": {
        "title": "Week 03 Knowledge Check: Prompt Engineering I",
        "questions": [
            {
                "num": 1,
                "prompt": "What is the primary focus of prompt engineering in generative AI?",
                "options": [
                    ("A", "Modifying neural network weights through gradient descent"),
                    ("B", "Task-specific optimization of input instructions to elicit desired outputs without altering model weights"),
                    ("C", "Generating synthetic pre-training corpora for foundation models"),
                    ("D", "Developing low-level GPU acceleration kernels for matrix multiplication")
                ],
                "correct": "B",
                "rationale": "Prompt engineering focuses on formulating, refining, and structuring textual inputs to guide frozen LLMs toward optimal outputs for specific tasks."
            },
            {
                "num": 2,
                "prompt": "In the RGC (Role, Goal, Context) prompting framework, what is the primary role of the 'Role' component?",
                "options": [
                    ("A", "Specifying the programming language used to format output tokens"),
                    ("B", "Establishing the persona, domain expertise, and tone the model should adopt in its response"),
                    ("C", "Providing example input-output pairs for few-shot in-context learning"),
                    ("D", "Restricting the total parameter count utilized during model inference")
                ],
                "correct": "B",
                "rationale": "Assigning a Role (e.g., 'Act as a senior cybersecurity auditor') steers the model's latent representation toward domain-relevant vocabulary, conventions, and depth."
            },
            {
                "num": 3,
                "prompt": "What is the key difference between Zero-Shot prompting and Few-Shot prompting?",
                "options": [
                    ("A", "Zero-shot uses no context, while few-shot requires fine-tuning weights on thousands of labeled examples"),
                    ("B", "Zero-shot prompts provide task instructions without demonstrations, while few-shot prompts include one or more input-output examples directly in the context"),
                    ("C", "Zero-shot runs on CPU, while few-shot requires specialized GPU clusters"),
                    ("D", "Zero-shot only works for classification, while few-shot only works for code generation")
                ],
                "correct": "B",
                "rationale": "Zero-shot relies entirely on the model's pre-trained knowledge without task examples. Few-shot provides in-context demonstrations to establish pattern and format."
            },
            {
                "num": 4,
                "prompt": "Why is specifying output format (e.g., JSON, markdown table) in a prompt crucial for production applications?",
                "options": [
                    ("A", "It prevents the model from consuming GPU memory"),
                    ("B", "It guarantees the model cannot hallucinate factual data"),
                    ("C", "It enables deterministic downstream parsing and seamless software integration"),
                    ("D", "It automatically fine-tunes the model on user schema")
                ],
                "correct": "C",
                "rationale": "Enforcing structured schemas like JSON ensures automated parsers and downstream APIs can ingest model outputs reliably without human manual reformatting."
            },
            {
                "num": 5,
                "prompt": "What does 'delimiters' (such as triple backticks or XML tags) achieve when crafting complex prompts?",
                "options": [
                    ("A", "Increases model inference speed by skipping tokenization"),
                    ("B", "Clearly separates instructions from reference content, preventing prompt injection and contextual confusion"),
                    ("C", "Encrypts sensitive data before transmission to the inference server"),
                    ("D", "Forces the model to execute embedded code directly in sandbox")
                ],
                "correct": "B",
                "rationale": "Delimiters create explicit structural boundaries so the model understands which text constitutes instructions and which text is raw data to be analyzed."
            },
            {
                "num": 6,
                "prompt": "Which of the following is considered a prompt engineering anti-pattern?",
                "options": [
                    ("A", "Providing clear, concise positive instructions on what to do"),
                    ("B", "Vague, open-ended instructions like 'Write something about AI' without specifying audience, length, or goals"),
                    ("C", "Using few-shot demonstrations with diverse examples"),
                    ("D", "Specifying constraints and edge cases explicitly")
                ],
                "correct": "B",
                "rationale": "Vague instructions leave too much variance in the model's probability distribution, leading to generic, irrelevant, or unhelpful responses."
            },
            {
                "num": 7,
                "prompt": "How does the 'Context' component in the RGC framework improve output quality?",
                "options": [
                    ("A", "By grounding the model with background facts, constraints, and source data to reduce generic speculation"),
                    ("B", "By retraining the neural network's self-attention heads"),
                    ("C", "By bypassing the model's safety alignment filters"),
                    ("D", "By increasing the temperature hyperparameter")
                ],
                "correct": "A",
                "rationale": "Providing explicit context gives the model domain-specific grounding data, significantly reducing hallucination and aligning responses to the real scenario."
            },
            {
                "num": 8,
                "prompt": "What is the primary benefit of 'system prompts' compared to standard user prompts in LLM APIs?",
                "options": [
                    ("A", "System prompts set foundational behavioral rules and persistent constraints that govern the entire multi-turn interaction"),
                    ("B", "System prompts bypass billing costs for API users"),
                    ("C", "System prompts are only readable by human developers, not the model"),
                    ("D", "System prompts can only be written in compiled binary format")
                ],
                "correct": "A",
                "rationale": "System messages establish high-level behavioral bounds, persona, safety policies, and operating constraints that persist throughout a conversation session."
            },
            {
                "num": 9,
                "prompt": "When asking an LLM to perform complex reasoning, why is 'Think step by step' effective?",
                "options": [
                    ("A", "It increases model parameter weights during runtime"),
                    ("B", "It encourages the model to generate intermediate reasoning tokens, giving the attention mechanism computational space to derive the correct conclusion"),
                    ("C", "It causes the model to search external search engines automatically"),
                    ("D", "It compresses the context window to reduce latency")
                ],
                "correct": "B",
                "rationale": "Because Transformers predict one token at a time, generating explicit reasoning steps provides intermediate context that guides subsequent tokens toward correct mathematical and logical deductions."
            },
            {
                "num": 10,
                "prompt": "Which prompt engineering technique is best suited for categorizing customer support tickets into defined department queues?",
                "options": [
                    ("A", "Few-shot classification with explicit schema, examples for each category, and a specified fallback class"),
                    ("B", "Unconstrained creative story generation"),
                    ("C", "High temperature sampling without instructions"),
                    ("D", "Omitting category labels so the model invents its own taxonomy")
                ],
                "correct": "A",
                "rationale": "Classification tasks require deterministic mapping: few-shot examples for each category combined with strict output schema ensure predictable, reliable categorization."
            }
        ]
    },
    "week_04_prompt_engineering_ii": {
        "title": "Week 04 Knowledge Check: Prompt Engineering II",
        "questions": [
            {
                "num": 1,
                "prompt": "What is the primary benefit of Chain-of-Thought (CoT) prompting?",
                "options": [
                    ("A", "Generating high-resolution raster graphic images"),
                    ("B", "Decomposing complex multi-step reasoning problems into sequential, verifiable steps"),
                    ("C", "Reducing the total number of output tokens generated by the model"),
                    ("D", "Synthesizing real-time audio streams without latency")
                ],
                "correct": "B",
                "rationale": "CoT prompts encourage models to break down complex mathematical, logical, and symbolic reasoning tasks into explicit sequential intermediate steps."
            },
            {
                "num": 2,
                "prompt": "How does the ReAct (Reasoning + Acting) prompting framework enhance LLM problem-solving?",
                "options": [
                    ("A", "It alternates between generating reasoning thoughts and executing tool actions to observe environment feedback"),
                    ("B", "It fine-tunes all attention layers using supervised gradient descent"),
                    ("C", "It restricts the model to pure internal thinking without any external tool access"),
                    ("D", "It compresses text prompts into latent audio representations")
                ],
                "correct": "A",
                "rationale": "ReAct combines reasoning traces ('Thought') with task-specific actions ('Action' / tool calls) and environment feedback ('Observation') to dynamically adapt and solve tasks."
            },
            {
                "num": 3,
                "prompt": "What is 'Directional Stimulus Prompting'?",
                "options": [
                    ("A", "Providing a small hint or guiding keyword (stimulus) that steers the model's generation toward specific desired aspects"),
                    ("B", "Hardware beam-steering on GPU tensor cores"),
                    ("C", "Translating user prompts into magnetic directional pulses"),
                    ("D", "Running prompt iterations backwards from end to start")
                ],
                "correct": "A",
                "rationale": "Directional stimulus prompting guides the LLM by injecting specific hints, target keywords, or key phrases to steer output focus without rigid manual drafting."
            },
            {
                "num": 4,
                "prompt": "What is 'Prompt Chaining' in generative AI workflows?",
                "options": [
                    ("A", "Connecting multiple models on separate GPU nodes via physical cables"),
                    ("B", "Breaking a large, complex workflow into sequential sub-tasks where the output of one prompt becomes the input to the next"),
                    ("C", "Repeating the exact same prompt multiple times in a single query"),
                    ("D", "Enforcing blockchain consensus algorithms on prompt tokens")
                ],
                "correct": "B",
                "rationale": "Prompt chaining modularizes complex workflows: step 1 extracts data, step 2 validates it, step 3 transforms it, improving reliability and debuggability."
            },
            {
                "num": 5,
                "prompt": "What is 'Self-Consistency' prompting in Chain-of-Thought reasoning?",
                "options": [
                    ("A", "Sampling multiple independent reasoning paths at temperature > 0 and selecting the most consistent majority answer"),
                    ("B", "Ensuring that the model always generates the exact same tokens every run"),
                    ("C", "Fine-tuning the model to agree with all user opinions"),
                    ("D", "Running self-attention only within individual sentences")
                ],
                "correct": "A",
                "rationale": "Self-consistency generates multiple reasoning trajectories for a problem and picks the most frequent final answer, significantly boosting mathematical and reasoning accuracy."
            },
            {
                "num": 6,
                "prompt": "Which vulnerability describes a prompt maliciously designed to override developer system instructions?",
                "options": [
                    ("A", "Buffer Overflow"),
                    ("B", "Prompt Injection / Jailbreak"),
                    ("C", "Gradient Inversion"),
                    ("D", "Cross-Site Scripting (XSS)")
                ],
                "correct": "B",
                "rationale": "Prompt injection occurs when untrusted user input tricks the model into ignoring system instructions, leaking confidential prompts, or bypassing safety guardrails."
            },
            {
                "num": 7,
                "prompt": "What is 'Tree of Thoughts' (ToT) prompting?",
                "options": [
                    ("A", "A hierarchical framework that explores multiple reasoning branches, evaluates intermediate thoughts, and backtracks when necessary"),
                    ("B", "Organizing training corpora into binary search trees before tokenization"),
                    ("C", "Restricting the model to taxonomic biological tree classifications"),
                    ("D", "A random forest algorithm operating alongside a neural network")
                ],
                "correct": "A",
                "rationale": "Tree of Thoughts generalizes Chain of Thought by allowing models to explore multiple heuristic reasoning branches, look ahead, self-evaluate, and backtrack."
            },
            {
                "num": 8,
                "prompt": "How does Least-to-Most prompting differ from standard Chain-of-Thought prompting?",
                "options": [
                    ("A", "It first explicitly decomposes a complex problem into simpler sub-problems, then solves them sequentially from easiest to hardest"),
                    ("B", "It uses the smallest available model for the final response"),
                    ("C", "It eliminates all intermediate reasoning tokens to minimize latency"),
                    ("D", "It trains the model with the minimum number of dataset tokens")
                ],
                "correct": "A",
                "rationale": "Least-to-most prompting first breaks down a problem into ordered sub-questions, solving simpler prerequisite components before tackling the overarching challenge."
            },
            {
                "num": 9,
                "prompt": "What is the primary role of an 'Evaluator-Optimizer' prompt loop?",
                "options": [
                    ("A", "One prompt generates a candidate draft, a second evaluator prompt critiques it against criteria, and feedback iterates until quality thresholds are met"),
                    ("B", "A hardware optimizer that scales GPU core clock speeds"),
                    ("C", "A script that automatically lowers user API subscription tiers"),
                    ("D", "A database query optimizer that indexes prompt text")
                ],
                "correct": "A",
                "rationale": "In evaluator-optimizer loops, one LLM call generates solutions while another call acts as an adversarial or rubric-based judge, prompting revisions until satisfactory."
            },
            {
                "num": 10,
                "prompt": "Why are defensive system instructions and output format constraints important when building agentic prompt pipelines?",
                "options": [
                    ("A", "To prevent unexpected schema drift, protect against untrusted data execution, and ensure deterministic downstream handling"),
                    ("B", "To force the model to compile code directly in the client browser"),
                    ("C", "To eliminate the need for any testing or software verification"),
                    ("D", "To disable all model reasoning capabilities")
                ],
                "correct": "A",
                "rationale": "Defensive prompting insulates automated workflows from prompt injection attacks, ensures predictable JSON/data serialization, and protects tool-calling integrity."
            }
        ]
    },
    "week_10_transformers_llm_evolution": {
        "title": "Week 10 Knowledge Check: Transformers and Evolution of Large Language Models",
        "questions": [
            {
                "num": 1,
                "prompt": "What major architectural breakthrough did the 2017 paper 'Attention Is All You Need' introduce to replace recurrent connections (RNNs)?",
                "options": [
                    ("A", "Convolutional feature maps"),
                    ("B", "Multi-Head Self-Attention mechanisms"),
                    ("C", "Gated Recurrent Units (GRUs)"),
                    ("D", "Support Vector Machines (SVMs)")
                ],
                "correct": "B",
                "rationale": "The Transformer architecture eliminated recurrent loops in favor of multi-head self-attention, allowing models to process entire sequences in parallel and capture long-range dependencies."
            },
            {
                "num": 2,
                "prompt": "Why does self-attention enable massive scaling compared to traditional Recurrent Neural Networks (RNNs)?",
                "options": [
                    ("A", "RNNs require sequential token-by-token processing where step t depends on step t-1, while self-attention processes all tokens in parallel"),
                    ("B", "RNNs only work on audio data, while self-attention works on text"),
                    ("C", "Self-attention requires zero training data"),
                    ("D", "RNNs have fixed vocabulary sizes of under 100 words")
                ],
                "correct": "A",
                "rationale": "RNNs suffer from sequential processing bottlenecks. Self-attention enables full parallelization across GPU hardware, unlocking modern foundation model scale."
            },
            {
                "num": 3,
                "prompt": "What are the two primary sub-layers found within each Transformer encoder block?",
                "options": [
                    ("A", "Convolutional layer and MaxPooling layer"),
                    ("B", "Multi-Head Self-Attention mechanism and a Feed-Forward Neural Network (with residual connections and normalization)"),
                    ("C", "Softmax classifier and k-Nearest Neighbors clustering"),
                    ("D", "Recurrent LSTM cell and Dropout layer")
                ],
                "correct": "B",
                "rationale": "Each standard encoder layer contains a multi-head self-attention sub-layer followed by a position-wise fully connected feed-forward network, wrapped in residual connections."
            },
            {
                "num": 4,
                "prompt": "What activation function is typically applied at the final output projection of a Transformer decoder to produce token probability distributions?",
                "options": [
                    ("A", "ReLU"),
                    ("B", "Sigmoid"),
                    ("C", "Softmax"),
                    ("D", "Hyperbolic Tangent (Tanh)")
                ],
                "correct": "C",
                "rationale": "Softmax normalizes raw output logits into a valid probability distribution over the model's vocabulary, summing to 1.0."
            },
            {
                "num": 5,
                "prompt": "What is the primary function of positional encodings in Transformer architectures?",
                "options": [
                    ("A", "To inject information about the order/position of tokens in the sequence, since self-attention contains no inherent recurrent or spatial order"),
                    ("B", "To compress model weights into 8-bit integers"),
                    ("C", "To encrypt user prompts during inference"),
                    ("D", "To filter out grammatical stop words")
                ],
                "correct": "A",
                "rationale": "Self-attention is permutation-invariant. Positional encodings (sinusoidal or learned) are added to token embeddings to communicate sequence order."
            },
            {
                "num": 6,
                "prompt": "Which of the following correctly pairs a Transformer architecture type with its representative model?",
                "options": [
                    ("A", "Encoder-only: GPT; Decoder-only: BERT"),
                    ("B", "Encoder-only: BERT; Decoder-only: GPT; Encoder-Decoder: T5"),
                    ("C", "Encoder-only: T5; Decoder-only: BERT; Encoder-Decoder: GPT"),
                    ("D", "Encoder-only: ResNet; Decoder-only: YOLO; Encoder-Decoder: VGG")
                ],
                "correct": "B",
                "rationale": "BERT is an encoder-only model (masked language modeling); GPT is a decoder-only model (autoregressive causal generation); T5 is an encoder-decoder model (sequence-to-sequence)."
            },
            {
                "num": 7,
                "prompt": "True or False: BERT is an autoregressive generative model that predicts tokens from left to right.",
                "options": [
                    ("A", "True"),
                    ("B", "False")
                ],
                "correct": "B",
                "rationale": "BERT is an autoencoding (bidirectional) model trained with Masked Language Modeling (MLM), not an autoregressive left-to-right generator like GPT."
            },
            {
                "num": 8,
                "prompt": "In the standard Transformer pipeline, what component first converts raw input text into a sequence of integer IDs before embedding lookup?",
                "options": [
                    ("A", "Tokenizer"),
                    ("B", "Softmax"),
                    ("C", "Layer Normalization"),
                    ("D", "Residual Connection")
                ],
                "correct": "A",
                "rationale": "A tokenizer (such as Byte-Pair Encoding or WordPiece) maps raw text strings into discrete subword token identifiers."
            },
            {
                "num": 9,
                "prompt": "What do Query (Q), Key (K), and Value (V) represent in scaled dot-product attention?",
                "options": [
                    ("A", "Database SQL query parameters"),
                    ("B", "Linear projections of token embeddings used to compute attention weights (how much each token focuses on every other token)"),
                    ("C", "Hardware registers in GPU thread blocks"),
                    ("D", "Hyperparameters that define learning rate and weight decay")
                ],
                "correct": "B",
                "rationale": "Tokens project into Query, Key, and Value vectors. Attention is calculated by computing dot products between Q and K, scaling, taking softmax, and multiplying by V."
            },
            {
                "num": 10,
                "prompt": "What are the two foundational stages involved in training modern Large Language Models?",
                "options": [
                    ("A", "Unsupervised Pre-training on massive text corpora followed by Supervised Fine-Tuning / Alignment"),
                    ("B", "Feature engineering followed by polynomial regression"),
                    ("C", "Manual rule authoring followed by hardcoded compiling"),
                    ("D", "Data clustering followed by decision tree pruning")
                ],
                "correct": "A",
                "rationale": "LLM creation begins with compute-intensive pre-training on trillions of tokens to learn general language representation, followed by fine-tuning (SFT and RLHF) for task alignment."
            }
        ]
    },
    "week_11_diffusion_models_text_to_image": {
        "title": "Week 11 Knowledge Check: Diffusion Models and Text-to-Image Generation",
        "questions": [
            {
                "num": 1,
                "prompt": "What is the primary advantage of Diffusion Models compared to traditional Generative Adversarial Networks (GANs)?",
                "options": [
                    ("A", "They require significantly smaller training datasets"),
                    ("B", "They have more stable training dynamics and do not suffer from adversarial mode collapse"),
                    ("C", "They generate images instantaneously in a single forward pass"),
                    ("D", "They do not require any GPU acceleration")
                ],
                "correct": "B",
                "rationale": "GANs suffer from unstable min-max adversarial training and mode collapse. Diffusion models optimize standard variational bounds with stable mean squared error loss."
            },
            {
                "num": 2,
                "prompt": "How does the forward diffusion process operate in a Denoising Diffusion Probabilistic Model (DDPM)?",
                "options": [
                    ("A", "It progressively adds small amounts of Gaussian noise to an image over T timesteps until it becomes pure noise"),
                    ("B", "It sharpens an image by removing blur filters"),
                    ("C", "It compresses an image using JPEG encoding"),
                    ("D", "It generates an image from a random seed in one step")
                ],
                "correct": "A",
                "rationale": "The forward process is a fixed Markov chain that systematically adds Gaussian noise to data according to a variance schedule until data structure is destroyed."
            },
            {
                "num": 3,
                "prompt": "What is the neural network (typically a U-Net or DiT) trained to predict during the reverse diffusion process?",
                "options": [
                    ("A", "The RGB color histogram of the original image"),
                    ("B", "The specific noise component added at timestep t, allowing the system to subtract it and denoise"),
                    ("C", "The camera focal length used to take the picture"),
                    ("D", "The text sentiment of the user prompt")
                ],
                "correct": "B",
                "rationale": "The reverse process neural network learns to predict the noise vector present at step t, enabling iterative denoising to recover clear images."
            },
            {
                "num": 4,
                "prompt": "What is the major innovation of Latent Diffusion Models (LDMs, such as Stable Diffusion) over pixel-space diffusion?",
                "options": [
                    ("A", "Running the diffusion process in a compressed latent space learned by a VAE rather than high-dimensional pixel space"),
                    ("B", "Eliminating the need for neural network weights"),
                    ("C", "Generating 3D models instead of 2D images"),
                    ("D", "Using decision trees instead of convolutional networks")
                ],
                "correct": "A",
                "rationale": "Pixel-space diffusion is computationally expensive. LDMs compress images into a low-dimensional latent space using an autoencoder, vastly reducing compute requirements."
            },
            {
                "num": 5,
                "prompt": "How does text conditioning work in text-to-image models like Stable Diffusion?",
                "options": [
                    ("A", "Text is encoded via a model like CLIP or T5 and injected into the diffusion U-Net via cross-attention layers"),
                    ("B", "Text is directly converted into pixel RGB values at the top left corner"),
                    ("C", "Text prompt length dictates the output canvas pixel width"),
                    ("D", "The system searches a database of images and crops them")
                ],
                "correct": "A",
                "rationale": "Text encoders (like CLIP or T5) produce vector embeddings for prompt tokens, which guide intermediate image latent representations via cross-attention mechanisms."
            },
            {
                "num": 6,
                "prompt": "What does Classifier-Free Guidance (CFG) control during diffusion generation?",
                "options": [
                    ("A", "The physical resolution of the image sensor"),
                    ("B", "The trade-off between prompt fidelity (how strictly the image follows the prompt) and sample diversity/realism"),
                    ("C", "The monetary cost per generation on cloud GPUs"),
                    ("D", "The aspect ratio of the generated image canvas")
                ],
                "correct": "B",
                "rationale": "Higher CFG scales force the reverse process to adhere more aggressively to the text prompt conditioning, while lower values yield more creative diversity."
            },
            {
                "num": 7,
                "prompt": "In image generation, what is 'Inpainting'?",
                "options": [
                    ("A", "Generating a completely new image from scratch without a prompt"),
                    ("B", "Restoring, replacing, or modifying a specific masked region of an existing image while preserving surrounding context"),
                    ("C", "Converting a 2D image into a vectorized SVG outline"),
                    ("D", "Upscaling an image resolution using nearest-neighbor interpolation")
                ],
                "correct": "B",
                "rationale": "Inpainting masks an area of an image and uses diffusion conditioning to regenerate plausible, seamless content consistent with the unmasked boundaries."
            },
            {
                "num": 8,
                "prompt": "How do Vision Transformers (ViTs) process input images?",
                "options": [
                    ("A", "They scan images one individual pixel at a time from top-left to bottom-right"),
                    ("B", "They divide the image into non-overlapping patches (e.g. 16x16 pixels), flatten them, and treat each patch as a token sequence with self-attention"),
                    ("C", "They use exclusively 3x3 convolutional kernels with zero attention"),
                    ("D", "They convert all images into grayscale audio waveforms")
                ],
                "correct": "B",
                "rationale": "ViTs break images into a grid of patches, linearly project them into embeddings, prepend positional embeddings, and process them like text tokens via standard self-attention."
            },
            {
                "num": 9,
                "prompt": "True or False: Diffusion models can only generate 2D still images and cannot be adapted for video, audio, or 3D synthesis.",
                "options": [
                    ("A", "True"),
                    ("B", "False")
                ],
                "correct": "B",
                "rationale": "Diffusion principles have been successfully generalized to generate temporal video frames, audio spectrograms, and 3D NeRFs/Gaussian splats."
            },
            {
                "num": 10,
                "prompt": "What role does the VAE (Variational Autoencoder) play in latent diffusion architectures?",
                "options": [
                    ("A", "It encodes high-resolution pixel images into compact latent representations for efficient diffusion, then decodes latents back into pixels"),
                    ("B", "It acts as the primary web search engine for training images"),
                    ("C", "It replaces the cross-attention mechanism between text and image"),
                    ("D", "It regulates cooling fans on GPU hardware")
                ],
                "correct": "A",
                "rationale": "The VAE encoder compresses high-dimensional pixel space into latent space, and the VAE decoder reconstructs the finalized denoised latent array into human-visible pixels."
            }
        ]
    },
    "week_12_pretraining_generative_ai": {
        "title": "Week 12 Knowledge Check: Pre-Training Generative AI Models",
        "questions": [
            {
                "num": 1,
                "prompt": "What is the primary training objective used in autoregressive causal language modeling (such as GPT)?",
                "options": [
                    ("A", "Predicting the next token in a sequence given all preceding tokens (Next Token Prediction)"),
                    ("B", "Predicting random masked words anywhere in a sentence (Masked Language Modeling)"),
                    ("C", "Classifying whether an image contains a dog or a cat"),
                    ("D", "Minimizing the number of active GPU cores")
                ],
                "correct": "A",
                "rationale": "Autoregressive causal language models are trained via maximum likelihood estimation to predict token x_t given previous tokens x_1 through x_{t-1}."
            },
            {
                "num": 2,
                "prompt": "Which data curation challenge is most critical when assembling a massive web-scraped pre-training corpus?",
                "options": [
                    ("A", "Filtering out duplicate content, toxic language, spam, personally identifiable information (PII), and low-quality boilerplate text"),
                    ("B", "Ensuring all documents are exactly 1,000 words long"),
                    ("C", "Translating all internet text into Latin before training"),
                    ("D", "Converting all images on web pages into ASCII text")
                ],
                "correct": "A",
                "rationale": "Raw web text (like Common Crawl) is filled with machine-generated spam, duplicates, toxic speech, and formatting garbage. Rigorous deduplication and quality filtering are essential."
            },
            {
                "num": 3,
                "prompt": "What is the key functional difference between Pre-Training and Fine-Tuning an LLM?",
                "options": [
                    ("A", "Pre-training learns general linguistic, factual, and reasoning representations from vast unlabeled corpora; fine-tuning specializes the model for specific tasks or styles using curated datasets"),
                    ("B", "Fine-tuning happens before pre-training to establish baseline grammar"),
                    ("C", "Pre-training only takes a few minutes on a laptop, while fine-tuning takes months on a supercomputer"),
                    ("D", "Pre-training uses human labels, while fine-tuning uses raw uncleaned text")
                ],
                "correct": "A",
                "rationale": "Pre-training consumes 95%+ of the compute budget to absorb world knowledge and grammar. Fine-tuning shapes that capability toward desired task formats and conversational behaviors."
            },
            {
                "num": 4,
                "prompt": "When a researcher takes an LLM pre-trained on general web text and further pre-trains it on specialized biomedical literature, this is an example of:",
                "options": [
                    ("A", "Domain Adaptation (Continued Pre-training)"),
                    ("B", "Adversarial Prompt Injection"),
                    ("C", "Catastrophic Forgetting failure"),
                    ("D", "Zero-shot inference")
                ],
                "correct": "A",
                "rationale": "Continued pre-training on domain-specific corpora (medicine, law, finance) adapts the base model's vocabulary and conceptual grasp to specialized terminology."
            },
            {
                "num": 5,
                "prompt": "What do the Chinchilla scaling laws state regarding optimal compute allocation during LLM pre-training?",
                "options": [
                    ("A", "Model parameters and training token volume should be scaled in approximately equal proportion for compute-optimal efficiency"),
                    ("B", "Parameter count should be maximized while keeping training tokens under 10 billion"),
                    ("C", "Model size does not impact performance; only learning rate matters"),
                    ("D", "Compute budget should be spent exclusively on hardware cooling")
                ],
                "correct": "A",
                "rationale": "Hoffmann et al. (Chinchilla) demonstrated that previous models (like Gopher and GPT-3) were undertrained: for optimal compute, tokens and parameters should scale equally."
            },
            {
                "num": 6,
                "prompt": "How does Byte-Pair Encoding (BPE) handle out-of-vocabulary (OOV) words during tokenization?",
                "options": [
                    ("A", "It breaks unfamiliar words down into smaller subword units or individual characters that are in the vocabulary"),
                    ("B", "It discards the word entirely and skips to the next token"),
                    ("C", "It replaces all unknown words with a random dictionary definition"),
                    ("D", "It crashes the inference process with a syntax error")
                ],
                "correct": "A",
                "rationale": "Subword tokenizers (like BPE) break rare or unknown words into frequent subword fragments (or individual byte tokens), eliminating out-of-vocabulary failures."
            },
            {
                "num": 7,
                "prompt": "In Masked Language Modeling (MLM, used in BERT), what is the training task?",
                "options": [
                    ("A", "Predicting randomly masked tokens within a sequence using bidirectional context from both left and right"),
                    ("B", "Predicting the next sentence in an autoregressive chain"),
                    ("C", "Classifying whether an entire paragraph was written by an AI"),
                    ("D", "Translating masked tokens into another spoken language")
                ],
                "correct": "A",
                "rationale": "MLM corrupts ~15% of input tokens with a [MASK] symbol and trains the encoder to reconstruct the original tokens by attending to surrounding bidirectional context."
            },
            {
                "num": 8,
                "prompt": "Why is data deduplication (such as MinHash or exact matching) critical in pre-training data preparation?",
                "options": [
                    ("A", "To prevent models from memorizing repeated text verbatim, reducing training instability and copyright risks"),
                    ("B", "To make sure every token appears an odd number of times"),
                    ("C", "To force the model to learn only single-syllable words"),
                    ("D", "To compress the training file into ZIP format")
                ],
                "correct": "A",
                "rationale": "Duplicate data skews model probability distributions, encourages rote memorization over generalization, and wastes expensive training FLOPs."
            },
            {
                "num": 9,
                "prompt": "What is the primary role of Synthetic Data generation in modern pre-training pipelines?",
                "options": [
                    ("A", "Creating high-quality reasoning traces, code solutions, and textbook-style explanations using capable frontier models to overcome web data scarcity"),
                    ("B", "Encrypting training weights against competitor reverse engineering"),
                    ("C", "Faking benchmark test scores to inflate marketing claims"),
                    ("D", "Replacing all human authors in historical texts")
                ],
                "correct": "A",
                "rationale": "High-quality web data is rapidly being exhausted. State-of-the-art training pipelines (like Phi, Llama 3) generate clean, synthetic educational curricula using frontier models."
            },
            {
                "num": 10,
                "prompt": "Which distributed training strategy splits individual model layer weights across multiple GPUs when a model is too large to fit in a single GPU's memory?",
                "options": [
                    ("A", "Tensor Parallelism (Model Parallelism)"),
                    ("B", "Single-threaded Batch Processing"),
                    ("C", "Serial CPU Offloading"),
                    ("D", "Round-robin HTTP Load Balancing")
                ],
                "correct": "A",
                "rationale": "Tensor parallelism shards linear weight matrices (e.g. across attention heads) across multiple GPUs within a node so massive models can be trained simultaneously."
            }
        ]
    },
    "week_13_finetuning_generative_ai": {
        "title": "Week 13 Knowledge Check: Fine-Tuning Generative AI Models",
        "questions": [
            {
                "num": 1,
                "prompt": "What is the primary objective of Supervised Fine-Tuning (SFT) for foundational language models?",
                "options": [
                    ("A", "Teaching the model basic English grammar and vocabulary from scratch"),
                    ("B", "Adapting a raw pre-trained base model into a helpful conversational assistant using curated instruction-response pairs"),
                    ("C", "Compressing the neural network weights into an Excel spreadsheet"),
                    ("D", "Filtering web pages to remove duplicate URLs")
                ],
                "correct": "B",
                "rationale": "Base models naturally want to complete text documents. SFT teaches the model the conversational turn-taking format: interpreting instructions and returning helpful answers."
            },
            {
                "num": 2,
                "prompt": "What problem does Parameter-Efficient Fine-Tuning (PEFT, such as LoRA) solve?",
                "options": [
                    ("A", "It allows adaptation of massive models by training only a tiny fraction (<1%) of added parameters, drastically reducing GPU memory and storage requirements"),
                    ("B", "It eliminates the need for any training data"),
                    ("C", "It converts language models into computer vision models"),
                    ("D", "It guarantees the model will never generate hallucinations")
                ],
                "correct": "A",
                "rationale": "Full fine-tuning requires updating and storing gradients for billions of parameters. PEFT methods freeze base weights and train small adapter modules, cutting memory footprints."
            },
            {
                "num": 3,
                "prompt": "How does LoRA (Low-Rank Adaptation) mathematically represent weight updates during fine-tuning?",
                "options": [
                    ("A", "It decomposes the weight update matrix ΔW into the product of two low-rank matrices A and B (ΔW = B × A)"),
                    ("B", "It sets all negative weights to zero using a ReLU threshold"),
                    ("C", "It rounds all 32-bit floating point weights to 1-bit integers"),
                    ("D", "It multiplies model weights by a random Gaussian vector")
                ],
                "correct": "A",
                "rationale": "LoRA freezes the original weight W_0 and injects trainable rank decomposition matrices: ΔW = B × A, where the rank r is much smaller than the hidden dimension d."
            },
            {
                "num": 4,
                "prompt": "What is 'Catastrophic Forgetting' in the context of fine-tuning language models?",
                "options": [
                    ("A", "When a model completely deletes its own configuration files during inference"),
                    ("B", "When fine-tuning on a narrow task causes the model to lose its general capabilities, common sense reasoning, or previously learned skills"),
                    ("C", "When GPU memory overheats and loses cached KV tokens"),
                    ("D", "When the context window overflows beyond maximum token limits")
                ],
                "correct": "B",
                "rationale": "Catastrophic forgetting occurs when gradient updates on a specialized domain overwrite neural pathways responsible for general reasoning and linguistic fluency."
            },
            {
                "num": 5,
                "prompt": "What is 'Quantized Low-Rank Adaptation' (QLoRA)?",
                "options": [
                    ("A", "An extension of LoRA that quantizes the frozen base model to 4-bit precision (NF4) while maintaining 16-bit brain float adapters, enabling fine-tuning of 70B models on consumer GPUs"),
                    ("B", "A technique that restricts prompts to 4 letters"),
                    ("C", "A quantum computing algorithm for searching embeddings"),
                    ("D", "A hardware cooling system for overclocked GPUs")
                ],
                "correct": "A",
                "rationale": "QLoRA combines 4-bit NormalFloat base model quantization, double quantization, and paged optimizers with LoRA adapters, drastically democratizing fine-tuning."
            },
            {
                "num": 6,
                "prompt": "In instruction fine-tuning, how are training examples typically structured?",
                "options": [
                    ("A", "As structured conversations containing System, User (Instruction/Input), and Assistant (Target Output) roles"),
                    ("B", "As continuous raw text streams without any role delimiters or special tokens"),
                    ("C", "As binary machine code instructions"),
                    ("D", "As unlabelled spreadsheets with missing headers")
                ],
                "correct": "A",
                "rationale": "Instruction datasets (like ShareGPT or Alpaca format) structure examples into clear conversational roles (system, human, assistant) using chat templates."
            },
            {
                "num": 7,
                "prompt": "Which method is commonly used to mitigate catastrophic forgetting during domain-specific fine-tuning?",
                "options": [
                    ("A", "Mixing a percentage of general-domain pre-training data into the fine-tuning instruction set (Replay / Mixed Task Training)"),
                    ("B", "Increasing the learning rate by 100x"),
                    ("C", "Removing all validation sets from the training loop"),
                    ("D", "Training only on the single most difficult domain example")
                ],
                "correct": "A",
                "rationale": "Co-training with a mix of general instruction data and specialized domain data prevents model weights from drifting excessively away from foundational competencies."
            },
            {
                "num": 8,
                "prompt": "When should an organization choose In-Context Learning (RAG) over Fine-Tuning an LLM?",
                "options": [
                    ("A", "When business data updates frequently in real time and requires strict source attribution / citations"),
                    ("B", "When teaching a model a completely new linguistic syntax or specialized code style"),
                    ("C", "When wanting to minimize prompt context window size and token costs"),
                    ("D", "When the organization has no network access to external databases")
                ],
                "correct": "A",
                "rationale": "RAG is ideal for dynamic knowledge that updates frequently and needs direct source auditability. Fine-tuning is preferred for teaching style, format, and static specialization."
            },
            {
                "num": 9,
                "prompt": "What does 'Knowledge Distillation' involve in model optimization?",
                "options": [
                    ("A", "Training a smaller, faster 'student' model to reproduce the predictions and reasoning outputs of a larger, highly capable 'teacher' model"),
                    ("B", "Scraping Wikipedia to build an encyclopedia embedding database"),
                    ("C", "Filtering out all non-scientific words from a vocabulary dictionary"),
                    ("D", "Deleting random layers from a neural network")
                ],
                "correct": "A",
                "rationale": "Distillation transfers the reasoning density of massive teacher models (e.g. 70B+) into lightweight student models (e.g. 3B-8B) for fast, low-cost edge deployment."
            },
            {
                "num": 10,
                "prompt": "What metric is most commonly monitored during fine-tuning to prevent overfitting on the training set?",
                "options": [
                    ("A", "Validation Loss (eval_loss)"),
                    ("B", "GPU core temperature"),
                    ("C", "Total disk space occupied by logs"),
                    ("D", "The length of user prompts in testing")
                ],
                "correct": "A",
                "rationale": "If training loss decreases while validation loss starts rising, the model is overfitting to the training examples and losing generalization ability."
            }
        ]
    },
    "week_15_prototyping_genai_apps": {
        "title": "Week 15 Knowledge Check: Prototyping Generative AI Applications",
        "questions": [
            {
                "num": 1,
                "prompt": "What is the primary role of application frameworks like LangChain or LlamaIndex in Generative AI development?",
                "options": [
                    ("A", "To manage low-level GPU silicon drivers"),
                    ("B", "To provide standardized abstractions for chaining LLM calls, connecting external tools, managing memory, and implementing RAG pipelines"),
                    ("C", "To compile Python code directly into assembly language"),
                    ("D", "To replace SQL databases with plain text files")
                ],
                "correct": "B",
                "rationale": "Frameworks like LangChain orchestrate application components: prompt templates, model connectors, memory persistence, vector retrieval, and tool execution."
            },
            {
                "num": 2,
                "prompt": "What is the primary function of a Vector Database (such as Pinecone, Chroma, or Qdrant) in RAG applications?",
                "options": [
                    ("A", "Storing high-dimensional vector embeddings and performing fast approximate nearest neighbor (ANN) similarity search"),
                    ("B", "Storing raw video files for streaming"),
                    ("C", "Executing automated Python unit tests"),
                    ("D", "Generating synthetic cryptographic keys")
                ],
                "correct": "A",
                "rationale": "Vector databases index embeddings and calculate cosine or dot-product distance at scale, allowing applications to retrieve relevant context chunks for a query in milliseconds."
            },
            {
                "num": 3,
                "prompt": "Why are tools like Streamlit and Gradio popular for rapid AI prototyping?",
                "options": [
                    ("A", "They allow data scientists and engineers to build interactive web user interfaces entirely in Python with zero frontend HTML/CSS/JS expertise"),
                    ("B", "They replace the need for an underlying language model"),
                    ("C", "They run AI models on mobile devices without an internet connection"),
                    ("D", "They automatically write production database schemas")
                ],
                "correct": "A",
                "rationale": "Streamlit and Gradio turn Python scripts into responsive web apps in minutes, making them the standard for prototyping, testing, and demonstrating AI workflows."
            },
            {
                "num": 4,
                "prompt": "In a Retrieval-Augmented Generation (RAG) system, what does the 'Chunking' step accomplish?",
                "options": [
                    ("A", "Breaking large unstructured documents into smaller, semantically coherent segments suitable for embedding and context window limits"),
                    ("B", "Deleting random paragraphs from documents to save disk space"),
                    ("C", "Compressing text into zip archives"),
                    ("D", "Splitting GPU memory into virtual partitions")
                ],
                "correct": "A",
                "rationale": "LLMs have finite context windows, and embedding entire books at once degrades retrieval precision. Chunking breaks text into searchable, granular pieces."
            },
            {
                "num": 5,
                "prompt": "What does LLMOps (Large Language Model Operations) encompass in enterprise software engineering?",
                "options": [
                    ("A", "Practices and tooling for model deployment, monitoring, cost tracking, evaluation, latency management, and guardrails in production"),
                    ("B", "Manual human review of every token output by a chatbot"),
                    ("C", "Hardware maintenance of server rack cables"),
                    ("D", "Writing marketing copy for AI product launches")
                ],
                "correct": "A",
                "rationale": "LLMOps extends DevOps/MLOps to handle LLM-specific operational concerns: token costs, latency, drift, prompt versioning, eval benchmarks, and security guardrails."
            },
            {
                "num": 6,
                "prompt": "What is the function of Experiment Tracking platforms like Weights & Biases (W&B) or MLflow?",
                "options": [
                    ("A", "Logging hyperparameters, prompt versions, evaluation metrics, and training loss curves for systematic reproducibility and comparison"),
                    ("B", "Streaming video tutorials to student developers"),
                    ("C", "Generating synthetic user bug reports"),
                    ("D", "Managing employee payroll for data science teams")
                ],
                "correct": "A",
                "rationale": "Experiment tracking logs every training run or prompt configuration with metrics and artifacts, making AI development reproducible and auditable."
            },
            {
                "num": 7,
                "prompt": "What is 'Semantic Search' and how does it improve upon traditional keyword search?",
                "options": [
                    ("A", "It matches queries based on conceptual meaning and vector similarity rather than exact lexical word overlap"),
                    ("B", "It searches only for words that rhyme with the query"),
                    ("C", "It translates all queries into binary machine code"),
                    ("D", "It requires the user to know the exact filename where information is stored")
                ],
                "correct": "A",
                "rationale": "Keyword search fails when users use synonyms (e.g. 'automobile' vs 'car'). Semantic search maps concepts into embedding space where related meanings cluster together."
            },
            {
                "num": 8,
                "prompt": "Why is 'Re-ranking' often used after initial vector retrieval in advanced RAG architectures?",
                "options": [
                    ("A", "A specialized cross-encoder re-evaluates the top candidate chunks against the query to score true relevance, overcoming embedding retrieval noise"),
                    ("B", "It shuffles retrieved chunks randomly to increase answer creativity"),
                    ("C", "It discards all chunks that contain punctuation"),
                    ("D", "It translates retrieved chunks into French")
                ],
                "correct": "A",
                "rationale": "Dense vector search retrieves candidate chunks quickly but can suffer from low precision. Cross-encoder re-rankers analyze the full query-chunk pair to prioritize the most relevant text."
            },
            {
                "num": 9,
                "prompt": "What is the primary role of AI code assistants (like GitHub Copilot or Cursor)?",
                "options": [
                    ("A", "Suggesting context-aware code completions, function implementations, documentation, and unit tests directly in the developer's IDE"),
                    ("B", "Automatically deploying untested code to production without human review"),
                    ("C", "Replacing the operating system kernel with an LLM"),
                    ("D", "Monitoring developer keystrokes for employee surveillance")
                ],
                "correct": "A",
                "rationale": "AI coding assistants accelerate developer productivity by synthesizing boilerplate, implementing algorithms, suggesting tests, and explaining code in real time."
            },
            {
                "num": 10,
                "prompt": "What critical metric must developers monitor when designing production generative AI user experiences?",
                "options": [
                    ("A", "Time to First Token (TTFT) and overall generation latency to maintain responsive interactivity"),
                    ("B", "The color temperature of the user's computer monitor"),
                    ("C", "The number of punctuation marks in the model weights"),
                    ("D", "The serial number of the client's network router")
                ],
                "correct": "A",
                "rationale": "User experience degrades rapidly if users stare at blank screens. Streaming responses and optimizing Time to First Token (TTFT) ensure fluid, interactive software."
            }
        ]
    },
    "week_16_llm_alignment_responsible_ai": {
        "title": "Week 16 Knowledge Check: LLM Alignment and Responsible AI",
        "questions": [
            {
                "num": 1,
                "prompt": "In AI safety and ethics, what is the 'Alignment Problem'?",
                "options": [
                    ("A", "The challenge of ensuring an AI system's objectives, behaviors, and values reliably conform to intended human values and safety standards"),
                    ("B", "Aligning text margins to the left and right borders of a page"),
                    ("C", "Ensuring GPU hardware cables are plugged into the correct slots"),
                    ("D", "Synchronizing system clock times across cloud data centers")
                ],
                "correct": "A",
                "rationale": "The alignment problem centers on building powerful AI systems whose goals, decision heuristics, and real-world actions remain beneficial and faithful to human intent."
            },
            {
                "num": 2,
                "prompt": "What are the three core principles of the 'HHH' alignment framework popularized by Anthropic?",
                "options": [
                    ("A", "Helpful, Harmless, and Honest"),
                    ("B", "Hyper-fast, Highly-accurate, and Hardware-efficient"),
                    ("C", "Heavy, Heuristic, and Holistic"),
                    ("D", "Hierarchical, Hybrid, and Homogeneous")
                ],
                "correct": "A",
                "rationale": "The HHH criteria define target model behavior: Helpful (fulfills user intent), Harmless (avoids promoting illegal/dangerous actions), and Honest (truthful, calibrated certainty)."
            },
            {
                "num": 3,
                "prompt": "How does Reinforcement Learning from Human Feedback (RLHF) align language models?",
                "options": [
                    ("A", "A reward model is trained on human preference rankings between model outputs, then used via PPO to guide the policy model toward preferred responses"),
                    ("B", "Humans manually rewrite all possible token sequences in the base vocabulary"),
                    ("C", "Models are penalized with electric shocks when they make grammatical errors"),
                    ("D", "Human users review every single query before the model can answer")
                ],
                "correct": "A",
                "rationale": "RLHF trains a reward model to score responses based on human pairwise preferences, using reinforcement learning (e.g. PPO) to optimize the LLM policy toward high-reward behaviors."
            },
            {
                "num": 4,
                "prompt": "What is 'Constitutional AI' (RLAIF)?",
                "options": [
                    ("A", "An alignment method where an AI system uses a written constitution of safety principles to critique, revise, and align its own outputs with minimal human labeling"),
                    ("B", "Training models exclusively on government legal constitutions"),
                    ("C", "Requiring models to pass a bar examination before deployment"),
                    ("D", "A hardware firewall implemented inside server motherboard firmware")
                ],
                "correct": "A",
                "rationale": "Constitutional AI replaces expensive human feedback loops with AI feedback: the model critiques and refines candidate answers against explicit constitutional principles."
            },
            {
                "num": 5,
                "prompt": "How does Direct Preference Optimization (DPO) simplify model alignment compared to classic RLHF?",
                "options": [
                    ("A", "It directly optimizes the policy network on preference pairs using a closed-form loss function, eliminating the need to train a separate reward model or run PPO"),
                    ("B", "It deletes all negative data from the internet"),
                    ("C", "It forces the model to choose only the shortest possible answers"),
                    ("D", "It requires no training data whatsoever")
                ],
                "correct": "A",
                "rationale": "DPO analytically reparameterizes the reward model, optimizing policy weights directly from preference pairs without the complexity and instability of multi-stage RL."
            },
            {
                "num": 6,
                "prompt": "True or False: An AI system that is extremely proficient at summarizing facts and writing creative essays is guaranteed to be aligned and safe.",
                "options": [
                    ("A", "True"),
                    ("B", "False")
                ],
                "correct": "B",
                "rationale": "Capability is orthogonal to alignment. A highly capable model can still generate deceptive arguments, toxic rhetoric, or instructions for dangerous weapons if unaligned."
            },
            {
                "num": 7,
                "prompt": "What is 'Red Teaming' in the context of responsible generative AI deployment?",
                "options": [
                    ("A", "Adversarial testing where security and domain experts deliberately probe the system with adversarial prompts, jailbreaks, and edge cases to uncover vulnerabilities"),
                    ("B", "Painting server rack cases red for visual identification"),
                    ("C", "Assigning developers to wear red shirts during release sprints"),
                    ("D", "Rewriting code in the Rust programming language")
                ],
                "correct": "A",
                "rationale": "Red teaming is structured adversarial exploration: probing an AI with malicious, deceptive, and harmful inputs before release to discover and patch safety failures."
            },
            {
                "num": 8,
                "prompt": "Why can the principles of 'Helpful' and 'Harmless' sometimes conflict with each other?",
                "options": [
                    ("A", "A user might ask for 'help' synthesizing an explosive or hacking a network; being truly harmless requires refusing to be helpful for that request"),
                    ("B", "Helpful models use more electricity, which causes harmless heat"),
                    ("C", "Honesty is impossible for artificial neural networks"),
                    ("D", "Only human beings can understand the concept of harm")
                ],
                "correct": "A",
                "rationale": "Refusal dilemmas occur when users request actionable assistance for malicious ends. The model must prioritize harmlessness over helpfulness and decline the request."
            },
            {
                "num": 9,
                "prompt": "What is a 'Jailbreak' in large language model security?",
                "options": [
                    ("A", "A crafted prompt or adversarial token sequence that bypasses a model's safety alignment guardrails to elicit prohibited responses"),
                    ("B", "Installing alternative operating systems on Apple iPhones"),
                    ("C", "Breaking physical locks on enterprise server cages"),
                    ("D", "Running an LLM outside of a Python virtual environment")
                ],
                "correct": "A",
                "rationale": "Jailbreaking uses roleplay, hypothetical framing, obfuscated encodings, or adversarial suffixes to trick the model into ignoring its safety training."
            },
            {
                "num": 10,
                "prompt": "True or False: Technical alignment eliminates the need for human governance, legal regulations, or organizational compliance policies.",
                "options": [
                    ("A", "True"),
                    ("B", "False")
                ],
                "correct": "B",
                "rationale": "Technical alignment is only one layer of defense. Robust AI deployment requires comprehensive socio-technical governance: laws, institutional policies, and human auditing."
            }
        ]
    }
}


def build_markdown_quiz(mod_key: str, qdata: dict) -> str:
    lines = []
    lines.append(f"# {qdata['title']}\n")
    lines.append(f"**Course**: AIML 1010: Introduction to Artificial Intelligence  ")
    lines.append(f"**Assessment Type**: Multiple Choice Knowledge Check  ")
    lines.append(f"**Allowed Attempts**: 3 | **Scoring Policy**: Keep Highest Score | **Points Possible**: 30.0\n")
    lines.append("---\n")
    lines.append("## Assessment Questions\n")

    for q in qdata["questions"]:
        lines.append(f"### Question {q['num']}")
        lines.append(f"{q['prompt']}\n")
        for letter, text in q["options"]:
            lines.append(f"* {letter}) {text}")
        lines.append("")

    lines.append("---\n")
    lines.append("## Answer Key\n")
    lines.append("| Question # | Correct Answer | Concept Tested & Rationale |")
    lines.append("| :--- | :--- | :--- |")
    for q in qdata["questions"]:
        lines.append(f"| **{q['num']}** | **{q['correct']}** | {q['rationale']} |")
    lines.append("")

    return "\n".join(lines)


def main():
    base_units_dir = os.path.join(REPO_ROOT, "modules/aiml-1010-generative-ai-update/units")
    dist_qti_root = os.path.join(REPO_ROOT, "modules/aiml-1010-generative-ai-update/_qti_build")
    os.makedirs(dist_qti_root, exist_ok=True)

    print("Auditing and compiling all 9 quizzes...")
    compiled_results = []

    for mod_key, qdata in QUIZZES.items():
        unit_dir = os.path.join(base_units_dir, mod_key)
        os.makedirs(unit_dir, exist_ok=True)
        md_path = os.path.join(unit_dir, "quiz.md")

        # 1. Write clean markdown quiz
        md_content = build_markdown_quiz(mod_key, qdata)
        with open(md_path, "w", encoding="utf-8") as f:
            f.write(md_content)
        print(f"[Markdown] Written {md_path}")

        # 2. Package into QTI 1.2
        quiz_id = make_canvas_id(f"quiz_{mod_key}")
        quiz_group_id = make_canvas_id("quizzes_group")
        res = package_quiz(
            md_path,
            dist_qti_root,
            quiz_id,
            qdata["title"],
            quiz_group_id,
            points_possible=30.0,
            allowed_attempts=3
        )
        compiled_results.append({
            "key": mod_key,
            "title": qdata["title"],
            "quiz_id": quiz_id,
            "questions": int(res["question_count"]),
            "qti_path": res["qti_path"]
        })
        print(f"[QTI 1.2] Compiled {qdata['title']} -> {quiz_id} ({res['question_count']} questions)")

    # Verification
    print("\n=== Verification Audit: All 9 QTI 1.2 Quizzes ===")
    all_ok = True
    for r in compiled_results:
        if r["questions"] == 10 and os.path.exists(r["qti_path"]):
            print(f"PASS: {r['key']} -> {r['title']} (10 questions verified)")
        else:
            print(f"FAIL: {r['key']} (Expected 10 questions, got {r['questions']})")
            all_ok = False

    if not all_ok:
        sys.exit(1)

    print("\nTask 2 Complete: All 9 quizzes cleaned, audited, and compiled to native QTI 1.2!")


if __name__ == "__main__":
    main()
