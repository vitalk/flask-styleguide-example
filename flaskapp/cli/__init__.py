#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
    flaskapp.cli
    ~~~~~~~~~~~~

    Command line interface for application.

    :copyright: (c) 2015 by Vital Kudzelka <vital.kudzelka@gmail.com>
    :license: MIT
"""
from setuptools import Command

from ..app import create_app


class command(Command):
    """Base class for application commands."""

    user_options = []

    def create_app(self, *args, **kwargs):
        """Some commands require application context to run. A handy way to
        access application instance.
        """
        return create_app(*args, **kwargs)

    def initialize_options(self):
        """Set defaults to command options."""
        pass

    def finalize_options(self):
        """Finalize command options."""
        pass


# Fix possible circular imports.
from . import (
    serve,
    test,
)
