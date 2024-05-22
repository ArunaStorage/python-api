#!/usr/bin/env python

from setuptools import setup, find_packages

setup(
    name='Aruna-Python-API',
    version="2.0.0-beta.13",
    description='Aruna Object Storage Python API builds',
    long_description=open('README.md', 'r').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/ArunaStorage/python-api',
    license='Apache 2.0',
    author='Sebastian Beyvers, Jannis Hochmuth, Lukas Brehm',
    author_email='sebastian.beyvers@computational.bio.uni-giessen.de, '
                 'jannis.hochmuth@computational.bio.uni-giessen.de, '
                 'lukas.brehm@computational.bio.uni-giessen.de',
    # packages=find_packages('aruna')
    packages=['aruna',
              'aruna.api',
              'aruna.api.dataproxy', 'aruna.api.dataproxy.services', 'aruna.api.dataproxy.services.v2',
              'aruna.api.hooks', 'aruna.api.hooks.services', 'aruna.api.hooks.services.v2',
              'aruna.api.notification', 'aruna.api.notification.services', 'aruna.api.notification.services.v2',
              'aruna.api.storage',
              'aruna.api.storage.models', 'aruna.api.storage.models.v2',
              'aruna.api.storage.services', 'aruna.api.storage.services.v2',
              'protoc_gen_openapiv2.options'],
    package_data={'aruna.api.dataproxy.services.v2': ['*.pyi'],
                  'aruna.api.hooks.services.v2': ['*.pyi'],
                  'aruna.api.notification.services.v2': ['*.pyi'],
                  'aruna.api.storage.models.v2': ['*.pyi'],
                  'aruna.api.storage.services.v2': ['*.pyi'],
                  'protoc_gen_openapiv2.options': ['*.pyi'],
                },
    install_requires=[
        'protobuf',
        'grpcio',
        'google-api-python-client'
    ],
)
