#!/bin/bash

# Download script for Cologne streets CSV data

NAME="streets"

curl -s http://www.offenedaten-koeln.de/node/569/download \
	|in2csv -f csv -s ";"|csvsort >> $NAME.csv
