#!/usr/bin/env python

from distutils.core import setup

setup(name='ScienceObjectsDBClient',
      version='v0.3.0-alpha.2',
      description='ScienceObjectsDB python client',
      author='Marius Dieckmann',
      packages=['sciobjsdb'],
    install_requires=[
          'grpc',
          'requests'
      ],
     )