#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
    app.app
    ~~~~~~~

    Example of living Styleguide made with Flask-Styleguide.

    :copyright: (c) 2015 by Vital Kudzelka <vital.kudzelka@gmail.com>
    :license: MIT
"""
from flask import Flask

from .assets import assets
from .extensions import (
    freezer,
    style_guide
)


def create_app(config='dev.cfg', **options):
    app = Flask(__name__)

    configure_application(app, config, options)
    configure_extensions(app)
    configure_blueprints(app)

    return app


def configure_application(app, config, options):
    """Configure application."""
    app.config.from_pyfile(config)
    app.config.from_envvar('APP_CONFIG', silent=True)
    app.config.update(options)
    return None


def configure_extensions(app):
    """Register extensions to application."""
    assets.init_app(app)
    freezer.init_app(app)
    style_guide.init_app(app)
    return None


def configure_blueprints(app):
    """Configure application blueprints."""
    from .frontend import frontend
    app.register_blueprint(frontend)

    return None
