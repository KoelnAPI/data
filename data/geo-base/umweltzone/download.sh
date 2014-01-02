# Download script for downloading the source in the current folder.
#
# Execute this script from within the same directory as work directory, like this:
#   
#   sh ./download.sh


SOURCE_URL="http://www.offenedaten-koeln.de/node/132/download"
NAME="Umweltzone"
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

# Workaround from September 26, 2013: rename files according to old version
mv _source/Umweltzone/Umweltzone_2012_OSM_Sep2013.dbf _source/Umweltzone/Umweltzone.dbf
mv _source/Umweltzone/Umweltzone_2012_OSM_Sep2013.prj _source/Umweltzone/Umweltzone.prj
mv _source/Umweltzone/Umweltzone_2012_OSM_Sep2013.sbn _source/Umweltzone/Umweltzone.sbn
mv _source/Umweltzone/Umweltzone_2012_OSM_Sep2013.sbx _source/Umweltzone/Umweltzone.sbx
mv _source/Umweltzone/Umweltzone_2012_OSM_Sep2013.shp _source/Umweltzone/Umweltzone.shp
mv _source/Umweltzone/Umweltzone_2012_OSM_Sep2013.shx _source/Umweltzone/Umweltzone.shx
