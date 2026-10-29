# Week 03 Knowledge Check: Prompt Engineering I

**Course**: AIML 1010: Introduction to Artificial Intelligence  
**Assessment Type**: Multiple Choice Knowledge Check  
**Allowed Attempts**: 3 | **Scoring Policy**: Keep Highest Score | **Points Possible**: 30.0

---

## Assessment Questions

### Question 1
What is the primary focus of prompt engineering in generative AI?

* A) Modifying neural network weights through gradient descent
* B) Task-specific optimization of input instructions to elicit desired outputs without altering model weights
* C) Generating synthetic pre-training corpora for foundation models
* D) Developing low-level GPU acceleration kernels for matrix multiplication

### Question 2
In the RGC (Role, Goal, Context) prompting framework, what is the primary role of the 'Role' component?

* A) Specifying the programming language used to format output tokens
* B) Establishing the persona, domain expertise, and tone the model should adopt in its response
* C) Providing example input-output pairs for few-shot in-context learning
* D) Restricting the total parameter count utilized during model inference

### Question 3
What is the key difference between Zero-Shot prompting and Few-Shot prompting?

* A) Zero-shot uses no context, while few-shot requires fine-tuning weights on thousands of labeled examples
* B) Zero-shot prompts provide task instructions without demonstrations, while few-shot prompts include one or more input-output examples directly in the context
* C) Zero-shot runs on CPU, while few-shot requires specialized GPU clusters
* D) Zero-shot only works for classification, while few-shot only works for code generation

### Question 4
Why is specifying output format (e.g., JSON, markdown table) in a prompt crucial for production applications?

* A) It prevents the model from consuming GPU memory
* B) It guarantees the model cannot hallucinate factual data
* C) It enables deterministic downstream parsing and seamless software integration
* D) It automatically fine-tunes the model on user schema

### Question 5
What does 'delimiters' (such as triple backticks or XML tags) achieve when crafting complex prompts?

* A) Increases model inference speed by skipping tokenization
* B) Clearly separates instructions from reference content, preventing prompt injection and contextual confusion
* C) Encrypts sensitive data before transmission to the inference server
* D) Forces the model to execute embedded code directly in sandbox

### Question 6
Which of the following is considered a prompt engineering anti-pattern?

* A) Providing clear, concise positive instructions on what to do
* B) Vague, open-ended instructions like 'Write something about AI' without specifying audience, length, or goals
* C) Using few-shot demonstrations with diverse examples
* D) Specifying constraints and edge cases explicitly

### Question 7
How does the 'Context' component in the RGC framework improve output quality?

* A) By grounding the model with background facts, constraints, and source data to reduce generic speculation
* B) By retraining the neural network's self-attention heads
* C) By bypassing the model's safety alignment filters
* D) By increasing the temperature hyperparameter

### Question 8
What is the primary benefit of 'system prompts' compared to standard user prompts in LLM APIs?

* A) System prompts set foundational behavioral rules and persistent constraints that govern the entire multi-turn interaction
* B) System prompts bypass billing costs for API users
* C) System prompts are only readable by human developers, not the model
* D) System prompts can only be written in compiled binary format

### Question 9
When asking an LLM to perform complex reasoning, why is 'Think step by step' effective?

* A) It increases model parameter weights during runtime
* B) It encourages the model to generate intermediate reasoning tokens, giving the attention mechanism computational space to derive the correct conclusion
* C) It causes the model to search external search engines automatically
* D) It compresses the context window to reduce latency

### Question 10
Which prompt engineering technique is best suited for categorizing customer support tickets into defined department queues?

* A) Few-shot classification with explicit schema, examples for each category, and a specified fallback class
* B) Unconstrained creative story generation
* C) High temperature sampling without instructions
* D) Omitting category labels so the model invents its own taxonomy

---

## Answer Key

| Question # | Correct Answer | Concept Tested & Rationale |
| :--- | :--- | :--- |
| **1** | **B** | Prompt engineering focuses on formulating, refining, and structuring textual inputs to guide frozen LLMs toward optimal outputs for specific tasks. |
| **2** | **B** | Assigning a Role (e.g., 'Act as a senior cybersecurity auditor') steers the model's latent representation toward domain-relevant vocabulary, conventions, and depth. |
| **3** | **B** | Zero-shot relies entirely on the model's pre-trained knowledge without task examples. Few-shot provides in-context demonstrations to establish pattern and format. |
| **4** | **C** | Enforcing structured schemas like JSON ensures automated parsers and downstream APIs can ingest model outputs reliably without human manual reformatting. |
| **5** | **B** | Delimiters create explicit structural boundaries so the model understands which text constitutes instructions and which text is raw data to be analyzed. |
| **6** | **B** | Vague instructions leave too much variance in the model's probability distribution, leading to generic, irrelevant, or unhelpful responses. |
| **7** | **A** | Providing explicit context gives the model domain-specific grounding data, significantly reducing hallucination and aligning responses to the real scenario. |
| **8** | **A** | System messages establish high-level behavioral bounds, persona, safety policies, and operating constraints that persist throughout a conversation session. |
| **9** | **B** | Because Transformers predict one token at a time, generating explicit reasoning steps provides intermediate context that guides subsequent tokens toward correct mathematical and logical deductions. |
| **10** | **A** | Classification tasks require deterministic mapping: few-shot examples for each category combined with strict output schema ensure predictable, reliable categorization. |
