"""
build_sass.py - builds sass project.
"""
import os

from django.core.management.base import BaseCommand

from .settings import get_setting


class Command(BaseCommand):
    help = 'Build SASS project'

    def handle(self, *args, **options):
        cmd = '{exec} --style {style} --load-path {path} {app} {out}'.format(
            exec=get_setting('sassc_executable'),
            style=get_setting('sass_style'),
            path=get_setting('foundation_path'),
            app=get_setting('sass_app'),
            out=get_setting('sass_output')
        )
        os.execl(cmd)
