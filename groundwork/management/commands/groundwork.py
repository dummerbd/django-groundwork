"""
groundwork.py - groundwork management command.
"""
from django.core.management.base import BaseCommand

from groundwork import tools


class Command(BaseCommand):
    """
    Run various tasks for Groundwork.
    """
    tools = {
        'sass': tools.BuildSassTool,
        'js': tools.BuildJsTool,
        'build': tools.BuildTool,
        'watch': tools.WatchTool,
        'info': tools.InfoTool,
    }

    def add_arguments(self, parser):
        """
        Add extra arguments.
        """
        parser.add_argument('command', choices=self.tools.keys())

    def handle(self, *args, **options):
        """
        Run the command.
        """
        tool = self.tools[options['command']](stdout=self.stdout)
        tool.run()
