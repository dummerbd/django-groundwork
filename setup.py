import os
from setuptools import setup

README = open(os.path.join(os.path.dirname(__file__), 'README.rst')).read()

os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name='django-groundwork',

    version='1.0.0-beta',

    packages=['groundwork'],

    include_package_data=True,

    license='MIT License',

    description='A simple Django wrapper for Zurb Foundation',
    long_description=README,

    keywords='zurb foundation sass groundwork django',

    url='https://github.com/dummerbd/django-groundwork',

    author='Benjamin Dummer',
    author_email='dummerbenjamin@gmail.edu',

    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Software Development',
        'Topic :: Software Development :: Pre-processors'
    ]
)
