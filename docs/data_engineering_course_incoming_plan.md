COSC 2060: Modern Data Engineering & AI Infrastructure
Format: 16 Weeks (8 Units) Prerequisites: Beginning SQL & Intermediate Python Pedagogical Model: Backward Design (Target-Driven Architecture)
Phase 1: Terminal Course Outcomes (What Students Will Be Able to Do)
By the end of week 16, students will have built a fully functional, production-ready AI data ecosystem. Specifically, they will be able to:
Design Target-Driven Pipelines: Transform raw, multimodal data (relational, textual, visual) backward from the exact schema required by downstream machine learning models.
Prevent Model Sabotage: Implement defensive engineering tactics, such as point-in-time joins, to prevent temporal data leakage and look-ahead bias.
Deploy Data as a Service (DaaS): Wrap cleaned, scaled data products inside secure RESTful APIs instead of exporting flat CSV files.
Build Agentic Bridges: Implement the Model Context Protocol (MCP) to safely expose enterprise databases and APIs to autonomous LLMs.
Orchestrate the Lifecycle: Automate the entire ingestion-to-inference workflow using modern DAG-based schedulers (e.g., Dagster, Prefect, or n8n).
Phase 2 & 3: The 16-Week Canvas Module Progression
Unit 1: The Relational Foundation (Supervised Learning Targets)
Duration: Weeks 1 & 2 The Goal: Transform raw transactional logs into a flat, wide feature matrix for predicting delivery delays, explicitly avoiding temporal data leakage.
Lessons:
Lesson 1.1: The Shape of AI Data: BI Dashboards vs. ML Feature Matrices.
Lesson 1.2: The Danger of Time: Look-ahead bias and why standard SQL joins ruin ML models.
Lesson 1.3: Advanced SQL for AI: Rolling windows, lags, point-in-time (As-Of) joins, and navigating DuckDB vs. standard Postgres syntax quirks.
Lab Assignment: Lab 1: The Feature Matrix Builder
Task: Students are given 3 messy relational tables (Drivers, Routes, Weather). Using DuckDB or Advanced SQL, they must write a script that outputs a single flat feature matrix predicting delivery_delay, ensuring no future weather data leaks into historical route records.
Unit 2: The Anomaly Engine (Unsupervised Learning Targets)
Duration: Weeks 3 & 4 The Goal: Prepare scaled, standardized data to feed an Isolation Forest algorithm to detect fraudulent fuel purchases or anomalous route deviations.
Lessons:
Lesson 2.1: Why Scale Matters: Distance metrics and the mathematics of clustering.
Lesson 2.2: Data Normalization: Z-scores, Min-Max scaling, and handling missing numerical/categorical values programmatically.
Lesson 2.3: High-Performance Python: Ditching Pandas for Polars to process millions of rows, and understanding "Lazy vs. Eager" execution models.
Lab Assignment: Lab 2: The Outlier Detection Pipeline
Task: Using Python and Polars, ingest 1 million raw fuel transaction records. Clean the nulls, One-Hot encode categorical variables, scale the continuous variables, and output a sparse matrix perfectly formatted for scikit-learn's unsupervised models.
Unit 3: The Visual Sensor Layer (Computer Vision Targets)
Duration: Weeks 5 & 6 The Goal: Process a chaotic folder of raw truck inspection images into a standardized YOLO (You Only Look Once) training manifest for object detection (e.g., identifying tire damage).
Lessons:
Lesson 3.1: The Anatomy of Visual Data: Pixels, tensors, and EXIF metadata.
Lesson 3.2: Normalizing the Real World: Resizing, padding, and grayscale conversions.
Lesson 3.3: Target Schemas for Vision: Understanding bounding box coordinates (COCO vs. YOLO formats).
Lab Assignment: Lab 3: The Fleet Vision Manifest
Task: Write a Python OS script (using OpenCV) that iterates through a nested directory of 1,000 unevenly sized images, resizes them uniformly, and extracts their metadata. Using a provided visual GUI tool for the coordinate math, students will generate a master .txt manifest mapping image paths to their bounding box labels, allowing them to focus on the pipeline logic rather than the geometry.
Unit 4: Unstructured Text & RAG (LLM Targets)
Duration: Weeks 7 & 8 The Goal: Ingest years of PDF maintenance logs and driver notes, chunking and embedding them for Semantic Search and Large Language Model fine-tuning.
Lessons:
Lesson 4.1: The Language Target: Tokens, chunking strategies, and the ChatML JSONL format.
Lesson 4.2: Introduction to Vector Space: How embedding models turn paragraphs into math.
Lesson 4.3: Structuring the Unstructured: Injecting metadata tags to prevent LLM hallucinations.
Lab Assignment: Lab 4: Maintenance Log Vectorization
Task: Use Regex and Hugging Face Tokenizers to parse a curated folder of text-layered PDF mechanic reports (specifically avoiding scanned image OCR bottlenecks). Chunk the text by semantic paragraphs, embed them using a local model, and load them into a local vector database (like FAISS or Chroma) attached to original metadata tags.
Unit 5: Data as a Service (The API Layer)
Duration: Weeks 9 & 10 The Goal: Stop passing flat files around. Wrap the feature matrices, visual manifests, and vector indices into a live, queryable web server.
Lessons:
Lesson 5.1: The Death of the CSV: Why production AI relies on RESTful endpoints.
Lesson 5.2: Web Frameworks for Data: Introduction to FastAPI, route generation, HTTP verbs (GET, POST), and managing App State and Lifespans to safely host a database.
Lesson 5.3: Data Contracts: Validating incoming and outgoing API requests using Pydantic.
Lab Assignment: Lab 5: The Logistics Data API
Task: Build and launch a local FastAPI server. Create specific endpoints that allow a user to GET the latest weather features (from Unit 1), GET a specific truck's maintenance history (from Unit 4), and validate inputs via strict Pydantic schemas.
Unit 6: The Agentic Interface (MCP Integration)
Duration: Weeks 11 & 12 The Goal: Give an autonomous AI agent the "keys" to the data pipeline so it can read the enterprise data without hallucinatory guessing.
Lessons:
Lesson 6.1: Tool Calling & Agentic AI: How LLMs execute code and request data.
Lesson 6.2: The Model Context Protocol (MCP): Standardizing how AI talks to enterprise infrastructure.
Lesson 6.3: Secure Boundaries: Exposing read-only endpoints and sandboxing the LLM.
Lab Assignment: Lab 6: The MCP Server Build
Task: Construct an MCP server that registers the APIs built in Unit 5 as "Tools". Connect a lightweight local LLM (like a sub-2B parameter model for rapid testing) or an API key to the MCP server, proving the AI can successfully answer the prompt: "What is the maintenance history and current weather risk for Truck #402?" by pulling live data.
Unit 7: Orchestration & Automation
Duration: Weeks 13 & 14 The Goal: Tie the disparate scripts together. Build a scheduler that runs the entire ingestion, transformation, and API update process automatically.
Lessons:
Lesson 7.1: Directed Acyclic Graphs (DAGs): Managing script dependencies and mapping visual architecture diagrams to show how orchestrators trigger your scripts.
Lesson 7.2: Modern Orchestrators: Introduction to code-based orchestration (e.g., Dagster, Prefect, or n8n).
Lesson 7.3: Resiliency: Error handling, automatic retries, and dead-letter queues.
Lab Assignment: Lab 7: The Unsleeping Pipeline
Task: Wrap the Python scripts from Units 1 through 4 into orchestrated steps. Configure the DAG to run on a simulated daily schedule, ensuring that if a raw data file is missing, the pipeline logs an error but does not crash the server.
Unit 8: Capstone Defense & Handoff
Duration: Weeks 15 & 16 The Goal: Stress-test the full "Lifecycle of the AI App" and defend its architectural decisions in a simulated stakeholder meeting.
Lessons:
Lesson 8.1: System Hardening: Edge cases, token limits, and API rate limiting.
Lesson 8.2: Containerization Basics: Packaging the environment using Docker so it runs anywhere.
Lesson 8.3: The Executive Pitch: Explaining complex data plumbing to non-technical stakeholders and drafting a Stakeholder Evaluation Rubric to map technical metrics to business value.
Lab Assignment: Lab 8: Live Stakeholder Defense
Task: Students ingest a brand-new, unseen batch of raw logistics data into their fully automated pipeline. They must demonstrate the pipeline processing the data, updating the APIs, and their Agentic LLM successfully reasoning over the new data in real-time to a panel.
Appendix A: Technical Dependencies & Lab Environment
Pedagogical Stance: This course is designed to be 100% open-source, free of vendor lock-in, and entirely executable on local lab hardware. We are teaching the fundamental plumbing of AI systems, which is best learned close to the metal rather than abstracted away behind paid cloud services.
Hardware Requirements
Minimum Setup: Standard lab PCs with modern multi-core processors (Intel i5/i7 or AMD Ryzen), 16GB of RAM, and 50GB of free disk space.
Recommended (For Unit 6 Local LLMs): Machines with dedicated GPUs (NVIDIA RTX series) are highly recommended for running Ollama smoothly. However, if GPUs are unavailable, quantized small-parameter models (like qwen2.5:0.5b via Ollama) will run on CPU efficiently for tool-calling validation.
Software Stack (All 100% Open Source / Free)
All tools should be installed within a local Python Virtual Environment (venv or conda).
1. Data Processing & Tabular Transformations (Units 1 & 2)
Python 3.10+: The core programming language for the entire course.
DuckDB: An in-process, high-performance SQL OLAP database. Acts as our local data warehouse (No server setup required).
Polars: A lightning-fast DataFrame library written in Rust. Replaces Pandas to teach memory-efficient, multi-threaded columnar data processing.
Scikit-Learn: For mathematical transformations, scaling, and generating the Isolation Forest anomaly baseline.
2. Visual & Textual Unstructured Processing (Units 3 & 4)
OpenCV (opencv-python): The industry standard for image manipulation, resizing, and bounding-box coordination.
Hugging Face transformers & tokenizers: For semantic chunking and interacting with open-source embedding models.
ChromaDB or FAISS: Open-source, local-first vector databases to store and query embeddings without needing a cloud subscription.
3. API & Agentic Routing (Units 5 & 6)
FastAPI & Uvicorn: The fastest, most modern framework for spinning up local REST APIs.
Pydantic (v2): For strict data validation and creating "Data Contracts."
Ollama: A local runtime for serving Large Language Models. Students will use this to run a small, instruction-tuned model locally for the agentic reasoning lab.
Model Context Protocol (MCP) SDK: The open-source standard for connecting LLMs to data sources and tools.
4. Orchestration & Containerization (Units 7 & 8)
Dagster (or Prefect): Open-source, code-first orchestrators. We will use their local execution environments to teach DAGs (Directed Acyclic Graphs) and job scheduling.
Docker Desktop: Essential for the final capstone to package the entire pipeline, API, and agent into a portable, deployable container.
