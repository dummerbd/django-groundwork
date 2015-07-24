"""
components.py - contains definitions for Foundation components.
"""
from os import path
from functools import reduce
from collections import OrderedDict

from groundwork.settings import get_setting


BASE_DIR = path.abspath(path.join(path.dirname(path.abspath(__file__)), '..'))


class BaseComponent:
    """
    Base component.
    """
    js_path = path.join(BASE_DIR, 'libs')
    sass_prefix = ''

    def __init__(self, js=[], sass=[], default=True):
        """
        `js` and `sass` should be a list of names such as `accordion`, or `tab`
        that can be formed with the path settings.
        """
        self.js = js
        self.sass = sass
        self.default = default

    @property
    def js_files(self):
        return [path.join(self.js_path, '%s.js' % name) for name in self.js]

    @property
    def sass_imports(self):
        return ['%s%s' % (self.sass_prefix, name) for name in self.sass]


class Component(BaseComponent):
    """
    Foundation component.
    """
    js_path = get_setting('foundation_js_path')
    sass_prefix = 'foundation/components/'


# The ordering of these components matters since this will be the same ordering
# in the built JS and CSS files.
COMPONENTS = OrderedDict()

COMPONENTS['modernizr'] = BaseComponent(
    js=['modernizr/modernizr'], default=False
)
COMPONENTS['modernizr-slim'] = BaseComponent(
    js=['modernizr-slim/modernizr.custom']
)
COMPONENTS['jquery'] = BaseComponent(
    js=['jquery/dist/jquery']
)
COMPONENTS['jquery-placeholder'] = BaseComponent(
    js=['jquery-placeholder/jquery.placeholder'], default=False
)
COMPONENTS['jquery-cookie'] = BaseComponent(
    js=['jquery.cookie/jquery.cookie'], default=False
)
COMPONENTS['fastclick'] = BaseComponent(
    js=['fastclick/lib/fastclick'], default=False
)
COMPONENTS['foundation'] = Component(
    js=['foundation']
)
COMPONENTS['accordion'] = Component(
    js=['foundation.accordion'], sass=['accordion']
)
COMPONENTS['alert'] = Component(
    js=['foundation.alert'], sass=['alert-boxes']
)
COMPONENTS['abide'] = Component(
    js=['foundation.abide']
)
COMPONENTS['block-grid'] = Component(
    sass=['block-grid']
)
COMPONENTS['breadcrumbs'] = Component(
    sass=['breadcrumbs']
)
COMPONENTS['buttons'] = Component(
    sass=['buttons', 'button-groups', 'split-buttons']
)
COMPONENTS['clearing'] = Component(
    js=['foundation.clearing'], sass=['clearing']
)
COMPONENTS['dropdown'] = Component(
    js=['foundation.dropdown'], sass=['dropdown', 'dropdown-buttons']
)
COMPONENTS['equalizer'] = Component(
    js=['foundation.equalizer']
)
COMPONENTS['flex-video'] = Component(
    sass=['flex-video']
)
COMPONENTS['forms'] = Component(
    sass=['forms']
)
COMPONENTS['grid'] = Component(
    sass=['grid']
)
COMPONENTS['inline-lists'] = Component(
    sass=['inline-lists']
)
COMPONENTS['interchange'] = Component(
    js=['foundation.interchange']
)
COMPONENTS['joyride'] = Component(
    js=['foundation.joyride'], sass=['joyride']
)
COMPONENTS['keystrokes'] = Component(
    sass=['keystrokes']
)
COMPONENTS['labels'] = Component(
    sass=['labels']
)
COMPONENTS['magellan'] = Component(
    js=['foundation.magellan'], sass=['magellan']
)
COMPONENTS['offcanvas'] = Component(
    js=['foundation.offcanvas'], sass=['offcanvas']
)
COMPONENTS['orbit'] = Component(
    js=['foundation.orbit'], sass=['orbit']
)
COMPONENTS['pagination'] = Component(
    sass=['pagination']
)
COMPONENTS['panels'] = Component(
    sass=['panels']
)
COMPONENTS['pricing-tables'] = Component(
    sass=['pricing-tables']
)
COMPONENTS['progress-bars'] = Component(
    sass=['progress-bars']
)
COMPONENTS['nav'] = Component(
    sass=['side-nav', 'sub-nav']
)
COMPONENTS['reveal'] = Component(
    js=['foundation.reveal'], sass=['reveal']
)
COMPONENTS['slider'] = Component(
    js=['foundation.slider'], sass=['range-slider']
)
COMPONENTS['switches'] = Component(
    sass=['switches']
)
COMPONENTS['tables'] = Component(
    sass=['tables']
)
COMPONENTS['tabs'] = Component(
    js=['foundation.tab'], sass=['tabs']
)
COMPONENTS['thumbs'] = Component(
    sass=['thumbs']
)
COMPONENTS['tooltips'] = Component(
    js=['foundation.tooltip'], sass=['tooltips']
)
COMPONENTS['topbar'] = Component(
    js=['foundation.topbar'], sass=['top-bar']
)
COMPONENTS['type'] = Component(
    sass=['type']
)
COMPONENTS['visibility'] = Component(
    sass=['visibility']
)


# This provides a set of frequent component builds that can be used instead of
# listing all the individual components, which can be useful when you want to
# slim down your build to only the components you need.
SHORTCUTS = {}

_all_comps = [k for k, c in COMPONENTS.items() if c.default]
SHORTCUTS['all'] = _all_comps
SHORTCUTS['foundation_only'] = [k for k in _all_comps if k not in [
    'jquery', 'modernizr', 'modernizr-slim'
]]
SHORTCUTS['no_js'] = [k for k, c in COMPONENTS.items() if c.default and c.js == []]


def flatten(lst):
    return reduce(lambda el, lst: el + lst, lst, [])


def _get_components():
    components = get_setting('components')
    if type(components) == str:
        return SHORTCUTS.get(components, None)
    return components


def get_sass_imports():
    """
    Get a list of all the required SASS components.
    """
    return flatten(
        (c.sass_imports for n, c in COMPONENTS.items() if n in _get_components())
    )


def get_js_files():
    """
    Get a list of all the required JS components.
    """
    return flatten(
        (c.js_files for n, c in COMPONENTS.items() if n in _get_components())
    )
