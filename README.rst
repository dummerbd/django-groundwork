==========
Groundwork
==========

Groundwork is a small set of template tags and filters that simplifies
working with Zurb Foundation. Many common django components like paginators,
messages, and forms can be used natively with this package. These components
get wrapped in nice pretty Foundation goodness.


Quick Start
-----------
1. Install Groundwork using pip::

    pip install django-groundwork

2. Add "groundwork" to your INSTALLED_APPS like so::

    INSTALLED_APPS = (
        ...
        'groundwork',
    )

Available Tags/Filters
----------------------
To use the Groundwork tags in your template, include at the top::

    {% load groundwork_tags %}

See templates/goundwork/examples/base.html for examples on how to get started 
with Foundation quickly. Or, you can choose to use is as your base page to help
you get started. Simply put as the first line in your templates::

    {% extends 'groundwork/examples/base.html' %}

To include the Foundation Javascript files (in your html <head>), use the
groundwork_js tag. You can specify a filename like `foundation.abide.js` or
you can leave it blank to include the `foundation.min.js` file::

    {% groundwork_js %}
    {% groundwork_js 'foundation.abide' %}

To include the Foundation vendor Javascript files, use the groundwork_vendor
tag with the name of the script name::

    {% groundwork_vendor 'jquery' %}

To include the Foundation StyleSheet files (in your html <head>), use the
groundwork_css tag::

    {% groundwork_css 'normalize' %}
    {% groundwork_css 'foundation.min' %}

To use the Foundation Icons pack use the groundwork_icon tag with the name of
the Icon class. You can find examples of all the included icons by going to
/groundwork/icons after adding the Groundwork URLConf, it also accepts optional
`size` and `classes` arguments::

    {% groundwork_icon 'info' %}
    {% groundwork_icon 'info' '5em' 'text-centered' %}

Foundation alert boxes are a really nice way to inform the user of the result of
completing some action, like logging in, or saving a file. Much of Django uses
the django.contrib.messages framework to do that, and Groundwork provides a nice
wrapper to display them with Foundation alerts. The included example base.html
will automatically display messages from the messages framework for you, but you
can also use the groundwork_alert tag for custom alerts::

    {% groundwork_alert 'this is a message!' %}

Some views that display a list of models, like the generic ListView class can
make good use of paginators. Groundwork provides a super easy to use paginator
tag called groundwork_paginator. Just make sure to set the `paginate_by`
attribute on your ListView view to enable automatic pagination. The tag takes
no arguments::

    {% groundwork_paginator %}

References
----------
Github: https://github.com/dummerbd/django-groundwork

PyPI: https://pypi.python.org/pypi/django-groundwork

This package was inspired by: https://github.com/amarsahinovic/django-zurb-foundation
