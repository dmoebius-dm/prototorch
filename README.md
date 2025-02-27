# ProtoTorch: Prototype Learning in PyTorch

![ProtoTorch Logo](https://prototorch.readthedocs.io/en/latest/_static/horizontal-lockup.png)

[![Build Status](https://travis-ci.org/si-cim/prototorch.svg?branch=master)](https://travis-ci.org/si-cim/prototorch)
![tests](https://github.com/si-cim/prototorch/workflows/tests/badge.svg)
[![GitHub tag (latest by date)](https://img.shields.io/github/v/tag/si-cim/prototorch?color=yellow&label=version)](https://github.com/si-cim/prototorch/releases)
[![PyPI](https://img.shields.io/pypi/v/prototorch)](https://pypi.org/project/prototorch/)
[![codecov](https://codecov.io/gh/si-cim/prototorch/branch/master/graph/badge.svg)](https://codecov.io/gh/si-cim/prototorch)
[![Codacy Badge](https://api.codacy.com/project/badge/Grade/76273904bf9343f0a8b29cd8aca242e7)](https://www.codacy.com/gh/si-cim/prototorch?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=si-cim/prototorch&amp;utm_campaign=Badge_Grade)
![PyPI - Downloads](https://img.shields.io/pypi/dm/prototorch?color=blue)
[![GitHub license](https://img.shields.io/github/license/si-cim/prototorch)](https://github.com/si-cim/prototorch/blob/master/LICENSE)

*Tensorflow users, see:* [ProtoFlow](https://github.com/si-cim/protoflow)

## Description

This is a Python toolbox brewed at the Mittweida University of Applied Sciences
in Germany for bleeding-edge research in Prototype-based Machine Learning
methods and other interpretable models. The focus of ProtoTorch is ease-of-use,
extensibility and speed.

## Installation

ProtoTorch can be installed using `pip`.
```bash
pip install -U prototorch
```
To also install the extras, use
```bash
pip install -U prototorch[all]
```

*Note: If you're using [ZSH](https://www.zsh.org/) (which is also the default
shell on MacOS now), the square brackets `[ ]` have to be escaped like so:
`\[\]`, making the install command `pip install -U prototorch\[all\]`.*

To install the bleeding-edge features and improvements:
```bash
git clone https://github.com/si-cim/prototorch.git
cd prototorch
git checkout dev
pip install -e .[all]
```

## Documentation

The documentation is available at <https://www.prototorch.ml/en/latest/>. Should
that link not work try <https://prototorch.readthedocs.io/en/latest/>.

## Bibtex

If you would like to cite the package, please use this:
```bibtex
@misc{Ravichandran2020b,
  author = {Ravichandran, J},
  title = {ProtoTorch},
  year = {2020},
  publisher = {GitHub},
  journal = {GitHub repository},
  howpublished = {\url{https://github.com/si-cim/prototorch}}
}
