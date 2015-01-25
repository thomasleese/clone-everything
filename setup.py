#!/usr/bin/env python3
from setuptools import find_packages, setup


setup(
    name='clone_everything',
    version='1.0.0',
    description='A tool to clone many repositories.',
    url='https://github.com/tomleese/clone-everything',
    author='Tom Leese',
    author_email='inbox@tomleese.me.uk',
    packages=find_packages(exclude=['tests*']),
    setup_requires=[
        'nose >=1, <2'
    ],
    install_requires=[
        'requests >=2.5, <3'
    ],
    entry_points={
        'console_scripts': ['clone-everything = clone_everything.cli:main']
    },
    test_suite='nose.collector'
)
