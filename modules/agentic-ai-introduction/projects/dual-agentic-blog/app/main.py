"""Unified Command-Line Interface and entrypoint for Dual-Agentic-Blog."""

import argparse
import sys
import os
from .config import AppConfig
from .providers.mock_provider import MockProvider
from .providers.ollama_provider import OllamaProvider
from .providers.google_provider import GoogleProvider
from .coordinator import PipelineCoordinator
from .ui.terminal import TerminalUI


def parse_args():
    parser = argparse.ArgumentParser(
        description="Dual-Backend Multi-Agent Self-Correcting Blog Writer (Google Gemini + Local Ollama)"
    )
    parser.add_argument(
        "--topic",
        type=str,
        default="Modern Vector Search & RAG Architectures",
        help="Blog post topic to generate"
    )
    parser.add_argument(
        "--provider",
        type=str,
        choices=["mock", "ollama", "google"],
        default="mock",
        help="Backend model provider: 'mock' (offline), 'ollama' (local open-source), or 'google' (Gemini cloud)"
    )
    parser.add_argument(
        "--model",
        type=str,
        default=None,
        help="Model identifier (e.g. 'llama3.1:8b', 'qwen2.5:7b', 'gemini-1.5-flash')"
    )
    parser.add_argument(
        "--max-iterations",
        type=int,
        default=3,
        help="Maximum self-correction retry budget (default: 3)"
    )
    parser.add_argument(
        "--output",
        type=str,
        default=None,
        help="Optional path to save final markdown blog post"
    )
    parser.add_argument(
        "--web",
        action="store_true",
        help="Launch the standalone local web dashboard instead of CLI terminal mode"
    )
    parser.add_argument(
        "--port",
        type=int,
        default=8000,
        help="Port for local web dashboard (default: 8000)"
    )
    return parser.parse_args()


def main():
    args = parse_args()

    # Launch Web Server if requested
    if args.web:
        import uvicorn
        from .ui.web.server import create_app
        print(f"\n[+] Launching Multi-Agent Local Web Dashboard at http://localhost:{args.port}")
        uvicorn.run(create_app(), host="127.0.0.1", port=args.port, log_level="info")
        return

    # CLI Terminal Mode
    default_models = {
        "mock": "mock-agent-v1",
        "ollama": "llama3.1:8b",
        "google": "gemini-1.5-flash"
    }
    model_name = args.model or default_models.get(args.provider, "mock-agent-v1")

    config = AppConfig(
        provider=args.provider,
        model=model_name,
        max_iterations=args.max_iterations,
    )

    try:
        config.validate()
    except ValueError as e:
        print(f"\n[ERROR] Configuration Error: {e}\n")
        sys.exit(1)

    # Initialize Provider
    if args.provider == "mock":
        provider = MockProvider(model_name=model_name)
    elif args.provider == "ollama":
        provider = OllamaProvider(model_name=model_name, host=config.ollama_host)
        if not provider.is_healthy():
            print(f"\n[WARNING] Could not connect to Ollama at {config.ollama_host}.")
            print("Run `ollama serve` in a terminal or pass `--provider mock` for offline simulation.\n")
            sys.exit(1)
    elif args.provider == "google":
        provider = GoogleProvider(model_name=model_name, api_key=config.gemini_api_key)
        if not provider.is_healthy():
            print("\n[WARNING] GEMINI_API_KEY is not set or Google provider is not ready.")
            print("Set your API key via `set GEMINI_API_KEY=your_key` or use `--provider ollama` / `--provider mock`.\n")
            sys.exit(1)

    ui = TerminalUI()
    ui.print_banner(
        topic=args.topic,
        provider=args.provider,
        model=model_name,
        max_iterations=args.max_iterations
    )

    coordinator = PipelineCoordinator(config=config, provider=provider)

    last_draft = None

    def on_step(step):
        nonlocal last_draft
        ui.print_step(step)

    # Execute
    state = coordinator.run(topic=args.topic, on_step_callback=on_step)

    # Print Plan
    if state.plan:
        ui.print_plan(state.plan)

    # Print validation reports and diffs
    for idx, report in enumerate(state.validation_reports, 1):
        ui.print_validation_report(report, iteration=idx)

    if len(state.draft_history) > 1:
        ui.print_diff(
            draft_before=state.draft_history[0],
            draft_after=state.draft_history[-1],
            from_iter=1,
            to_iter=state.total_iterations
        )

    # Print published article
    if state.current_draft:
        ui.print_final_article(state.current_draft)

    # Save to disk if requested
    if args.output and state.current_draft:
        with open(args.output, "w", encoding="utf-8") as f:
            f.write(state.current_draft)
        print(f"\n[+] Saved final article to: {args.output}")

    # Summary
    ui.print_summary(state)


if __name__ == "__main__":
    main()
