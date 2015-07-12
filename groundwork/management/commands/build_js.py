"""
build_js.py - builds js project.
"""
import os
import sys

from django.core.management.base import BaseCommand

from groundwork.tools import build_js_project, ToolFailureError
from groundwork.settings import get_setting


class Command(BaseCommand):
    help = 'Build Foundation JS project'

    def handle(self, *args, **options):
        write = self.stdout.write

        write('From:       ' + get_setting('foundation_js_path'))
        try:
            build_js_project(readline=write)
        except ToolFailureError as e:
            write('Failed on command: ' + e.command)
            sys.exit(1)

        write('Output:     ' + get_setting('js_output'))
        write('Min Output: ' + get_setting('js_min_output'))
        write('Done')
