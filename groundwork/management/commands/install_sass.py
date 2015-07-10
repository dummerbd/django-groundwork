"""
install_sass.py - custom command to install LibSass and SassC.
"""
import os

from django.core.management.base import BaseCommand, CommandError


BASE_DIR = os.path.dirname(os.path.abspath(__file__), '../../..')
LIBSASS_DIR = os.path.join(BASE_DIR, 'libs/libsass')
SASSC_DIR = os.path.join(BASE_DIR, 'libs/sassc')


class Command(BaseCommand):
    help = 'Install the LibSass and Sass libraries'

    def _print_lines(self, prefix, fd):
        line = fd.readline()
        while line:
            self.stdout.write(prefix, line.rstrip('\n'))
            line = fd.readline()

    def handle(self, *args, **options):
        w = self.stdout.write

        w('Building LibSass (this can take a while)')
        os.chdir(LIBSASS_DIR)
        fd = os.popen('make')
        print_lines('libsass:\t', fd)
        if fd.close():
            w('\nError encountered building LibSass')
            os.exit(1)


        w('Building SassC')
        os.chdir(SASSC_DIR)
        os.environ['SASS_LIBSASS_PATH'] = LIBSASS_DIR
        fd = os.popen('make')
        print_lines('sassc:\t', fd)
        if fd.close():
            w('\nError encountered building SassC')


        w('Copying SassC executable')
        os.chdir(BASE_DIR)
        try:
            os.mkdir('bin')
        except:
            pass
        os.symlink(os.path.join(SASSC_DIR, 'bin/sassc'), 'bin/sassc')
        w('Done')
