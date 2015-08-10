#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: Yuande Liu <miraclecome (at) gmail.com>

from __future__ import print_function, division

from distutils.core import setup

setup(
    name = 'pgwrapper'
    version = '0.1'
    author = 'Clark Liu'
    author_email = 'miraclecome@gmail.com'
    description = 'A simple, fast way to access postgresql'
    classifiers = [
        "Programming Language :: Python :: 2.7",
        "Development Status :: 4 - Beta",
        "Environment :: Other Environment",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: OS Independent",
        "Topic :: Software Development :: Libraries :: Python Modules",
        ],
    long_description = """
        - It is a postgresql python connection pool at lower layer.
        - It is a mongo-like query formula system upper layer.
        - It is a rough version to access postgresql in python2.
    """
)