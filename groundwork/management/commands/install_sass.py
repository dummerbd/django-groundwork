"""
install_sass.py - custom command to install LibSass and SassC.
"""
import sys
import os

from django.core.management.base import BaseCommand

from groundwork.tools import install_sassc, ToolFailureError


class Command(BaseCommand):
    help = 'Install the LibSass and Sass libraries'

    def handle(self, *args, **options):
        write = self.stdout.write

        write('Building LibSass (this can take a while)')
        try:
            install_sassc(readline=write)
        except ToolFailureError as e:
            write('Failed on command: ' + e.command)
            sys.exit(1)

        write('Done')
