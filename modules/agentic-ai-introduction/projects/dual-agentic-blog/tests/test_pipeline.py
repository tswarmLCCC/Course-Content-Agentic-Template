"""Tests for pipeline coordinator and mock provider."""

import pytest
from app.config import AppConfig
from app.providers.mock_provider import MockProvider
from app.coordinator import PipelineCoordinator


def test_coordinator_mock_execution():
    config = AppConfig(provider="mock", max_iterations=3)
    provider = MockProvider()
    coordinator = PipelineCoordinator(config=config, provider=provider)

    state = coordinator.run("Testing Vector Search")
    assert state.final_status == "PASSED"
    assert state.total_iterations == 2
    assert len(state.draft_history) == 2
    assert state.validation_reports[0].passed is False
    assert state.validation_reports[1].passed is True
