"""Tests for Pydantic data schemas."""

import pytest
from app.schemas import SectionPlan, BlogPlan, ValidationReport, AgentTraceStep, PipelineRunState


def test_blog_plan_schema():
    plan = BlogPlan(
        title="Testing Title",
        target_audience="Developers",
        total_target_words=250,
        sections=[
            SectionPlan(heading="Sec 1", key_points=["Point A"], target_words=100),
            SectionPlan(heading="Sec 2", key_points=["Point B"], target_words=150),
        ]
    )
    schema = BlogPlan.model_json_schema()
    assert "title" in schema["properties"]
    assert len(plan.sections) == 2


def test_validation_report_schema():
    report = ValidationReport(
        passed=True,
        overall_score=95,
        word_count_actual=240,
        word_count_status="OK",
        missing_sections=[],
        critiques=[],
        actionable_feedback=[]
    )
    assert report.passed is True
    assert report.overall_score == 95
