# Week 15 Knowledge Check: Prototyping Generative AI Applications

**Course**: AIML 1010: Introduction to Artificial Intelligence  
**Assessment Type**: Multiple Choice Knowledge Check  
**Allowed Attempts**: 3 | **Scoring Policy**: Keep Highest Score | **Points Possible**: 30.0

---

## Assessment Questions

### Question 1
What is the primary role of application frameworks like LangChain or LlamaIndex in Generative AI development?

* A) To manage low-level GPU silicon drivers
* B) To provide standardized abstractions for chaining LLM calls, connecting external tools, managing memory, and implementing RAG pipelines
* C) To compile Python code directly into assembly language
* D) To replace SQL databases with plain text files

### Question 2
What is the primary function of a Vector Database (such as Pinecone, Chroma, or Qdrant) in RAG applications?

* A) Storing high-dimensional vector embeddings and performing fast approximate nearest neighbor (ANN) similarity search
* B) Storing raw video files for streaming
* C) Executing automated Python unit tests
* D) Generating synthetic cryptographic keys

### Question 3
Why are tools like Streamlit and Gradio popular for rapid AI prototyping?

* A) They allow data scientists and engineers to build interactive web user interfaces entirely in Python with zero frontend HTML/CSS/JS expertise
* B) They replace the need for an underlying language model
* C) They run AI models on mobile devices without an internet connection
* D) They automatically write production database schemas

### Question 4
In a Retrieval-Augmented Generation (RAG) system, what does the 'Chunking' step accomplish?

* A) Breaking large unstructured documents into smaller, semantically coherent segments suitable for embedding and context window limits
* B) Deleting random paragraphs from documents to save disk space
* C) Compressing text into zip archives
* D) Splitting GPU memory into virtual partitions

### Question 5
What does LLMOps (Large Language Model Operations) encompass in enterprise software engineering?

* A) Practices and tooling for model deployment, monitoring, cost tracking, evaluation, latency management, and guardrails in production
* B) Manual human review of every token output by a chatbot
* C) Hardware maintenance of server rack cables
* D) Writing marketing copy for AI product launches

### Question 6
What is the function of Experiment Tracking platforms like Weights & Biases (W&B) or MLflow?

* A) Logging hyperparameters, prompt versions, evaluation metrics, and training loss curves for systematic reproducibility and comparison
* B) Streaming video tutorials to student developers
* C) Generating synthetic user bug reports
* D) Managing employee payroll for data science teams

### Question 7
What is 'Semantic Search' and how does it improve upon traditional keyword search?

* A) It matches queries based on conceptual meaning and vector similarity rather than exact lexical word overlap
* B) It searches only for words that rhyme with the query
* C) It translates all queries into binary machine code
* D) It requires the user to know the exact filename where information is stored

### Question 8
Why is 'Re-ranking' often used after initial vector retrieval in advanced RAG architectures?

* A) A specialized cross-encoder re-evaluates the top candidate chunks against the query to score true relevance, overcoming embedding retrieval noise
* B) It shuffles retrieved chunks randomly to increase answer creativity
* C) It discards all chunks that contain punctuation
* D) It translates retrieved chunks into French

### Question 9
What is the primary role of AI code assistants (like GitHub Copilot or Cursor)?

* A) Suggesting context-aware code completions, function implementations, documentation, and unit tests directly in the developer's IDE
* B) Automatically deploying untested code to production without human review
* C) Replacing the operating system kernel with an LLM
* D) Monitoring developer keystrokes for employee surveillance

### Question 10
What critical metric must developers monitor when designing production generative AI user experiences?

* A) Time to First Token (TTFT) and overall generation latency to maintain responsive interactivity
* B) The color temperature of the user's computer monitor
* C) The number of punctuation marks in the model weights
* D) The serial number of the client's network router

---

## Answer Key

| Question # | Correct Answer | Concept Tested & Rationale |
| :--- | :--- | :--- |
| **1** | **B** | Frameworks like LangChain orchestrate application components: prompt templates, model connectors, memory persistence, vector retrieval, and tool execution. |
| **2** | **A** | Vector databases index embeddings and calculate cosine or dot-product distance at scale, allowing applications to retrieve relevant context chunks for a query in milliseconds. |
| **3** | **A** | Streamlit and Gradio turn Python scripts into responsive web apps in minutes, making them the standard for prototyping, testing, and demonstrating AI workflows. |
| **4** | **A** | LLMs have finite context windows, and embedding entire books at once degrades retrieval precision. Chunking breaks text into searchable, granular pieces. |
| **5** | **A** | LLMOps extends DevOps/MLOps to handle LLM-specific operational concerns: token costs, latency, drift, prompt versioning, eval benchmarks, and security guardrails. |
| **6** | **A** | Experiment tracking logs every training run or prompt configuration with metrics and artifacts, making AI development reproducible and auditable. |
| **7** | **A** | Keyword search fails when users use synonyms (e.g. 'automobile' vs 'car'). Semantic search maps concepts into embedding space where related meanings cluster together. |
| **8** | **A** | Dense vector search retrieves candidate chunks quickly but can suffer from low precision. Cross-encoder re-rankers analyze the full query-chunk pair to prioritize the most relevant text. |
| **9** | **A** | AI coding assistants accelerate developer productivity by synthesizing boilerplate, implementing algorithms, suggesting tests, and explaining code in real time. |
| **10** | **A** | User experience degrades rapidly if users stare at blank screens. Streaming responses and optimizing Time to First Token (TTFT) ensure fluid, interactive software. |
