#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
    flaskapp
    ~~~~~~~~

    Example of Live Style Guide made with Flask-Styleguide.

    :copyright: (c) 2015 by Vital Kudzelka <vital.kudzelka@gmail.com>
    :license: MIT
"""
import io
import os
import sys
from setuptools import (
    find_packages,
    setup,
)

from flaskapp import (
    __version__,
    cli,
)


def read(*parts):
    try:
        return io.open(os.path.join(*parts), 'r', encoding='utf-8').read()
    except IOError:
        return ''


requirements = read('requirements', 'main.txt').splitlines()
tests_require = read('requirements', 'test.txt').splitlines()

setup(
    name='flask-styleguide-example',
    version=__version__,

    author='Vital Kudzelka',
    author_email='vital.kudzelka@gmail.com',

    url='https://github.com/vitalk/flask-styleguide-example',
    description='Example of Live Style Guide made with Flask-Styleguide.',
    long_description=read('README.md'),
    license='MIT',

    packages=find_packages(exclude=['docs', 'tests']),
    zip_safe=False,
    platforms='any',
    install_requires=requirements,
    tests_require=tests_require,
    test_suite='tests',
    cmdclass={
        'freeze': cli.freezer.freeze,
        'serve': cli.serve.run,
        'test': cli.test.pytest,
    },

    # See https://pypi.python.org/pypi?%3Aaction=list_classifiers
    classifiers=[
        # Pypi will refuse to accept packages with unknown classifiers, so
        # the following line prevents me from uploading private package to
        # pypi. Just remove this line before publish.
        'Private :: Do Not Upload',
        'Development Status :: 3 - Alpha',
        'Framework :: Flask',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ]
)
