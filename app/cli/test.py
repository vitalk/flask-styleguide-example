#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
    app.cli.test
    ~~~~~~~~~~~~

    Run test suite.

    :copyright: (c) 2015 by Vital Kudzelka <vital.kudzelka@gmail.com>
    :license: MIT
"""
import sys
from setuptools.command.test import test


class pytest(test):
    """Run test suite."""

    def run_tests(self):
        import pytest

        errno = pytest.main(self.test_args)
        sys.exit(errno)
