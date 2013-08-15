# Download script for downloading the source in the current folder.
#
# Execute this script from within the same directory as work directory, like this:
#   
#   sh ./download.sh


SOURCE_URL="http://www.offenedaten-koeln.de/wp-content/plugins/download-monitor/download.php?id=34"
NAME="result_stadtteil"
FINAL_FOLDER=$NAME
FILENAME=${NAME}.csv
NEW_FOLDER=${NAME}_new
USER_AGENT="datahub-cgn/0.1"

# single file download
echo "Downloading $NAME - $FILENAME to $NEW_FOLDER"
mkdir _source
rm -rf ./_source/*
cd ./_source/
wget -U $USER_AGENT -O $FILENAME $SOURCE_URL
cd ..
