#!/bin/bash

ROOT=$(pwd)

## Wasserstände
# aktuelle Messwerte
URL1="http://luadb.lds.nrw.de/LUA/wiski/messwerte/messwerte.tar.gz"
# Bestand an Rohdaten
URL2="http://luadb.lds.nrw.de/LUA/hygon/messwerte/pegeldaten.tar.gz"

## Wassertemperatur
# aktuelle Messwerte
#http://luadb.lds.nrw.de/LUA/wiski/messwerte/temperatur.tar.gz
# Bestand an Rohdaten
#http://luadb.lds.nrw.de/LUA/hygon/messwerte/temperaturdaten.tar.gz

## Gewässergüte
# Bestand an Rohdaten
#http://luadb.lds.nrw.de/LUA/hygon/messwerte/guetedaten.tar.gz

# Load source files
echo "Downloading source data..."
test -d "_source" && rm -r _source
mkdir -p _source/gauge
curl -s $URL2 > _source/gauge/historic.tar.gz

# unzip source files
echo "Unzipping source data..."
cd $ROOT/_source/gauge
tar xzf historic.tar.gz
rm historic.tar.gz

cd $ROOT

# convert stations file
echo "Creating station files..."
test -f "gauge_stations_tmp.geojson" && rm -f gauge_stations_tmp.geojson
in2csv -f csv -e latin1 _source/gauge/pegel_stationen.txt > stations_EPSG-32632.csv
ogr2ogr -f GeoJSON gauge_stations_tmp.geojson gauge_stations_EPSG-32632.vrt -t_srs "EPSG:4326"
python ../../../tools/lessprecise/lessprecise.py \
	--indent 4 --sort 1 -o gauge_stations.geojson \
	gauge_stations_tmp.geojson
rm gauge_stations_tmp.geojson
ogr2ogr -f CSV stations_tmp.csv gauge_stations.geojson -lco GEOMETRY=AS_XY
csvcut -c 3,4,5,6,7,8,9,10,11,1,2 stations_tmp.csv > gauge_stations.csv
rm -f stations_EPSG-32632.csv
rm -f stations_tmp.csv

# append daily values to stored file
echo "Creating value files..."
tail -n+2 gauge_values_daily.csv > out.csv
in2csv -f csv -e latin1 _source/gauge/pegel_tageswerte.txt|tail -n+2 >> out.csv
sort -u out.csv > out_uniq.csv
rm out.csv
head -n 1 _source/gauge/pegel_tageswerte.txt|in2csv -f csv -e latin1 > gauge_values_daily.csv
cat out_uniq.csv >> gauge_values_daily.csv
rm out_uniq.csv

rm -r _source
