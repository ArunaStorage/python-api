#!/usr/bin/env python

from setuptools import setup, find_packages

setup(name='ScienceObjectsDBClient',
      version='v0.3.0-alpha.2',
      description='ScienceObjectsDB python client',
      author='Marius Dieckmann',
      packages=['sciobjsdb', 'sciobjsdb.api', 'sciobjsdb.api.storage.services.v1', 'sciobjsdb.api.storage.models.v1'],
    install_requires=[
          'grpcio',
          'requests'
      ],
     )