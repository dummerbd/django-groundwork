"""
settings.py - configuration options for groundwork.
"""
import os
from os import path

from django.conf import settings


BASE_DIR = path.abspath(path.join(path.dirname(path.abspath(__file__)), '..'))


DEFAULTS = {
    'GROUNDWORK_COMPONENTS':
        'all',

    'GROUNDWORK_SASSC_EXECUTABLE':
        path.join(BASE_DIR, 'libs/sassc/bin/sassc'),

    'GROUNDWORK_FOUNDATION_SASS_PATH':
        path.join(BASE_DIR, 'libs/foundation/scss'),

    'GROUNDWORK_FOUNDATION_JS_PATH':
        path.join(BASE_DIR, 'libs/foundation/js/foundation'),

    'GROUNDWORK_SASS_APP':
        path.join(BASE_DIR, 'groundwork/scss/default.scss'),

    'GROUNDWORK_SASS_INCLUDE_PATHS':
        [],

    'GROUNDWORK_SASS_OUTPUT':
        path.join(settings.STATIC_ROOT, 'css/foundation.css'),

    'GROUNDWORK_SASS_MIN_OUTPUT':
        path.join(settings.STATIC_ROOT, 'css/foundation.min.css'),

    'GROUNDWORK_JS_OUTPUT':
        path.join(settings.STATIC_ROOT, 'js/foundation.js'),

    'GROUNDWORK_JS_MIN_OUTPUT':
        path.join(settings.STATIC_ROOT, 'js/foundation.min.js')
}


def get_setting(name):
    """
    Get a defined setting value.
    """
    name = 'GROUNDWORK_' + name.upper()
    if hasattr(settings, name):
        return getattr(settings, name)
    return DEFAULTS[name]
