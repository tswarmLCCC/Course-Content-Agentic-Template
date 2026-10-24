# Master Curriculum & Project Defense Rubric (100 Points Total)
**Standardized Evaluation Framework for Intel AI Modernization & Student Capstone Systems**

---

# Part 1: Course Modernization & Instructional Slide Quality Rubric
*Evaluates the quality, pedagogical rigor, and technical depth of modernized lecture modules and slide decks.*

### Scoring Overview
Rated across 4 core domains (25 points each). A score of 90+ denotes production-ready, enterprise-grade instructional delivery.

---

### Domain 1: Technical Depth & Calibrated Parity (25 Points)
- **1.1 Calibrated Depth & Scope (No Slide Bloat):** Uses the legacy Intel materials as a reliable ballpark benchmark for conceptual depth and rigor without arbitrarily inflating slide count. Prioritizes concise, high-impact instruction over sprawling, redundant decks. (___ / 5)
- **1.2 Modern Technology Integration:** Accurately bridges legacy topics (e.g., scikit-learn, CNNs, classical computer vision) with modern frontiers (GenAI, SLMs, agentic workflows, OpenVINO 2024+). (___ / 5)
- **1.3 Architectural & Mathematical Accuracy:** Mathematically precise formulations (Perceptron weights, loss functions, confusion matrices, evaluation metrics). (___ / 5)
- **1.4 Toolchain Fidelity:** References real-world production libraries, SDKs, and platforms (Intel OpenVINO, Hugging Face, PyTorch, CVAT) with zero fabricated API calls. (___ / 5)
- **1.5 Hardware & Edge Grounding:** Explicitly covers hardware execution tradeoffs (CPU vs. iGPU vs. VPU/NPU, quantization, memory bandwidth). (___ / 5)
*Domain 1 Subtotal: _____ / 25*

---

### Domain 2: Pedagogical Scaffolding & Problem-First Cadence (25 Points)
- **2.1 Problem-First Scaffolding Cadence:** Every technical concept systematically moves through 4 explicit stages:
  1. *The Context:* Why are students studying this?
  2. *The Problem Without It:* What is the severe bottleneck, limitation, or failure mode if this technology did not exist?
  3. *How It Works:* What is the conceptual/architectural mechanism solving that problem?
  4. *How to Use It:* How do we implement, measure, and deploy it in modern workflows? (___ / 5)
- **2.2 Upfront Objectives & Outcomes Slide:** Opening slides explicitly state conceptual learning objectives alongside tangible software/model deliverables students will build. (___ / 5)
- **2.3 "Battle Plan" Alignment Slide:** A dedicated roadmap slide visually connecting the lecture's sections directly to the hands-on spinal project milestone. (___ / 5)
- **2.4 Cognitive Load & Text Density Management:** Zero walls of text; adherence to card encapsulation and concise, bold-anchored takeaways. (___ / 5)
- **2.5 Deep Speaker Notes Coverage:** 100% of slides feature rich instructor narrative, addressing common student misconceptions and live-coding guidance. (___ / 5)
*Domain 2 Subtotal: _____ / 25*

---

### Domain 3: Visual Polish & Presentation Standards (25 Points)
- **3.1 Assertion-Evidence Headlines:** Slide titles make declarative engineering assertions rather than generic topic labels. (___ / 5)
- **3.2 Archetype Discipline:** Correctly implements the 5 visual archetypes (Split-Hero, Section Divider, Two-Column, Normal Card, Code Card) defined in `SLIDE_DESIGN_PLAYBOOK.md`. (___ / 5)
- **3.3 Strict Left-Aligned Code Formatting:** Code blocks strictly adhere to `PP_ALIGN.LEFT` in Consolas with zero center-justification. (___ / 5)
- **3.4 WCAG 2.1 AAA Contrast:** Visual cards enforce high-contrast ratios (>7:1 body, >11:1 titles); zero low-contrast text on white cards. (___ / 5)
- **3.5 Master Layout Cleanliness:** All legacy partner watermarks and third-party logos cleanly purged from slide masters. (___ / 5)
*Domain 3 Subtotal: _____ / 25*

---

