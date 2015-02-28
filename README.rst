
==========================
fix - Simple test fixtures
==========================

:Author: Zero Piraeus
:Contact: z@etiol.net

**fix** is a simple library to assist with the creation of fixtures for test
functions, methods etc. It provides one decorator, ``with_fixture``, which
allows you to attach ``setup()`` and ``teardown()`` functions to the decorated
callable, and access information defined in the fixture from within the test
function.

**fix** was written for use with nose_, but doesn't depend on it, and may also
prove useful with other test frameworks.

.. _nose: http://nose.readthedocs.org/en/latest/index.html


Examples
--------

Here's a basic example with setup but no teardown::

    from fix import with_fixture

    def setup_only(context):

        def setup():
            """Add something to the context."""
            assert context == {}
            context.squee = "kapow"

        return setup

    @with_fixture(setup_only)
    def case(context):
        assert context == {"squee": "kapow"}

... and here's a rather more involved one that creates some temporary files to
work with, then deletes them during teardown::

    import os
    import shutil
    import tempfile

    from fix import with_fixture

    def external(context, files=3):

        def setup():
            context.temp_dir = tempfile.mkdtemp()
            context.filenames = ["file_%03d" % i for i in range(files)]
            for filename in context.filenames:
                with open(os.path.join(context.temp_dir, filename), "w") as f:
                    f.write("This is the file %r.\n" % filename)

        def teardown():
            shutil.rmtree(context.temp_dir)

        return setup, teardown

    @with_fixture(external, files=5)
    def check_files(context):
        present = 0
        absent = 0
        for filename in context.filenames:
            if os.path.exists(os.path.join(context.temp_dir, filename)):
                present += 1
            else:
                absent += 1
        return context.temp_dir, present, absent

    temp_dir, present, absent = check_files()
    assert not os.path.exists(temp_dir)
    assert present == 5
    assert absent == 0


Installation
------------

This should do the trick::

    pip install fix


Licence
---------

**fix** is released under the GNU General Public License (version 3 or later),
a copy of which is included with this distribution in the file **COPYING**.

