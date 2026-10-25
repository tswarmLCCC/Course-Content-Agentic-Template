"""Local Ollama provider implementation using official ollama Python SDK."""

from typing import List, Dict, Any, Type, TypeVar, Tuple, Optional
from pydantic import BaseModel

from .base import BaseLLMProvider

T = TypeVar("T", bound=BaseModel)


class OllamaProvider(BaseLLMProvider):
    """Interfaces with a local Ollama daemon (default: http://localhost:11434)."""

    def __init__(self, model_name: str = "llama3.1:8b", host: str = "http://localhost:11434", **kwargs):
        super().__init__(model_name=model_name, **kwargs)
        self.host = host
        try:
            import ollama
            self.client = ollama.Client(host=self.host)
        except Exception:
            self.client = None

    def is_healthy(self) -> bool:
        if self.client is None:
            return False
        try:
            self.client.list()
            return True
        except Exception:
            return False

    def generate_structured(
        self,
        messages: List[Dict[str, str]],
        response_model: Type[T],
        temperature: float = 0.2,
    ) -> T:
        if not self.is_healthy():
            raise ConnectionError(
                f"Cannot connect to Ollama at {self.host}. "
                "Ensure Ollama is running (`ollama serve`) or use `--provider mock`."
            )

        # Utilize native Ollama JSON schema constrained decoding
        schema = response_model.model_json_schema()
        response = self.client.chat(
            model=self.model_name,
            messages=messages,
            format=schema,
            options={"temperature": temperature},
        )

        content = response.message.content
        return response_model.model_validate_json(content)

    def generate_text(
        self,
        messages: List[Dict[str, str]],
        temperature: float = 0.7,
        tools: Optional[List[Any]] = None,
    ) -> Tuple[str, List[Dict[str, Any]]]:
        if not self.is_healthy():
            raise ConnectionError(
                f"Cannot connect to Ollama at {self.host}. "
                "Ensure Ollama is running or use `--provider mock`."
            )

        executed_tools_trace = []
        call_messages = list(messages)

        # 1. Initial invocation with optional tools
        chat_kwargs: Dict[str, Any] = {
            "model": self.model_name,
            "messages": call_messages,
            "options": {"temperature": temperature},
        }
        if tools:
            chat_kwargs["tools"] = tools

        response = self.client.chat(**chat_kwargs)

        # 2. Check for tool calls
        if hasattr(response.message, "tool_calls") and response.message.tool_calls:
            call_messages.append(response.message)
            func_map = {f.__name__: f for f in (tools or [])}

            for tool_call in response.message.tool_calls:
                fn_name = tool_call.function.name
                fn_args = tool_call.function.arguments

                if fn_name in func_map:
                    try:
                        res = func_map[fn_name](**fn_args)
                    except Exception as e:
                        res = f"Tool Execution Error: {str(e)}"

                    executed_tools_trace.append({
                        "tool": fn_name,
                        "args": fn_args,
                        "result": res
                    })
                    call_messages.append({
                        "role": "tool",
                        "content": str(res),
                        "name": fn_name
                    })

            # Follow-up call with tool results
            final_response = self.client.chat(
                model=self.model_name,
                messages=call_messages,
                options={"temperature": temperature},
            )
            return final_response.message.content, executed_tools_trace

        return response.message.content, executed_tools_trace
