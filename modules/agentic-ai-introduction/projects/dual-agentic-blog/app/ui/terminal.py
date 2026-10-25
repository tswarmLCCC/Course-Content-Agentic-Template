"""Rich terminal user interface with live traces and revision diffs."""

import difflib
from typing import Optional, List
from rich.console import Console
from rich.panel import Panel
from rich.table import Table
from rich.syntax import Syntax
from rich.tree import Tree
from rich.text import Text

from ..schemas import PipelineRunState, AgentTraceStep, ValidationReport, BlogPlan


class TerminalUI:
    """Renders formatted multi-agent execution traces to the terminal using Rich."""

    def __init__(self):
        self.console = Console()

    def print_banner(self, topic: str, provider: str, model: str, max_iterations: int):
        """Prints startup banner with execution parameters."""
        banner_text = Text()
        banner_text.append("DUAL-BACKEND MULTI-AGENT BLOG WRITER\n", style="bold cyan")
        banner_text.append(f"Topic:          {topic}\n", style="bold white")
        banner_text.append(f"Provider:       {provider.upper()}\n", style="green")
        banner_text.append(f"Model:          {model}\n", style="yellow")
        banner_text.append(f"Max Iterations: {max_iterations}", style="magenta")

        panel = Panel(
            banner_text,
            title="[bold green]Agentic Pipeline Active[/bold green]",
            border_style="cyan",
            expand=False
        )
        self.console.print("\n", panel)

    def print_plan(self, plan: BlogPlan):
        """Renders the strategic outline as a tree structure."""
        tree = Tree(f"[bold cyan]Plan: {plan.title}[/bold cyan] ({plan.total_target_words} words target)")
        for idx, s in enumerate(plan.sections, 1):
            sec_node = tree.add(f"[bold yellow]Section {idx}: {s.heading}[/bold yellow] (~{s.target_words} words)")
            for kp in s.key_points:
                sec_node.add(f"[dim]{kp}[/dim]")
        
        panel = Panel(tree, title="[bold cyan]Planner Agent Strategic Blueprint[/bold cyan]", border_style="blue")
        self.console.print(panel)

    def print_step(self, step: AgentTraceStep):
        """Prints an individual agent step trace."""
        colors = {
            "PLAN": "cyan",
            "DRAFT": "yellow",
            "VALIDATE": "magenta",
            "TOOL_CALL": "green"
        }
        color = colors.get(step.phase, "white")
        badge = f"[{color} bold]{step.agent_name}[/{color} bold] [dim]({step.phase} - {step.latency_ms}ms)[/dim]"
        self.console.print(f"  [bold]>[/bold] {badge}: {step.content_snippet}")

        if step.tool_calls:
            for tc in step.tool_calls:
                self.console.print(f"    [green][+] Tool Executed:[/green] [bold]{tc.get('tool')}[/bold] -> [dim]{tc.get('result')}[/dim]")

    def print_validation_report(self, report: ValidationReport, iteration: int):
        """Renders the validator scorecard."""
        if report.passed:
            title = f"[bold green]Validation Gate PASSED (Iteration {iteration})[/bold green]"
            border = "green"
            body = (
                f"[bold green]Score: {report.overall_score}/100[/bold green] | "
                f"Words: {report.word_count_actual} | All quality gates satisfied!"
            )
        else:
            title = f"[bold red]Validation Gate REJECTED (Iteration {iteration} -> Retry Required)[/bold red]"
            border = "red"
            body = (
                f"[bold red]Score: {report.overall_score}/100[/bold red] | "
                f"Words: {report.word_count_actual} ({report.word_count_status})\n"
            )
            if report.critiques:
                body += "\n[bold]Issues Identified:[/bold]\n"
                for c in report.critiques:
                    body += f"  [red]x[/red] {c}\n"
            if report.actionable_feedback:
                body += "\n[bold yellow]Instructions for Next Iteration:[/bold yellow]\n"
                for af in report.actionable_feedback:
                    body += f"  [yellow]->[/yellow] {af}\n"

        panel = Panel(body.strip(), title=title, border_style=border)
        self.console.print(panel)

    def print_diff(self, draft_before: str, draft_after: str, from_iter: int, to_iter: int):
        """Displays unified git-style diff between two drafts."""
        diff_lines = list(difflib.unified_diff(
            draft_before.splitlines(keepends=True),
            draft_after.splitlines(keepends=True),
            fromfile=f"Draft_v{from_iter}.md",
            tofile=f"Draft_v{to_iter}.md",
        ))
        if diff_lines:
            diff_text = "".join(diff_lines)
            syntax = Syntax(diff_text, "diff", theme="monokai", line_numbers=False)
            panel = Panel(
                syntax,
                title=f"[bold yellow]Self-Correction Diff (Iteration {from_iter} -> Iteration {to_iter})[/bold yellow]",
                border_style="yellow"
            )
            self.console.print(panel)

    def print_final_article(self, article: str):
        """Displays the final publication-ready markdown article."""
        syntax = Syntax(article, "markdown", theme="monokai", word_wrap=True)
        panel = Panel(syntax, title="[bold green]FINAL PUBLISHED BLOG ARTICLE[/bold green]", border_style="green")
        self.console.print(panel)

    def print_summary(self, state: PipelineRunState):
        """Prints the executive execution metrics summary."""
        table = Table(title="[bold]Pipeline Execution Summary[/bold]", border_style="cyan")
        table.add_column("Metric", style="bold white")
        table.add_column("Value", style="green")

        table.add_row("Final Status", state.final_status)
        table.add_row("Total Iterations", str(state.total_iterations))
        table.add_row("Final Word Count", str(len(state.current_draft.split())))
        final_score = state.validation_reports[-1].overall_score if state.validation_reports else "N/A"
        table.add_row("Final Quality Score", f"{final_score}/100")
        table.add_row("Total Steps Recorded", str(len(state.trace_steps)))

        self.console.print("\n", table, "\n")
