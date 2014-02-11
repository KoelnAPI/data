#!/bin/bash

# Download latest news from KVB website
# and make it available as proper data

SOURCE_URL1="http://www.kvb-koeln.de/german/home/mofis_bahn.html"
SOURCE_URL2="http://www.kvb-koeln.de/german/home/mofis_bus.html"

cd _source/
curl -R -A "Mozilla/5.0" $SOURCE_URL1 > mofis_bahn.html
curl -R -A "Mozilla/5.0" $SOURCE_URL2 > mofis_bus.html
cd ..

