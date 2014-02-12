#!/bin/bash

# Download earthquakes within the area
# (maxlatitude=52, minlatitude=50, maxlongitude=8, minlongitude=5)
# to a GeoJSON file

SOURCE_URL="http://comcat.cr.usgs.gov/fdsnws/event/1/query?starttime=1980-00-00%2000:00:00&maxlatitude=52&minlatitude=50&maxlongitude=8&minlongitude=5&minmagnitude=1&format=geojson&endtime=2020-12-31%2023:59:59&orderby=time"
curl -s $SOURCE_URL > earthquakes.temp.geojson

# make predictable and source code control friendly format
python ../../../tools/lessprecise/lessprecise.py \
	--indent 4 --sort 1 \
	-o earthquakes.geojson earthquakes.temp.geojson
rm earthquakes.temp.geojson
