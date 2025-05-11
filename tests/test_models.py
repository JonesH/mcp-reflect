"""
Tests for the models module.

This module tests the Pydantic models used for data validation.
"""

from typing import Any

import pytest
from pydantic import ValidationError

from mcp_reflect.models import (
    DimensionScore,
    EvaluationDimension,
    ReflectionInput,
    ReflectionResult,
)


class TestEvaluationDimension:
    """Tests for the EvaluationDimension enum."""

    def test_enum_values(self) -> None:
        """Verify all expected dimensions exist with correct values."""
        expected_dimensions = {
            "accuracy",
            "clarity",
            "completeness",
            "relevance",
            "coherence",
            "conciseness",
            "helpfulness",
            "reasoning",
            "safety",
        }

        actual_dimensions = {dim.value for dim in EvaluationDimension}

        assert actual_dimensions == expected_dimensions


class TestDimensionScore:
    """Tests for the DimensionScore model."""

    def test_valid_score(self) -> None:
        """Verify valid scores are accepted."""
        # Test boundary conditions and middle value
        valid_scores = [1.0, 5.5, 10.0]

        for score in valid_scores:
            dimension_score = DimensionScore(
                dimension=EvaluationDimension.ACCURACY,
                score=score,
                reasoning="Test reasoning",
                improvement_suggestion="Test suggestion",
            )
            assert dimension_score.score == score

    def test_invalid_scores(self) -> None:
        """Verify scores outside the valid range (1-10) are rejected."""
        invalid_scores = [0.9, 10.1, -1, 11]

        for score in invalid_scores:
            with pytest.raises(ValidationError):
                DimensionScore(
                    dimension=EvaluationDimension.ACCURACY,
                    score=score,
                    reasoning="Test reasoning",
                    improvement_suggestion="Test suggestion",
                )


class TestReflectionResult:
    """Tests for the ReflectionResult model."""

    def test_valid_result(self) -> None:
        """Verify a valid reflection result can be created."""
        scores = [
            DimensionScore(
                dimension=EvaluationDimension.ACCURACY,
                score=7.5,
                reasoning="Good accuracy",
                improvement_suggestion="Add references",
            ),
            DimensionScore(
                dimension=EvaluationDimension.CLARITY,
                score=8.0,
                reasoning="Clear explanation",
                improvement_suggestion="Add more examples",
            ),
        ]

        result = ReflectionResult(
            original_response="Original text",
            improved_response="Improved text",
            scores=scores,
            overall_assessment="Overall good response",
        )

        assert result.original_response == "Original text"
        assert result.improved_response == "Improved text"
        assert len(result.scores) == 2
        assert result.overall_assessment == "Overall good response"
        assert result.metadata is None

    def test_result_with_metadata(self) -> None:
        """Verify metadata can be included in the result."""
        scores = [
            DimensionScore(
                dimension=EvaluationDimension.ACCURACY,
                score=7.5,
                reasoning="Good accuracy",
                improvement_suggestion="Add references",
            )
        ]

        metadata: dict[str, Any] = {
            "processing_time": 0.35,
            "model_version": "test-1.0",
            "dimensions_analyzed": ["accuracy"],
        }

        result = ReflectionResult(
            original_response="Original text",
            improved_response="Improved text",
            scores=scores,
            overall_assessment="Good",
            metadata=metadata,
        )

        assert result.metadata is not None
        assert result.metadata["processing_time"] == 0.35
        assert result.metadata["model_version"] == "test-1.0"
        assert result.metadata["dimensions_analyzed"] == ["accuracy"]


class TestReflectionInput:
    """Tests for the ReflectionInput model."""

    def test_minimal_input(self) -> None:
        """Verify minimal input with only response works."""
        input_data = ReflectionInput(response="Test response")

        assert input_data.response == "Test response"
        assert input_data.query is None
        assert input_data.focus_dimensions is None
        assert input_data.improvement_prompt is None

    def test_complete_input(self) -> None:
        """Verify input with all fields works."""
        focus_dimensions = [EvaluationDimension.ACCURACY, EvaluationDimension.CLARITY]

        input_data = ReflectionInput(
            response="Test response",
            query="Test query",
            focus_dimensions=focus_dimensions,
            improvement_prompt="Make it better",
        )

        assert input_data.response == "Test response"
        assert input_data.query == "Test query"
        assert input_data.focus_dimensions is not None
        assert list(input_data.focus_dimensions) == focus_dimensions
        assert input_data.improvement_prompt == "Make it better"

    def test_empty_response_invalid(self) -> None:
        """Verify empty response is rejected."""
        with pytest.raises(ValidationError):
            ReflectionInput(response="")
