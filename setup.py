import os
from setuptools import setup

README = open(os.path.join(os.path.dirname(__file__), 'README.rst')).read()

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name='django-groundwork',
    version='0.2.5',
    packages=['groundwork'],
    include_package_data=True,
    license='BSD License',
    description='A simple Django wrapper for Zurb Foundation',
    long_description=README,
    url='https://github.com/dummerbd/django-groundwork',
    author='Benjamin Dummer',
    author_email='dummerbd@appstate.edu',
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'License :: OSI Approved :: BSD License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    ],
    scripts=['install.py']
)