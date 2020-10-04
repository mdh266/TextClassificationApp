#!/usr/bin/env python

"""The setup script."""

from setuptools import setup, find_packages

setup(
    author="Mike Harmon",
    author_email='mdh266@gmail.com',
    python_requires='>=3.5',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
    description="",
    license="MIT license",
    include_package_data=True,
    keywords='modelapi',
    name='modelapi',
    packages=find_packages(include=['modelapi', 'modelapi.*']),
    url='https://github.com/mdh266/modelapi',
    version='0.1.0',
    zip_safe=False,
)
