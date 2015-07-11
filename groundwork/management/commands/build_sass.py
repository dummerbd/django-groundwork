"""
build_sass.py - builds sass project.
"""
import os

from django.core.management.base import BaseCommand

from groundwork.tools import build_sass_project
from groundwork.settings import get_setting


class Command(BaseCommand):
    help = 'Build SASS project'

    def handle(self, *args, **options):
        write = self.stdout.write

        write('Project: ' + get_setting('sass_app'))
        try:
            build_sass_project(readline=write)
        except ToolFailureError as e:
            write('Failed on command: ' + e.command)
            sys.exit(1)

        write('Output:  ' + get_setting('sass_output'))
        write('Done')
