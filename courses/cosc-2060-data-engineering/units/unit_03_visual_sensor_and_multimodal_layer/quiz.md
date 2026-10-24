# Unit 03 Knowledge Check: Multimodal Sensor & Visual Feature Stores

### Question 1
What is a dense vector embedding in the context of visual and multimodal data engineering?
* A) A compressed JPEG image encoded using Base64 ASCII characters.
* B) A fixed-length array of continuous floating-point numbers representing semantic and visual features extracted by a neural network.
* C) A binary bitmap matrix indicating black and white pixel coordinates.
* D) A relational foreign key pointing to an image URL on a public web server.

### Question 2
Why must raw image files undergo pre-processing (such as resizing and tensor normalization) before being passed into vision embedding models?
* A) Embedding models can only process images stored on physical optical media.
* B) Neural networks expect standardized input tensor dimensions and normalized pixel value distributions (e.g. mean 0, standard deviation 1) for consistent feature extraction.
* C) Resizing converts images into human-readable SQL statements.
* D) Normalization deletes the color channels from RGB images to save memory.

### Question 3
How does a multimodal model like CLIP (Contrastive Language-Image Pre-training) enable joint text-and-image search?
* A) By converting all images into optical character recognition (OCR) text strings.
* B) By mapping both image tensors and text tokens into a shared high-dimensional vector space where semantic concepts lie close to each other.
* C) By executing SQL LIKE queries on image file names.
* D) By translating text queries into binary image sprites.

### Question 4
When comparing two normalized embedding vectors $\mathbf{u}$ and $\mathbf{v}$, why is cosine similarity mathematically equivalent to their dot product?
* A) Because the cosine of zero is always zero.
* B) Because cosine similarity is $\frac{\mathbf{u} \cdot \mathbf{v}}{\|\mathbf{u}\| \|\mathbf{v}\|}$, and when both vectors are unit-normalized (length 1), the denominator equals 1.
* C) Because dot products can only be calculated on 2-dimensional vectors.
* D) Because neural networks only output vectors with values of 0 or 1.

### Question 5
In an enterprise feature store, what is the role of an "immutable feature manifest"?
* A) A database table that allows any developer to update historical records at will.
* B) An append-only, versioned ledger that binds feature vectors, data schemas, and pipeline run metadata to guarantee reproducible model training.
* C) A configuration file that disables password authentication on database ports.
* D) A temporary cache that is purged every 60 seconds.

### Question 6
Why is storing multi-gigabyte raw image binary blobs directly inside relational table columns (e.g. `BLOB` or `BYTEA`) considered an anti-pattern in data engineering?
* A) Relational databases cannot store binary files larger than 10 kilobytes.
* B) Blobs bloat database page caches and table heap sizes, severely degrading query performance and backup speeds; images should reside in object stores with URIs in the database.
* C) Storing images in databases causes hard drives to spin in reverse.
* D) Image files cannot be indexed by primary keys.

### Question 7
What is an "As-Of" temporal join, and why is it essential when joining visual sensor frames with vehicle telemetry?
* A) It joins two tables based on whether their column names start with the letter A.
* B) It joins records based on the closest preceding timestamp, aligning unsynchronized high-frequency telemetry with discrete image capture events without data leakage.
* C) It forces both tables to delete all records older than 24 hours.
* D) It joins records only if their timestamps match down to the exact microsecond.

### Question 8
What computational trade-off occurs when scaling vector embeddings from 128 dimensions to 1,536 dimensions?
* A) Higher dimensions capture richer semantic nuance, but dramatically increase RAM consumption, storage footprint, and vector distance computation latency.
* B) Higher dimensions reduce the amount of RAM needed to store vectors.
* C) Higher dimensions eliminate the need for vector indexing algorithms.
* D) Higher dimensions make vector similarity search impossible on modern CPUs.

### Question 9
In a production visual feature pipeline, why is batch inference preferred over single-image inference when generating embeddings on a GPU?
* A) Single-image inference crashes the GPU operating system.
* B) Batch inference saturates GPU tensor cores and amortizes memory transfer overhead between CPU and GPU, yielding 5x to 20x higher throughput.
* C) Batch inference guarantees that all images have identical file sizes.
* D) GPUs can only execute Python code when processing 10,000 images at once.

### Question 10
What metadata must always be captured alongside image feature embeddings to ensure governance and traceability?
* A) The personal cell phone number of the engineer who wrote the script.
* B) Sensor identifier, UTC capture timestamp, source image hash/URI, embedding model version, and pipeline execution ID.
* C) The CSS color theme of the Canvas LMS instance.
* D) A copy of the Python interpreter executable.

## Answer Key
| Question # | Correct Answer | Concept Tested & Rationale |
| :--- | :--- | :--- |
| **1** | **B** | Vector embeddings are numeric vectors in a continuous geometric space capturing latent semantic properties extracted by deep learning encoders. |
| **2** | **B** | Vision backbones require fixed tensor dimensions (e.g. 224x224x3) and normalized channel statistics to ensure numerical stability during forward passes. |
| **3** | **B** | CLIP trains an image encoder and text encoder jointly with a contrastive loss so related text and visual concepts project into the same vector space. |
| **4** | **B** | When vectors are unit-normalized (magnitude = 1), Euclidean distance and cosine similarity become monotonic transformations of the simple dot product. |
| **5** | **B** | Feature manifests provide an immutable record of historical feature state, preventing training-serving skew and enabling model auditability. |
| **6** | **B** | Large binary objects bloat database pages and exhaust buffer pools; industry standard practice stores blobs in S3/MinIO and stores metadata/URIs in SQL. |
| **7** | **B** | As-Of joins match events on approximate temporal proximity (e.g. matching an image at 10:00:00.12 with the telemetry reading at 10:00:00.08). |
| **8** | **A** | High dimensionality improves representation capacity but increases distance computation cost and requires more memory per vector in RAM. |
| **9** | **B** | Batching leverages GPU parallelism by computing matrix-matrix multiplications rather than inefficient sequential matrix-vector operations. |
| **10** | **B** | Data lineage requires recording model version, input hash, timestamps, and pipeline identifiers to diagnose drift and reproduce embeddings. |
