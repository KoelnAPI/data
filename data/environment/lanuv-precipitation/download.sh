#!/bin/bash

ROOT=$(pwd)

## Niederschläge

# aktuelle stündliche Messwerte
#URL1="http://luadb.lds.nrw.de/LUA/wiski/messwerte/niederschlag.tar.gz"

# Stationen, historische Tages- und Stundenwerte
URL2="http://luadb.lds.nrw.de/LUA/hygon/messwerte/niederschlagsdaten.tar.gz"


# Load source files
echo "Downloading source data..."
test -d "_source" && rm -r _source
mkdir -p _source
curl -s $URL2 > _source/historic.tar.gz

# unzip source files
echo "Unzipping source data..."
cd $ROOT/_source
tar xzf historic.tar.gz

# remove unwanted files
rm historic.tar.gz
rm nieder_tageswerte.txt

cd $ROOT

# convert stations file
echo "Creating station files..."
test -f "stations_tmp.geojson" && rm -f stations_tmp.geojson
in2csv -f csv -e latin1 _source/nieder_stationen.txt > stations_EPSG-32632.csv
ogr2ogr -f GeoJSON stations_tmp.geojson stations_EPSG-32632.vrt -t_srs "EPSG:4326"
python ../../../tools/lessprecise/lessprecise.py \
	--indent 4 --sort 1 -o stations.geojson \
	stations_tmp.geojson
rm stations_tmp.geojson
ogr2ogr -f CSV stations_tmp.csv stations.geojson -lco GEOMETRY=AS_XY
csvcut -c 4,3,7,1,2 stations_tmp.csv > stations.csv
rm -f stations_EPSG-32632.csv
rm -f stations_tmp.csv

# append daily values to stored file
echo "Creating value files..."
# save content of values.csv (without header) to out.csv
in2csv -f csv -d ";" -e latin1 _source/nieder_messwerte.txt > messwerte_temp.csv
tail -n+2 values.csv > out.csv
tail -n+2 messwerte_temp.csv >> out.csv
sort -u out.csv > out_uniq.csv
rm out.csv
head -n 1 messwerte_temp.csv > values.csv
cat out_uniq.csv >> values.csv
rm out_uniq.csv
rm messwerte_temp.csv

rm -r _source/*
