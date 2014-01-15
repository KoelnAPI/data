# Download script for downloading the source in the current folder.
#
# Execute this script from within the same directory as work directory, like this:
#   
#   sh ./download.sh


SOURCE_URL="http://www.offenedaten-koeln.de/sites/default/files/2014_Flaechennutzungsplan.zip"
NAME="Flaechennutzungsplan"
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

SHAPEFILES=( \
	"abgrabungszone" \
	"fnp_agl" \
	"fnp_aktuell" \
	"naturschutz" \
	"sanierungsgebiete" \
	"signet_aktuell" \
	"tunnel" \
	"VerkehrNachricht" \
)

for shapefile in "${SHAPEFILES[@]}"
do
	echo "Converting $shapefile"

	# Create temporary GeoJSON
	ogr2ogr -f GeoJSON $shapefile_temp.geojson \
		"_source/$NAME/$shapefile.shp" \
		-t_srs "EPSG:4326"

	# set 7 digits float precision, sort, indent
	python ../../../tools/lessprecise/lessprecise.py \
		--indent 4 --sort 1 -o $shapefile.geojson \
		$shapefile_temp.geojson
	
	# remove temp GeoJSON file
	rm $shapefile_temp.geojson
	
	# Create KML
	ogr2ogr -f KML $shapefile.kml _source/$NAME/$shapefile.shp
done

# Create CSV version of the main layer
ogr2ogr -f CSV fnp_aktuell_temp.csv \
	"_source/$NAME/fnp_aktuell.shp"
csvsort fnp_aktuell_temp.csv > fnp_aktuell.csv
rm fnp_aktuell_temp.csv