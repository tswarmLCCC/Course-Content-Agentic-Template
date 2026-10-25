#!/usr/bin/env python3
"""
Unit 01 Applied Lab Starter Code: Auto-Correcting Multi-Agent Blog Pipeline
=============================================================================
Course: Agentic AI — Autonomous Agents & Tool Use
Architecture: Evaluator-Optimizer Loop & ReAct State Traces
Dependencies: Pure Python 3 standard library (no pip packages required).

This script implements an autonomous multi-agent content creation pipeline
inspired by Smitha Kolan's Google Cloud Tech architecture and Anthropic's
"Building Effective Agents" Evaluator-Optimizer pattern.
=============================================================================
"""

import re
import json
import time
from typing import Dict, List, Any, Tuple, Optional


# =============================================================================
# 1. Mock / Pluggable LLM Interface (Runs Offline with Zero API Keys)
# =============================================================================

class MockLLM:
    """
    Simulated LLM engine that produces deterministic, realistic agent outputs.
    Allows students without API credits to execute, test, and debug the entire
    multi-agent feedback loop locally.
    """
    def __init__(self):
        self.call_count = 0

    def generate(self, system_prompt: str, user_prompt: str) -> str:
        self.call_count += 1
        
        # 1. Planner Agent Prompt Handler
        if "PLANNER AGENT" in system_prompt:
            return json.dumps({
                "title": "Why Vector Databases Are Essential for Modern RAG",
                "target_words": 150,
                "sections": [
                    "Introduction to Dense Embeddings",
                    "Approximate Nearest Neighbors (ANN) vs Exact Search",
                    "Practical Architecture & Takeaways"
                ]
            })

        # 2. Writer Agent Prompt Handler
        elif "WRITER AGENT" in system_prompt:
            # On first draft, deliberately introduce a validation error (too short)
            # to trigger the Validator's critique and demonstrate the self-correcting loop!
            if "CRITIQUE FEEDBACK" not in user_prompt:
                return (
                    "# Why Vector Databases Are Essential for Modern RAG\n\n"
                    "## Introduction to Dense Embeddings\n"
                    "Traditional keyword search matches exact tokens. In contrast, dense embeddings capture semantic meaning "
                    "by mapping text into high-dimensional geometric spaces.\n\n"
                    "## Practical Architecture & Takeaways\n"
                    "Vector databases enable fast semantic retrieval for enterprise knowledge bases."
                )
            else:
                # Corrected second draft addressing the validator's feedback:
                return (
                    "# Why Vector Databases Are Essential for Modern RAG\n\n"
                    "## Introduction to Dense Embeddings\n"
                    "Traditional keyword search matches exact tokens. In contrast, dense embeddings capture semantic meaning "
                    "by mapping sentences and code snippets into high-dimensional geometric coordinate spaces.\n\n"
                    "## Approximate Nearest Neighbors (ANN) vs Exact Search\n"
                    "Comparing a query vector against millions of document vectors using exhaustive cosine distance scales "
                    "linearly (O(N)), quickly becoming a latency bottleneck. Vector databases utilize Approximate Nearest Neighbor "
                    "(ANN) algorithms such as Hierarchical Navigable Small World (HNSW) graphs and Inverted File Indexing (IVF). "
                    "These structures trade negligible recall accuracy for sub-millisecond retrieval speeds at scale.\n\n"
                    "## Practical Architecture & Takeaways\n"
                    "Modern Retrieval-Augmented Generation (RAG) architectures pair columnar metadata filtering with vector index lookups. "
                    "By grounding language models with high-fidelity context, engineering teams eliminate hallucinations and establish "
                    "defensive enterprise knowledge pipelines."
                )

        # 3. Validator Agent Prompt Handler
        elif "VALIDATOR AGENT" in system_prompt:
            # Parse text and check criteria
            text = user_prompt
            words = len(text.split())
            has_ann = "Approximate Nearest Neighbors" in text
            has_intro = "Introduction to Dense Embeddings" in text
            has_arch = "Practical Architecture" in text

            issues = []
            if words < 120:
                issues.append(f"Word count is too low ({words} words). Must be between 120 and 200 words.")
            if not has_ann:
                issues.append("Missing mandatory section: 'Approximate Nearest Neighbors (ANN) vs Exact Search'.")
            if not has_intro:
                issues.append("Missing mandatory section: 'Introduction to Dense Embeddings'.")
            if not has_arch:
                issues.append("Missing mandatory section: 'Practical Architecture & Takeaways'.")

            passed = len(issues) == 0
            score = 100 if passed else max(40, 100 - (len(issues) * 25))

            return json.dumps({
                "passed": passed,
                "score": score,
                "word_count": words,
                "issues": issues,
                "recommendation": "APPROVED" if passed else "REVISE: Expand depth and restore missing section."
            })

        return "Default response."


# =============================================================================
# 2. Specialized Agent Definitions (Separation of Concerns)
# =============================================================================

class PlannerAgent:
    """Agent 1: Generates a structured multi-part outline."""
    def __init__(self, llm: MockLLM):
        self.llm = llm
        self.system_prompt = (
            "You are a PLANNER AGENT. Your job is to take a technical topic and decompose it "
            "into a clean 3-part outline with target word counts. Output strictly valid JSON."
        )

    def plan(self, topic: str) -> Dict[str, Any]:
        print(f"\n[Planner Agent] Formulating structured outline for topic: '{topic}'...")
        raw_json = self.llm.generate(self.system_prompt, f"Topic: {topic}")
        plan_dict = json.loads(raw_json)
        print(f"  [+] Plan generated: '{plan_dict['title']}' with {len(plan_dict['sections'])} sections.")
        return plan_dict


