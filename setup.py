# -*- coding: utf-8 -*-

# Learn more: https://github.com/janusson/setup.py

from setuptools import setup, find_packages


with open('README.md') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='example',
    version='0.1.0',
    description='Sample package',
    long_description=readme,
    author='',
    author_email='',
    url='https://github.com/ ',
    license=license,
    packages=find_packages(exclude=('tests', 'docs'))
)

