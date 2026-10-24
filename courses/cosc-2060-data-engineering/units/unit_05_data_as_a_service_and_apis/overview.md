# Unit 05 Overview: Data-as-a-Service & Asynchronous APIs

Data pipelines are useless if downstream applications and AI models cannot access their output reliably. Unit 05 teaches you how to expose curated analytical data as high-concurrency, asynchronous RESTful web services using FastAPI, Pydantic, and ASGI servers.

---

## Weekly Contact Hour Budget (300 Minutes Total)
- **Conceptual Study & Readings (150 min)**: Master asynchronous Python (`async`/`await`), non-blocking database queries, OpenAPI specifications, and HTTP status codes.
- **Asynchronous Preparation & Drills (60 min)**: Trace async event loops, design clean URL hierarchies, and write Pydantic response models.
- **Hands-on Engineering Lab (90 min)**: Develop and test the Production Logistics REST API service.

---

## Measurable Learning Objectives
By the end of this unit, you will be able to:
1. **Develop** asynchronous REST API endpoints using FastAPI with automated OpenAPI / Swagger documentation.
2. **Validate** request payloads and serialize response schemas using strict Pydantic v2 models.
3. **Implement** pagination, filtering, and rate limiting to protect backend databases from query exhaustion.
4. **Write** automated API integration test suites verifying HTTP 200, 400, 404, and 422 error states.

---

## Weekly Learning Roadmap & Deliverables

Follow the sequential module workflow in Canvas to complete this unit:

1. **Step 1: Required Readings & Reference Architecture**  
   Study asynchronous Python concurrency (`async`/`await`), non-blocking database queries, and OpenAPI data contracts in the module reading.
2. **Step 2: Diagnostic Drills & Syntax Checks**  
   Complete the asynchronous concept checks, async event loop traces, and HTTP error code matching drills before tackling the lab.
3. **Step 3: Applied Engineering Lab & Starter Code**  
   Build and test your unified logistics FastAPI microservice (`lab5_starter.py`) adhering to the 100-point rubric, then submit your script to the assignment dropbox.
4. **Step 4: Knowledge Check & Concept Verification**  
   Take the untimed 10-question formative assessment in Canvas (up to 3 attempts, highest score kept) to lock in key terminology and mental models.
