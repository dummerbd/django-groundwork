"""
groundwork.py - grounwork template tags.
"""
from django import template
from django.templatetags.static import static
from django.conf import settings

from groundwork.settings import get_setting


register = template.Library()


@register.simple_tag
def groundwork_js(minify=None):
    """
    Render a script tag that links to the groundwork Js build.

    An optional `minify` argument determines if this will include the minified
    or full source. By default, the full source is included when `DEBUG=True`
    and the minified source is included when `DEBUG=False`.
    """
    if minify is None:
        minify = not settings.DEBUG

    path = 'js_min_static_path' if minify else 'js_static_path'
    url = static(get_setting(path))
    return '<script type="text/javascript" src="%s"></script>' % url


@register.simple_tag
def groundwork_css(minify=None):
    """
    Render a style tag that links to the groundwork Sass build.

    An optional `minify` argument determines if this will include the minified
    or full source. By default, the full source is included when `DEBUG=True`
    and the minified source is included when `DEBUG=False`.
    """
    if minify is None:
        minify = not settings.DEBUG

    path = 'sass_min_static_path' if minify else 'sass_static_path'
    url = static(get_setting(path))
    return '<link rel="stylesheet" type="text/css" href="%s" />' % url
