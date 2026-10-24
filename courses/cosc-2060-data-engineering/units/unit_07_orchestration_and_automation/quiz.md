# Unit 07 Knowledge Check: Orchestration, Resilient DAGs & Telemetry Alerting

### Question 1
In workflow orchestration, what is a Directed Acyclic Graph (DAG)?
* A) A cyclical loop of tasks that executes indefinitely without ever stopping.
* B) A mathematical representation of pipeline tasks where directed edges define strict dependencies and no path leads back to a previously executed node.
* C) A graphical chart used exclusively for displaying team member salaries.
* D) A database index structure used only for spatial GIS coordinates.

### Question 2
What does it mean for a data engineering task or pipeline to be "idempotent"?
* A) The task executes in zero milliseconds regardless of data size.
* B) Executing the task multiple times with the same input produces the exact same system state and output as executing it once, preventing duplicate records.
* C) The task can only be executed by a user with administrative credentials.
* D) The task automatically converts all output data into CSV format.

### Question 3
Why is "exponential backoff with jitter" preferred over immediate fixed retries when handling transient network failures in automated pipelines?
* A) It guarantees that the network failure will never happen again.
* B) It exponentially increases the delay between retries and injects random noise (jitter) to prevent the "thundering herd" problem from overwhelming recovering servers.
* C) It forces the operating system to reboot after each retry attempt.
* D) It reduces the memory size of the database.

### Question 4
In automated data pipeline design, what is the consequence of designing non-idempotent batch append tasks (`INSERT INTO table SELECT * FROM stage`)?
* A) The query will execute 10 times faster on every run.
* B) If a pipeline fails mid-run and is restarted by an orchestrator, duplicate rows will be inserted, corrupting financial reports and downstream metric calculations.
* C) The database will automatically delete all older tables.
* D) The database will switch from SQL to MongoDB.

### Question 5
What is the function of a "circuit breaker" pattern in distributed data pipelines?
* A) To physically shut off power to the server rack during an electrical surge.
* B) To temporarily halt requests to a failing upstream service after a threshold of consecutive errors, preventing system cascading failure and allowing recovery.
* C) To encrypt database connections using TLS certificates.
* D) To force all Python scripts to run with administrator rights.

### Question 6
When designing automated data quality gates in a DAG, what should occur if an automated schema validation test fails?
* A) The pipeline should silently ignore the error and publish the bad data to production dashboards.
* B) Downstream dependent tasks should be blocked immediately, the corrupt batch quarantined, and an alerting event dispatched to on-call engineers.
* C) The server should delete the source code of the pipeline.
* D) The database should reverse the direction of all primary keys.

### Question 7
In pipeline observability, what are the three foundational telemetry pillars?
* A) HTML, CSS, and JavaScript.
* B) Metrics (numeric time-series), Logs (structured event records), and Traces (end-to-end request lifecycle spans).
* C) CPU, RAM, and Hard Drive.
* D) Python, DuckDB, and Polars.

### Question 8
What is a Service Level Agreement (SLA) breach in data engineering operations?
* A) A student failing to submit their laboratory assignment on time.
* B) A failure to deliver data, pipeline updates, or query responses within a contractual or operational time threshold (e.g. data fresh within 15 minutes of midnight).
* C) A legal lawsuit filed by an operating system vendor.
* D) A syntax error caught during Python compilation.

### Question 9
How does deterministic partition processing (e.g., executing pipelines by discrete partition date `2026-10-24`) facilitate pipeline backfilling?
* A) It requires all historical data to be deleted before running backfills.
* B) It allows historical date ranges to be reprocessed safely and independently in parallel without mutating or corrupting adjacent date partitions.
* C) It converts all historical dates into Julian calendar formats.
* D) It prevents any query from accessing data older than 7 days.

### Question 10
Why should production orchestrator credentials and database passwords never be hardcoded into pipeline DAG definitions?
* A) Because Python scripts run 50% slower when they contain passwords.
* B) Hardcoded secrets in source control expose systems to catastrophic credential theft; credentials should be injected via environment variables or secret vaults.
* C) Because Git repositories automatically delete files containing passwords.
* D) Because hardcoded passwords cause syntax errors in YAML files.

## Answer Key
| Question # | Correct Answer | Concept Tested & Rationale |
| :--- | :--- | :--- |
| **1** | **B** | A DAG defines execution dependencies between tasks where execution flows forward along directed edges with zero circular loops. |
| **2** | **B** | Idempotence guarantees that retrying a failed task produces identical state without side effects, data duplication, or double-counting. |
| **3** | **B** | Exponential backoff prevents pounding downstream services, and jitter desynchronizes clients to avoid synchronized retry waves. |
| **4** | **B** | Unbounded inserts on retry duplicate data; idempotent patterns use staging tables, partition replacements, or `UPSERT`/merge logic. |
| **5** | **B** | Circuit breakers trip when error thresholds are crossed, fast-failing traffic to allow degraded upstream dependencies time to recover. |
| **6** | **B** | Quality gates enforce fail-fast behavior: bad batches are stopped before contaminating production data marts, and alerts are dispatched. |
| **7** | **B** | Metrics provide quantitative state monitoring, logs provide contextual diagnostic records, and distributed traces map request journeys. |
| **8** | **B** | SLAs define business-critical delivery commitments; an SLA breach indicates the pipeline failed to complete within agreed freshness windows. |
| **9** | **B** | Partition isolation ensures that backfilling or re-running a specific historical date operates cleanly without affecting current data state. |
| **10** | **B** | Hardcoding credentials in version-controlled scripts risks compromise; production systems inject secrets securely at runtime via vaults. |
