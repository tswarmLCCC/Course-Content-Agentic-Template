"""Tests for ReAct tools."""

import pytest
from app.tools import calculate_reading_metrics, verify_code_syntax, local_grounding_search


def test_calculate_reading_metrics():
    metrics = calculate_reading_metrics("Sentence one. Sentence two.")
    assert metrics["word_count"] == 4
    assert metrics["sentence_count"] == 2


def test_verify_code_syntax():
    valid = verify_code_syntax("x = 10\ny = 20\nprint(x + y)")
    assert valid["valid"] is True

    invalid = verify_code_syntax("def broken_func(:\n  pass")
    assert invalid["valid"] is False


def test_local_grounding_search():
    res = local_grounding_search("ReAct")
    assert res["match_count"] >= 1