class WriterAgent:
    """Agent 2: Generates and refines draft text based on plan and critique."""
    def __init__(self, llm: MockLLM):
        self.llm = llm
        self.system_prompt = (
            "You are a WRITER AGENT. Your job is to draft high-rigor, educational blog articles "
            "following the provided outline and addressing any validator critiques."
        )

    def draft(self, plan: Dict[str, Any], critique: Optional[Dict[str, Any]] = None) -> str:
        if critique is None:
            print("\n[Writer Agent] Authoring initial draft based on outline...")
            prompt = f"Outline: {json.dumps(plan)}"
        else:
            print(f"\n[Writer Agent] RE-DRAFTING based on validator feedback: {critique['issues']}...")
            prompt = f"Outline: {json.dumps(plan)}\nCRITIQUE FEEDBACK: {json.dumps(critique)}"

        content = self.llm.generate(self.system_prompt, prompt)
        word_count = len(content.split())
        print(f"  [+] Draft produced: {word_count} words.")
        return content


class ValidatorAgent:
    """Agent 3: Evaluates output against strict editorial and structural rubric."""
    def __init__(self, llm: MockLLM):
        self.llm = llm
        self.system_prompt = (
            "You are a VALIDATOR AGENT. You act as an impartial automated rubric checker. "
            "Verify word count, section presence, and tone. Output strictly valid JSON."
        )

    def validate(self, draft_text: str, plan: Dict[str, Any]) -> Dict[str, Any]:
        print("\n[Validator Agent] Inspecting draft against rubric requirements...")
        raw_json = self.llm.generate(self.system_prompt, draft_text)
        result = json.loads(raw_json)
        status = "PASSED" if result["passed"] else "FAILED (NEEDS REVISION)"
        print(f"  [>] Validation Result: {status} (Score: {result['score']}/100, Words: {result['word_count']})")
        if not result["passed"]:
            for issue in result["issues"]:
                print(f"      - Issue: {issue}")
        return result


# =============================================================================
# 3. Agent Coordinator & Evaluator-Optimizer Loop Harness
# =============================================================================

class MultiAgentBlogPipeline:
    """
    Orchestrates the multi-agent loop with defensive stopping conditions:
    - Enforces hard max_iterations cap.
    - Tracks complete execution history trace.
    - Yields clean terminal outputs.
    """
    def __init__(self, max_iterations: int = 3):
        self.llm = MockLLM()
        self.planner = PlannerAgent(self.llm)
        self.writer = WriterAgent(self.llm)
        self.validator = ValidatorAgent(self.llm)
        self.max_iterations = max_iterations
        self.execution_trace: List[Dict[str, Any]] = []

    def run(self, topic: str) -> Tuple[bool, str, Dict[str, Any]]:
        print("=" * 70)
        print(f"STARTING MULTI-AGENT AUTONOMOUS BLOG PIPELINE (Max Iterations: {self.max_iterations})")
        print("=" * 70)

        # Step 1: Planning
        plan = self.planner.plan(topic)
        self.execution_trace.append({"step": "plan", "data": plan})

        # Step 2: Evaluator-Optimizer Feedback Loop
        current_critique = None
        current_draft = ""
        success = False

        for iteration in range(1, self.max_iterations + 1):
            print(f"\n--- EXECUTION CYCLE {iteration}/{self.max_iterations} ---")
            
            # Action: Writer drafts (or re-drafts)
            current_draft = self.writer.draft(plan, critique=current_critique)
            
            # Action: Validator critiques draft
            current_critique = self.validator.validate(current_draft, plan)
            
            self.execution_trace.append({
                "iteration": iteration,
                "draft": current_draft,
                "critique": current_critique
            })

            # Gate: Did it pass validation?
            if current_critique["passed"]:
                print(f"\n[SUCCESS] Content passed all validation gates on iteration {iteration}!")
                success = True
                break
            else:
                print(f"[RETRY] Validator rejected draft. Feeding critique back into next cycle...")

        if not success:
            print(f"\n[WARNING] Loop exceeded max_iterations ({self.max_iterations}) without full pass.")

        return success, current_draft, {
            "total_iterations": iteration,
            "final_score": current_critique["score"],
            "plan": plan,
            "trace": self.execution_trace
        }


# =============================================================================
# 4. Self-Checking Test Harness (Run Directly to Verify)
# =============================================================================

if __name__ == "__main__":
    pipeline = MultiAgentBlogPipeline(max_iterations=3)
    passed, final_blog, meta = pipeline.run("Modern Vector Search & RAG Pipelines")
    
    print("\n" + "=" * 70)
    print("FINAL PUBLISHED OUTPUT")
    print("=" * 70)
    print(final_blog)
    print("\n" + "=" * 70)
    print(f"EXECUTION METRICS: Passed={passed} | Iterations={meta['total_iterations']} | Score={meta['final_score']}/100")
    print("=" * 70)

    # Automated assertions for test pass
    assert passed is True, "Pipeline failed to self-correct!"
    assert meta["total_iterations"] == 2, "Expected self-correction on iteration 2!"
    assert "Approximate Nearest Neighbors" in final_blog, "Missing required section in final blog!"
    print("\n[ALL TESTS PASSED] Self-correcting multi-agent loop successfully verified!")
