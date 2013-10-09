# Download script for downloading the source in the current folder.
#
# Execute this script from within the same directory as work directory, like this:
#   
#   sh ./download.sh


SOURCE_URL="http://wahlen.stadt-koeln.de/Bundestagswahl11.csv"
NAME="result_stadtteil"
FINAL_FOLDER=$NAME
FILENAME=${NAME}.csv
NEW_FOLDER=${NAME}_new
USER_AGENT="datahub-cgn/0.1"

# single file download
echo "Downloading $NAME to $FILENAME"
test -d _source || mkdir _source
rm -rf ./_source/*
curl -s $SOURCE_URL > _source/$FILENAME

# remove dots from within figures, replace seperator
echo "Creating improved version in $FILENAME"
cat _source/$FILENAME|in2csv -f csv -d ";"  > $FILENAME
