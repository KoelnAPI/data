#!/bin/bash

USER_AGENT="datahub-cgn/0.1"

### Download der CSV-Datei der Stadt Köln
SOURCE_URL="http://www.offenedaten-koeln.de/node/592/download"
FILENAME="aed_stadt_koeln.csv"
echo "Downloading Stadt Köln AEDs to _source/$FILENAME"
cd _source
rm $FILENAME
wget -q -U $USER_AGENT -O $FILENAME $SOURCE_URL
cd ..

### Download AEDs von AED4EU
echo "Downloading AED4EU AEDs to _source/$FILENAME"
cd _source
SOURCE_URL="http://www.aed4.eu/?page=mobile&lat=51&lon=6.9&north=51.2&east=7.2&south=50.8&west=6.7&zoom=14&available=1&validated=0"
FILENAME="aed_aed4eu.json"
rm $FILENAME
wget -q -O $FILENAME $SOURCE_URL
cd ..

### Download POIs von crowdsav.com
echo "Downloading CrowdSav AEDs to _source/$FILENAME"
cd _source
SOURCE_URL="https://www.crowdsav.com/aeds/get_by_bounds?maxlat=51.2&minlat=50.8&maxlng=7.2&minlng=6.7&limit=500&offset=0"
FILENAME="aed_crowdsav.json"
rm $FILENAME
MOZILLA="Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.114 Safari/537.36"
wget -q -U $MOZILLA -O $FILENAME $SOURCE_URL
cd ..

# Konvertiere Crowdsav JSON zu CSV-Datei
in2csv -f json -k pois _source/$FILENAME > _source/aed_crowdsav.csv

### Download HTML-Tabelle von defikoeln.de
SOURCE_URL="http://www.defikoeln.de/defi-in-koeln/standorte-nach-stadtbezirken/"
FILENAME="aed_defikoeln.html"
echo "Downloading defikoeln AEDs to _source/$FILENAME"
cd _source
rm $FILENAME
wget -q -U $USER_AGENT -O $FILENAME $SOURCE_URL
cd ..
