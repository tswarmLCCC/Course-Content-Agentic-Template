# Unit 1 Knowledge Check: Fundamentals & Core Syntax

This assessment evaluates your conceptual understanding of core syntax, query execution semantics, and common relational traps.

---

### Question 1
What is the primary role of the `SELECT` clause in a relational SQL query?
* A) It specifies the physical storage engine and file path on disk.
* B) It declares which attributes (columns) are projected into the output result set.
* C) It filters rows before they are processed by the storage engine.
* D) It enforces primary key constraints during data insertion.

### Question 2
In standard SQL execution order, which clause is evaluated **first**?
* A) SELECT
* B) ORDER BY
* C) FROM
* D) LIMIT

### Question 3
Why is using `SELECT *` considered a dangerous anti-pattern in production environments?
* A) It causes an immediate syntax error if the table exceeds 1,000 rows.
* B) It bypasses all database security policies and table permissions.
* C) It increases unnecessary I/O network bandwidth and breaks application models when schemas change.
* D) It converts integer columns into floating point numbers automatically.

---

## Answer Key

| Question # | Correct Answer | Concept Tested & Rationale |
| :--- | :--- | :--- |
| **1** | **B** | Relational projection. The SELECT clause determines which expressions or columns appear in the query projection. |
| **2** | **C** | Query execution lifecycle. The FROM clause must be evaluated first to establish the working data source before projection or filtering. |
| **3** | **C** | Production safety and performance. SELECT * retrieves all columns across the wire, consuming memory and bandwidth, and introduces schema coupling bugs. |
