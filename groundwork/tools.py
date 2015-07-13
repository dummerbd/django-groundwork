"""
tools.py - common tasks for installing, configuring, and using external tools.
"""
import sys
import os
import re
from os import path
from tempfile import NamedTemporaryFile
from contextlib import contextmanager

import jsmin

from groundwork.settings import get_setting
from groundwork.components import get_sass_imports, get_js_files


BASE_DIR = path.abspath(path.join(path.dirname(path.abspath(__file__)), '..'))


class ToolFailureError(Exception):
    """
    Raised when a tool fails.
    """
    def __init__(self, exit_code, command, output):
        self.exit_code = exit_code
        self.command = command
        self.output = output


class Tool:
    def __init__(self, stdin=None, stdout=None):
        """
        `stdin` and `stdout` should be file-like objects with a `write` and
        `read` method.
        """
        self.stdin = stdin or sys.stdin
        self.read = self.stdin.read
        self.stdout = stdout or sys.stdout
        self.write = self.stdout.write

    def run(self, *args, **kwargs):
        raise NotImplementedError

    def info(self, label=None, msg=None):
        """
        Shortcut to write an info message to `stdout`.
        """
        label = label + ':' if label else ''
        self.write('%-15s%s' % (label, msg or ''))

    @contextmanager
    def change_dir(self, path):
        """
        Run commands in the specified directory.
        """
        old_path = os.getcwd()
        os.chdir(path)
        try:
            yield
        finally:
            os.chdir(old_path)

    def run_external_tool(self, command, in_dir=None, redirect_stderr=True):
        """
        Run a shell command.
        """
        in_dir = in_dir or BASE_DIR
        output = ''

        if redirect_stderr:
            command = command + ' 2>&1'

        with self.change_dir(in_dir):
            fd = os.popen(command)
            line = fd.readline()
            while line:
                output += line
                self.info(msg=line)
                line = fd.readline()

        exit_code = fd.close()
        if exit_code:
            raise ToolFailureError(exit_code, command, output)

        return output


class BuildSassTool(Tool):
    """
    Build the Sass project defined in the settings.
    """
    @contextmanager
    def app_file_path(self, imports):
        app_sass = '\n'.join(['@import "%s";' % name for name in imports])
        with NamedTemporaryFile('w+') as temp:
            temp.write(app_sass)
            temp.seek(0)
            yield temp.name

    def run(self, *args, **kwargs):
        self.info('Sass', 'building...')

        app_name = get_setting('sass_app')
        settings_name = get_setting('sass_settings')

        self.info('App', app_name)
        self.info('Settings', settings_name)

        output = get_setting('sass_output')
        min_output = get_setting('sass_min_output')
        try:
            os.makedirs(os.path.dirname(output))
            os.makedirs(os.path.dirname(min_output))
        except:
            pass

        include_paths = list(get_setting('sass_include_paths')) + [
            get_setting('foundation_sass_path')
        ]
        self.info('Paths')
        [self.info(msg=path) for path in include_paths]

        imports = [settings_name] + list(get_sass_imports()) + [app_name]
        includes = ' '.join(['--include-path %s' % path for path in include_paths])

        self.info('Output', output)
        with self.app_file_path(imports) as app_file:
            self.run_external_tool(
                'sassc --output-style expanded {includes} {app} {out}'.format(
                    includes=includes,
                    app=app_file,
                    out=output
            ))

        self.info('Min Output', min_output)
        self.run_external_tool(
            'sassc --output-style compressed {app} {out}'.format(
                app=output,
                out=min_output
        ))

        self.write('Done')


class BuildJsTool(Tool):
    """
    Build the Foundation Js library.
    """
    def run(self, *args, **kwargs):
        self.info('Js', 'building...')

        js_root = get_setting('foundation_js_path')
        main_js_file = os.path.join(js_root, 'foundation.js')
        self.info('Foundation Dir', js_root)

        output = get_setting('js_output')
        min_output = get_setting('js_min_output')
        try:
            os.makedirs(os.path.dirname(output))
            os.makedirs(os.path.dirname(min_output))
        except:
            pass

        self.info('Output', output)
        js_files = [main_js_file] + get_js_files()
        source = ''
        for path in js_files:
            with open(path, 'r') as src_file:
                source += src_file.read()

        with open(output, 'w+') as output_file:
            output_file.write(source)

        self.info('Min Output', min_output)
        compressed = jsmin.jsmin(source)
        with open(min_output, 'w+') as output_file:
            output_file.write(compressed)

        self.write('Done')


class BuildTool(Tool):
    """
    Build the Sass and Js projects.
    """
    def run(self, *args, **kwargs):
        sass_tool = BuildSassTool(self.stdin, self.stdout)
        js_tool = BuildJsTool(self.stdin, self.stdout)

        sass_tool.run(*args, **kwargs)
        js_tool.run(*args, **kwargs)


class WatchTool(Tool):
    """
    Watch for filesystem changes and build when needed.
    """
    pass