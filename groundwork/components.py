"""
components.py - contains definitions for Foundation components.
"""
from functools import reduce

from groundwork.settings import get_setting


class Component:
    """
    Foundation component, really just a pairing of JS and SASS files.
    """
    def __init__(self, js=[], sass=[]):
        """
        `js` and `sass` should be a list of names such as `accordian`, or `tab`
        that can be formed with the path settings.
        """
        self.js = js
        self.sass = sass
        self.name = self.__class__.__name__.lower()

    @property
    def js_files(self):
        """
        Format the `js` components into file paths.
        """
        root = get_setting('foundation_js_path')
        return ['%s/foundation.%s.js' % (root, name) for name in self.js]

    @property
    def sass_imports(self):
        return['foundation/components/%s' % name for name in self.sass]
    


COMPONENTS = {
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


def get_sass_imports():
    """ 
    Get a list of all the required SASS components.
    """
    components = get_setting('components')
    if components == 'all':
        components = COMPONENTS.keys()
    return reduce(
        lambda c, cs: c + cs,
        (c.sass_imports for n, c in COMPONENTS.items() if n in components),
        []
    )


def get_js_files():
    """
    Get a list of all the required JS components.
    """
    components = get_setting('components')
    if components == 'all':
        components = COMPONENTS.keys()
    return reduce(
        lambda c, cs: c + cs,
        (c.js_files for n, c in COMPONENTS.items() if n in components),
        []
    )
