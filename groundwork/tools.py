"""
tools.py - common tasks for installing, configuring, and using external tools.
"""
import sys
import os
import time
from os import path

from groundwork.settings import get_setting, get_output_path, DEFAULT_SETTINGS
from groundwork import components

try:
    from watchdog.observers import Observer
    from watchdog.events import FileSystemEventHandler as Handler
except ImportError:
    pass

try:
    import jsmin
except ImportError:
    pass

try:
    import sass
except ImportError:
    pass


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

    def get_sass_include_paths(self):
        """
        Get a list of file paths that contain Sass code.
        """
        paths = [get_setting('foundation_sass_path')]
        paths += list(get_setting('sass_include_paths'))
        paths += list(get_setting('sass_extra_include_paths'))
        return paths

    def get_js_files(self):
        """
        Get a list of the Js files to be built.
        """
        return components.get_js_files()

    def makedirs(self, *paths):
        for p in paths:
            os.makedirs(path.dirname(p), exist_ok=True)


class BuildSassTool(Tool):
    """
    Build the Sass project defined in the settings. This requires the `libsass`
    package.
    """
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.app = get_setting('sass_app')
        self.settings = get_setting('sass_settings')
        self.output = get_output_path('sass')
        self.min_output = get_output_path('sass_min')
        self.paths = self.get_sass_include_paths()
        self.imports = [self.settings] + components.get_sass_imports() + [self.app]

    def sass(self, compress=False):
        if not compress:
            raw_sass = '\n'.join(['@import "%s";' % name for name in self.imports])
            options = {
                'string': raw_sass, 'output_style': 'expanded', 'include_paths': self.paths
            }
        else:
            options = {'filename': self.output, 'output_style': 'compressed'}
        with open(self.min_output if compress else self.output, 'w+') as fd:
            try:
                fd.write(sass.compile(**options))
            except sass.CompileError as ce:
                msg = str(ce)
                self.stdout.write(msg[2:-2].replace(r'\n', '\n'))
                return False
        return True

    def run(self, *args, **kwargs):
        self.info('Sass', 'building...')
        self.info('App', self.app)
        self.info('Settings', self.settings)
        self.info('Paths')
        for p in self.paths:
            self.info(msg=p)
        self.makedirs(self.output, self.min_output)

        if not self.sass():
            return
        self.info('Output', self.output)

        if not self.sass(True):
            return
        self.info('Min Output', self.min_output)
        self.write('Done')


class BuildJsTool(Tool):
    """
    Build the Foundation Js library. This requies installing the `jsmin`
    package.
    """
    def run(self, *args, **kwargs):
        self.info('Js', 'building...')

        output = get_output_path('js')
        min_output = get_output_path('js_min')
        self.makedirs(output, min_output)

        self.info('Output', output)
        source = ''
        for p in self.get_js_files():
            with open(p, 'r') as src_file:
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
    Watch for filesystem changes and build when needed. This tool is optional
    and requires installing `watchdog`.
    """
    def __init__(self, *args, **kwargs):
        """
        Delegate building assets to the Js and Sass tools.
        """
        super().__init__(*args, **kwargs)
        self.js_tool = BuildJsTool(*args, **kwargs)
        self.sass_tool = BuildSassTool(*args, **kwargs)

    def _sass(self, event):
        self.sass_tool.run()

    def _js(self, event):
        self.js_tool.run()

    def run(self, *args, **kwargs):
        sass_paths = self.get_sass_include_paths()
        js_paths = [get_setting('foundation_js_path')]

        sass_handler = type('Handler', (Handler,), {'on_modified': self._sass})()
        js_handler = type('Handler', (Handler,), {'on_modified': self._js})()
        observer = Observer()

        for p in sass_paths:
            observer.schedule(sass_handler, p, recursive=True)
        for p in js_paths:
            observer.schedule(js_handler, p, recursive=True)

        self.write('Watching...')
        observer.start()
        try:
            while True:
                time.sleep(1)
        except:
            observer.stop()
        observer.join()


class InfoTool(Tool):
    """
    Lists information about the groundwork installation.
    """
    def run(self):
        self.write('Available Tools:')
        self.info(
            'sass',
            'compile and compress the Foundation Sass project into Css (requires libsass)')
        self.info(
            'js',
            'compile and compress the Foundation Js project (requires jsmin)')
        self.info(
            'build',
            'runs both the sass and js tools')
        self.info(
            'watch',
            'runs a filesystem watcher that automatically runs the Js or Sass tool when a file changes')

        self.write('Current Groundwork Configration:')
        for k, v in DEFAULT_SETTINGS.items():
            self.write('  %s\n    - %s' % (k, v))

        self.write('Available Components:')
        for n, c in components.COMPONENTS.items():
            self.write('  %s' % n)
            if c.sass:
                self.write('    - sass: %s' % ', '.join(c.sass))
            if c.js:
                self.write('    - js  : %s' % ', '.join(c.js))
