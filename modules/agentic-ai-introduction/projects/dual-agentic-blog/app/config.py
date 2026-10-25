"""Configuration module for dual-agentic-blog."""

import os
from dataclasses import dataclass
from typing import Optional

@dataclass
class AppConfig:
    """Runtime configuration settings."""
    provider: str = "mock"  # "ollama", "google", or "mock"
    model: str = "llama3.1:8b"  # Default model for chosen provider
    ollama_host: str = os.getenv("OLLAMA_HOST", "http://localhost:11434")
    gemini_api_key: Optional[str] = os.getenv("GEMINI_API_KEY")
    max_iterations: int = 3
    temperature: float = 0.2
    target_words_min: int = 150
    target_words_max: int = 300
    enable_tools: bool = True

    def validate(self) -> None:
        """Validate configuration settings based on provider."""
        if self.provider == "google" and not self.gemini_api_key:
            raise ValueError(
                "GEMINI_API_KEY environment variable is required when provider='google'. "
                "Set it via `set GEMINI_API_KEY=your_key` or switch to `--provider ollama` or `--provider mock`."
            )
        if self.provider not in ("google", "ollama", "mock"):
            raise ValueError(f"Unknown provider: '{self.provider}'. Must be 'google', 'ollama', or 'mock'.")
