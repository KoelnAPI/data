SOURCE_URL="http://www.offenedaten-koeln.de/wp-content/plugins/download-monitor/download.php?id=14"
FILENAME="Stadtbezirk.zip"
NEW_FOLDER="Stadtbezirk_new"
FINAL_FOLDER="Stadtbezirk"
USER_AGENT="datahub-cgn/0.1"

rm -r _source/$NEW_FOLDER
mkdir -p _source/$NEW_FOLDER
cd _source/$NEW_FOLDER
wget -U $USER_AGENT -O $FILENAME $SOURCE_URL
unzip $FILENAME
rm $FILENAME
cd ..
rm -r $FINAL_FOLDER
mv $NEW_FOLDER $FINAL_FOLDER
