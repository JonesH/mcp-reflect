"""
Tests for the server module.

This module tests the MCP server implementation and tool definitions.
"""

from unittest.mock import AsyncMock, patch

import pytest

from mcp_reflect.models import (
    DimensionScore,
    EvaluationDimension,
    ReflectionResult,
)
from mcp_reflect.server import reflect, sequential_reflect


def create_mock_result(original: str, improved: str) -> ReflectionResult:
    """Create a mock reflection result for testing."""
    return ReflectionResult(
        original_response=original,
        improved_response=improved,
        scores=[
            DimensionScore(
                dimension=EvaluationDimension.ACCURACY,
                score=7.0,
                reasoning="Mock reasoning",
                improvement_suggestion="Mock suggestion",
            )
        ],
        overall_assessment="Mock assessment",
    )


@pytest.mark.asyncio
class TestReflectTool:
    """Tests for the reflect tool."""

    @patch("mcp_reflect.server.evaluate_response")
    async def test_reflect_basic(self, mock_evaluate: AsyncMock) -> None:
        """Test basic functionality of the reflect tool."""
        # Setup mock
        mock_result = create_mock_result(original="Original response", improved="Improved response")
        mock_evaluate.return_value = mock_result

        # Call function
        result = await reflect(response="Test response")

        # Verify result
        assert result == mock_result
        mock_evaluate.assert_called_once()
        call_arg = mock_evaluate.call_args[0][0]
        assert call_arg.response == "Test response"
        assert call_arg.query is None

    @patch("mcp_reflect.server.evaluate_response")
    async def test_reflect_with_all_params(self, mock_evaluate: AsyncMock) -> None:
        """Test reflect tool with all parameters specified."""
        # Setup mock
        mock_result = create_mock_result(original="Original response", improved="Improved response with focus")
        mock_evaluate.return_value = mock_result

        # Call function
        result = await reflect(
            response="Test response",
            query="Test query",
            focus_dimensions=[EvaluationDimension.ACCURACY, EvaluationDimension.CLARITY],
            improvement_prompt="Make it better",
        )

        # Verify result
        assert result == mock_result
        mock_evaluate.assert_called_once()
        call_arg = mock_evaluate.call_args[0][0]
        assert call_arg.response == "Test response"
        assert call_arg.query == "Test query"
        assert EvaluationDimension.ACCURACY in call_arg.focus_dimensions
        assert EvaluationDimension.CLARITY in call_arg.focus_dimensions
        assert call_arg.improvement_prompt == "Make it better"


@pytest.mark.asyncio
class TestSequentialReflectTool:
    """Tests for the sequential_reflect tool."""

    @patch("mcp_reflect.server.evaluate_response")
    async def test_sequential_independent_mode(self, mock_evaluate: AsyncMock) -> None:
        """Test sequential_reflect with independent mode."""
        # Setup mocks
        mock_results = [
            create_mock_result("Original 1", "Improved 1"),
            create_mock_result("Original 2", "Improved 2"),
        ]
        mock_evaluate.side_effect = mock_results

        # Call function
        results = await sequential_reflect(responses=["Response 1", "Response 2"], mode="independent")

        # Verify results
        assert len(results) == 2
        assert results[0].improved_response == "Improved 1"
        assert results[1].improved_response == "Improved 2"
        assert mock_evaluate.call_count == 2

    @patch("mcp_reflect.server.evaluate_response")
    async def test_sequential_iterative_mode(self, mock_evaluate: AsyncMock) -> None:
        """Test sequential_reflect with iterative mode."""
        # Setup mocks
        mock_results = [
            create_mock_result("Original", "Improved 1"),
            create_mock_result("Improved 1", "Improved 2"),
        ]
        mock_evaluate.side_effect = mock_results

        # Call function
        results = await sequential_reflect(
            responses=["Original", "Ignored"],
            mode="iterative",  # Second response ignored in iterative mode
        )

        # Verify results
        assert len(results) == 2
        assert results[0].improved_response == "Improved 1"
        assert results[1].improved_response == "Improved 2"
        assert mock_evaluate.call_count == 2

        # Verify second call uses improved response from first call
        second_call_arg = mock_evaluate.call_args_list[1][0][0]
        assert second_call_arg.response == "Improved 1"

    @patch("mcp_reflect.server.evaluate_response")
    async def test_sequential_comparative_mode(self, mock_evaluate: AsyncMock) -> None:
        """Test sequential_reflect with comparative mode."""
        # Setup mocks
        mock_results = [
            create_mock_result("Response 1", "Improved 1"),
            create_mock_result("Response 2", "Improved 2"),
        ]
        mock_evaluate.side_effect = mock_results

        # Call function
        results = await sequential_reflect(responses=["Response 1", "Response 2"], mode="comparative")

        # Verify results
        assert len(results) == 2
        assert results[0].improved_response == "Improved 1"
        assert results[1].improved_response == "Improved 2"
        assert mock_evaluate.call_count == 2

        # Verify improvement prompt mentions comparison
        for i in range(2):
            call_arg = mock_evaluate.call_args_list[i][0][0]
            assert "Compare" in call_arg.improvement_prompt
