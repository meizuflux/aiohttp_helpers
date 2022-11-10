import re

from setuptools import find_packages, setup

version = None
with open("aiohttp_helpers/__init__.py") as f:
    for line in f.read().splitlines():
        if line.startswith("__version__"):
            # __version__ = "0.9"
            delim = '"' if '"' in line else "'"
            version = line.split(delim)[1]
if version is None:
    raise RuntimeError("Unable to find version string.")

setup(
    name="aiohttp_helpers",
    description="custom aiohttp framework ish",
    author="meizuflux",
    project_urls={
        "Issue Tracker": "https://github.com/meizuflux/aiohttp_helpers/issues",
        "Source Code": "https://github.com/aiohttp_helpers/cion",
    },
    license="MIT",
    url="https://github.com/meizuflux/aiohttp_helpers",
    packages=find_packages(),
    package_data={"aiohttp_helpers": ["py.typed"]},
    classifiers=[
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3.10",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Typing :: Typed",
    ],
    version=version,
    install_requires=["aiohttp", "jinja2"],
    extras_require={
        "build": [
            "setuptools",
            "wheel",
            "build",
            "twine",
        ],
        "format": [
            "black",
            "isort",
        ],
    },
    python_requires=">=3.10",
)