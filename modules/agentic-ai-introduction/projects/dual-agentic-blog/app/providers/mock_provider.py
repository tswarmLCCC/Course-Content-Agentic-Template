"""Deterministic mock provider for offline testing and CI/CD."""

import time
from typing import List, Dict, Any, Type, TypeVar, Tuple, Optional
from pydantic import BaseModel

from .base import BaseLLMProvider
from ..schemas import BlogPlan, SectionPlan, ValidationReport

T = TypeVar("T", bound=BaseModel)


class MockProvider(BaseLLMProvider):
    """Deterministic simulation provider mimicking realistic multi-agent feedback loops."""

    def __init__(self, model_name: str = "mock-agent-v1", **kwargs):
        super().__init__(model_name=model_name, **kwargs)
        self.call_count = 0
        self.draft_iteration = 0

    def is_healthy(self) -> bool:
        return True

    def generate_structured(
        self,
        messages: List[Dict[str, str]],
        response_model: Type[T],
        temperature: float = 0.2,
    ) -> T:
        self.call_count += 1
        time.sleep(0.05)  # Simulate realistic fast inference delay

        user_content = ""
        for m in messages:
            if m.get("role") == "user":
                user_content += m.get("content", "") + " "

        # 1. Planner request
        if response_model == BlogPlan:
            topic = "Agentic AI Architecture"
            if "Topic:" in user_content:
                topic = user_content.split("Topic:")[1].split("\n")[0].strip()

            return BlogPlan(
                title=f"Architectural Guide: {topic}",
                target_audience="Computer Science Undergraduates & Software Engineers",
                total_target_words=180,
                sections=[
                    SectionPlan(
                        heading="Introduction & Core Principles",
                        key_points=["Stateless LLMs vs stateful decision engines", "The cognitive friction of prompt engineering"],
                        target_words=50
                    ),
                    SectionPlan(
                        heading="The ReAct State Machine & Reasoning Loops",
                        key_points=["Interleaving Thought, Action, and Observation", "Synergizing reasoning with environmental feedback"],
                        target_words=70
                    ),
                    SectionPlan(
                        heading="Defensive Engineering & Runaway Loop Guards",
                        key_points=["Poka-Yoke tool design", "Hard iteration caps and schema validation"],
                        target_words=60
                    )
                ]
            )

        # 2. Validator request
        if response_model == ValidationReport:
            self.draft_iteration += 1
            # If it's iteration 1, simulate a deliberate failure to demonstrate self-correction!
            if self.draft_iteration == 1:
                return ValidationReport(
                    passed=False,
                    overall_score=55,
                    word_count_actual=68,
                    word_count_status="TOO_SHORT",
                    missing_sections=["Defensive Engineering & Runaway Loop Guards"],
                    critiques=[
                        "Measured length (68 words) is below the required minimum target threshold (150 words).",
                        "Mandatory section 'Defensive Engineering & Runaway Loop Guards' was completely omitted in the draft."
                    ],
                    actionable_feedback=[
                        "Expand technical depth in all sections to achieve at least 150 words.",
                        "Add the missing section: '## Defensive Engineering & Runaway Loop Guards' explaining iteration caps."
                    ]
                )
            else:
                # Iteration 2 passes with flying colors!
                return ValidationReport(
                    passed=True,
                    overall_score=100,
                    word_count_actual=175,
                    word_count_status="OK",
                    missing_sections=[],
                    critiques=[],
                    actionable_feedback=[]
                )

        # Fallback for generic models
        return response_model.model_validate({})

    def generate_text(
        self,
        messages: List[Dict[str, str]],
        temperature: float = 0.7,
        tools: Optional[List[Any]] = None,
    ) -> Tuple[str, List[Dict[str, Any]]]:
        self.call_count += 1
        time.sleep(0.05)

        user_content = ""
        for m in messages:
            if m.get("role") == "user":
                user_content += m.get("content", "") + " "

        tool_traces = []
        if tools:
            # Simulate a tool call if tools provided
            for t in tools:
                if t.__name__ == "calculate_reading_metrics":
                    res = t("Sample text for metrics evaluation.")
                    tool_traces.append({"tool": t.__name__, "args": {"text_len": 32}, "result": res})

        # Draft generation
        if "feedback" in user_content.lower() or "critique" in user_content.lower() or self.draft_iteration >= 1:
            # Revised draft addressing feedback
            revised_draft = """# Architectural Guide: Agentic AI Systems

## Introduction & Core Principles
Traditional language models operate as stateless function approximations, mapping static prompts to probabilistic text predictions. In contrast, autonomous agentic systems transform LLMs into stateful reasoning engines equipped with sensors, effectors, and dynamic control loops.

## The ReAct State Machine & Reasoning Loops
As demonstrated by Yao et al. (ICLR 2023), pure verbal reasoning suffers from compounding hallucinations, while pure tool use lacks strategic coherence. The ReAct paradigm synergizes both by interleaving internal Thoughts, external tool Actions, and runtime Observations, keeping the model continuously grounded in environmental truth.

## Defensive Engineering & Runaway Loop Guards
Production agent deployments require rigorous Agent-Computer Interface (ACI) hygiene. Engineers must enforce Poka-Yoke error-proofing, absolute filesystem path resolution, strict Pydantic schema validation, and hard max-iteration cutoff thresholds to prevent runaway infinite token loops.
"""
            return revised_draft.strip(), tool_traces
        else:
            # Initial brief draft (intentionally short to trigger Validator critique)
            initial_draft = """# Architectural Guide: Agentic AI Systems

## Introduction & Core Principles
Large language models are moving from passive chatbots to active decision engines.

## The ReAct State Machine & Reasoning Loops
Agents use Thoughts and Actions to solve multi-step problems in software engineering.
"""
            return initial_draft.strip(), tool_traces
