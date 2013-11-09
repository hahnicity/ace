#!/usr/bin/env python
from setuptools import setup, find_packages

__version__ = "0.1"


setup(
    name="ace",
    author="Gregory Rehm",
    author_email="grehm87@gmail.com",
    version=__version__,
    description="Work in 'Applied Computational Economics and Finance'",
    packages=find_packages(),
    entry_points={},
    install_requires=[
        "matplotlib",
    ],
)
