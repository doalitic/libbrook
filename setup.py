# coding: utf-8

import sys
from setuptools import setup, find_packages

NAME = "libbrook"
VERSION = "0.4"



# To install the library, run the following
#
# python setup.py install
#
# prerequisite: setuptools
# http://pypi.python.org/pypi/setuptools

REQUIRES = ["urllib3 >= 1.10", "six >= 1.9", "certifi", "python-dateutil"]

setup(
    name=NAME,
    version=VERSION,
    description="Brook.io API",
    author_email="devops@doalitic.com",
    url="https://github.com/doalitic/libbrook",
    keywords=["brook.io", "api", "cloud"],
    install_requires=REQUIRES,
    packages=find_packages(),
    include_package_data=True,
    long_description="""\
    Brook.io API for managing multi-provider cloud infrastructure
    """
)

