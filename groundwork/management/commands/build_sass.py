"""
build_sass.py - builds sass project.
"""
import os

from django.core.management.base import BaseCommand

from groundwork.settings import get_setting


class Command(BaseCommand):
    help = 'Build SASS project'

    def handle(self, *args, **options):
        output = get_setting('sass_output')
        try:
            os.makedirs(os.path.dirname(output))
        except:
            pass

        cmd = '{exec} --style {style} --load-path {path} {app} {out}'.format(
            exec=get_setting('sassc_executable'),
            style=get_setting('sass_style'),
            path=get_setting('foundation_path'),
            app=get_setting('sass_app'),
            out=output
        )
        
        fd = os.popen(cmd)
        line = fd.readline()
        while line:
            self.stdout.write(line)
            line = fd.readline()
        fd.close()

        self.stdout.write('Success\nOutput: ' + output)
