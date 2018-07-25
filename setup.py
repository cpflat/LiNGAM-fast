#!/usr/bin/env python

from __future__ import print_function

import sys
import os
from setuptools import setup

setup(name='lingam_fast',
    version='0.0.1',
    description='/* setup.py for private use */',
    author='Takeshi Morinibu',
    url='https://github.com/NibuTake/LiNGAM-fast',
    install_requires=['numpy>=1.9.2'],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Console',
        'Intended Audience :: Information Technology',
        'Intended Audience :: Science/Research',
        ('License :: OSI Approved :: MIT License'),
        'Programming Language :: Python :: 3.4.3',
        'Topic :: Scientific/Engineering :: Information Analysis',
        'Topic :: Software Development :: Libraries :: Python Modules'],
    license='MIT License',
    
    packages=['lingam_fast']
    )
