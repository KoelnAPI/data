Open Data Cologne Tools
=======================


## shapefile-to-various.py

This script currently converts ESRI Shapefiles containing polygon collections
(like e.g. city district boundaries) to GeoJSON.

It is also planned to add KML export to this file.

### Usage

    python shapefile-to-various.py <infile_prefix> <outfile_prefix>

"infile_prefix" is the path to the input shapefile, without the ".shp" ending.

"outfile_prefix" accordingly is the path to the GeoJSON export file, minus the ".geojson" ending.

### Example

Say you have a file 'myshapefile/myshapefile.shp' and you want to generate
'output/myconvertedfile.geojson. Then use:

    python shapefile-to-various.py myshapefile/myshapefile output/myconvertedfile

## Requirements

* Python
* GDAL
* pyproj
* shapefile (pip install pyshp)
