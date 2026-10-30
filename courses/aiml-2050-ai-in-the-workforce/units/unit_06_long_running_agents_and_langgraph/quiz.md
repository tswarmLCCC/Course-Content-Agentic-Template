# Unit 06 Knowledge Check: Long-Running Ambient Agents & State Machines with LangGraph

This assessment evaluates your conceptual understanding of Unit 06 competencies, enterprise workflows, and tool architectures.

---

### Question 1
What makes an agent “ambient”?
* A) It only responds to direct user prompts
* B) It only uses one tool at a time
* C) It runs continuously or periodically in the background to monitor goals, context, or tasks
* D) It does not require memory across different sessions

### Question 2
Why is persistent memory important for an ambient agent?
* A) It makes the LLM faster
* B) It allows the agent to remember goals, tasks, and progress after restart
* C) It removes the need for tools
* D) It prevents all errors

### Question 3
Why is it considered risky to give an agent too many tools at once?
* A) It may increase token usage and make tool selection less reliable
* B) It removes memory from the agent
* C) It prevents the agent from answering questions
* D) None of the above

### Question 4
Which design is more efficient for tool use?
* A) No tools binded initially to the agent
* B) One agent with all tools bound all the time
* C) Rebuilding the graph after every user message
* D) Multiple routines where each routine only sees the tools it needs

### Question 5
What should the agent do if a required file is missing?
* A) Run the task anyway
* B) Mark the task as blocked and explain what file is missing
* C) Consider the task as low priority
* D) Indicate file missing and mark the task as complete

### Question 6
An agent successfully completes a task, but then continues calling tools until it hits a recursion limit. What should be added to the graph?
* A) Add more specific tools to the agent
* B) Segregate the tool call with a well-defined routine
* C) Hardcode to delete the checkpoint database every time
* D) Add a stop condition that routes to END node after the task completion

### Question 7
Why should different routines have different tool groups?
* A) To reduce token usage and improve tool selection accuracy
* B) To make the agent’s responses more detailed
* C) To prevent the agent from reloading unnecessary memory
* D) To make every routine use all available tools

### Question 8
What is a checkpoint in LangGraph mainly used for?
* A) To record the conversation, task progress, and intermediate steps so long-running workflows can continue reliably
* B) To automatically prevent all recursion loops and tool-calling errors in the agent
* C) To save the graph’s current state so the agent can resume a thread after interruption or restart
* D) To permanently store every tool the agent has access to and decide which one is safest

### Question 9
What is the purpose of the 'tick' command in an ambient agent?
* A) To delete completed tasks from the todo JSON
* B) To manually trigger the agent’s ambient task-checking routine
* C) To restart the agent and restore the memory
* D) To install new Python libraries

### Question 10
What is the difference between LangGraph checkpoints and LangSmith traces?
* A) Checkpoints are used to evaluate model quality; traces are used to store the agent’s long-term memory after restart.
* B) Checkpoints show the full history of prompts, tool calls, latency, and cost; traces only save the latest message in the thread.
* C) Checkpoints and traces do the same thing, but checkpoints are used in LangGraph while traces are used in LangChain.
* D) Checkpoints save the graph’s state so the agent can resume execution; traces record what happened during a run so developers can inspect and debug it.

---

## Answer Key

| Question # | Correct Answer | Concept Tested & Rationale |
| :--- | :--- | :--- |
| **1** | **C** | Core concept check: What makes an agent “ambient”?... |
| **2** | **B** | Core concept check: Why is persistent memory important for an ambient agent?... |
| **3** | **A** | Core concept check: Why is it considered risky to give an agent too many tools a... |
| **4** | **D** | Core concept check: Which design is more efficient for tool use?... |
| **5** | **B** | Core concept check: What should the agent do if a required file is missing?... |
| **6** | **D** | Core concept check: An agent successfully completes a task, but then continues c... |
| **7** | **A** | Core concept check: Why should different routines have different tool groups?... |
| **8** | **C** | Core concept check: What is a checkpoint in LangGraph mainly used for?... |
| **9** | **B** | Core concept check: What is the purpose of the 'tick' command in an ambient agen... |
| **10** | **D** | Core concept check: What is the difference between LangGraph checkpoints and Lan... |