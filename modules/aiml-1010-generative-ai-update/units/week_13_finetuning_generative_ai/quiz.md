# Week 13 Knowledge Check: Fine-Tuning Generative AI Models

**Course**: AIML 1010: Introduction to Artificial Intelligence  
**Assessment Type**: Multiple Choice Knowledge Check  
**Allowed Attempts**: 3 | **Scoring Policy**: Keep Highest Score | **Points Possible**: 30.0

---

## Assessment Questions

### Question 1
What is the primary objective of Supervised Fine-Tuning (SFT) for foundational language models?

* A) Teaching the model basic English grammar and vocabulary from scratch
* B) Adapting a raw pre-trained base model into a helpful conversational assistant using curated instruction-response pairs
* C) Compressing the neural network weights into an Excel spreadsheet
* D) Filtering web pages to remove duplicate URLs

### Question 2
What problem does Parameter-Efficient Fine-Tuning (PEFT, such as LoRA) solve?

* A) It allows adaptation of massive models by training only a tiny fraction (<1%) of added parameters, drastically reducing GPU memory and storage requirements
* B) It eliminates the need for any training data
* C) It converts language models into computer vision models
* D) It guarantees the model will never generate hallucinations

### Question 3
How does LoRA (Low-Rank Adaptation) mathematically represent weight updates during fine-tuning?

* A) It decomposes the weight update matrix ΔW into the product of two low-rank matrices A and B (ΔW = B × A)
* B) It sets all negative weights to zero using a ReLU threshold
* C) It rounds all 32-bit floating point weights to 1-bit integers
* D) It multiplies model weights by a random Gaussian vector

### Question 4
What is 'Catastrophic Forgetting' in the context of fine-tuning language models?

* A) When a model completely deletes its own configuration files during inference
* B) When fine-tuning on a narrow task causes the model to lose its general capabilities, common sense reasoning, or previously learned skills
* C) When GPU memory overheats and loses cached KV tokens
* D) When the context window overflows beyond maximum token limits

### Question 5
What is 'Quantized Low-Rank Adaptation' (QLoRA)?

* A) An extension of LoRA that quantizes the frozen base model to 4-bit precision (NF4) while maintaining 16-bit brain float adapters, enabling fine-tuning of 70B models on consumer GPUs
* B) A technique that restricts prompts to 4 letters
* C) A quantum computing algorithm for searching embeddings
* D) A hardware cooling system for overclocked GPUs

### Question 6
In instruction fine-tuning, how are training examples typically structured?

* A) As structured conversations containing System, User (Instruction/Input), and Assistant (Target Output) roles
* B) As continuous raw text streams without any role delimiters or special tokens
* C) As binary machine code instructions
* D) As unlabelled spreadsheets with missing headers

### Question 7
Which method is commonly used to mitigate catastrophic forgetting during domain-specific fine-tuning?

* A) Mixing a percentage of general-domain pre-training data into the fine-tuning instruction set (Replay / Mixed Task Training)
* B) Increasing the learning rate by 100x
* C) Removing all validation sets from the training loop
* D) Training only on the single most difficult domain example

### Question 8
When should an organization choose In-Context Learning (RAG) over Fine-Tuning an LLM?

* A) When business data updates frequently in real time and requires strict source attribution / citations
* B) When teaching a model a completely new linguistic syntax or specialized code style
* C) When wanting to minimize prompt context window size and token costs
* D) When the organization has no network access to external databases

### Question 9
What does 'Knowledge Distillation' involve in model optimization?

* A) Training a smaller, faster 'student' model to reproduce the predictions and reasoning outputs of a larger, highly capable 'teacher' model
* B) Scraping Wikipedia to build an encyclopedia embedding database
* C) Filtering out all non-scientific words from a vocabulary dictionary
* D) Deleting random layers from a neural network

### Question 10
What metric is most commonly monitored during fine-tuning to prevent overfitting on the training set?

* A) Validation Loss (eval_loss)
* B) GPU core temperature
* C) Total disk space occupied by logs
* D) The length of user prompts in testing

---

## Answer Key

| Question # | Correct Answer | Concept Tested & Rationale |
| :--- | :--- | :--- |
| **1** | **B** | Base models naturally want to complete text documents. SFT teaches the model the conversational turn-taking format: interpreting instructions and returning helpful answers. |
| **2** | **A** | Full fine-tuning requires updating and storing gradients for billions of parameters. PEFT methods freeze base weights and train small adapter modules, cutting memory footprints. |
| **3** | **A** | LoRA freezes the original weight W_0 and injects trainable rank decomposition matrices: ΔW = B × A, where the rank r is much smaller than the hidden dimension d. |
| **4** | **B** | Catastrophic forgetting occurs when gradient updates on a specialized domain overwrite neural pathways responsible for general reasoning and linguistic fluency. |
| **5** | **A** | QLoRA combines 4-bit NormalFloat base model quantization, double quantization, and paged optimizers with LoRA adapters, drastically democratizing fine-tuning. |
| **6** | **A** | Instruction datasets (like ShareGPT or Alpaca format) structure examples into clear conversational roles (system, human, assistant) using chat templates. |
| **7** | **A** | Co-training with a mix of general instruction data and specialized domain data prevents model weights from drifting excessively away from foundational competencies. |
| **8** | **A** | RAG is ideal for dynamic knowledge that updates frequently and needs direct source auditability. Fine-tuning is preferred for teaching style, format, and static specialization. |
| **9** | **A** | Distillation transfers the reasoning density of massive teacher models (e.g. 70B+) into lightweight student models (e.g. 3B-8B) for fast, low-cost edge deployment. |
| **10** | **A** | If training loss decreases while validation loss starts rising, the model is overfitting to the training examples and losing generalization ability. |
