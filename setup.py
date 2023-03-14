#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author: Yuande Liu <miraclecome (at) gmail.com>


#from distutils.core import setup
from setuptools import setup, Extension
from pathlib import Path

this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text()

setup(
    name = 'pgwrapper',
    version = '0.2.1',
    packages = ['pgwrapper'],
    author = 'Richard Liu',
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
    long_description = long_description,
    long_description_content_type="text/markdown"
)
