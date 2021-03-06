# Download script for downloading the source in the current folder.
#
# Execute this script from within the same directory as work directory, like this:
#   
#   sh ./download.sh


SOURCE_URL="http://www.offenedaten-koeln.de/sites/default/files/2913-10-11_shape_stadtviertel.zip"
NAME="Stadtviertel"
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
ogr2ogr -f GeoJSON stadtviertel_temp.geojson \
	"_source/$NAME/Stadtviertel.shp" \
	-t_srs "EPSG:4326"

# set 7 digits float precision, sort, indent
python ../../../tools/lessprecise/lessprecise.py \
	--indent 4 --sort 1 -o stadtviertel.geojson \
	stadtviertel_temp.geojson

# remove temp GeoJSON file
rm stadtviertel_temp.geojson

# Create KML
ogr2ogr -f KML stadtviertel.kml _source/$NAME/Stadtviertel.shp
