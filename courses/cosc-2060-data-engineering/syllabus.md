# Course Syllabus: COSC 2060 — Modern Data Engineering & AI Infrastructure

**LARAMIE COUNTY COMMUNITY COLLEGE**
- **Semester and Year:** Fall 2026 (Block: A16 August 24 – December 18)
- **Course Number, Title, and Credit Hours:** COSC 2060: Modern Data Engineering & AI Infrastructure – 3.0 Credit Hours
- **Prerequisites:** CMAP 1815 (Introduction to Modern SQL / Relational Databases) and introductory Python programming
- **Time and Location:** Access in person M/W in Arp Building 102/104 or online via Canvas (HyFlex: In-Person, Online Synchronous, and Online Asynchronous)
- **Instructor Contact Information:**
  - **Name:** Trevor Swarm
  - **Office:** Arp 161
  - **Telephone:** (307) 778-1321
  - **E-mail Address:** `tswarm@lccc.wy.edu`
  - **Office Hours:** Monday and Wednesday, 11:00 AM – 1:30 PM in Arp 161 or via Microsoft Teams
- **Communicating with the Instructor:** To contact the instructor regarding this class, either call the number listed above or send a message through the Canvas Inbox. Phone calls and messages are typically returned within two business days.
- **Last Date to Drop or Withdraw:** The last day to drop this course to receive a 100% refund and NOT receive a `W` on your transcript is September 4. The last day to withdraw from this course is November 3. Please consult with Enrollment Services or your Student Success Coach and Student Hub before initiating any schedule changes so you know how a change might affect your graduation timeline and financial aid.
- **Course Description:** This course provides practical, bottom-up instruction in modern data engineering and AI data infrastructure. Building directly on foundational SQL and Python skills, students learn how to transform raw operational databases, sensor logs, images, and text documents into clean, well-structured datasets and services for analytics, machine learning, and AI applications.
- **Other Course Information:** This course is simultaneously taught in three modalities: in-person, online synchronous, and online asynchronous. Students choose how they want to attend and engage in the course. Assignments and competencies are assessed uniformly across all three modalities over 16 weeks (8 two-week units).

*Please review all of the information on this page. You can open the accordion content of any section below by selecting its title bar.*

---

## 1. Course Materials & Zero-Cost Software Stack

- **Textbook:** **None (Zero-Cost OER Model)** — All required reading materials, interactive notebooks, reference guides, and video walkthroughs are provided directly inside each unit module in Canvas and in your GitHub Codespaces sandbox.
- **Lab Environment:** **GitHub Codespaces Student Sandbox** (`https://github.com/tswarmLCCC/COSC-2060-Student-Sandbox`) — A free, pre-configured cloud Linux workstation running in your web browser or VS Code with zero local installation required.
- **Open-Source Software Stack (Pre-Installed in Your Sandbox):**
  - **Python 3.11 & Jupyter Notebooks:** Core programming language and interactive notebook environment.
  - **DuckDB & Apache Parquet:** Fast, single-file columnar SQL database and storage format (`Units 1–2`).
  - **Polars & Scikit-Learn:** High-speed DataFrame library and statistical feature scaling tools (`Unit 2`).
  - **OpenCV & Pillow:** Image loading, resizing, and computer vision bounding-box formatting (`Unit 3`).
  - **ChromaDB & Tokenizers:** Text chunking, embeddings, and local vector search for Retrieval-Augmented Generation (`Unit 4`).
  - **FastAPI, Uvicorn & Pydantic v2:** Building and validating web APIs to serve data (`Unit 5`).
  - **Model Context Protocol (MCP):** Connecting AI agents safely to database and API tools (`Unit 6`).
  - **Dagster, GitHub Actions & Docker:** Automating scheduled data pipelines and packaging projects in containers (`Units 7–8`).

---

## 2. Course Content Outline & 16-Week Schedule

The course is organized into 8 two-week units. Each unit builds one specific data shape or infrastructure layer from the ground up:

