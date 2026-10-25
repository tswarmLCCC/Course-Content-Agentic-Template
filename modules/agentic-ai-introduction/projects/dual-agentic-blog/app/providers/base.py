"""Abstract base class for LLM providers."""

from abc import ABC, abstractmethod
from typing import List, Dict, Any, Type, TypeVar, Tuple, Optional
from pydantic import BaseModel

T = TypeVar("T", bound=BaseModel)


class BaseLLMProvider(ABC):
    """Abstract interface for all language model providers (Ollama, Gemini, Mock)."""

    def __init__(self, model_name: str, **kwargs):
        self.model_name = model_name
        self.kwargs = kwargs

    @abstractmethod
    def generate_structured(
        self,
        messages: List[Dict[str, str]],
        response_model: Type[T],
        temperature: float = 0.2,
    ) -> T:
        """Generates a strictly validated Pydantic model response.
        
        Args:
            messages: OpenAI-style list of message dicts (role, content).
            response_model: Pydantic class to constrain output.
            temperature: Sampling temperature (lower = more deterministic).
        
        Returns:
            Validated instance of response_model.
        """
        pass

    @abstractmethod
    def generate_text(
        self,
        messages: List[Dict[str, str]],
        temperature: float = 0.7,
        tools: Optional[List[Any]] = None,
    ) -> Tuple[str, List[Dict[str, Any]]]:
        """Generates natural language text, optionally invoking tools.
        
        Args:
            messages: OpenAI-style list of message dicts.
            temperature: Sampling temperature.
            tools: Optional list of callable Python functions for tool calling.
            
        Returns:
            Tuple of (text_content, list_of_executed_tool_traces).
        """
        pass

    @abstractmethod
    def is_healthy(self) -> bool:
        """Returns True if the backend is reachable and ready."""
        pass
