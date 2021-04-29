#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author: Yuande Liu <miraclecome (at) gmail.com>


#from distutils.core import setup
from setuptools import setup, Extension

setup(
    name = 'pgwrapper',
    version = '0.2.0',
    packages = ['pgwrapper'],
    author = 'Clark Liu',
    author_email = 'miraclecome@gmail.com',
    url = 'https://github.com/LaoLiulaoliu/pgwrapper',
    install_requires=[ 'psycopg2 >= 2.8.5', ],
    description = 'A simple, fast way to access postgresql',
    classifiers = [
        "Programming Language :: Python :: 3.8",
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
        - It is a new version to access postgresql in python3.
    """
)
