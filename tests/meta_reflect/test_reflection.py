import pytest
from pydantic import ValidationError

from mcp_reflect import ReflectionStore
from mcp_reflect.server import reflection_store


class TestMetaReflection:
    """Tests for the meta-reflection functionality."""

    def test_reflection_creation(self) -> None:
        """Test creating a reflection and storing it."""
        # Create a fresh reflection store for testing
        store = ReflectionStore("TestStore")

        result = store.add_reflection(content="Testing the reflection mechanism", stage="problem", rtype="critical")

        assert result["ok"] is True
        assert "id" in result
        assert result["count"] == 1

    def test_reflection_sequence(self) -> None:
        """Test that reflections maintain proper sequence and references."""
        store = ReflectionStore("SequenceStore")

        # Add first reflection
        store.add_reflection(content="Initial problem statement", stage="problem", rtype="analytical")

        # Add second reflection that follows from the first
        store.add_reflection(
            content="Analysis of the problem",
            stage="analysis",
            rtype="critical",
            follows_from=[1],  # References the first reflection by sequence ID
        )

        # Get summary of all reflections
        summary = store.get_summary()

        assert len(summary) == 2
        assert summary[0]["seq"] == 1
        assert summary[1]["seq"] == 2
        assert summary[1]["follows_from"] == [1]

    def test_reset_functionality(self) -> None:
        """Test resetting the reflection store."""
        store = ReflectionStore("ResetStore")

        # Add a reflection
        store.add_reflection(content="This will be reset", stage="problem", rtype="creative")

        # Verify reflection was added
        assert len(store.get_summary()) == 1

        # Reset the store
        result = store.reset()

        # Verify store is empty and result is as expected
        assert len(store.get_summary()) == 0
        assert result["ok"] is True
        assert result["msg"] == "Reflection store reset"

    def test_global_reflection_store(self) -> None:
        """Test the global reflection_store instance."""
        # Clear any existing reflections
        reflection_store.reset()

        # Add a reflection
        result = reflection_store.add_reflection(
            content="Testing global store", stage="exploration", rtype="integrative"
        )

        # Verify result
        assert result["ok"] is True
        assert result["count"] == 1

        # Verify summary
        summary = reflection_store.get_summary()
        assert len(summary) == 1
        assert summary[0]["content"] == "Testing global store"
        assert summary[0]["stage"] == "exploration"
        assert summary[0]["rtype"] == "integrative"

    def test_invalid_inputs(self) -> None:
        """Test validation of invalid inputs."""
        store = ReflectionStore("ValidationStore")

        # Test empty content validation
        with pytest.raises(ValidationError):
            store.add_reflection("", "problem", "critical")

        # Test invalid stage
        with pytest.raises(ValueError):
            store.add_reflection("Valid content", "invalid_stage", "critical")

        # Test invalid reflection type
        with pytest.raises(ValueError):
            store.add_reflection("Valid content", "problem", "invalid_type")
