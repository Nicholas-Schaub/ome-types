# ome-types build preview

This branch is a *preview* of what the current master branch will look like at build time. (`ome-types` autogenerates the python classes based on the OME xml schema, as such the primary "product" of this repo is not checked into source.)

**Modifications or commits to this branch will be overwritten.**

To contribute to this project, see the [master branch](https://github.com/tlambert03/ome-types)

### `ome-types`

`ome-types` provides a set of python dataclasses and utility functions for
parsing the [OME-XML
format](https://docs.openmicroscopy.org/ome-model/latest/ome-xml/) into
fully-typed python objects for interactive or programmatic access in python. It
can also take these python objects and output them into valid OME-XML.

### Documentation

For more details on using this package, see the [documentation](https://ome-types.readthedocs.io/).

### Installation

To use this package, install from pip:

```shell
pip install ome-types
```
