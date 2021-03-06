#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
    app.extensions
    ~~~~~~~~~~~~~~

    Extensions module. Each extension is initialized in the app factory
    located in app.py.

    :copyright: (c) 2015 by Vital Kudzelka <vital.kudzelka@gmail.com>
    :license: MIT
"""
from flask_frozen import Freezer
freezer = Freezer()

from flask_styleguide import Styleguide
style_guide = Styleguide()
