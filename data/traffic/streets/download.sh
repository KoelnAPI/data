#!/bin/bash

# Download script for Cologne streets CSV data

NAME="streeets"

curl -s http://offenedaten-koeln.de/sites/default/files/2013-01-01_Stra%C3%9Fenverzeichnis_Standard.csv \
	|in2csv -f csv -s ";"|csvsort >> $NAME.csv
