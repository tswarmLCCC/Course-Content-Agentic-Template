# Week 16 Knowledge Check: LLM Alignment and Responsible AI

**Course**: AIML 1010: Introduction to Artificial Intelligence  
**Assessment Type**: Multiple Choice Knowledge Check  
**Allowed Attempts**: 3 | **Scoring Policy**: Keep Highest Score | **Points Possible**: 30.0

---

## Assessment Questions

### Question 1
In AI safety and ethics, what is the 'Alignment Problem'?

* A) The challenge of ensuring an AI system's objectives, behaviors, and values reliably conform to intended human values and safety standards
* B) Aligning text margins to the left and right borders of a page
* C) Ensuring GPU hardware cables are plugged into the correct slots
* D) Synchronizing system clock times across cloud data centers

### Question 2
What are the three core principles of the 'HHH' alignment framework popularized by Anthropic?

* A) Helpful, Harmless, and Honest
* B) Hyper-fast, Highly-accurate, and Hardware-efficient
* C) Heavy, Heuristic, and Holistic
* D) Hierarchical, Hybrid, and Homogeneous

### Question 3
How does Reinforcement Learning from Human Feedback (RLHF) align language models?

* A) A reward model is trained on human preference rankings between model outputs, then used via PPO to guide the policy model toward preferred responses
* B) Humans manually rewrite all possible token sequences in the base vocabulary
* C) Models are penalized with electric shocks when they make grammatical errors
* D) Human users review every single query before the model can answer

### Question 4
What is 'Constitutional AI' (RLAIF)?

* A) An alignment method where an AI system uses a written constitution of safety principles to critique, revise, and align its own outputs with minimal human labeling
* B) Training models exclusively on government legal constitutions
* C) Requiring models to pass a bar examination before deployment
* D) A hardware firewall implemented inside server motherboard firmware

### Question 5
How does Direct Preference Optimization (DPO) simplify model alignment compared to classic RLHF?

* A) It directly optimizes the policy network on preference pairs using a closed-form loss function, eliminating the need to train a separate reward model or run PPO
* B) It deletes all negative data from the internet
* C) It forces the model to choose only the shortest possible answers
* D) It requires no training data whatsoever

### Question 6
True or False: An AI system that is extremely proficient at summarizing facts and writing creative essays is guaranteed to be aligned and safe.

* A) True
* B) False

### Question 7
What is 'Red Teaming' in the context of responsible generative AI deployment?

* A) Adversarial testing where security and domain experts deliberately probe the system with adversarial prompts, jailbreaks, and edge cases to uncover vulnerabilities
* B) Painting server rack cases red for visual identification
* C) Assigning developers to wear red shirts during release sprints
* D) Rewriting code in the Rust programming language

### Question 8
Why can the principles of 'Helpful' and 'Harmless' sometimes conflict with each other?

* A) A user might ask for 'help' synthesizing an explosive or hacking a network; being truly harmless requires refusing to be helpful for that request
* B) Helpful models use more electricity, which causes harmless heat
* C) Honesty is impossible for artificial neural networks
* D) Only human beings can understand the concept of harm

### Question 9
What is a 'Jailbreak' in large language model security?

* A) A crafted prompt or adversarial token sequence that bypasses a model's safety alignment guardrails to elicit prohibited responses
* B) Installing alternative operating systems on Apple iPhones
* C) Breaking physical locks on enterprise server cages
* D) Running an LLM outside of a Python virtual environment

### Question 10
True or False: Technical alignment eliminates the need for human governance, legal regulations, or organizational compliance policies.

* A) True
* B) False

---

## Answer Key

| Question # | Correct Answer | Concept Tested & Rationale |
| :--- | :--- | :--- |
| **1** | **A** | The alignment problem centers on building powerful AI systems whose goals, decision heuristics, and real-world actions remain beneficial and faithful to human intent. |
| **2** | **A** | The HHH criteria define target model behavior: Helpful (fulfills user intent), Harmless (avoids promoting illegal/dangerous actions), and Honest (truthful, calibrated certainty). |
| **3** | **A** | RLHF trains a reward model to score responses based on human pairwise preferences, using reinforcement learning (e.g. PPO) to optimize the LLM policy toward high-reward behaviors. |
| **4** | **A** | Constitutional AI replaces expensive human feedback loops with AI feedback: the model critiques and refines candidate answers against explicit constitutional principles. |
| **5** | **A** | DPO analytically reparameterizes the reward model, optimizing policy weights directly from preference pairs without the complexity and instability of multi-stage RL. |
| **6** | **B** | Capability is orthogonal to alignment. A highly capable model can still generate deceptive arguments, toxic rhetoric, or instructions for dangerous weapons if unaligned. |
| **7** | **A** | Red teaming is structured adversarial exploration: probing an AI with malicious, deceptive, and harmful inputs before release to discover and patch safety failures. |
| **8** | **A** | Refusal dilemmas occur when users request actionable assistance for malicious ends. The model must prioritize harmlessness over helpfulness and decline the request. |
| **9** | **A** | Jailbreaking uses roleplay, hypothetical framing, obfuscated encodings, or adversarial suffixes to trick the model into ignoring its safety training. |
| **10** | **B** | Technical alignment is only one layer of defense. Robust AI deployment requires comprehensive socio-technical governance: laws, institutional policies, and human auditing. |
