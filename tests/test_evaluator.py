"""
Tests for the evaluator module.

This module provides comprehensive tests for the evaluation logic of MCP-Reflect.
"""

from collections.abc import Sequence

import pytest

from mcp_reflect.evaluator import (
    _build_evaluation_prompt,
    _parse_evaluation_response,
    evaluate_response,
)
from mcp_reflect.models import (
    DimensionScore,
    EvaluationDimension,
    ReflectionInput,
    ReflectionResult,
)


class TestEvaluationPromptBuilder:
    """Tests for the evaluation prompt builder function."""

    def test_basic_prompt_generation(self) -> None:
        """Verify basic prompt generation with minimal input."""
        input_data = ReflectionInput(response="This is a test response")
        prompt = _build_evaluation_prompt(input_data)

        assert "Evaluate and improve the following model response" in prompt
        assert "RESPONSE TO EVALUATE:\nThis is a test response" in prompt
        assert "provide a comprehensive evaluation" in prompt.lower()

    def test_prompt_with_query(self) -> None:
        """Verify prompt includes query when provided."""
        input_data = ReflectionInput(response="This is a test response", query="What is the test question?")
        prompt = _build_evaluation_prompt(input_data)

        assert "ORIGINAL QUERY:\nWhat is the test question?" in prompt

    def test_prompt_with_focus_dimensions(self) -> None:
        """Verify prompt includes only specified dimensions when provided."""
        input_data = ReflectionInput(
            response="This is a test response",
            focus_dimensions=[
                EvaluationDimension.ACCURACY,
                EvaluationDimension.CLARITY,
            ],
        )
        prompt = _build_evaluation_prompt(input_data)

        assert "- Accuracy" in prompt
        assert "- Clarity" in prompt
        assert "- Completeness" not in prompt

    def test_prompt_with_improvement_instructions(self) -> None:
        """Verify prompt includes improvement instructions when provided."""
        input_data = ReflectionInput(
            response="This is a test response",
            improvement_prompt="Focus on making it more concise",
        )
        prompt = _build_evaluation_prompt(input_data)

        assert "Additional improvement instructions: Focus on making it more concise" in prompt


@pytest.mark.asyncio
class TestResponseParser:
    """Tests for the evaluation response parser."""

    async def test_parse_valid_evaluation(self) -> None:
        """Test parsing a valid evaluation response."""
        raw_evaluation = (
            "EVALUATION:\n\n"
            "ACCURACY: 7/10\n"
            "Reasoning: The response is mostly accurate.\n"
            "Improvement: Add sources for claims.\n\n"
            "CLARITY: 8/10\n"
            "Reasoning: The explanation is clear.\n"
            "Improvement: Add headings for structure.\n\n"
            "OVERALL ASSESSMENT:\n"
            "Generally good response with minor issues.\n\n"
            "IMPROVED RESPONSE:\n"
            "This is an improved test response."
        )

        result = await _parse_evaluation_response(raw_evaluation)

        assert isinstance(result, ReflectionResult)
        assert result.original_response == raw_evaluation
        assert result.improved_response == "This is an improved test response."
        assert "Generally good response with minor issues." in result.overall_assessment
        assert len(result.scores) >= 2

        # Verify dimension scores
        accuracy_scores = [s for s in result.scores if s.dimension == EvaluationDimension.ACCURACY]
        assert len(accuracy_scores) == 1
        assert accuracy_scores[0].score == 7.0
        assert "Add sources" in accuracy_scores[0].improvement_suggestion

    async def test_parse_invalid_evaluation(self) -> None:
        """Test parsing an invalid evaluation response."""
        invalid_evaluation = "This is not a properly formatted evaluation."

        with pytest.raises(ValueError):
            await _parse_evaluation_response(invalid_evaluation)


@pytest.mark.asyncio
class TestEvaluator:
    """Tests for the complete evaluation process."""

    async def test_evaluate_response_structure(self) -> None:
        """Test that evaluate_response returns a properly structured result."""
        input_data = ReflectionInput(response="Test response to evaluate")

        result = await evaluate_response(input_data)

        assert isinstance(result, ReflectionResult)
        assert result.original_response is not None
        assert result.improved_response is not None
        assert isinstance(result.scores, Sequence)
        assert all(isinstance(s, DimensionScore) for s in result.scores)
        assert result.overall_assessment is not None
