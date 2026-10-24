# Unit 02 Knowledge Check: Real-Time Anomaly Detection & Schema Enforcement

### Question 1
Why is validating streaming data with Pydantic models superior to validating data using un-typed Python dictionaries?
* A) Pydantic models automatically convert all Python code into C binaries during startup.
* B) Pydantic enforces strict type coercion, field constraints, and descriptive validation errors at runtime before invalid records enter downstream pipelines.
* C) Python dictionaries cannot store floating-point numbers or timestamps.
* D) Pydantic bypasses the Python Global Interpreter Lock (GIL).

### Question 2
In stream processing, what is the fundamental difference between a "tumbling window" and a "sliding window"?
* A) Tumbling windows process data in reverse chronological order, while sliding windows process data alphabetically.
* B) Tumbling windows are fixed-size and non-overlapping, whereas sliding windows advance by an interval smaller than their window size and overlap.
* C) Tumbling windows only process integer values, while sliding windows process string fields.
* D) Sliding windows can only be executed on GPU clusters.

### Question 3
What statistical assumption must hold true for standard Z-score anomaly detection ($Z = \frac{x - \mu}{\sigma}$) to accurately identify outliers without excessive false positives?
* A) The underlying data distribution must be approximately normal (Gaussian).
* B) The dataset must contain exactly zero missing or null values.
* C) The data points must all be strictly positive integers.
* D) The variance of the dataset must be equal to zero.

### Question 4
When streaming telemetry data exhibits heavy skew or extreme outlier spikes, why is the Interquartile Range (IQR) method preferred over Z-score?
* A) IQR requires zero mathematical operations to compute.
* B) IQR uses the median and quartiles, making it robust against extreme outliers that would distort the sample mean and standard deviation.
* C) Z-score cannot be calculated on computers with less than 32GB of RAM.
* D) IQR automatically deletes anomalous rows from the database.

### Question 5
What is the primary role of a "dead-letter quarantine queue" in a production data ingestion pipeline?
* A) To discard all incoming data when server CPU utilization reaches 90%.
* B) To safely isolate corrupted, malformed, or unparseable records for inspection without halting the processing of valid streaming records.
* C) To compress old logs into ZIP archives once per year.
* D) To encrypt passwords before saving them to disk.

### Question 6
How does Pydantic's `Field(..., ge=0, le=100)` parameter contribute to defensive data engineering?
* A) It rounds all floating-point numbers to two decimal places.
* B) It enforces declarative boundary checks (e.g. value must be greater than or equal to 0 and less than or equal to 100), rejecting out-of-range sensor readings automatically.
* C) It forces the field to be stored as a 64-bit integer on disk.
* D) It converts string percentages into boolean values.

### Question 7
In time-series data engineering, what critical issue occurs if timestamps are parsed without explicit timezone handling (e.g., naive vs. aware datetime objects)?
* A) The database will refuse to start upon reboot.
* B) Telemetry points from daylight saving transitions or multi-region servers will be misaligned in time, producing false latency anomalies and corrupted sliding windows.
* C) The CPU clock frequency will throttle by 50%.
* D) Timestamps will automatically be converted to hexadecimal strings.

### Question 8
What is "concept drift" in the context of streaming anomaly detection systems?
* A) The physical failure of hard disk drive sectors holding telemetry logs.
* B) A statistical change in the underlying data distribution over time (e.g. seasonal baseline shifts), causing static anomaly thresholds to become inaccurate.
* C) A syntax error introduced when updating Python packages via pip.
* D) The loss of network packets over UDP connections.

### Question 9
In Pydantic v2, what is the purpose of `@field_validator(mode='before')`?
* A) It runs validation and transformation logic on raw input data before Pydantic applies its internal type coercion.
* B) It deletes the field before saving the object to SQLite.
* C) It executes the validation function asynchronously in a background thread.
* D) It prevents any student from viewing the source code of the model.

### Question 10
When calculating rolling metrics over a streaming telemetry window, what is "event time" versus "processing time"?
* A) Event time is when the operating system boots; processing time is when Python starts.
* B) Event time is when the physical sensor generated the record; processing time is when the pipeline engine actually ingests and analyzes the record.
* C) Event time is measured in seconds; processing time is measured in milliseconds.
* D) Event time and processing time are completely identical in all distributed systems.

## Answer Key
| Question # | Correct Answer | Concept Tested & Rationale |
| :--- | :--- | :--- |
| **1** | **B** | Pydantic validates types, ranges, and constraints at runtime, raising ValidationError on bad input rather than passing dirty data downstream. |
| **2** | **B** | Tumbling windows segment time into non-overlapping blocks; sliding windows advance incrementally and overlap, smoothing rolling trends. |
| **3** | **A** | Z-score assumes a Gaussian distribution; in skewed or bimodal distributions, standard deviation is inflated, resulting in high false alarm rates. |
| **4** | **B** | The median and IQR ($Q3 - Q1$) are non-parametric and resistant to extreme values, whereas mean and standard deviation are easily skewed by outliers. |
| **5** | **B** | Dead-letter queues prevent bad records from crashing streaming pipelines while preserving the payload and error logs for debugging and replay. |
| **6** | **B** | Declarative constraints like ge/le guard against physically impossible sensor readings (e.g. negative fuel volume or temperature above 5000 degrees). |
| **7** | **B** | Naive datetimes assume local system time, causing catastrophic ordering and temporal join errors across daylight savings changes or multiple timezones. |
| **8** | **B** | Concept drift occurs when the statistical properties of the target metric change over time, requiring dynamic baselines rather than hardcoded thresholds. |
| **9** | **A** | `mode='before'` validators intercept raw inputs (like stringified numbers or malformed dates) to sanitize them before standard type coercion runs. |
| **10** | **B** | Event time represents the authentic timestamp when an observation occurred at the edge, whereas processing time reflects server arrival time. |
