# [Institution Name] [Department Name]
## Capstone Peer Review Audit Rubric (20 Points Total)
**Course:** [Course Code] ([Course Title])  
**Corequisite:** [Corequisite Project Name]  
**Auditor Name:** ________________________  
**Author / Team Audited:** ________________________  
**Date of Audit:** ________________________  

---

### Instructions for the Auditor
Conduct an empirical, constructive peer review audit of a classmate's codebase or project deliverable. Test their project on your workstation—never take claims on faith! Rate each pillar from 0 to 5 points.

---

### Pillar 1: Reproducibility & Environment Hygiene (5 Points)
| Criterion | Target Standard | Score (0-5) | Auditor Notes |
| :--- | :--- | :--- | :--- |
| **1.1 Automated Setup & Launch** | Clone repo -> run setup script -> system running in < 3 minutes without manual path hacks. | ___ / 1.5 | |
| **1.2 Pinned Dependency Tree** | Dependencies specify explicit version bounds to prevent breaking changes. | ___ / 1.0 | |
| **1.3 Environment Variable Hygiene** | Valid configuration template (`.env.example`) provided. Zero hardcoded secrets or absolute local paths. | ___ / 1.5 | |
| **1.4 Packaging Standards** | Self-contained package or container with clean non-root permissions and healthcheck. | ___ / 1.0 | |

*Pillar 1 Subtotal: _____ / 5.0*

---

### Pillar 2: Defensive Posture & Edge-Case Guardrails (5 Points)
| Criterion | Target Standard | Score (0-5) | Auditor Notes |
| :--- | :--- | :--- | :--- |
| **2.1 Input Boundary Validation** | Intercepts invalid, out-of-bound, or malicious inputs at the boundary. | ___ / 1.5 | |
| **2.2 Privacy & Sensitive Data Scrubbing** | Sanitizes sensitive tokens, keys, or personal identifiers before core processing. | ___ / 1.5 | |
| **2.3 Data Leakage Prevention (DLP)** | Verifies internal system context never leaks into client-facing outputs. | ___ / 1.0 | |
| **2.4 High-Impact Authorization Gates** | High-impact actions require explicit operator or human sign-off. | ___ / 1.0 | |

*Pillar 2 Subtotal: _____ / 5.0*

---

### Pillar 3: Chaos Resilience & Graceful Degradation (5 Points)
| Criterion | Target Standard | Score (0-5) | Auditor Notes |
| :--- | :--- | :--- | :--- |
| **3.1 Circuit Breaker / Watchdog** | External dependencies wrapped in watchdogs that trip after consecutive failures. | ___ / 1.5 | |
| **3.2 Exponential Backoff with Jitter** | Transient errors trigger exponential delay with randomized jitter. | ___ / 1.0 | |
| **3.3 Deterministic Output Recovery** | Malformed or corrupted responses are rescued into safe typed defaults. | ___ / 1.5 | |
| **3.4 Graceful Fallback Communication** | Application communicates offline status clearly rather than crashing with unhandled tracebacks. | ___ / 1.0 | |

*Pillar 3 Subtotal: _____ / 5.0*

---

### Pillar 4: Architecture & Software Hygiene (5 Points)
| Criterion | Target Standard | Score (0-5) | Auditor Notes |
| :--- | :--- | :--- | :--- |
| **4.1 Strict Typing & Signatures** | Functions utilize explicit type annotations and complete docstrings. | ___ / 1.5 | |
| **4.2 Modular Separation of Concerns** | Clear directory layout with separated components. | ___ / 1.5 | |
| **4.3 Automated Verification Suite** | Test runner passes 100% assertions on first execution. | ___ / 1.0 | |
| **4.4 Professional Documentation** | Comprehensive `README.md` with architectural diagram and domain problem statement. | ___ / 1.0 | |

*Pillar 4 Subtotal: _____ / 5.0*

---

### Final Scoring Summary
- **TOTAL SCORE:** _______ / 20 Points
- **Status:**
  - [ ] **Ready for Final Defense (18 - 20 pts)**
  - [ ] **Conditional Approval (14 - 17.5 pts)**
  - [ ] **Revision Required (< 14 pts)**

**Auditor Signature:** __________________________________
