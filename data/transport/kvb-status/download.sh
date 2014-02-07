#!/bin/bash

# Download latest news from KVB website
# and make it available as proper data

SOURCE_URL="http://www.kvb-koeln.de/german/home/mofis_bahn.html"

# Seems to be necessary for KVB
USER_AGENT="Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/32.0.1700.107 Safari/537.36"
#USER_AGENT="Mozilla/5.0"

cd _source/
curl -R -A "Mozilla/5.0" $SOURCE_URL > mofis_bahn.html
cd ..

