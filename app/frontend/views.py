"""
    app.frontend.views
    ~~~~~~~~~~~~~~~~~~

    The application frontpage.

    :copyright: (c) 2015 by Vital Kudzelka <vital.kudzelka@gmail.com>
    :license: MIT
"""
from flask import (
    Blueprint,
    render_template,
)


frontend = Blueprint('frontend', __name__, static_folder='../static')


@frontend.route('/')
def index():
    return render_template('frontend/index.html')
