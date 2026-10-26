#!/usr/bin/env python3
"""
=============================================================================
AENG 2100: Agentic Software Engineering & The New SDLC
Unit 01 Applied Lab: Automated Spec-Driven Development (SDD) Agent Harness
=============================================================================
Author: LCCC Computer Science & Agentic Engineering Faculty
Environment: Python 3.10+, Requests, Pytest
Backends: Google Gemini Flash REST API / Local Ollama (Qwen 2.5 Coder) / Mock
=============================================================================
"""

import os
import sys
import json
import re
import subprocess
import tempfile
from typing import Dict, Any, List, Optional, Tuple


# =============================================================================
# 1. Configuration & Model Dispatcher
# =============================================================================

DEFAULT_OLLAMA_URL = os.environ.get("OLLAMA_URL", "http://localhost:11434/api/generate")
DEFAULT_OLLAMA_MODEL = os.environ.get("OLLAMA_MODEL", "qwen2.5-coder:7b")
GEMINI_API_KEY = os.environ.get("GEMINI_API_KEY", "")
GEMINI_ENDPOINT = "https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash:generateContent"


class AgentModelClient:
    """
    Unified dual-backend client supporting Google Gemini Flash, local Ollama,
    and a deterministic simulation mock for offline verification.
    """
    def __init__(self, backend: str = "auto", model_name: Optional[str] = None):
        self.backend = backend
        self.model_name = model_name or DEFAULT_OLLAMA_MODEL
        if self.backend == "auto":
            if GEMINI_API_KEY:
                self.backend = "gemini"
            else:
                self.backend = "ollama"

    def query(self, system_prompt: str, user_prompt: str) -> str:
        """Dispatches query to the configured backend."""
        if self.backend == "mock":
            return self._query_mock(system_prompt, user_prompt)
        elif self.backend == "gemini":
            return self._query_gemini(system_prompt, user_prompt)
        elif self.backend == "ollama":
            return self._query_ollama(system_prompt, user_prompt)
        else:
            raise ValueError(f"Unknown backend: {self.backend}")

    def _query_mock(self, system_prompt: str, user_prompt: str) -> str:
        """Deterministic simulation for offline testing."""
        # Return candidate code that solves the string utility spec
        return '''```python
def reverse_words(s: str) -> str:
    """Reverses the words in a string while preserving single spaces."""
    if not s or not s.strip():
        return ""
    words = s.strip().split()
    return " ".join(reversed(words))

def is_palindrome(s: str) -> bool:
    """Checks if a string is a palindrome, ignoring non-alphanumeric chars and case."""
    clean = "".join(ch.lower() for ch in s if ch.isalnum())
    return clean == clean[::-1]

def count_vowels(s: str) -> int:
    """Counts the total number of vowels in a string (case-insensitive)."""
    if not s:
        return 0
    vowels = set("aeiouAEIOU")
    return sum(1 for ch in s if ch in vowels)
```'''

    def _query_gemini(self, system_prompt: str, user_prompt: str) -> str:
        """Sends request to Google Gemini Flash REST API via urllib/requests."""
        import urllib.request
        import urllib.error

        if not GEMINI_API_KEY:
            print("[INFO] GEMINI_API_KEY not set. Falling back to local Ollama / mock backend.")
            return self._query_ollama(system_prompt, user_prompt)

        url = f"{GEMINI_ENDPOINT}?key={GEMINI_API_KEY}"
        payload = {
            "contents": [
                {
                    "parts": [
                        {"text": f"System Instructions:\n{system_prompt}\n\nTask:\n{user_prompt}"}
                    ]
                }
            ],
            "generationConfig": {
                "temperature": 0.2,
                "maxOutputTokens": 2048
            }
        }
        req = urllib.request.Request(
            url,
            data=json.dumps(payload).encode("utf-8"),
            headers={"Content-Type": "application/json"}
        )
        try:
            with urllib.request.urlopen(req, timeout=30) as response:
                result = json.loads(response.read().decode("utf-8"))
                return result["candidates"][0]["content"]["parts"][0]["text"]
        except urllib.error.URLError as e:
            # Fall back to mock if network fails
            print(f"[WARN] Gemini API failed ({e}). Falling back to simulation mock.")
            return self._query_mock(system_prompt, user_prompt)

    def _query_ollama(self, system_prompt: str, user_prompt: str) -> str:
        """Sends request to local Ollama instance."""
        import urllib.request
        import urllib.error

        payload = {
            "model": self.model_name,
            "system": system_prompt,
            "prompt": user_prompt,
            "stream": False,
            "options": {"temperature": 0.2}
        }
        req = urllib.request.Request(
            DEFAULT_OLLAMA_URL,
            data=json.dumps(payload).encode("utf-8"),
            headers={"Content-Type": "application/json"}
        )
        try:
            with urllib.request.urlopen(req, timeout=45) as response:
                result = json.loads(response.read().decode("utf-8"))
                return result.get("response", "")
        except urllib.error.URLError as e:
            print(f"[WARN] Ollama local service unreachable ({e}). Falling back to simulation mock.")
            return self._query_mock(system_prompt, user_prompt)


