# Week 12 Knowledge Check: Pre-Training Generative AI Models

**Course**: AIML 1010: Introduction to Artificial Intelligence  
**Assessment Type**: Multiple Choice Knowledge Check  
**Allowed Attempts**: 3 | **Scoring Policy**: Keep Highest Score | **Points Possible**: 30.0

---

## Assessment Questions

### Question 1
What is the primary training objective used in autoregressive causal language modeling (such as GPT)?

* A) Predicting the next token in a sequence given all preceding tokens (Next Token Prediction)
* B) Predicting random masked words anywhere in a sentence (Masked Language Modeling)
* C) Classifying whether an image contains a dog or a cat
* D) Minimizing the number of active GPU cores

### Question 2
Which data curation challenge is most critical when assembling a massive web-scraped pre-training corpus?

* A) Filtering out duplicate content, toxic language, spam, personally identifiable information (PII), and low-quality boilerplate text
* B) Ensuring all documents are exactly 1,000 words long
* C) Translating all internet text into Latin before training
* D) Converting all images on web pages into ASCII text

### Question 3
What is the key functional difference between Pre-Training and Fine-Tuning an LLM?

* A) Pre-training learns general linguistic, factual, and reasoning representations from vast unlabeled corpora; fine-tuning specializes the model for specific tasks or styles using curated datasets
* B) Fine-tuning happens before pre-training to establish baseline grammar
* C) Pre-training only takes a few minutes on a laptop, while fine-tuning takes months on a supercomputer
* D) Pre-training uses human labels, while fine-tuning uses raw uncleaned text

### Question 4
When a researcher takes an LLM pre-trained on general web text and further pre-trains it on specialized biomedical literature, this is an example of:

* A) Domain Adaptation (Continued Pre-training)
* B) Adversarial Prompt Injection
* C) Catastrophic Forgetting failure
* D) Zero-shot inference

### Question 5
What do the Chinchilla scaling laws state regarding optimal compute allocation during LLM pre-training?

* A) Model parameters and training token volume should be scaled in approximately equal proportion for compute-optimal efficiency
* B) Parameter count should be maximized while keeping training tokens under 10 billion
* C) Model size does not impact performance; only learning rate matters
* D) Compute budget should be spent exclusively on hardware cooling

### Question 6
How does Byte-Pair Encoding (BPE) handle out-of-vocabulary (OOV) words during tokenization?

* A) It breaks unfamiliar words down into smaller subword units or individual characters that are in the vocabulary
* B) It discards the word entirely and skips to the next token
* C) It replaces all unknown words with a random dictionary definition
* D) It crashes the inference process with a syntax error

### Question 7
In Masked Language Modeling (MLM, used in BERT), what is the training task?

* A) Predicting randomly masked tokens within a sequence using bidirectional context from both left and right
* B) Predicting the next sentence in an autoregressive chain
* C) Classifying whether an entire paragraph was written by an AI
* D) Translating masked tokens into another spoken language

### Question 8
Why is data deduplication (such as MinHash or exact matching) critical in pre-training data preparation?

* A) To prevent models from memorizing repeated text verbatim, reducing training instability and copyright risks
* B) To make sure every token appears an odd number of times
* C) To force the model to learn only single-syllable words
* D) To compress the training file into ZIP format

### Question 9
What is the primary role of Synthetic Data generation in modern pre-training pipelines?

* A) Creating high-quality reasoning traces, code solutions, and textbook-style explanations using capable frontier models to overcome web data scarcity
* B) Encrypting training weights against competitor reverse engineering
* C) Faking benchmark test scores to inflate marketing claims
* D) Replacing all human authors in historical texts

### Question 10
Which distributed training strategy splits individual model layer weights across multiple GPUs when a model is too large to fit in a single GPU's memory?

* A) Tensor Parallelism (Model Parallelism)
* B) Single-threaded Batch Processing
* C) Serial CPU Offloading
* D) Round-robin HTTP Load Balancing

---

## Answer Key

| Question # | Correct Answer | Concept Tested & Rationale |
| :--- | :--- | :--- |
| **1** | **A** | Autoregressive causal language models are trained via maximum likelihood estimation to predict token x_t given previous tokens x_1 through x_{t-1}. |
| **2** | **A** | Raw web text (like Common Crawl) is filled with machine-generated spam, duplicates, toxic speech, and formatting garbage. Rigorous deduplication and quality filtering are essential. |
| **3** | **A** | Pre-training consumes 95%+ of the compute budget to absorb world knowledge and grammar. Fine-tuning shapes that capability toward desired task formats and conversational behaviors. |
| **4** | **A** | Continued pre-training on domain-specific corpora (medicine, law, finance) adapts the base model's vocabulary and conceptual grasp to specialized terminology. |
| **5** | **A** | Hoffmann et al. (Chinchilla) demonstrated that previous models (like Gopher and GPT-3) were undertrained: for optimal compute, tokens and parameters should scale equally. |
| **6** | **A** | Subword tokenizers (like BPE) break rare or unknown words into frequent subword fragments (or individual byte tokens), eliminating out-of-vocabulary failures. |
| **7** | **A** | MLM corrupts ~15% of input tokens with a [MASK] symbol and trains the encoder to reconstruct the original tokens by attending to surrounding bidirectional context. |
| **8** | **A** | Duplicate data skews model probability distributions, encourages rote memorization over generalization, and wastes expensive training FLOPs. |
| **9** | **A** | High-quality web data is rapidly being exhausted. State-of-the-art training pipelines (like Phi, Llama 3) generate clean, synthetic educational curricula using frontier models. |
| **10** | **A** | Tensor parallelism shards linear weight matrices (e.g. across attention heads) across multiple GPUs within a node so massive models can be trained simultaneously. |
