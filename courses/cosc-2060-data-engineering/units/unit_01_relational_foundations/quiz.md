# Unit 01 Knowledge Check: Relational Foundations & Vectorized Ingestion

### Question 1
Why do traditional row-oriented relational database engines experience severe performance degradation when executing analytical queries (e.g., computing an average across 50 million rows of a single column)?
* A) Row-oriented engines lack support for B-Tree indexing algorithms.
* B) Entire tuples (all columns of every row) must be read from disk into RAM, polluting CPU cache lines with irrelevant data.
* C) Row-oriented databases cannot execute SQL queries containing aggregate functions without converting them to procedural loops.
* D) Analytical queries require distributed cluster nodes, which row-oriented engines cannot support.

### Question 2
What is the primary architectural mechanism that enables DuckDB and Polars to execute analytical queries substantially faster than traditional Python Pandas?
* A) They compile SQL queries into C++ shared libraries at runtime and store intermediate data in Redis.
* B) They utilize vectorized columnar execution on Apache Arrow memory buffers, leveraging CPU SIMD instructions to process batches of values concurrently.
* C) They run queries inside a Java Virtual Machine (JVM) optimized for parallel garbage collection.
* D) They automatically compress all integers into 8-bit floats before executing aggregation operations.

### Question 3
How does columnar projection pruning improve query execution efficiency on Parquet files?
* A) It rewrites user queries to remove WHERE clauses that filter by string literals.
* B) It completely avoids reading unreferenced columns from disk into memory, dramatically cutting I/O bandwidth.
* C) It sorts the dataset in descending order before executing aggregations.
* D) It converts floating-point columns into fixed-width integers during disk reads.

### Question 4
In analytical query planning, what is the purpose of "predicate pushdown"?
* A) Deferring filter evaluation until after all table joins and aggregations are completed.
* B) Evaluating filtering conditions as close to the storage layer as possible so non-matching row groups are never read into memory.
* C) Pushing SQL syntax parsing errors into an asynchronous error log.
* D) Forcing all query filters to be executed sequentially on a single CPU core.

### Question 5
Why does Apache Parquet utilize dictionary encoding for low-cardinality string columns?
* A) To encrypt sensitive text data using symmetric encryption keys.
* B) To replace repetitive strings with small integer keys and store the unique dictionary once, drastically compressing file size and accelerating equality checks.
* C) To guarantee that all strings are converted to uppercase for case-insensitive matching.
* D) To permit duplicate primary keys across partitioned files.

### Question 6
When analyzing a query plan using `EXPLAIN ANALYZE` in DuckDB, what does a `SEQ_SCAN` operator indicate?
* A) The query engine used a pre-computed hash index to retrieve rows in O(1) time.
* B) The query engine performed a sequential scan across the table or file because no index or partition pruning could narrow the search.
* C) The query failed validation and defaulted to a mock dataset.
* D) The scan was performed across multiple network nodes using SSH tunnels.

### Question 7
In Python data processing, what is the main consequence of Pandas' legacy memory model when processing large tabular files?
* A) Pandas cannot parse CSV files with more than 10 columns.
* B) Pandas creates redundant intermediate memory allocations, frequently requiring 5x to 10x the raw file size in RAM, leading to out-of-memory (OOM) crashes.
* C) Pandas requires all datasets to be pre-sorted in ascending numerical order.
* D) Pandas forces all Python threads to execute on GPU cores exclusively.

### Question 8
What is the core benefit of the Apache Arrow columnar in-memory specification in modern data engineering?
* A) It provides zero-copy data interchange between analytical runtimes (like DuckDB, Polars, and PyArrow) without serialization overhead.
* B) It replaces SQL with a proprietary assembly programming language.
* C) It forces all operating systems to allocate 64GB of swap space automatically.
* D) It eliminates the need for data types in relational databases.

### Question 9
In SQL query processing order, when is a window function (e.g., `ROW_NUMBER() OVER (...)`) evaluated?
* A) Before the `FROM` and `JOIN` clauses.
* B) After `FROM`, `WHERE`, `GROUP BY`, and `HAVING`, but before final `SELECT`, `DISTINCT`, and `ORDER BY`.
* C) Immediately before the `WHERE` clause filters rows.
* D) At the storage layer during the initial Parquet read.

### Question 10
When writing DuckDB queries over partitioned datasets (`date=2026-10-24/data.parquet`), how does partition pruning reduce query cost?
* A) By skipping entire directory subtrees whose partition key values do not satisfy the query's WHERE filter.
* B) By deleting old files from disk automatically during query execution.
* C) By merging all partitioned files into a single temporary CSV file in RAM.
* D) By bypassing data type validation on partitioned columns.

## Answer Key
| Question # | Correct Answer | Concept Tested & Rationale |
| :--- | :--- | :--- |
| **1** | **B** | Row-oriented storage reads entire tuples from disk blocks, which pollutes CPU caches with unneeded columns during aggregate queries. |
| **2** | **B** | Vectorized columnar engines like DuckDB process columnar batches (chunks) using SIMD CPU registers, eliminating Python interpreter overhead. |
| **3** | **B** | Projection pruning instructs the Parquet reader to only load byte ranges corresponding to requested columns, saving significant disk and memory I/O. |
| **4** | **B** | Predicate pushdown moves filters down into the file reader (e.g. Parquet row group statistics) so non-matching data is skipped at the storage layer. |
| **5** | **B** | Dictionary encoding maps repeated strings to small integer identifiers, achieving high compression ratios and allowing fast integer comparisons. |
| **6** | **B** | A SEQ_SCAN scans all records sequentially; while fast in vectorized columnar systems, it indicates full table reads rather than index lookups. |
| **7** | **B** | Legacy Pandas creates defensive copies and unboxed Python objects for strings, causing massive memory bloat and frequent OOM failures on large datasets. |
| **8** | **A** | Apache Arrow defines a standardized columnar memory buffer, enabling DuckDB, Polars, and Spark to share memory without costly serialization copies. |
| **9** | **B** | Window functions operate on the rows resulting from FROM, WHERE, and GROUP BY/HAVING clauses before the final result projection is formatted. |
| **10** | **A** | Hive-style directory partitioning allows the query engine's file scanner to skip entire directory trees when the partition key is filtered in the query. |