# =============================================================================
# 2. Poka-Yoke Non-Destructive Diff Patcher
# =============================================================================

class DiffPatcher:
    """
    Enforces non-destructive, targeted chunk replacements.
    Rejects full-file overwrites to eliminate token blowups and silent truncation.
    """
    @staticmethod
    def apply_targeted_patch(original_content: str, target_chunk: str, replacement_chunk: str) -> Tuple[bool, str]:
        """
        Replaces exactly one instance of target_chunk with replacement_chunk.
        Returns (success: bool, updated_content: str).
        """
        if target_chunk not in original_content:
            return False, f"Target chunk not found in original content: '{target_chunk[:40]}...'"
        
        occurrences = original_content.count(target_chunk)
        if occurrences > 1:
            return False, f"Target chunk is ambiguous ({occurrences} occurrences found)."
            
        updated = original_content.replace(target_chunk, replacement_chunk, 1)
        return True, updated


# =============================================================================
# 3. Spec Parser (EARS Syntax Extractor)
# =============================================================================

class SpecParser:
    """
    Parses machine-actionable specifications adhering to EARS syntax.
    """
    @staticmethod
    def parse_ears_spec(spec_text: str) -> Dict[str, List[str]]:
        """Extracts EARS requirements into categorized buckets."""
        categories = {
            "ubiquitous": [],
            "event_driven": [],
            "state_driven": [],
            "unwanted": [],
            "optional": []
        }
        for line in spec_text.strip().splitlines():
            line = line.strip()
            if not line or not line.startswith("- "):
                continue
            cleaned = line.lstrip("- ").strip()
            upper = cleaned.upper()
            if upper.startswith("WHEN "):
                categories["event_driven"].append(cleaned)
            elif upper.startswith("WHILE "):
                categories["state_driven"].append(cleaned)
            elif upper.startswith("IF "):
                categories["unwanted"].append(cleaned)
            elif upper.startswith("WHERE "):
                categories["optional"].append(cleaned)
            elif "SHALL" in upper:
                categories["ubiquitous"].append(cleaned)
        return categories


# =============================================================================
# 4. Closed-Loop Spec-Driven Development (SDD) Harness Engine
# =============================================================================

SAMPLE_SPECIFICATION = """
# String Utilities Micro-Library Specification
- REQ-01: The system shall provide a function `reverse_words(s: str) -> str` that reverses words in a string.
- REQ-02: WHEN given an empty or whitespace-only string, `reverse_words` shall return an empty string.
- REQ-03: The system shall provide a function `is_palindrome(s: str) -> bool` that checks if a string is a palindrome.
- REQ-04: The system shall provide a function `count_vowels(s: str) -> int` that counts total vowels.
- REQ-05: IF input is null or empty, THEN `count_vowels` shall return 0.
"""

SAMPLE_TEST_SUITE = '''
import pytest
from candidate_module import reverse_words, is_palindrome, count_vowels

def test_reverse_words_standard():
    assert reverse_words("hello world") == "world hello"
    assert reverse_words("agentic ai engineering") == "engineering ai agentic"

def test_reverse_words_empty():
    assert reverse_words("") == ""
    assert reverse_words("   ") == ""

def test_is_palindrome():
    assert is_palindrome("Racecar") is True
    assert is_palindrome("A man, a plan, a canal: Panama") is True
    assert is_palindrome("software") is False

def test_count_vowels():
    assert count_vowels("Agentic") == 3
    assert count_vowels("xyz") == 0
    assert count_vowels("") == 0
'''


