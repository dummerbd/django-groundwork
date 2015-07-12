"""
tools.py - common tasks for installing, configuring, and using external tools.
"""
import sys
import os
import re
from os import path
from contextlib import contextmanager

import jsmin

from groundwork.settings import get_setting
from groundwork.components import get_sass_imports, get_js_files


BASE_DIR = path.abspath(path.join(path.dirname(path.abspath(__file__)), '..'))
LIBSASS_DIR = path.join(BASE_DIR, 'libs/libsass')
SASSC_DIR = path.join(BASE_DIR, 'libs/sassc')


class ToolFailureError(Exception):
    """
    Raised when a tool fails.
    """
    def __init__(self, exit_code, command, output):
        self.exit_code = exit_code
        self.command = command
        self.output = output


@contextmanager
def change_dir(path):
    """
    Run commands in the specified directory.
    """
    old_path = os.getcwd()
    os.chdir(path)
    try:
        yield
    finally:
        os.chdir(old_path)


def run_external_tool(command, in_dir=None, readline=None, redirect_stderr=True):
    """
    Run a shell command.
    """
    in_dir = in_dir or BASE_DIR
    readline = readline or print
    output = ''

    if redirect_stderr:
        command = command + ' 2>&1'

    with change_dir(in_dir):
        fd = os.popen(command)
        line = fd.readline()
        while line:
            output += line
            readline(line)
            line = fd.readline()

    exit_code = fd.close()
    if exit_code:
        raise ToolFailureError(exit_code, command, output)

    return output


def install_libsass(readline=None):
    """
    The `LibSass` source code is included as a git submodule and must be built
    for `SassC`.
    """
    run_external_tool('make', LIBSASS_DIR, readline)


def install_sassc(readline=None):
    """
    The `SassC` source code is included as a git submodule. This installs the
    included `LibSass` library first.
    """
    install_libsass(readline)
    os.environ['SASS_LIBSASS_PATH'] = LIBSASS_DIR
    run_external_tool('make', SASSC_DIR, readline)


def build_sass_project(readline=None):
    """
    Build the SASS project defined in the settings.
    """
    output = get_setting('sass_output')
    min_output = get_setting('sass_min_output')
    try:
        os.makedirs(os.path.dirname(output))
        os.makedirs(os.path.dirname(min_output))
    except:
        pass

    app_file = get_setting('sass_app')
    app_name = re.match(r'^.*/(.*)\.scss$', app_file).groups(1)
    app_include_path = os.path.dirname(app_file)

    include_paths = list(get_setting('sass_include_paths')) + [
        get_setting('foundation_sass_path'), app_include_path]

    imports = get_sass_imports() + [app_name]
    app_input = '\n'.join(['@import "%s";' % name for name in imports])
    includes = ' '.join(['--load-path %s' % path for path in include_paths])

    sassc = get_setting('sassc_executable')
    cmd = 'echo \'{input}\' | {sassc} --style expanded {includes} --stdin {out}'.format(
        input=app_input,
        sassc=sassc,
        includes=includes,
        out=output
    )
    run_external_tool(cmd, readline=readline)

    cmd = '{sassc} --style compressed {app} {out}'.format(
        sassc=sassc,
        app=output,
        out=min_output
    )
    run_external_tool(cmd, readline=readline)


def build_js_project(readline=None):
    """
    Build the Foundation JS library.
    """
    js_root = get_setting('foundation_js_path')
    output = get_setting('js_output')
    min_output = get_setting('js_min_output')
    try:
        os.makedirs(os.path.dirname(output))
        os.makedirs(os.path.dirname(min_output))
    except:
        pass

    js_files = get_js_files()
    js_files.insert(0, os.path.join(js_root, 'foundation.js'))

    source = ''
    for path in js_files:
        with open(path, 'r') as src_file:
            source += src_file.read()

    with open(output, 'w+') as output_file:
        output_file.write(source)

    compressed = jsmin.jsmin(source)
    with open(min_output, 'w+') as output_file:
        output_file.write(compressed)
