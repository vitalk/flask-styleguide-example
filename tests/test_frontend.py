#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pytest

from flask import url_for


class TestFrontend:

    def test_frontend_access(self, client):
        res = client.get(url_for('frontend.index'))
        assert res.status_code == 200

    def test_frontend_render(self, client):
        res = client.get(url_for('frontend.index'))
        assert 'Welcome' in res.data