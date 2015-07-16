"""
components.py - contains definitions for Foundation components.
"""
from os import path
from functools import reduce

from groundwork.settings import get_setting


BASE_DIR = path.abspath(path.join(path.dirname(path.abspath(__file__)), '..'))


class BaseComponent:
    """
    Base component.
    """
    def __init__(self, js=[], sass=[], default=True):
        """
        `js` and `sass` should be a list of names such as `accordion`, or `tab`
        that can be formed with the path settings.
        """
        self.root = path.join(BASE_DIR, 'libs')
        self.js = js
        self.sass = sass
        self.default = default

    @property
    def js_files(self):
        return [path.join(self.root, '%s.js' % name) for name in self.js]

    @property
    def sass_imports(self):
        return self.sass


class Component(BaseComponent):
    """
    Foundation component, really just a pairing of JS and SASS files.
    """
    @property
    def js_files(self):
        root = get_setting('foundation_js_path')
        return [path.join(root, 'foundation.%s.js' % name) for name in self.js]

    @property
    def sass_imports(self):
        return['foundation/components/%s' % name for name in self.sass]


COMPONENTS = {
    'fastclick':
        BaseComponent(js=['fastclick/lib/fastclick'], default=False),

    'jquery':
        BaseComponent(js=['jquery/dist/jquery']),

    'jquery-placeholder':
        BaseComponent(js=['jquery-placeholder/jquery.placeholder'], default=False),

    'jquery-cookie':
        BaseComponent(js=['jquery.cookie/jquery.cookie'], default=False),

    'modernizr':
        BaseComponent(js=['modernizr/modernizr'], default=False),

    'modernizr-slim':
        BaseComponent(js=['modernizr-slim/modernizr.custom']),

    'accordion':
        Component(js=['accordion'], sass=['accordion']),

    'alert':
        Component(js=['alert'], sass=['alert-boxes']),

    'abide':
        Component(js=['abide']),

    'block-grid':
        Component(sass=['block-grid']),

    'breadcrumbs':
        Component(sass=['breadcrumbs']),

    'buttons':
        Component(sass=['buttons', 'button-groups', 'split-buttons']),

    'clearing':
        Component(js=['clearing'], sass=['clearing']),

    'dropdown':
        Component(js=['dropdown'], sass=['dropdown', 'dropdown-buttons']),

    'equalizer':
        Component(js=['equalizer']),

    'flex-video':
        Component(sass=['flex-video']),

    'forms':
        Component(sass=['forms']),

    'grid':
        Component(sass=['grid']),

    'inline-lists':
        Component(sass=['inline-lists']),

    'interchange':
        Component(js=['interchange']),

    'joyride':
        Component(js=['joyride'], sass=['joyride']),

    'keystrokes':
        Component(sass=['keystrokes']),

    'labels':
        Component(sass=['labels']),

    'magellan':
        Component(js=['magellan'], sass=['magellan']),

    'offcanvas':
        Component(js=['offcanvas'], sass=['offcanvas']),

    'orbit':
        Component(js=['orbit'], sass=['orbit']),

    'pagination':
        Component(sass=['pagination']),

    'panels':
        Component(sass=['panels']),

    'pricing-tables':
        Component(sass=['pricing-tables']),

    'progress-bars':
        Component(sass=['progress-bars']),

    'nav':
        Component(sass=['side-nav', 'sub-nav']),

    'reveal':
        Component(js=['reveal'], sass=['reveal']),

    'slider':
        Component(js=['slider']),

    'switches':
        Component(sass=['switches']),

    'tables':
        Component(sass=['tables']),

    'tabs':
        Component(js=['tab'], sass=['tabs']),

    'thumbs':
        Component(sass=['thumbs']),

    'tooltips':
        Component(js=['tooltip'], sass=['tooltips']),

    'topbar':
        Component(js=['topbar'], sass=['top-bar']),

    'type':
        Component(sass=['type']),

    'visibility':
        Component(sass=['visibility'])
}


def flatten(lst):
    return reduce(lambda el, lst: el + lst, lst, [])


def _get_components():
    components = get_setting('components')
    if components == 'all':
        components = [k for k, c in COMPONENTS.items() if c.default]
    return components


def get_sass_imports():
    """
    Get a list of all the required SASS components.
    """
    imports = flatten(
        (c.sass_imports for n, c in COMPONENTS.items()
            if n in _get_components()))
    imports.sort()
    return imports


def get_js_files():
    """
    Get a list of all the required JS components.
    """
    files = flatten(
        (c.js_files for n, c in
            COMPONENTS.items() if n in _get_components()))
    files.sort()
    return files
