
![GitHub Workflow Status (branch)](https://img.shields.io/github/workflow/status/NCAR/projectraijin.github.io/deploy-site/main?logo=github&style=for-the-badge)

> NOTE: This repository only contains source code for the Project Raijin website.
For the source code for the UXarray package, please visit the [UXarray Github repository](https://github.com/UXARRAY/uxarray)

This is the home repository for the [Project Raijin](https://raijin.ucar.edu).
The website is built with [sphinx](https://www.sphinx-doc.org/).

![Project Raijin logo](raijin/_static/images/logos/ProjectRaijin_Logo.png)

# Project Raijin

> *Community-owned, sustainable, scalable tools on unstructured climate and global weather data*

Project Raijin is an NSF EarthCube-funded effort whose goal is to
enhance the open source analysis and visualization tool landscape
by developing community-owned, sustainable, scalable tools that
facilitate operating on unstructured climate and global weather
data. Working in close collaboration with atmospheric modelers,
we plan to: (1) develop extensible, scalable, open source tools
supporting fundamental analysis and visualization methods capable
of operating directly (without resampling) on unstructured grid
model outputs at global storm resolving resolutions; and (2)
establish an active, vibrant community of user-contributors,
committed to extending our work beyond the scope of this NSF
award, thus helping ensure the long term sustainability of
the project.

# Introduction

Culminating nearly two decades of development and evaluation, the climate and global weather modeling
communities have in recent years begun to transition in earnest to dynamical cores employing more flexible,
but more complex, unstructured grids upon which governing numerical equations of state are solved.
The move away from the more simple, regularly structured “latitude-longitude” grids that served these
modeling communities for so long has been driven by, perhaps more than anything else, greatly improved
computational scalability afforded by unstructured meshes, allowing for higher and higher resolutions,
and therefore, more realistic simulations of the earth’s oceans and atmosphere. Numerous institutions
worldwide are now deploying unstructured grid dynamical cores (or “dycores”) with the ultimate long
term pursuit of producing the world’s first global cloud resolving model.

![diagram showing three global grids, the first is latitude-longitude structured grid, the second is an icocahedral grid (MPAS-A), and the third is a variable resolution cube sphere grid (CAM-SE)](raijin/_static/images/lat_lon-mpas-cam_se.png)

The adoption of unstructured mesh models by so many geoscience communities brings with it a two-
fold cost. First, the increased model resolution enabled by these dycores results in the output of more
data, further exacerbating an already existing “Big Data” problem. Second, the existing, general purpose
software tools available for analyzing, post-processing, and visualizing geoscience model outputs primarily
operate on structured grid data, providing little or no support for unstructured meshes. The combined
impact of greatly increasing data volume, and lack of tools capable of operating on these model outputs, let
alone scalable tools, gravely impacts the climate and global weather modeling community’s ability to reap
the full benefits of the substantial investments made in these next generation models.

# Goals

The goal of this project, which we call Raijin, is to enhance the analysis and visualization tool landscape
by developing community-owned, sustainable, scalable tools that facilitate operating on unstructured grid
model outputs arising from climate and global weather simulations. Working in close collaboration with
climate and weather modelers we plan to:

- develop extensible, scalable, open source tools supporting fundamental analysis and visualization
  methods capable of operating directly (without resampling) on unstructured grid model outputs at
  global storm resolving resolutions, and
- establish a vibrant community of user-contributors, committed to extending our work beyond the
  scope of this proposal, and helping ensure the long term sustainability of the project.

# Development Environment

The primary environment for this effort will be the Scientific Python Ecosystem. We will leverage, in
particular, the NSF-supported, open development Xarray and Dask packages, and the Pangeo community.
To better support both of our primary goals, our work will be conducted under an open development
model that encourages participation in the project at all levels. Relatedly, to better support
interoperability, sustainability, usability and repurposing our work, we will adhere to practices
advocated by the NSF Recommended Standards and Specifications for EarthCube Projects.

# UXarray

To import unstructured data into Python, we are creating a new Python package based on Xarray,
called UXarray, which will support reading and recognizing unstructured grid models. To read
further documentation, work with the code, start a discussion, make a request, or report
an issue, please visit:

- [UXarray at Raijin homepage](https://raijin.ucar.edu/uxarray.html)

- [UXarray Github repository](https://github.com/UXARRAY/uxarray)

- [UXarray documentation](https://uxarray.readthedocs.io/en/latest/index.html)
