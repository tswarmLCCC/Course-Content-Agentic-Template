# Feature Specification: [Iteration Title]

- **ID**: `specs/[NNN-name]`
- **Status**: Draft | In Review | Approved | Completed
- **Created**: [YYYY-MM-DD]
- **Target Completion**: [Estimated duration, e.g., 30 minutes]

---

## 1. Objective & Target Audience
- **Primary Persona**: [Who is using or consuming this? e.g., Student, Instructor, Curriculum Designer]
- **Problem Statement**: [What core problem or learning friction does this solve?]
- **One Job**: [The single, focused job this iteration delivers]

---

## 2. Requirements (EARS Syntax)

Requirements must use Easy Approach to Requirements Syntax:
- **Always (Ubiquitous)**:
  - `REQ-01`: The system/module **shall** [core ubiquitous behavior].
- **When (Event-Driven)**:
  - `REQ-02`: **When** [trigger event occurs], the system **shall** [response/action].
- **While (State-Driven)**:
  - `REQ-03`: **While** [in specific state/mode], the system **shall** [behavior].
- **If-Then (Error/Unwanted Behavior)**:
  - `REQ-04`: **If** [unwanted condition or invalid input], **then** the system **shall** [fallback/error mitigation].
- **Where (Optional Features)**:
  - `REQ-05`: **Where** [optional capability or setting enabled], the system **shall** [behavior].

---

## 3. Deliberately Out of Scope
*List items explicitly excluded from this iteration to prevent scope creep:*
- [Excluded feature or complexity 1]
- [Excluded feature or complexity 2]

---

## 4. Acceptance Criteria & Definition of Done
- [ ] Every requirement from REQ-01 through REQ-NN is verified and passing.
- [ ] Conforms to ADR-001 (Accessibility: WCAG 2.1/2.2 AA).
- [ ] Conforms to ADR-002 (Spec-driven documentation complete).
- [ ] Deliverables reviewed and accepted by the user.
