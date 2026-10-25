"""Validator Agent: Evaluates drafts against rubric criteria and issues actionable feedback."""

from typing import List, Dict, Any
from ..providers.base import BaseLLMProvider
from ..schemas import BlogPlan, ValidationReport
from ..tools import calculate_reading_metrics

VALIDATOR_SYSTEM_PROMPT = """You are a rigorous Lead Technical Editor and Code Reviewer.
Your mission is to evaluate a technical blog draft against an approved outline and objective quality gates.

Evaluation Gates:
1. Length Gate: Compare the actual word count against the target budget. If the text is severely under target (< 80% of minimum) or overly bloated (> 130% of maximum), flag word_count_status accordingly.
2. Structure Gate: Verify that every section heading specified in the plan appears as a '## Heading' in the draft. List any omitted headings in missing_sections.
3. Quality Gate: Evaluate whether the content provides concrete technical substance rather than superficial buzzword summaries.

Output Rules:
- Return a strictly conforming ValidationReport JSON object.
- If any gate fails (missing sections, out-of-bounds length, or shallow content), you MUST set passed = False and overall_score < 75.
- If passed is False, provide specific, constructive bullet points in actionable_feedback so the Writer knows exactly what to fix.
- Only set passed = True if all sections are present and quality standards are satisfied.
"""


class ValidatorAgent:
    """Agent responsible for quality gating, rubric verification, and feedback generation."""

    def __init__(self, provider: BaseLLMProvider):
        self.provider = provider

    def validate(
        self,
        plan: BlogPlan,
        draft: str,
        target_words_min: int = 150,
        target_words_max: int = 300,
    ) -> ValidationReport:
        """Inspects draft against rubric and plan."""
        # Calculate objective metrics upfront
        metrics = calculate_reading_metrics(draft)
        measured_words = metrics["word_count"]

        # Check section presence
        missing = []
        for s in plan.sections:
            if s.heading.lower() not in draft.lower():
                missing.append(s.heading)

        context_prompt = (
            f"Approved Plan:\n{plan.model_dump_json(indent=2)}\n\n"
            f"Measured Pre-Analysis:\n"
            f"- Word Count: {measured_words} (Target Range: {target_words_min}-{target_words_max})\n"
            f"- Missing Headings Detected: {missing if missing else 'None'}\n\n"
            f"Current Blog Draft to Review:\n{draft}\n\n"
            "Please evaluate the draft and return a strict ValidationReport."
        )

        messages = [
            {"role": "system", "content": VALIDATOR_SYSTEM_PROMPT},
            {"role": "user", "content": context_prompt}
        ]

        report = self.provider.generate_structured(
            messages=messages,
            response_model=ValidationReport,
            temperature=0.0
        )
        return report
