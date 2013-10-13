# Convert ESRI Shapefile to CSV
#
# ogr2ogr is part of the GDAL software suite,
# avaiable at http://www.gdal.org/

# export shapefile data including point coordinates in WGS84
# format (lon/lat) to intermediate file
ogr2ogr -f CSV adressen_temp.csv _source/Adressen/Adresse.shp -lco GEOMETRY=AS_XY -t_srs "EPSG:4326"

# set predictable floating point precision, remove trailing zeroes
perl -CSD -pe "s/([0-9]+\.[0-9]{7})[0-9]*/\\1/g" adressen_temp.csv|perl -CSD -pe "s/([0-9]+\.[0-9]*[^0])[0]+,/\\1,/g" > adressen_temp2.csv

# Sort by address ID
csvsort -y 10000 -c 3 adressen_temp2.csv > adressen.csv

# delete intermediate file
rm adressen_temp.csv
rm adressen_temp2.csv
