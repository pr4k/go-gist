import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="Gist",
    version="0.0.1",
    author="Prakhar",
    description="Command line wrapper for github gist",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/pr4k/go-gist",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)


