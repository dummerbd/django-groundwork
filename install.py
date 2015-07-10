#!python
"""
install.py - simple install script that builds our libraries.
"""
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
LIBSASS_DIR = os.path.join(BASE_DIR, 'libs/libsass')
SASSC_DIR = os.path.join(BASE_DIR, 'libs/sassc')


def print_lines(prefix, fd):
    line = fd.readline()
    while line:
        print(prefix, line.rstrip('\n'))
        line = fd.readline()


print('Building LibSass (this can take a while)')
os.chdir(LIBSASS_DIR)
fd = os.popen('make')
print_lines('libsass:\t', fd)
if fd.close():
    print('\nError encountered building LibSass')
    os.exit(1)


print('Building SassC')
os.chdir(SASSC_DIR)
os.environ['SASS_LIBSASS_PATH'] = LIBSASS_DIR
fd = os.popen('make')
print_lines('sassc:\t', fd)
if fd.close():
    print('\nError encountered building SassC')


print('Copying SassC executable')
os.chdir(BASE_DIR)
try:
    os.mkdir('bin')
except:
    pass
os.symlink(os.path.join(SASSC_DIR, 'bin/sassc'), 'bin/sassc')
print('Done')
