#!/usr/bin/env python

from setuptools import setup, find_packages

setup(
    name='Aruna-Python-API',
    version="1.0.0-rc.2",
    description='Aruna Object Storage Python API builds',
    long_description=open('README.md', 'r').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/ArunaStorage/python-api',
    license='Apache 2.0',
    author='Marius Dieckmann, Jannis Hochmuth',
    author_email='marius.dieckmann@computational.bio.uni-giessen.de, '
                 'jannis.hochmuth@computational.bio.uni-giessen.de',
    # packages=find_packages('aruna')
    packages=['aruna',
              'aruna.api',
              'aruna.api.internal', 'aruna.api.internal.v1',
              'aruna.api.notification', 'aruna.api.notification.services', 'aruna.api.notification.services.v1',
              'aruna.api.storage',
              'aruna.api.storage.models', 'aruna.api.storage.models.v1',
              'aruna.api.storage.services', 'aruna.api.storage.services.v1'],
    package_data={'aruna.api.internal.v1': ['*.pyi'],
                  'aruna.api.notification.services.v1': ['*.pyi'],
                  'aruna.api.storage.models.v1': ['*.pyi'],
                  'aruna.api.storage.services.v1': ['*.pyi']},
    install_requires=[
        'protobuf==3.20.3',
        'grpcio',
        'grpc-gateway-protoc-gen-openapiv2',
        'google-api-python-client'
    ],
)
