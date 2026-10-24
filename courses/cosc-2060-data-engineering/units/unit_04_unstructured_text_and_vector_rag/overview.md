# Unit 04 Overview: Unstructured Text Engineering & Vector Search (RAG)

Retrieval-Augmented Generation (RAG) is the dominant architecture for grounding generative AI in factual institutional data. Unit 04 covers the end-to-end data pipeline behind RAG: text extraction, semantic chunking strategies, embedding generation, and approximate nearest neighbor (ANN) vector search.

---

## Weekly Contact Hour Budget (300 Minutes Total)
- **Conceptual Study & Readings (150 min)**: Deconstruct chunking trade-offs, vector similarity search algorithms (HNSW, IVF), and context window limits.
- **Asynchronous Preparation & Drills (60 min)**: Evaluate chunk overlap boundaries, tokenization costs, and retrieval precision.
- **Hands-on Engineering Lab (90 min)**: Build the Diagnostic RAG Knowledge Base and Vector Index Lab.

---

## Measurable Learning Objectives
By the end of this unit, you will be able to:
1. **Design** recursive and semantic chunking pipelines that preserve context across document boundaries.
2. **Generate** text embeddings and index document vectors into ChromaDB or local vector stores.
3. **Implement** hybrid retrieval queries combining keyword filters with dense vector similarity search.
4. **Construct** an automated retrieval evaluation pipeline measuring precision at rank K (P@K).

---

## Weekly Learning Roadmap & Deliverables

Follow the sequential module workflow in Canvas to complete this unit:

1. **Step 1: Required Readings & Reference Architecture**  
   Study sliding-window chunking trade-offs, vector similarity search algorithms (HNSW), and context window economics in the module reading.
2. **Step 2: Diagnostic Drills & Syntax Checks**  
   Complete the asynchronous concept checks, chunk overlap edge cases, and hybrid retrieval scoring drills before tackling the lab.
3. **Step 3: Applied Engineering Lab & Starter Code**  
   Build and test your local vector ingestion pipeline (`lab4_starter.py`) adhering to the 100-point rubric, then submit your script to the assignment dropbox.
4. **Step 4: Knowledge Check & Concept Verification**  
   Take the untimed 10-question formative assessment in Canvas (up to 3 attempts, highest score kept) to lock in key terminology and mental models.
