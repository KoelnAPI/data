#!/bin/bash


### Download der CSV-Datei der Stadt Köln

SOURCE_URL="http://www.offenedaten-koeln.de/node/592/download"
NAME="aed_stadt_koeln"
FINAL_FOLDER=$NAME
FILENAME=${NAME}.csv
USER_AGENT="datahub-cgn/0.1"

echo "Downloading $NAME to _source/$FILENAME"

cd _source
rm $FILENAME
wget -q -U $USER_AGENT -O $FILENAME $SOURCE_URL
cd ..


### / ENDE Download der CSV-Datei der Stadt Köln


### Download POIs von crowdsav.com

SOURCE_URL="https://www.crowdsav.com/aeds/get_by_bounds?maxlat=51.097485&minlat=50.810274&maxlng=7.158737&minlng=6.753&limit=500&offset=0"
FILENAME=aed_crowdsav.json

echo "Downloading $NAME to _source/$FILENAME"
cd _source
rm $FILENAME
UA="Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.114 Safari/537.36"
wget -q -U $UA -O $FILENAME $SOURCE_URL
cd ..

# Konvertiere Crowdsav JSON zu CSV-Datei
in2csv -f json -k pois _source/$FILENAME > _source/aed_crowdsav.csv

### Download HTML-Tabelle von defikoeln.de

SOURCE_URL="http://www.defikoeln.de/defi-in-koeln/standorte-nach-stadtbezirken/"
FILENAME=aed_defikoeln.html
echo "Downloading $NAME to _source/$FILENAME"
cd _source
rm $FILENAME
wget -q -U $USER_AGENT -O $FILENAME $SOURCE_URL
cd ..
