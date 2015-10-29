#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pytest

from app.app import create_app


@pytest.fixture(scope='session')
def app(request):
    options = {
        'TESTING': True,
        'DEBUG': True,
    }
    app = create_app(**options)

    return app
