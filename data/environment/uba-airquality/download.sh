#!/bin/bash

# Download stations list form UBA
wget -O stations_raw.csv "http://www.env-it.de/stationen/public/download.do?event=euMetaStation"

# convert to proper CSV
tail -n+2 stations_raw.csv|in2csv -d ";" -e "ISO-8859-1" -f csv|csvcut -C "dem_status,_unnamed" > stations_complete.csv

# create list with active stations only (no end date)
csvgrep -c "station_end_date" -r "[0-9]" -i stations_complete.csv > stations_active.csv

# GeoJSON version
csvjson --lat station_latitude_d --lon station_longitude_d -k station_code -i 4 stations_active.csv > stations_active.geojson

# remove rest
rm stations_raw.csv