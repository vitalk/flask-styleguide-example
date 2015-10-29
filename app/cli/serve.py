#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
    app.cli.serve
    ~~~~~~~~~~~~~

    Serve application.

    :copyright: (c) 2015 by Vital Kudzelka <vital.kudzelka@gmail.com>
    :license: MIT
"""
from . import command


class run(command):
    """Serve application."""

    description = "run the application on a local development server"

    user_options = [
        ('debug', 'd',
         'Enable debugging of the application'),
        ('no-debug', 'D',
         "Disable debugging of the application"),
        ('use-reloader', 'r',
         'Enable live reload of the application'),
        ('no-use-reloader', 'R',
         'Disable live reload of the application'),
        ('host=', 'h',
         'The hostname to which application listen on'),
        ('port=', 'p',
         'The port of the web server'),
    ]

    def run(self):
        app = self.create_app()
        app.run(debug=self.debug,
                host=self.host,
                port=self.port,
                use_debugger=self.debug,
                use_reloader=self.use_reloader)

    def initialize_options(self):
        self.debug = False
        self.no_debug = None
        self.use_reloader = None
        self.no_use_reloader = None
        self.host = '127.0.0.1'
        self.port = 5000

    def finalize_options(self):
        if self.debug is None:
            if self.no_debug:
                self.debug = False

        if self.use_reloader is None:
            if self.no_use_reloader:
                self.use_reloader = False
            else:
                self.use_reloader = self.debug

        if self.port:
            try:
                self.port = int(self.port)
            except ValueError:
                self.port = None
