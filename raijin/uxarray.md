# Uxarray

The Xarray package extends the capabilities of NumPy arrays by introducing labeled
dimensions, coordinates, and attributes, as well as the ability to read data from
a number of scientific file formats such as netCDF. Xarray was designed with regular
gridded data in mind and does not recognize unstructured grids, treating them simply
as one-dimensional arrays of points.

We are creating a new Python object based on Xarray, called UXarray, which will
support reading and recognizing unstructured grid models. Initially, we will support: MPAS (atmosphere and ocean), SE, FV3, and ICON. UXarray
will follow the model of the UGRID specification, currently under consideration
to be included in the netCDF CF conventions, as well as support SCRIP, Exodus, and
shapefile formats for the internal representation of auxiliary data needed to
describe an unstructured mesh (e.g. cell types and cell connectivity information).

We note that basing UXarray on Xarray will facilitate interoperability with the
multitude of Xarray-compatible packages, a priority for our work.


## Open development and community engagement

The UXarray effort is a result of the collaboration between Project Raijin and
DOE's SEATS Project (Argonne National Laboratory, UC Davis, and Lawrence Livermore
National Laboratory). The Uxarray team welcomes other community members to become
part of this collaboration at any level of contribution. To read further
documentation, work with the code, start a discussion, make a request, or report
an issue, please visit:

[UXarray Github repository](https://github.com/UXARRAY/uxarray)

[UXarray documentation](https://uxarray.readthedocs.io/en/latest/index.html)

Lastly, in anticipation that community members will want to add support for other
unstructured grid models outside the scope of this proposal, including global and
regional ocean models such as FVCOM, our project’s
[Contributor's guide](https://raijin.ucar.edu/contributing.html) will provide
a detailed description of this particular topic.
