from __future__ import absolute_import
from werkzeug.utils import find_modules


def register_modules(app):
    for module in find_modules(__name__):
        app.register_blueprint(__import__(module, None, None, ['bp']).bp)