| Unit | Weeks | Unit Topic | Target Data Shape / Deliverable | Core Tools |
| :--- | :--- | :--- | :--- | :--- |
| **Unit 01** | Weeks 1–2 | Relational Foundations & Supervised Learning Tables | Flat 2D Feature Matrix (`X` inputs and `y` target) | SQL, DuckDB, Parquet |
| **Unit 02** | Weeks 3–4 | Anomaly Detection & Feature Scaling | Scaled & Encoded Numerical Matrix (`Z`-scores, One-Hot) | Polars, Apache Arrow |
| **Unit 03** | Weeks 5–6 | Visual Sensor Data & Image Preprocessing | Normalized Image Tensors & YOLO Bounding-Box Labels | OpenCV, NumPy |
| **Unit 04** | Weeks 7–8 | Unstructured Text & Vector Search (RAG) | Chunked Text Embeddings + Metadata in a Vector Store | ChromaDB, Regex, JSONL |
| **Unit 05** | Weeks 9–10 | Serving Data with Web APIs | Validated JSON REST Endpoints (`GET` / `POST`) | FastAPI, Pydantic v2 |
| **Unit 06** | Weeks 11–12 | Connecting AI Agents to Data (MCP) | Deterministic Python Tool Functions & MCP Server | Python MCP SDK |
| **Unit 07** | Weeks 13–14 | Automating & Scheduling Data Pipelines | Asset Dependency Graph (DAG) & Automated Retries | Dagster, GitHub Actions |
| **Unit 08** | Weeks 15–16 | Packaging with Docker & Capstone Defense | Multi-Stage Containerized Pipeline & Stakeholder Pitch | Docker, pytest |

---

## 3. Course Competencies (Learning Outcomes)

Upon successful completion of this course, students will be able to:

1. **Design and query** columnar analytical tables using DuckDB and Parquet to build flat feature tables from normalized databases.
2. **Prevent temporal data leakage** by using rolling window functions and point-in-time `ASOF JOIN` queries.
3. **Clean, scale, and encode** large tabular datasets using Polars expressions and Z-score standardization for anomaly detection.
4. **Process raw image files** into uniformly resized arrays and normalized YOLO bounding-box label files using OpenCV.
5. **Split unstructured text documents** into overlapping chunks with metadata tags and load them into a vector database for semantic search.
6. **Build and test** asynchronous REST APIs using FastAPI and Pydantic schemas to serve validated data over HTTP.
7. **Expose database queries and APIs** as safe, read-only tools for AI agents using the Model Context Protocol (MCP).
8. **Automate, containerize, and explain** an end-to-end data pipeline using DAG orchestration, Docker, and clear technical communication.

---

## 4. Attendance & Course Drop Policy

- **Attendance Definition:** Attendance in a face-to-face class is defined as physically attending a class where there is an opportunity for direct interaction between the instructor and student. Attendance in an online class, or the online portion of a hybrid or HyFlex class, is measured by the submission of coursework. The last date of attendance for all students is documented by the last on-time submission of work or physical attendance in class.
- **Drop for Non-Attendance:** To avoid being dropped from this class for non-attendance, students must participate in the class by either attending physically or virtually or by submitting an assignment by **September 4**. Students dropped for non-attendance will not be billed for the course.
- **Course Attendance Policy:** Student participation in all instructional sessions is expected. Any alterations to due dates or weekly materials will be announced via Canvas Announcements. Approved absences are defined in Administrative Procedure 4.4.2.1P.
- **Absence Due to College-Sponsored Activities:** Any student who will miss class for an LCCC-sponsored activity (such as an athletic team or class trip) must communicate with the instructor a minimum of five days prior to the absence and complete missed coursework within the timeline established with the instructor (Administrative Procedure 4.10.2P).
- **Class Cancellation Announcements:** When LCCC is closed due to weather or other emergencies, all on-campus classes are cancelled and communicated via the LCCC homepage and Rave text alerts. Instruction and assignment instructions will continue via Canvas.

---

## 5. Grading Policy, Weights & Scale

Your final grade in this course is determined by four weighted assignment categories in Canvas:

