"""
build_sass.py - builds sass project.
"""
import os
import sys

from django.core.management.base import BaseCommand

from groundwork.tools import build_sass_project, ToolFailureError
from groundwork.settings import get_setting


class Command(BaseCommand):
    help = 'Build SASS project'

    def handle(self, *args, **options):
        write = self.stdout.write

        write('App:        ' + get_setting('sass_app'))
        write('Settings:   ' + get_setting('sass_settings'))
        write('Paths:')
        [write('            ' + path) for path in get_setting('sass_include_paths')]

        try:
            build_sass_project(readline=write)
        except ToolFailureError as e:
            write('Failed on command: ' + e.command)
            sys.exit(1)

        write('Output:     ' + get_setting('sass_output'))
        write('Min Output: ' + get_setting('sass_min_output'))
        write('Done')
