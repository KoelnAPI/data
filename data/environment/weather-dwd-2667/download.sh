#!/bin/bash

ROOT=$(pwd)

URL1="http://www.dwd.de/bvbw/generator/DWDWWW/Content/Oeffentlichkeit/KU/KU2/KU21/klimadaten/german/download/tageswerte/kl__10513__hist__txt,templateId=raw,property=publicationFile.zip/kl_10513_hist_txt.zip"
URL2="http://www.dwd.de/bvbw/generator/DWDWWW/Content/Oeffentlichkeit/KU/KU2/KU21/klimadaten/german/download/tageswerte/kl__10513__akt__txt,templateId=raw,property=publicationFile.zip/kl_10513_akt_txt.zip"

# Load source files
rm -r _source
mkdir _source
mkdir _source/historic
mkdir _source/latest
curl -s $URL1 > _source/historic/historic.zip
curl -s $URL2 > _source/latest/latest.zip

# unzip source files
cd $ROOT/_source/historic
unzip historic.zip
rm historic.zip

cd $ROOT/_source/latest/
unzip latest.zip
rm latest.zip

cd $ROOT

# convert and merge CSV data

TXTFILE=$(find _source/historic -iname "produkt*.txt")
in2csv -f csv -S $TXTFILE|csvcut -C eor > weather-dwd-2667.csv

TXTFILE=$(find _source/latest -iname "produkt*.txt")
in2csv -f csv -S $TXTFILE|csvcut -C eor|tail -n+2 >> weather-dwd-2667.csv
