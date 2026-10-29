# Week 10 Knowledge Check: Transformers and Evolution of Large Language Models

**Course**: AIML 1010: Introduction to Artificial Intelligence  
**Assessment Type**: Multiple Choice Knowledge Check  
**Allowed Attempts**: 3 | **Scoring Policy**: Keep Highest Score | **Points Possible**: 30.0

---

## Assessment Questions

### Question 1
What major architectural breakthrough did the 2017 paper 'Attention Is All You Need' introduce to replace recurrent connections (RNNs)?

* A) Convolutional feature maps
* B) Multi-Head Self-Attention mechanisms
* C) Gated Recurrent Units (GRUs)
* D) Support Vector Machines (SVMs)

### Question 2
Why does self-attention enable massive scaling compared to traditional Recurrent Neural Networks (RNNs)?

* A) RNNs require sequential token-by-token processing where step t depends on step t-1, while self-attention processes all tokens in parallel
* B) RNNs only work on audio data, while self-attention works on text
* C) Self-attention requires zero training data
* D) RNNs have fixed vocabulary sizes of under 100 words

### Question 3
What are the two primary sub-layers found within each Transformer encoder block?

* A) Convolutional layer and MaxPooling layer
* B) Multi-Head Self-Attention mechanism and a Feed-Forward Neural Network (with residual connections and normalization)
* C) Softmax classifier and k-Nearest Neighbors clustering
* D) Recurrent LSTM cell and Dropout layer

### Question 4
What activation function is typically applied at the final output projection of a Transformer decoder to produce token probability distributions?

* A) ReLU
* B) Sigmoid
* C) Softmax
* D) Hyperbolic Tangent (Tanh)

### Question 5
What is the primary function of positional encodings in Transformer architectures?

* A) To inject information about the order/position of tokens in the sequence, since self-attention contains no inherent recurrent or spatial order
* B) To compress model weights into 8-bit integers
* C) To encrypt user prompts during inference
* D) To filter out grammatical stop words

### Question 6
Which of the following correctly pairs a Transformer architecture type with its representative model?

* A) Encoder-only: GPT; Decoder-only: BERT
* B) Encoder-only: BERT; Decoder-only: GPT; Encoder-Decoder: T5
* C) Encoder-only: T5; Decoder-only: BERT; Encoder-Decoder: GPT
* D) Encoder-only: ResNet; Decoder-only: YOLO; Encoder-Decoder: VGG

### Question 7
True or False: BERT is an autoregressive generative model that predicts tokens from left to right.

* A) True
* B) False

### Question 8
In the standard Transformer pipeline, what component first converts raw input text into a sequence of integer IDs before embedding lookup?

* A) Tokenizer
* B) Softmax
* C) Layer Normalization
* D) Residual Connection

### Question 9
What do Query (Q), Key (K), and Value (V) represent in scaled dot-product attention?

* A) Database SQL query parameters
* B) Linear projections of token embeddings used to compute attention weights (how much each token focuses on every other token)
* C) Hardware registers in GPU thread blocks
* D) Hyperparameters that define learning rate and weight decay

### Question 10
What are the two foundational stages involved in training modern Large Language Models?

* A) Unsupervised Pre-training on massive text corpora followed by Supervised Fine-Tuning / Alignment
* B) Feature engineering followed by polynomial regression
* C) Manual rule authoring followed by hardcoded compiling
* D) Data clustering followed by decision tree pruning

---

## Answer Key

| Question # | Correct Answer | Concept Tested & Rationale |
| :--- | :--- | :--- |
| **1** | **B** | The Transformer architecture eliminated recurrent loops in favor of multi-head self-attention, allowing models to process entire sequences in parallel and capture long-range dependencies. |
| **2** | **A** | RNNs suffer from sequential processing bottlenecks. Self-attention enables full parallelization across GPU hardware, unlocking modern foundation model scale. |
| **3** | **B** | Each standard encoder layer contains a multi-head self-attention sub-layer followed by a position-wise fully connected feed-forward network, wrapped in residual connections. |
| **4** | **C** | Softmax normalizes raw output logits into a valid probability distribution over the model's vocabulary, summing to 1.0. |
| **5** | **A** | Self-attention is permutation-invariant. Positional encodings (sinusoidal or learned) are added to token embeddings to communicate sequence order. |
| **6** | **B** | BERT is an encoder-only model (masked language modeling); GPT is a decoder-only model (autoregressive causal generation); T5 is an encoder-decoder model (sequence-to-sequence). |
| **7** | **B** | BERT is an autoencoding (bidirectional) model trained with Masked Language Modeling (MLM), not an autoregressive left-to-right generator like GPT. |
| **8** | **A** | A tokenizer (such as Byte-Pair Encoding or WordPiece) maps raw text strings into discrete subword token identifiers. |
| **9** | **B** | Tokens project into Query, Key, and Value vectors. Attention is calculated by computing dot products between Q and K, scaling, taking softmax, and multiplying by V. |
| **10** | **A** | LLM creation begins with compute-intensive pre-training on trillions of tokens to learn general language representation, followed by fine-tuning (SFT and RLHF) for task alignment. |
