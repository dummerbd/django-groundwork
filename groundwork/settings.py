"""
settings.py - configuration options for groundwork.
"""
import os

from django.conf import settings


BASE_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..')

DEFAULTS = {
    'GROUNDWORK_SASSC_EXECUTABLE':
        os.path.join(BASE_DIR, 'bin/sassc'),

    'GROUNDWORK_SASS_APP':
        os.path.join(BASE_DIR, 'groundwork/scss/app.scss'),

    'GROUNDWORK_SASS_OUTPUT':
        os.path.join(settings.STATIC_ROOT  , 'css/app.min.css'),

    'GROUNDWORK_SASS_STYLE':
        'compressed',

    'GROUNDWORK_FOUNDATION_PATH':
        os.path.join(BASE_DIR, 'libs/foundation/scss')
}


def get_setting(name):
    """
    Get a defined setting value.
    """
    name = 'GROUNDWORK_' + name.upper()
    if hasattr(settings, name):
        return getattr(settings, name)
    return DEFAULTS[name]