### Domain 4: Hands-On Spinal Project & Lab Integration (25 Points)
- **4.1 Progressive Milestone Alignment:** Unit activities contribute directly to the evolving course-wide project rather than isolated toy exercises. (___ / 5)
- **4.2 Agentic Engineering Integration:** Guides students to effectively use agentic AI tools to scaffold, test, and refactor features responsibly. (___ / 5)
- **4.3 Intel AI Lifecycle Continuity:** Lab activities explicitly track and update the 6-stage Intel AI project lifecycle. (___ / 5)
- **4.4 Responsible AI / Ethics Audit:** Incorporates real bias checks, privacy filters, or transparency views into the working app. (___ / 5)
- **4.5 Automated Verification:** Exercises include automated test scripts, data validation checks, or empirical benchmarks. (___ / 5)
*Domain 4 Subtotal: _____ / 25*

---

# Part 2: Student Course-Wide Capstone Project Defense Rubric
*Evaluates the student's end-of-course functioning system, technical defense, and engineering execution.*

### Domain 1: Problem Formulation & Intel AI Lifecycle (25 Points)
- **1.1 Scoping & The 4Ws Problem Canvas:** Thorough identification of Who, What, Where, and Why, with clear in-scope and out-of-scope boundaries. (___ / 5)
- **1.2 Data Acquisition & Hygiene:** Rigorous data sourcing, license verification, privacy anonymization, and exploratory distribution analysis. (___ / 5)
- **1.3 Algorithmic Fairness & Bias Mitigation:** Documented audit for demographic, label, or representation bias in training data and model outputs. (___ / 5)
- **1.4 Feasibility & Impact Matrix:** Realistic assessment of technical feasibility vs. business/operational value. (___ / 5)
- **1.5 Executive Problem Hook:** Engaging explanation of the operational bottleneck solved by the application. (___ / 5)
*Domain 1 Subtotal: _____ / 25*

---

### Domain 2: Technical Architecture & Agentic Implementation (25 Points)
- **2.1 Multi-Modal Capability Integration:** Cohesive integration of tabular ML, computer vision, and NLP/conversational capabilities within a single UI. (___ / 5)
- **2.2 Codebase Modularization & Cleanliness:** Clear separation of concerns (frontend, data pipelines, model inference, utility wrappers). (___ / 5)
- **2.3 Responsible Agentic Collaboration:** Documented prompt engineering and agent interaction logs demonstrating active oversight rather than blind copy-pasting. (___ / 5)
- **2.4 Error Handling & Fallback Guardrails:** Graceful failure handling when models encounter out-of-distribution inputs or low confidence. (___ / 5)
- **2.5 Rigorous Evaluation Dashboard:** Live visualization of evaluation metrics (Confusion Matrix, Precision/Recall, ROC/AUC, MAE/RMSE). (___ / 5)
*Domain 2 Subtotal: _____ / 25*

---

### Domain 3: Edge Optimization & Hardware Acceleration (25 Points)
- **3.1 Intel OpenVINO Integration:** Successful conversion and execution of models using the OpenVINO runtime engine. (___ / 5)
- **3.2 Empirical Latency & Memory Benchmarks:** Documented profiling of inference latency (p50, p95), FPS, and RAM footprint across devices. (___ / 5)
- **3.3 Model Quantization & Compression:** Practical application of FP16 or INT8 quantization with measured accuracy trade-offs. (___ / 5)
- **3.4 Edge Deployment Readiness:** Ability to run locally without persistent cloud API dependencies. (___ / 5)
- **3.5 Hardware Target Justification:** Defensible rationale for target silicon (Intel Core CPU, iGPU, or edge NPU). (___ / 5)
*Domain 3 Subtotal: _____ / 25*

---

### Domain 4: Live Demonstration, Governance & Oral Defense (25 Points)
- **4.1 Live Critical Journey Execution:** Flawless live demonstration of the end-to-end user workflow within a 3-minute window. (___ / 5)
- **4.2 Transparency & Explainability (XAI):** UI displays confidence scores, saliency heatmaps, or source citations explaining AI outputs. (___ / 5)
- **4.3 Adversarial Defense & Cross-Examination:** Poised, authoritative technical answers defending architectural choices under instructor questioning. (___ / 5)
- **4.4 Societal & Ethical Governance Compliance:** Evidence of alignment with the AI Ethics Canvas and responsible deployment guidelines. (___ / 5)
- **4.5 Professional Demeanor & Technical Vocabulary:** Confident, accurate use of industry-standard AI and software engineering terminology. (___ / 5)
*Domain 4 Subtotal: _____ / 25*

---

### Scoring Tier Summary
- **90 – 100 Points:** Exemplary Honors (Enterprise / Production Grade)
- **80 – 89.5 Points:** Proficient (Meets Workforce Readiness Standards)
- **70 – 79.5 Points:** Developing (Requires Targeted Technical Remediation)
- **< 70 Points:** Unsatisfactory (Significant Redesign Required)