class SDDHarnessEngine:
    """
    Orchestrates the 5-stage Spec-Driven Development cycle with automated test feedback.
    """
    def __init__(self, client: AgentModelClient, max_retries: int = 3):
        self.client = client
        self.max_retries = max_retries
        self.patcher = DiffPatcher()

    def run_cycle(self, spec_markdown: str, test_suite_code: str) -> Dict[str, Any]:
        """
        Executes the closed-loop SDD cycle:
        1. Ingest Spec
        2. Plan Implementation
        3. Generate Code
        4. Execute Pytest Sandbox
        5. Auto-Patch on Failure (up to max_retries)
        """
        history = []
        print("\n[STAGE 1] Ingesting EARS Specification...")
        parsed_ears = SpecParser.parse_ears_spec(spec_markdown)
        total_reqs = sum(len(v) for v in parsed_ears.values())
        print(f"  -> Extracted {total_reqs} formal EARS requirements across 5 categories.")

        print("\n[STAGE 2] Generating Architecture & Implementation Plan...")
        system_rules = (
            "You are an autonomous Agentic Software Engineer. You write clean, production-grade Python 3.10+.\n"
            "Rules:\n"
            "1. Output ONLY executable code in fenced blocks (```python ... ```).\n"
            "2. No explanations or conversational chit-chat.\n"
            "3. Enforce all EARS requirements exactly as specified.\n"
        )
        plan_prompt = f"Given this specification, list required function signatures and docstrings:\n{spec_markdown}"
        plan_response = self.client.query(system_rules, plan_prompt)
        history.append({"stage": "plan", "output": plan_response[:200]})

        print("\n[STAGE 3] Generating Candidate Implementation Code...")
        code_prompt = (
            f"Generate the implementation code for module `candidate_module.py` adhering to:\n"
            f"{spec_markdown}\n\nInclude only clean Python code."
        )
        raw_code_response = self.client.query(system_rules, code_prompt)
        candidate_code = self._extract_python_code(raw_code_response)
        history.append({"stage": "initial_code", "length": len(candidate_code)})

        # Stage 4 & 5: Test Execution & Self-Healing Feedback Loop
        current_code = candidate_code
        iteration = 0
        all_passed = False
        last_error = ""

        with tempfile.TemporaryDirectory() as temp_dir:
            test_file_path = os.path.join(temp_dir, "test_candidate.py")
            module_file_path = os.path.join(temp_dir, "candidate_module.py")

            with open(test_file_path, "w", encoding="utf-8") as f:
                f.write(test_suite_code)

            while iteration <= self.max_retries and not all_passed:
                iteration += 1
                print(f"\n[STAGE 4] Executing Pytest Sandbox (Attempt {iteration}/{self.max_retries + 1})...")
                
                with open(module_file_path, "w", encoding="utf-8") as f:
                    f.write(current_code)

                passed, stdout, stderr = self._run_pytest(temp_dir)
                if passed:
                    all_passed = True
                    print(f"  [SUCCESS] All unit tests passed on attempt {iteration}!")
                    break
                else:
                    print(f"  [FAIL] Tests failed on attempt {iteration}.")
                    last_error = f"{stdout}\n{stderr}"
                    if iteration > self.max_retries:
                        print(f"  [ABORT] Exceeded maximum retry budget ({self.max_retries}).")
                        break

                    print(f"\n[STAGE 5] Reflection & Auto-Patching (Attempt {iteration})...")
                    patch_prompt = (
                        f"The following unit tests failed with this traceback:\n{last_error[:1500]}\n\n"
                        f"Current code:\n{current_code}\n\n"
                        f"Fix the failing test. Return the corrected complete module code in ```python ... ```."
                    )
                    fix_response = self.client.query(system_rules, patch_prompt)
                    current_code = self._extract_python_code(fix_response)
                    history.append({"stage": f"patch_{iteration}", "error": last_error[:200]})

        return {
            "success": all_passed,
            "attempts": iteration,
            "final_code": current_code,
            "history": history,
            "last_error": last_error if not all_passed else None
        }

    @staticmethod
    def _extract_python_code(raw_response: str) -> str:
        """Extracts python block from markdown fenced code."""
        match = re.search(r"```(?:python)?\s*([\s\S]*?)```", raw_response)
        if match:
            return match.group(1).strip()
        return raw_response.strip()

    @staticmethod
    def _run_pytest(cwd: str) -> Tuple[bool, str, str]:
        """Runs pytest inside the isolated temporary sandbox directory."""
        cmd = [sys.executable, "-m", "pytest", "test_candidate.py", "-q"]
        proc = subprocess.run(
            cmd,
            cwd=cwd,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True
        )
        return proc.returncode == 0, proc.stdout, proc.stderr


# =============================================================================
# 5. CLI Entrypoint
# =============================================================================

def main():
    """Command-line interface for the student lab harness."""
    import argparse
    parser = argparse.ArgumentParser(description="AENG 2100: Spec-Driven Development Agent Harness")
    parser.add_argument("--backend", choices=["auto", "gemini", "ollama", "mock"], default="mock",
                        help="LLM execution backend (default: mock for deterministic lab testing)")
    parser.add_argument("--model", type=str, default=DEFAULT_OLLAMA_MODEL,
                        help="Model name for Ollama backend")
    parser.add_argument("--retries", type=int, default=3,
                        help="Maximum self-healing retry iterations")
    args = parser.parse_args()

    print("=" * 75)
    print("AENG 2100: Automated Spec-Driven Development (SDD) Harness")
    print(f"Backend: {args.backend} | Retries: {args.retries}")
    print("=" * 75)

    client = AgentModelClient(backend=args.backend, model_name=args.model)
    engine = SDDHarnessEngine(client=client, max_retries=args.retries)

    result = engine.run_cycle(SAMPLE_SPECIFICATION, SAMPLE_TEST_SUITE)

    print("\n" + "=" * 75)
    print("HARNESS EXECUTION SUMMARY")
    print("=" * 75)
    print(f"Outcome: {'PASSED (100% Tests Green)' if result['success'] else 'FAILED'}")
    print(f"Total Iterations: {result['attempts']}")
    print("\nGenerated Code Preview:\n")
    print(result["final_code"][:400] + "\n...")
    print("=" * 75)

    sys.exit(0 if result["success"] else 1)


if __name__ == "__main__":
    main()
