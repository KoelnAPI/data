# Download script for downloading the source in the current folder.
#
# Execute this script from within the same directory as work directory, like this:
#   
#   sh ./download.sh


SOURCE_URL="http://offenedaten-koeln.de/sites/default/files/2013-06-25_shape_stadtteil_0.zip"
NAME="Stadtteil"
FINAL_FOLDER=$NAME
FILENAME=${NAME}.zip
NEW_FOLDER=${NAME}_new
USER_AGENT="datahub-cgn/0.1"

echo "Downloading $NAME - $FILENAME to $NEW_FOLDER"
rm -rf _source/$NEW_FOLDER
mkdir -p _source/$NEW_FOLDER
cd _source/$NEW_FOLDER
wget -q -U $USER_AGENT -O $FILENAME $SOURCE_URL
unzip -qq $FILENAME
rm $FILENAME
cd ..
rm -rf $FINAL_FOLDER
mv $NEW_FOLDER $FINAL_FOLDER
cd ..

# Create temporary GeoJSON
ogr2ogr -f GeoJSON stadtteile_temp.geojson \
	"_source/$NAME/Stadtteil.shp" \
	-t_srs "EPSG:4326"

# set 7 digits float precision, sort, indent
python ../../../tools/lessprecise/lessprecise.py \
	--indent 4 --sort 1 -o stadtteile.geojson \
	stadtteile_temp.geojson

# remove temp GeoJSON file
rm stadtteile_temp.geojson

# Create KML
ogr2ogr -f KML stadtteile.kml _source/$NAME/Stadtteil.shp
