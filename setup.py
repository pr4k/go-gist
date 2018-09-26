from distutils.core import setup

setup(
    # Application name:
    name="Gist",

    # Version number (initial):
    version="1.0",

    # Application author details:
    author="Prakhar"
    include_package_data=True,

    # Details
    url="http://pypi.python.org/pypi/Gist/",

    #
    # license="LICENSE.txt",
    description="Provides interface to push gist ",

    install_requires=[
        "simplegist",
    ],
)