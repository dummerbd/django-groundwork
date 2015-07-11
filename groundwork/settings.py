"""
settings.py - configuration options for groundwork.
"""
import os
from os import path

from django.conf import settings


BASE_DIR = path.abspath(path.join(path.dirname(path.abspath(__file__)), '..'))


DEFAULT_JS_COMPONENTS = [
    'abide', 'accordion', 'alert', 'clearing', 'dropdown', 'equalizer', 'interchange', 'joyride',
    'magellan', 'offcanvas', 'orbit', 'reveal', 'slider', 'tab', 'tooltip', 'topbar'
]


DEFAULTS = {
    'GROUNDWORK_SASSC_EXECUTABLE':
        path.join(BASE_DIR, 'libs/sassc/bin/sassc'),

    'GROUNDWORK_SASS_APP':
        path.join(BASE_DIR, 'groundwork/scss/app.scss'),

    'GROUNDWORK_FOUNDATION_SASS_PATH':
        path.join(BASE_DIR, 'libs/foundation/scss'),

    'GROUNDWORK_SASS_OUTPUT':
        path.join(settings.STATIC_ROOT, 'css/app.css'),

    'GROUNDWORK_SASS_MIN_OUTPUT':
        path.join(settings.STATIC_ROOT, 'css/app.min.css'),


    'GROUNDWORK_FOUNDATION_JS_PATH':
        path.join(BASE_DIR, 'libs/foundation/js/foundation'),

    'GROUNDWORK_JS_COMPONENTS':
        DEFAULT_JS_COMPONENTS,

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
