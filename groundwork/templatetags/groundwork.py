"""
groundwork.py - grounwork template tags.
"""
from django import template
from django.templatetags.static import static
from django.conf import settings

from groundwork.settings import get_setting


register = template.Library()


@register.simple_tag
def groundwork_js():
    """
    Render a script tag that links to the groundwork JS build.
    """
    path = 'js_min_static_path' if settings.DEBUG else 'js_static_path'
    url = static(get_setting(path))
    return '<script type="text/javascript" src="%s"></script>' % url


@register.simple_tag
def groundwork_css():
    """
    Render a style tag that links to the groundwork SASS build.
    """
    path = 'sass_min_static_path' if settings.DEBUG else 'sass_static_path'
    url = static(get_setting(path))
    return '<link rel="stylesheet" type="text/css" href="%s" />' % url
