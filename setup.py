#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Author:  Dominik Gresch <greschd@gmx.ch>

from setuptools import setup, find_packages

readme = """Implementation of strains for III-V materials."""

setup(
    name='strain',
    author='Dominik Gresch',
    author_email='greschd@gmx.ch',
    install_requires=['numpy', 'pymatgen'],
    extras_require={'test': ['pytest']},
    long_description=readme,
    classifiers=[
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Natural Language :: English',
        'Operating System :: Unix',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Intended Audience :: Science/Research',
        'Topic :: Scientific/Engineering :: Physics'
    ],
    license='GPL',
    py_modules=find_packages()
)
