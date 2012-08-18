"""Simple test fixtures."""

from functools import wraps


def with_fixture(create_fixture, **kwargs):
    """Decorate a callable with a fixture."""
    context = {}
    fixture = create_fixture(context, **kwargs)
    if isinstance(fixture, tuple):
        setup, teardown = fixture
    else:
        setup = fixture
        teardown = lambda: None

    def wrap(func):
        """Wrap the callable."""
        @wraps(func)
        def call():
            """Call `setup` and `teardown` before and after `func`."""
            setup()
            result = func(context)
            teardown()
            return result
        return call

    return wrap
