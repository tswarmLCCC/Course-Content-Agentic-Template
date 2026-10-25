"""Writer Agent: Generates and revises blog drafts based on plans and validator critique."""

from typing import List, Optional, Tuple, Dict, Any
from ..providers.base import BaseLLMProvider
from ..schemas import BlogPlan
from ..tools import ALL_TOOLS

WRITER_SYSTEM_PROMPT = """You are a senior technical writer and software educator.
Your task is to author a clean, engaging, publication-quality technical blog post formatted in standard GitHub Flavored Markdown.

Core Invariants:
1. Follow the approved BlogPlan strictly. Use second-level markdown headers (## Heading) matching each planned section.
2. Ensure technical rigor: explain architectural mechanics clearly without generic platitudes or marketing buzzwords.
3. If revision feedback or validator critiques are provided, you MUST explicitly address every single critique item and rewrite the draft to meet the standards.
4. Output only the clean markdown article (starting with a single # Main Title).
"""


class WriterAgent:
    """Agent responsible for writing the draft and applying self-correcting revisions."""

    def __init__(self, provider: BaseLLMProvider, enable_tools: bool = True):
        self.provider = provider
        self.enable_tools = enable_tools

    def draft(
        self,
        plan: BlogPlan,
        previous_draft: Optional[str] = None,
        critique_feedback: Optional[List[str]] = None,
    ) -> Tuple[str, List[Dict[str, Any]]]:
        """Drafts or revises the blog article based on the outline and feedback."""
        sections_summary = "\n".join(
            f"- ## {s.heading} (Target: ~{s.target_words} words)\n  Key points: {', '.join(s.key_points)}"
            for s in plan.sections
        )

        user_content = f"Title: {plan.title}\nTarget Audience: {plan.target_audience}\nTarget Total Words: {plan.total_target_words}\n\nApproved Sections Outline:\n{sections_summary}\n"

        if previous_draft and critique_feedback:
            feedback_str = "\n".join(f"  * {critique}" for critique in critique_feedback)
            user_content += f"\n--- PREVIOUS DRAFT (NEEDS REVISION) ---\n{previous_draft}\n\n--- VALIDATOR CRITIQUE FEEDBACK TO FIX ---\n{feedback_str}\n\nPlease author a revised draft that completely fixes every single critique item above while preserving the approved section structure."
        else:
            user_content += "\nPlease author the initial draft of this blog post adhering to the section structure above."

        messages = [
            {"role": "system", "content": WRITER_SYSTEM_PROMPT},
            {"role": "user", "content": user_content}
        ]

        tools_to_pass = ALL_TOOLS if self.enable_tools else None
        return self.provider.generate_text(
            messages=messages,
            temperature=0.7,
            tools=tools_to_pass
        )
