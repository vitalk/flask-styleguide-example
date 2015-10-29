#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
    app.compat
    ~~~~~~~~~~

    Python 2/3 compatibility module.

    :copyright: (c) 2015 by Vital Kudzelka <vital.kudzelka@gmail.com>
    :license: MIT
"""
import sys


PY2 = sys.version_info[0] == 2


if PY2:
    text_type = unicode
    binary_type = str
    string_types = basestring,
    unicode = unicode
    basestring = basestring
else:
    text_type = str
    binary_type = bytes
    string_types = str,
    unicode = str
    basestring = (str, bytes)
