# Download script for downloading the source in the current folder.
#
# Execute this script from within the same directory as work directory, like this:
#   
#   sh ./download.sh


SOURCE_URL="http://www.offenedaten-koeln.de/node/289/download"
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

# remove dots from within figures, replace seperator
echo "Creating improved version in $FILENAME"
perl -CSD -pe 'tr/\x{feff}//d' _source/$FILENAME > $FILENAME.tmp
cat $FILENAME.tmp|in2csv -f csv -d ";"  > $FILENAME
rm $FILENAME.tmp
