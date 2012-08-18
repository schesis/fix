"""Tests for the `fix.fix.with_fixture` function."""

from types import FunctionType

from fix import with_fixture


def test_exists():
    """`fix.with_fixture` function exists"""
    assert isinstance(with_fixture, FunctionType)


def test_call():
    """`fix.with_fixture` function does something sensible"""

    def my_fixture(context):
        """Create a fixture that assigns "bar" to `context["foo"]`."""
        def setup():
            """Assign "bar" to `context["foo"]`."""
            context["foo"] = "bar"
        return setup

    @with_fixture(my_fixture)
    def case(context):
        """Return `context["foo"]`."""
        return context["foo"]

    assert case() == "bar"  # pylint: disable=E1120
