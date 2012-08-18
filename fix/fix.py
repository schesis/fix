"""Decorators."""

from functools import wraps


def fixture(create_fixture, **kwargs):
    """Decorate a callable with a fixture."""
    context = {}
    fixt = create_fixture(context, **kwargs)
    if isinstance(fixt, tuple):
        setup, teardown = fixt
    else:
        setup = fixt
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
