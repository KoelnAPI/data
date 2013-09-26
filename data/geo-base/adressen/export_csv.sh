# Convert ESRI Shapefile to CSV
#
# ogr2ogr is part of the GDAL software suite,
# avaiable at http://www.gdal.org/

# export shapefile data including point coordinates in WGS84
# format (lon/lat) to intermediate file
ogr2ogr -f CSV adressen_temp.csv _source/Adressen/Adresse.shp -lco GEOMETRY=AS_XY -t_srs "EPSG:4326"

# You might want to check the output file manually
# for spurious rows and for records containing line breaks.
# Expecially check AD_NR 02795001500 and 02093002600!
#
# Otherwise, corrupt CSV will be generated
# in the sort step.

# write only first row (column names) to result file
head -n 1 adressen_temp.csv > adressen.csv

# sort all other rows and append them to the result file
tail -n+2 adressen_temp.csv|sort -t"," -k3 >> adressen.csv

# delete intermediate file
rm adressen_temp.csv
