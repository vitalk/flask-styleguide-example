#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
    flaskapp.assets
    ~~~~~~~~~~~~~~~

    Application assets.

    :copyright: (c) 2015 by Vital Kudzelka <vital.kudzelka@gmail.com>
    :license: MIT
"""
import io
import os
from datetime import datetime

from flask import json
from flask.ext.assets import (
    Bundle,
    Environment,
)


def read_json(*parts):
    with io.open(os.path.join(*parts)) as f:
        return json.load(f)


# Load package metadata.
package = read_json(os.path.dirname(__file__), os.pardir, 'package.json')

# Create copyright placeholder at init time.
banner = ('/*! {name} {version} | (c) {year} {author} | http://opensource.org/licenses/{license}\n'
          ' */\n'.format(year=datetime.today().year, **package))


def copyright(input, out, **kwargs):
    """Write copyrights to output."""
    out.write(banner)
    out.write(input.read())


cssmain = Bundle(
    'stylesheets/main.less',
    debug=False,
    depends=('**/*.less'),
    filters=('less', 'cssmin', copyright),
    output='dist/main.%(version)s.css'
)

scripts = Bundle(
    'scripts/main.js',
    filters=('jsmin', copyright),
    output='dist/main.%(version)s.js'
)


assets = Environment()

assets.register('cssmain', cssmain)
assets.register('scripts', scripts)
