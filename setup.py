#!/usr/bin/env python3

from setuptools import setup, find_packages

setup(
    name="bgit",
    version="0.0.1",
    description="Tool to manage multiple git repos",
    author="Hong Jiang",
    author_email="j@1byte.io",
    packages=find_packages(exclude=["tests*"]),
    install_requires=["gitpython"],
    entry_points={
        "console_scripts": [
            "bgit = bgit.cli:main",
        ],
    },
)
