"""Tests for the `fix.decorators.fixture` function."""

from types import FunctionType

from fix import fixture


def test_exists():
    """`fix.fixture` function exists"""
    assert isinstance(fixture, FunctionType)


def test_call():
    """`fix.fixture` function is callable"""
    assert fixture() is None
