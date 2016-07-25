#!/usr/bin/env python

import os
from setuptools import setup, find_packages

src_dir = os.path.abspath(os.path.dirname(__file__))
catalog_dir = os.path.join(src_dir, 'ninemlcatalog', 'catalog')

try:
    # Create a symlink to the catalog path inside the package directory so it
    # gets installed along side the package
    os.symlink(os.path.join(src_dir, 'xml'), catalog_dir)
    setup(
        name="ninemlcatalog",
        version="1.0",
        packages=find_packages(),
        package_data={'ninemlcatalog': ['catalog']},
        author=("Thomas G. Close"),
        author_email="nineml-users@incf.org",
        description=(
            "A collection of 9ML models and basic Python functions for "
            "accessing them"),
        long_description=open("README.rst").read(),
        license="MIT Licence",
        keywords="computational neuroscience modeling interoperability XML",
        url="http://nineml.incf.org",
        classifiers=['Development Status :: 4 - Beta',
                     'Environment :: Console',
                     'Intended Audience :: Science/Research',
                     'License :: OSI Approved :: MIT Licence',
                     'Natural Language :: English',
                     'Operating System :: OS Independent',
                     'Programming Language :: Python :: 2',
                     'Topic :: Scientific/Engineering'],
        install_requires=[], # ['nineml'],
        tests_require=['nose']
    )
finally:
    os.unlink(catalog_dir)
