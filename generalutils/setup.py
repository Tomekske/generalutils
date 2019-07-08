#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
===============================
HtmlTestRunner
===============================


.. image:: https://img.shields.io/pypi/v/generalutils.svg
        :target: https://pypi.python.org/pypi/generalutils
.. image:: https://img.shields.io/travis/Tomekske/generalutils.svg
        :target: https://travis-ci.org/Tomekske/generalutils

This package contains some common general utilisations modules


Links:
---------
* `Github <https://github.com/Tomekske/generalutils>`_
"""

from setuptools import setup, find_packages

requirements = [ ]

setup_requirements = [ ]

test_requirements = [ ]

setup(
    author="Tomek Joostens",
    author_email='joostenstomek@gmail.com',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        "Programming Language :: Python :: 2",
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],
    description="This package contains some common general utilisations modules",
    install_requires=requirements,
    license="MIT license",
    long_description=__doc__,
    include_package_data=True,
    keywords='generalutils',
    name='generalutils',
    packages=find_packages(include=['generalutils']),
    setup_requires=setup_requirements,
    test_suite='tests',
    tests_require=test_requirements,
    url='https://github.com/Tomekske/generalutils',
    version='0.1.0',
    zip_safe=False,
)
