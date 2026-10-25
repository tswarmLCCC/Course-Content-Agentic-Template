"""Planner Agent: Decomposes high-level topics into structured section plans."""

from typing import Dict, Any
from ..providers.base import BaseLLMProvider
from ..schemas import BlogPlan

PLANNER_SYSTEM_PROMPT = """You are an elite Technical Editorial Director and Curriculum Architect.
Your role is to analyze a technical topic and construct an authoritative, logically ordered blog post blueprint.

Guidelines:
1. Decompose the topic into 3 to 4 sequential sections (e.g., Fundamentals -> Mechanics/Architecture -> Practical Applications/Guardrails).
2. For each section, specify a compelling heading, 2-4 key technical concepts to address, and a realistic word budget (target: 40-70 words per section).
3. Ensure the overall target word count matches an accessible undergraduate read (150-250 total words).
4. Strictly return your output conforming to the BlogPlan schema.
"""


class PlannerAgent:
    """Agent responsible for initial strategic breakdown and section outlining."""

    def __init__(self, provider: BaseLLMProvider):
        self.provider = provider

    def plan(self, topic: str, target_audience: str = "Computer Science Undergraduates") -> BlogPlan:
        """Formulates an outline blueprint for the provided topic."""
        messages = [
            {"role": "system", "content": PLANNER_SYSTEM_PROMPT},
            {
                "role": "user",
                "content": f"Topic: {topic}\nTarget Audience: {target_audience}\nPlease generate a structured BlogPlan."
            }
        ]
        return self.provider.generate_structured(
            messages=messages,
            response_model=BlogPlan,
            temperature=0.2
        )
