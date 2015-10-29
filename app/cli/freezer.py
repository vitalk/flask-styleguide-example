#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
    app.cli.freezer
    ~~~~~~~~~~~~~~~

    Freeze application.

    :copyright: (c) 2015 by Vital Kudzelka <vital.kudzelka@gmail.com>
    :license: MIT
"""
from . import command


class freeze(command):
    """Freeze application."""

    description = "freeze application"

    def run(self):
        from ..extensions import freezer
        app = self.create_app()
        freezer.freeze()
