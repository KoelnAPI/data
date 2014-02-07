#!/bin/bash

# Download latest news from KVB website
# and make it available as proper data

SOURCE_URL="http://www.kvb-koeln.de/german/home/mofis_bahn.html"

cd _source/
wget -N -U --timeout=120 "Mozilla/1.0" $SOURCE_URL
cd ..

