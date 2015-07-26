"""
settings.py - configuration options for groundwork.
"""
from os import path

from django.conf import settings


BASE_DIR = path.abspath(path.join(path.dirname(path.abspath(__file__)), '..'))


DEFAULT_SETTINGS = {
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
        [path.join(BASE_DIR, 'scss'), path.join(BASE_DIR, 'libs/foundation-icon-fonts')],

    'GROUNDWORK_SASS_EXTRA_INCLUDE_PATHS':
        [],

    'GROUNDWORK_SASS_STATIC_PATH':
        'groundwork/css/foundation.css',

    'GROUNDWORK_SASS_MIN_STATIC_PATH':
        'groundwork/css/foundation.min.css',

    'GROUNDWORK_JS_STATIC_PATH':
        'groundwork/js/foundation.js',

    'GROUNDWORK_JS_MIN_STATIC_PATH':
        'groundwork/js/foundation.min.js',

    'GROUNDWORK_OUTPUT_ROOT_PATH':
        settings.STATIC_ROOT
}


def get_setting(name):
    """
    Get a defined setting value.
    """
    name = 'GROUNDWORK_' + name.upper()
    if hasattr(settings, name):
        return getattr(settings, name)
    return DEFAULT_SETTINGS[name]


if getattr(settings, 'GROUNDWORK_DISTRIBUTION_OUTPUT', False):
    output_root = path.join(BASE_DIR, 'groundwork/static')
else:
    output_root = get_setting('output_root_path')


def get_output_path(name):
    """
    For a path setting name, get the full path.
    """
    name += '_static_path'
    return path.join(output_root, get_setting(name))
