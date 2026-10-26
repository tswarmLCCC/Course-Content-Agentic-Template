#!/usr/bin/env python3
"""
Automated Pytest Suite for AENG 2100 Unit 01 SDD Harness Engine.
Verifies EARS parsing, Poka-Yoke diff patching, retry bounds, and dual-backend fallbacks.
"""

import os
import sys
import pytest

from starter_sdd_harness import (
    SpecParser,
    DiffPatcher,
    AgentModelClient,
    SDDHarnessEngine,
    SAMPLE_SPECIFICATION,
    SAMPLE_TEST_SUITE
)


def test_spec_parser_ears():
    """Verifies that EARS syntax requirements are properly parsed into correct categories."""
    spec_text = """
    - The engine shall record all transactions in SQLite.
    - WHEN a user clicks checkout, the engine shall validate cart items.
    - WHILE processing payment, the engine shall display a spinner.
    - IF card is declined, THEN the engine shall notify user.
    - WHERE dark_mode is true, the engine shall render black background.
    """
    parsed = SpecParser.parse_ears_spec(spec_text)
    assert len(parsed["ubiquitous"]) == 1
    assert "SQLite" in parsed["ubiquitous"][0]
    assert len(parsed["event_driven"]) == 1
    assert "checkout" in parsed["event_driven"][0]
    assert len(parsed["state_driven"]) == 1
    assert "processing payment" in parsed["state_driven"][0]
    assert len(parsed["unwanted"]) == 1
    assert "declined" in parsed["unwanted"][0]
    assert len(parsed["optional"]) == 1
    assert "dark_mode" in parsed["optional"][0]


def test_diff_patcher_success():
    """Verifies targeted single-instance chunk replacement."""
    original = "def foo():\n    return 41\n"
    target = "    return 41"
    replacement = "    return 42"
    success, updated = DiffPatcher.apply_targeted_patch(original, target, replacement)
    assert success is True
    assert updated == "def foo():\n    return 42\n"


def test_diff_patcher_not_found():
    """Verifies that DiffPatcher safely rejects target chunks that do not exist."""
    original = "def foo():\n    return 42\n"
    target = "non_existent_code()"
    replacement = "return 100"
    success, msg = DiffPatcher.apply_targeted_patch(original, target, replacement)
    assert success is False
    assert "not found" in msg.lower()


def test_diff_patcher_ambiguous():
    """Verifies that DiffPatcher rejects ambiguous chunks with multiple occurrences."""
    original = "x = 1\nx = 1\n"
    target = "x = 1"
    replacement = "x = 2"
    success, msg = DiffPatcher.apply_targeted_patch(original, target, replacement)
    assert success is False
    assert "ambiguous" in msg.lower()


def test_sdd_engine_mock_success():
    """Verifies that SDDHarnessEngine runs full 5-stage cycle and passes unit tests."""
    client = AgentModelClient(backend="mock")
    engine = SDDHarnessEngine(client=client, max_retries=2)
    result = engine.run_cycle(SAMPLE_SPECIFICATION, SAMPLE_TEST_SUITE)
    assert result["success"] is True
    assert result["attempts"] == 1
    assert "reverse_words" in result["final_code"]
    assert "is_palindrome" in result["final_code"]
    assert "count_vowels" in result["final_code"]


def test_sdd_engine_retry_limit():
    """Verifies that SDDHarnessEngine terminates cleanly when tests cannot pass."""
    impossible_tests = """
def test_impossible():
    assert False, "Forced failure to verify retry bounds"
"""
    client = AgentModelClient(backend="mock")
    engine = SDDHarnessEngine(client=client, max_retries=2)
    result = engine.run_cycle(SAMPLE_SPECIFICATION, impossible_tests)
    assert result["success"] is False
    assert result["attempts"] == 3  # Initial attempt + 2 retries
    assert result["last_error"] is not None
    assert "Forced failure" in result["last_error"]


def test_dual_backend_fallback_on_unreachable():
    """Verifies graceful fallback when an invalid endpoint or missing key is invoked."""
    client = AgentModelClient(backend="gemini")
    # If no key set, should gracefully fall back to mock
    resp = client.query("system", "Generate the implementation code for module candidate_module.py")
    assert "def reverse_words" in resp
