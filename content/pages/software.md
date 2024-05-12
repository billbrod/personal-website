Title: Software
Date: 2024-05-12
Summary: Open-source software projects that I work(ed) on

Starting during my PhD and continuing during my work at the [Flatiron Institute](https://www.simonsfoundation.org/flatiron/) [Center for Computational Neuroscience](https://www.simonsfoundation.org/flatiron/center-for-computational-neuroscience/), I have worked as a developer on several neuroscience-related open source software packages. In rough chronological order, they are:

- [pyrtools](https://github.com/LabForComputationalVision/pyrtools/) (core developer, maintainer): tools for multi-scale image processing. pyrtools is a python 3 / numpy port of Eero Simoncelli's [matlabPyrTools](https://github.com/LabForComputationalVision/matlabPyrTools). Several of its components also have differentiable implementations in plenoptic, below.

- [plenoptic](https://github.com/LabForComputationalVision/plenoptic/) (core developer, maintainer): a python library for model-based synthesis of perceptual stimuli, which enables researchers to better understand how their models process images. Powered by [pytorch](https://pytorch.org/)

- [CCN template](https://github.com/flatironinstitute/ccn-template/): not an actual python package, but this template is an attempt to make and document all the many decisions that go into writing open-source python packages: structure, documentation, testing, etc.

- [nemos](https://github.com/flatironinstitute/nemos) (developer): NEural MOdelS, a statistical modeling framework for systems neuroscience, powdered by [JAX](https://jax.readthedocs.io/en/latest/). It streamlines the process of creating and selecting models, through a collection of easy-to-use methods for feature design. The core of nemos includes GPU-accelerated, well-tested implementations of standard statistical models, currently focusing on the Generalized Linear Model (GLM).

