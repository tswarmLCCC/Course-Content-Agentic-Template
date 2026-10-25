"""Google Gemini provider implementation using official google-genai SDK."""

import os
from typing import List, Dict, Any, Type, TypeVar, Tuple, Optional
from pydantic import BaseModel

from .base import BaseLLMProvider

T = TypeVar("T", bound=BaseModel)


class GoogleProvider(BaseLLMProvider):
    """Interfaces with Google Gemini via google-genai (Gemini 1.5 Flash / Pro)."""

    def __init__(
        self,
        model_name: str = "gemini-1.5-flash",
        api_key: Optional[str] = None,
        **kwargs
    ):
        super().__init__(model_name=model_name, **kwargs)
        self.api_key = api_key or os.getenv("GEMINI_API_KEY")
        self.client = None
        if self.api_key:
            try:
                from google import genai
                self.client = genai.Client(api_key=self.api_key)
            except Exception:
                self.client = None

    def is_healthy(self) -> bool:
        return self.client is not None and bool(self.api_key)

    def _convert_messages_to_prompt(self, messages: List[Dict[str, str]]) -> Tuple[Optional[str], str]:
        system_instruction = None
        contents = []
        for m in messages:
            role = m.get("role", "user")
            content = m.get("content", "")
            if role == "system":
                system_instruction = content
            elif role == "user":
                contents.append(f"User: {content}")
            elif role == "assistant":
                contents.append(f"Assistant: {content}")
            elif role == "tool":
                contents.append(f"Tool Result ({m.get('name', 'tool')}): {content}")
        return system_instruction, "\n\n".join(contents)

    def generate_structured(
        self,
        messages: List[Dict[str, str]],
        response_model: Type[T],
        temperature: float = 0.2,
    ) -> T:
        if not self.is_healthy():
            raise ValueError(
                "Google Gemini provider requires GEMINI_API_KEY. "
                "Set it in your environment or use `--provider mock` / `--provider ollama`."
            )

        from google.genai import types

        sys_inst, full_prompt = self._convert_messages_to_prompt(messages)
        config = types.GenerateContentConfig(
            response_mime_type="application/json",
            response_schema=response_model,
            temperature=temperature,
            system_instruction=sys_inst,
        )

        response = self.client.models.generate_content(
            model=self.model_name,
            contents=full_prompt,
            config=config,
        )
        return response_model.model_validate_json(response.text)

    def generate_text(
        self,
        messages: List[Dict[str, str]],
        temperature: float = 0.7,
        tools: Optional[List[Any]] = None,
    ) -> Tuple[str, List[Dict[str, Any]]]:
        if not self.is_healthy():
            raise ValueError(
                "Google Gemini provider requires GEMINI_API_KEY. "
                "Set it in your environment or use `--provider mock` / `--provider ollama`."
            )

        from google.genai import types

        sys_inst, full_prompt = self._convert_messages_to_prompt(messages)
        config = types.GenerateContentConfig(
            temperature=temperature,
            system_instruction=sys_inst,
        )

        response = self.client.models.generate_content(
            model=self.model_name,
            contents=full_prompt,
            config=config,
        )
        return response.text, []
