#!/bin/bash


### Download der CSV-Datei der Stadt Köln

SOURCE_URL="http://www.offenedaten-koeln.de/node/592/download"
NAME="aed_stadt_koeln"
FINAL_FOLDER=$NAME
FILENAME=${NAME}.csv
USER_AGENT="datahub-cgn/0.1"

# creating SHA1 hash to compare before/after download
if [ -a _source/$FILENAME ]; then
    HASH=shasum.before
    shasum _source/$FILENAME > $HASH
fi

echo "Downloading $NAME to _source/$FILENAME"

cd _source
rm $FILENAME
wget -q -U $USER_AGENT -O $FILENAME $SOURCE_URL
cd ..

# Check SHA1 of new download
if [ -a $HASH ]; then
    shasum -c --status $HASH
    if [ $? -eq 0 ]; then
        echo "Source file hasn't changed"
        rm $HASH
        exit
    else
        echo "Source file has been updated"
        rm $HASH
    fi
fi


### / ENDE Download der CSV-Datei der Stadt Köln