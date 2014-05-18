# Download script for downloading the source in the current folder.
#
# Execute this script from within the same directory as work directory, like this:
#   
#   sh ./download.sh


SOURCE_URL="http://www.offenedaten-koeln.de/sites/default/files/20140513_Wahllokale_geo.csv"
NAME="wahllokale"
FINAL_FOLDER=$NAME
FILENAME=${NAME}.csv
NEW_FOLDER=${NAME}_new
USER_AGENT="datahub-cgn/0.1"

# single file download
echo "Downloading $NAME to $FILENAME"
rm -rf ./_source/*
cd ./_source/
wget -q -U $USER_AGENT -O $FILENAME $SOURCE_URL
cd ..

# Create temporary GeoJSON
ogr2ogr -f GeoJSON \
	wahllokale_tmp.geojson \
	wahllokale.vrt \
	-t_srs "EPSG:4326"

# set 7 digits float precision, sort, indent
python ../../../tools/lessprecise/lessprecise.py \
	--indent 4 --sort 1 -o wahllokale.geojson \
	wahllokale_tmp.geojson

# remove temp GeoJSON file
rm wahllokale_tmp.geojson