| Assignment Category | Weight | What It Covers |
| :--- | :---: | :--- |
| **Hands-on Data Engineering Labs** | **40%** | 8 applied Python/SQL labs completed in your personal GitHub Codespaces sandbox and submitted via GitHub repo link + changed files list in Canvas |
| **Comprehensive Capstone Defense** | **30%** | End-to-end containerized pipeline build and stakeholder architecture defense in Unit 8 |
| **Unit Knowledge Checks & Quizzes** | **20%** | 8 multiple-choice unit quizzes in Canvas (3 attempts allowed per quiz; highest score kept) |
| **Asynchronous Preparation & Drills** | **10%** | Weekly self-check drills, coding clinic practice, and Socratic AI review exercises |
| **Total** | **100%** | |

### Grading Scale
- **A:** 90.0% – 100%
- **B:** 80.0% – 89.9%
- **C:** 70.0% – 79.9%
- **D:** 60.0% – 69.9%
- **F:** Below 60.0%

### Late Work & Grade Appeals
- Specific due dates for all labs, quizzes, and drills are posted in Canvas. Assignments, projects, and lab work should be turned in on time; please reach out to the instructor in advance if an extension is needed or if accommodations have been issued by Student Accommodations.
- Students can access real-time grades in the Canvas Gradebook. Guidance for grade appeals is located in LCCC Administrative Procedure 3.17P.

---

## 6. Course Academic Integrity, Classroom Behavior & AI Policy

- **Academic Integrity (LCCC Administrative Procedures 3.15P & 3.16P):** Academic integrity involves creating and expressing your own ideas in coursework, acknowledging all sources, completing assignments independently or acknowledging collaboration, and accurately reporting lab results. Cheating—including submitting another person's code, sharing completed solution files, or using unauthorized aids—is prohibited under LCCC Administrative Procedures 3.15P and 3.16P.
- **Artificial Intelligence Policy:** LCCC requires all students to uphold academic integrity, including the use of AI. In COSC 2060, each unit includes a **Learn with AI** activity where you may use conversational AI tools (ChatGPT, Claude, Gemini, or Copilot) as a Socratic tutor and code reviewer. However, you are responsible for understanding, running, and verifying every line of code you push to your GitHub sandbox, and **you are ultimately responsible for any inaccuracies stemming from AI tools**. Never copy and paste unverified AI output into a lab submission.
- **Behavior in the Classroom:** All LCCC students are expected to display appropriate conduct (as defined in LCCC Administrative Procedure 3.15P) while on campus, in live synchronous sessions, or in online Canvas discussions.

---

## 7. LCCC Institutional Syllabus Addendum

- **Incomplete Grades:** The LCCC Catalog identifies the conditions under which a grade of `I` can be assigned based on attendance, course progress, prior assignment success, and instructor consent. Students can confirm eligibility by consulting the LCCC Catalog.
- **Student Rights and Responsibilities:** Students are expected to review and comply with the student rights and responsibilities outlined in the [LCCC Student Handbook](https://www.lccc.wy.edu/life/handbook/) and [LCCC College Policies](https://policies.lccc.wy.edu/).
- **Accommodations (Office of Student Accommodations — OSA):** Any student with a documented disability, Title IX issue (including pregnancy and breastfeeding needs), or Veteran disability is welcome to contact the Office of Student Accommodations (OSA) at any time in the semester. Please note that accommodations cannot be provided retroactively by law, so seeking accommodation as soon as it is needed is recommended.
  - **Cheyenne Campus & Online Students:** Pathfinder 207, call `(307) 778-1223`, or email `aclubb@lccc.wy.edu`.
  - **Laramie Campus:** Call `(307) 778-1223` or email `aclubb@lccc.wy.edu` (OSA staff are present on the Laramie Campus routinely).
- **Free Academic Tutoring:** All academic tutoring and resources are free and open to current LCCC students:
  - **Cheyenne Campus Learning Commons:** Visit LIB 137, call `(307) 778-4315`, or email `tutors@lccc.wy.edu`.
  - **Laramie Campus Library:** Visit Room 202A, call `(307) 772-4263` or `(307) 721-5138 ext. 4263`, or email `lctutors@lccc.wy.edu`.
  - **Online 24/7 Tutoring:** Schedule appointments through the **Navigate** app in myLCCC (select *Appointments → Schedule an Appointment → Learning Commons*) or access 24/7 online tutoring via **NetTutor** in the Canvas navigation menu.
