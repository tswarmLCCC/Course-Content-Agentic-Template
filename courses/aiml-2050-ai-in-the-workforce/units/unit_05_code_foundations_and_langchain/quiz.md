# Unit 05 Knowledge Check: Code Foundations: The Modular AI Agent Stack

This assessment evaluates your conceptual understanding of Unit 05 competencies, enterprise workflows, and tool architectures.

---

### Question 1
What is the main purpose of the AI agent stack?
* A) To organize the different layers needed to build an AI agent system
* B) To replace all Python code with prompt engineering
* C) To make the model permanently remember every conversation
* D) To remove the need for tools and retrieval

### Question 2
Why is a single model call considered stateless?
* A) Because it can only call one tool
* B) Because the model does not remember previous requests unless context is sent again
* C) Because it only works without an API key
* D) Because it cannot generate text

### Question 3
What does the memory layer mainly help an agent do?
* A) Store and reuse relevant conversation context across sessions
* B) Search external documents using embeddings
* C) Automatically create new Python libraries
* D) Remember every tool capability

### Question 4
Why should selective memory be used instead of always sending the full conversation history?
* A) It makes RAG unnecessary
* B) It prevents the model from answering any follow-up questions
* C) It removes the need for user preferences
* D) It helps reduce payload size, cost, irrelevant context, and context-window pressure

### Question 5
What is the main difference between memory and RAG?
* A) Memory is always semantic search, while RAG is always keyword search
* B) Memory uses tools, while RAG only stores API keys
* C) Memory stores conversation context, while RAG retrieves knowledge from external documents
* D) There is no difference between memory and RAG

### Question 6
In a RAG pipeline, what is the purpose of retrieval?
* A) To find relevant document chunks before the model generates an answer
* B) To check if the keywords are present in the knowledge base documents
* C) To fetch the response from the LLM
* D) All of the above

### Question 7
What does an embedding help with in semantic retrieval?
* A) Converts input text to ASCII
* B) Encrypts the API key in the .env file
* C) Formats terminal output
* D) Represents text as vectors so similar meanings can be compared

### Question 8
What makes tool calling an agentic capability?
* A) The model can decide when to request an external function to perform an action
* B) The model stops needing prompts and always runs the same fixed workflow
* C) The user has to manually run every Python function or API and then paste the results back to the model
* D) The agent no longer needs any orchestration or error handling once the tools are available

### Question 9
In Raw HTTP tool calling, why is a tool schema needed?
* A) Enables easier configuration of Frameworks
* B) It stores all conversation history permanently for later analysis
* C) It describes the tool name, purpose, and expected arguments so the model can request it correctly
* D) It converts all documents in the knowledge base into an LLM readable format

### Question 10
When should an agent use a tool instead of relying only on its knowledge from LLM provider training?
* A) Every time the user asks any question, even if it is simple general knowledge
* B) When the task needs live data, exact calculations, or actions in external systems that the model’s training alone cannot provide reliably
* C) Only when the model has completely failed to generate any natural‑language response
* D) None of the above

---

## Answer Key

| Question # | Correct Answer | Concept Tested & Rationale |
| :--- | :--- | :--- |
| **1** | **A** | Core concept check: What is the main purpose of the AI agent stack?... |
| **2** | **B** | Core concept check: Why is a single model call considered stateless?... |
| **3** | **A** | Core concept check: What does the memory layer mainly help an agent do?... |
| **4** | **D** | Core concept check: Why should selective memory be used instead of always sendin... |
| **5** | **C** | Core concept check: What is the main difference between memory and RAG?... |
| **6** | **A** | Core concept check: In a RAG pipeline, what is the purpose of retrieval?... |
| **7** | **D** | Core concept check: What does an embedding help with in semantic retrieval?... |
| **8** | **A** | Core concept check: What makes tool calling an agentic capability?... |
| **9** | **C** | Core concept check: In Raw HTTP tool calling, why is a tool schema needed?... |
| **10** | **B** | Core concept check: When should an agent use a tool instead of relying only on i... |