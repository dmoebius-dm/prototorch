"""
  _____           _     _______             _
 |  __ \         | |   |__   __|           | |
 | |__) | __ ___ | |_ ___ | | ___  _ __ ___| |__
 |  ___/ '__/ _ \| __/ _ \| |/ _ \| '__/ __| '_ \
 | |   | | | (_) | || (_) | | (_) | | | (__| | | |
 |_|   |_|  \___/ \__\___/|_|\___/|_|  \___|_| |_|

ProtoTorch Core Package
"""
from setuptools import find_packages, setup

PROJECT_URL = "https://github.com/si-cim/prototorch"
DOWNLOAD_URL = "https://github.com/si-cim/prototorch.git"

with open("README.md", "r") as fh:
    long_description = fh.read()

INSTALL_REQUIRES = [
    "torch>=1.3.1",
    "torchvision>=0.5.0",
    "numpy>=1.9.1",
]
DATASETS = [
    "requests",
    "sklearn",
    "tqdm",
]
DEV = ["bumpversion"]
DOCS = [
    "recommonmark",
    "sphinx",
    "sphinx_rtd_theme",
    "sphinxcontrib-katex",
]
EXAMPLES = [
    "sklearn",
    "matplotlib",
    "torchinfo",
]
TESTS = ["codecov", "pytest"]
ALL = DATASETS + DEV + DOCS + EXAMPLES + TESTS

setup(
    name="prototorch",
    version="0.4.4",
    description="Highly extensible, GPU-supported "
    "Learning Vector Quantization (LVQ) toolbox "
    "built using PyTorch and its nn API.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="Jensun Ravichandran",
    author_email="jjensun@gmail.com",
    url=PROJECT_URL,
    download_url=DOWNLOAD_URL,
    license="MIT",
    install_requires=INSTALL_REQUIRES,
    extras_require={
        "docs": DOCS,
        "datasets": DATASETS,
        "examples": EXAMPLES,
        "tests": TESTS,
        "all": ALL,
    },
    classifiers=[
        "Development Status :: 2 - Pre-Alpha",
        "Environment :: Console",
        "Intended Audience :: Developers",
        "Intended Audience :: Education",
        "Intended Audience :: Science/Research",
        "License :: OSI Approved :: MIT License",
        "Natural Language :: English",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Operating System :: OS Independent",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
        "Topic :: Software Development :: Libraries",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
    packages=find_packages(),
    zip_safe=False,
)
