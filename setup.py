#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os

from setuptools import setup, find_packages


requires = [
]

setup(
    name='simplefileserver',
    version='0.0.1',
    description='simplefileserver',
    long_description=open(os.path.join('README.md')).read(),
    author='perfectnewer',
    author_email='',
    packages=find_packages(),
    url='https://github.com/perfectnewer/simplefileserver',
    include_package_data=True,
    zip_safe=False,
    install_requires=requires,
)
