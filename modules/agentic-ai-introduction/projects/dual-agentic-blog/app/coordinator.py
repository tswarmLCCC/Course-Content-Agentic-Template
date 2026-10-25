"""Pipeline Coordinator: Orchestrates the Evaluator-Optimizer multi-agent loop with defensive guards."""

import time
from typing import Optional, Callable, List
from .config import AppConfig
from .providers.base import BaseLLMProvider
from .schemas import PipelineRunState, AgentTraceStep, BlogPlan, ValidationReport
from .agents.planner import PlannerAgent
from .agents.writer import WriterAgent
from .agents.validator import ValidatorAgent


class PipelineCoordinator:
    """State machine controller implementing the self-correcting Evaluator-Optimizer loop."""

    def __init__(self, config: AppConfig, provider: BaseLLMProvider):
        self.config = config
        self.provider = provider
        self.planner = PlannerAgent(provider)
        self.writer = WriterAgent(provider, enable_tools=config.enable_tools)
        self.validator = ValidatorAgent(provider)

    def run(
        self,
        topic: str,
        on_step_callback: Optional[Callable[[AgentTraceStep], None]] = None,
    ) -> PipelineRunState:
        """Executes the multi-agent pipeline for the specified topic."""
        state = PipelineRunState(
            topic=topic,
            provider=self.config.provider,
            model=self.config.model,
        )

        step_counter = 0

        def emit_step(agent_name: str, phase: str, snippet: str, latency: float, tool_calls=None):
            nonlocal step_counter
            step_counter += 1
            step = AgentTraceStep(
                step_id=step_counter,
                iteration=state.total_iterations,
                agent_name=agent_name,
                phase=phase,
                content_snippet=snippet,
                latency_ms=round(latency * 1000, 1),
                tool_calls=tool_calls,
            )
            state.trace_steps.append(step)
            if on_step_callback:
                on_step_callback(step)

        # -------------------------------------------------------------
        # Phase 1: Planning
        # -------------------------------------------------------------
        t0 = time.time()
        plan: BlogPlan = self.planner.plan(topic=topic)
        t_plan = time.time() - t0
        state.plan = plan
        emit_step(
            agent_name="PlannerAgent",
            phase="PLAN",
            snippet=f"Formulated strategic plan: '{plan.title}' with {len(plan.sections)} sections.",
            latency=t_plan
        )

        # -------------------------------------------------------------
        # Phase 2: Evaluator-Optimizer Execution Loop
        # -------------------------------------------------------------
        previous_draft: Optional[str] = None
        feedback: Optional[List[str]] = None

        while state.total_iterations < self.config.max_iterations:
            state.total_iterations += 1
            iter_num = state.total_iterations

            # 1. Writer Agent drafting / revising
            t_write_start = time.time()
            draft, tool_traces = self.writer.draft(
                plan=plan,
                previous_draft=previous_draft,
                critique_feedback=feedback,
            )
            t_write = time.time() - t_write_start
            state.current_draft = draft
            state.draft_history.append(draft)

            action_desc = "Authored initial draft" if iter_num == 1 else f"Revised draft based on {len(feedback or [])} critique items"
            emit_step(
                agent_name="WriterAgent",
                phase="DRAFT",
                snippet=f"{action_desc} ({len(draft.split())} words).",
                latency=t_write,
                tool_calls=tool_traces if tool_traces else None,
            )

            # 2. Validator Agent evaluating draft
            t_val_start = time.time()
            report: ValidationReport = self.validator.validate(
                plan=plan,
                draft=draft,
                target_words_min=self.config.target_words_min,
                target_words_max=self.config.target_words_max,
            )
            t_val = time.time() - t_val_start
            state.validation_reports.append(report)

            verdict = "PASSED" if report.passed else "NEEDS_REVISION"
            emit_step(
                agent_name="ValidatorAgent",
                phase="VALIDATE",
                snippet=f"Verdict: {verdict} (Score: {report.overall_score}/100, Words: {report.word_count_actual}). Issues: {len(report.critiques)}.",
                latency=t_val,
            )

            # 3. Validation Gate & State Transition
            if report.passed:
                state.final_status = "PASSED"
                break
            else:
                # Prepare feedback for next iteration
                previous_draft = draft
                feedback = report.actionable_feedback

        # Defensive Runaway Loop Check
        if state.final_status != "PASSED":
            state.final_status = "MAX_RETRIES_EXCEEDED"

        return state
