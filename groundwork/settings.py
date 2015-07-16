"""
settings.py - configuration options for groundwork.
"""
import os
from os import path

from django.conf import settings


BASE_DIR = path.abspath(path.join(path.dirname(path.abspath(__file__)), '..'))


if settings.GROUNDWORK_DISTRIBUTION_OUTPUT:
    output_root = path.join(BASE_DIR, 'groundwork/static/groundwork')
else:
    output_root = settings.STATIC_ROOT


DEFAULTS = {
    'GROUNDWORK_COMPONENTS':
        'all',

    'GROUNDWORK_FOUNDATION_SASS_PATH':
        path.join(BASE_DIR, 'libs/foundation/scss'),

    'GROUNDWORK_FOUNDATION_JS_PATH':
        path.join(BASE_DIR, 'libs/foundation/js/foundation'),

    'GROUNDWORK_SASS_SETTINGS':
        'default_settings',

    'GROUNDWORK_SASS_APP':
        'default_app',

    'GROUNDWORK_SASS_INCLUDE_PATHS':
        [path.join(BASE_DIR, 'scss')],

    'GROUNDWORK_SASS_OUTPUT':
        path.join(output_root, 'css/foundation.css'),

    'GROUNDWORK_SASS_MIN_OUTPUT':
        path.join(output_root, 'css/foundation.min.css'),

    'GROUNDWORK_JS_OUTPUT':
        path.join(output_root, 'js/foundation.js'),

    'GROUNDWORK_JS_MIN_OUTPUT':
        path.join(output_root, 'js/foundation.min.js'),
}


def get_setting(name):
    """
    Get a defined setting value.
    """
    name = 'GROUNDWORK_' + name.upper()
    if hasattr(settings, name):
        return getattr(settings, name)
    return DEFAULTS[name]
