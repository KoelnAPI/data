# Download script for downloading the source in the current folder.
#
# Execute this script from within the same directory as work directory, like this:
#   
#   sh ./download.sh

# URL of shapefile download
SOURCE_URL="http://www.offenedaten-koeln.de/node/576/download"
NAME="Adressen"
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

# extra move for inner folder "Shape Adresse"
mv $NEW_FOLDER/Shape\ Adresse/* $NEW_FOLDER/
rm -rf $NEW_FOLDER/Shape\ Adresse
# end extra move

rm -rf $FINAL_FOLDER
mv $NEW_FOLDER $FINAL_FOLDER
cd ..
