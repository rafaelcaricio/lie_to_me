#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Lie_to_me pyvows mock library
# https://github.com/rafaelcaricio/lie_to_me/

# Licensed under the MIT license:
# http://www.opensource.org/licenses/mit-license
# Copyright (c) 2011 Rafael Caricio rafael@caricio.com

from setuptools import setup
from lie_to_me import __version__

setup(
    name='lie_to_me',
    version=__version__,
    description="Lie to me is a mock library to test code using pyVows.",
    long_description="Lie to me is a mock library to test code using pyVows.",
    keywords='tdd vows testing mock pyvows',
    author='Rafael Caricio',
    author_email='rafael@caricio.com',
    url='http://github.com/rafaelcaricio/lie_to_me/',
    license='MIT',
    classifiers=['Development Status :: 3 - Alpha',
                   'Intended Audience :: Developers',
                   'License :: OSI Approved :: MIT License',
                   'Natural Language :: English',
                   'Operating System :: MacOS',
                   'Operating System :: Microsoft :: Windows',
                   'Operating System :: POSIX :: Linux',
                   'Topic :: Software Development :: Testing',
    ],
    packages=['lie_to_me'],

    install_requires=[
        "pyvows",
    ]

)
