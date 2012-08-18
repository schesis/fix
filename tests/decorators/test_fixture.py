"""Tests for the `fix.decorators.fixture` function."""

from types import FunctionType

from fix import fixture


def test_exists():
    """`fix.fixture` function exists"""
    assert isinstance(fixture, FunctionType)


def test_call():
    """`fix.fixture` function does something sensible"""

    def my_fixture(context):
        """Create a fixture that assigns "bar" to `context["foo"]`."""
        def setup():
            """Assign "bar" to `context["foo"]`."""
            context["foo"] = "bar"
        return setup

    @fixture(my_fixture)
    def case(context):
        """Return `context["foo"]`."""
        return context["foo"]

    assert case() == "bar"  # pylint: disable=E1120
