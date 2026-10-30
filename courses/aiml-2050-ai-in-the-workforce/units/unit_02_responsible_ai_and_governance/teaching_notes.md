# [Instructor Guide] Unit 02 Teaching Notes & Delivery Guide
## Responsible AI, Risk Management & Enterprise Governance

> **Target Audience**: Instructors & Facilitators  
> **Workflow State**: `unpublished` (Hidden from students in Canvas)

---

## 1. Synchronous Delivery Agenda (60-Minute In-Class Practicum)
- **00–15 min (Hook & The $50,000 Loop Lock)**: Present a case study of an autonomous agent that entered an infinite loop overnight, consuming thousands in API credits and generating 500 bogus Jira tickets.
- **15–30 min (NIST AI RMF Walkthrough)**: Walk through the 4 functions. Contrast NIST RMF with traditional cybersecurity frameworks (ISO 27001).
- **30–50 min (Active Learning Clinic: Break the Agent)**: Provide students with a sample agent specification and have them brainstorm adversarial attacks (indirect prompt injection via resume).
- **50–60 min (Debrief & Video Rubric Review)**: Review video submission guidelines and preview Unit 03 (Workplace Prototyping).

---

## 2. Common Student Misconceptions & Gotchas
- **"Ethical AI is just a policy document"**: Emphasize that governance in this course requires *technical controls* (iteration caps, Pydantic schema validation, out-of-band human confirmation).
- **"Human-in-the-loop slows everything down"**: Show that 90% of routine actions remain Tier 1 (autonomous); only high-impact actions are gated.
