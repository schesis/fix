"""Tests for the `fix.fix.with_fixture` function."""

from types import FunctionType

from fix import with_fixture


def test_exists():
    """`fix.with_fixture` function exists"""
    assert isinstance(with_fixture, FunctionType)


def test_setup_only():
    """`@with_fixture()` handles fixtures which return one function"""

    def fixture(context):
        """Create a fixture that assigns "bar" to `context["foo"]`."""
        def setup():
            """Assign "bar" to `context["foo"]`."""
            context["foo"] = "bar"
        return setup

    @with_fixture(fixture)
    def case(context):
        """Return `context["foo"]`."""
        return context["foo"]

    assert case() == "bar"  # pylint: disable=E1120


def test_setup_teardown():
    """`@with_fixture()` handles fixtures which return a tuple of functions"""
    pseudoglobal = {}

    def fixture(context):
        """Create a fixture that assigns "bar" to `context["foo"]`."""

        def setup():
            """Assign "bar" to `context["foo"]`."""
            context["foo"] = "squee"

        def teardown():
            """Delete `context["foo"]`."""
            del context["foo"]
            pseudoglobal["teardown_context"] = context

        return setup, teardown

    @with_fixture(fixture)
    def case(context):
        """Return `context["foo"]`."""
        return context["foo"]

    assert case() == "squee"  # pylint: disable=E1120
    assert pseudoglobal["teardown_context"] == {}
