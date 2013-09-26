# Convert ESRI Shapefile to CSV

ogr2ogr -f CSV adressen_temp.csv _source/Adressen/Adresse.shp -lco GEOMETRY=AS_XY -t_srs "EPSG:4326"

# You might want to check the output file manually
# for spurious rows and for records containing line breaks.
# Expecially check AD_NR 02795001500 and 02093002600!
#
# Otherwise, corrupt CSV will be generated
# in the sort step.

head -n 1 adressen_temp.csv > adressen.csv
tail -n+2 adressen_temp.csv|sort -t"," -k3 >> adressen.csv
rm adressen_temp.csv

