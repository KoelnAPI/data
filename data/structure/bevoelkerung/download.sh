# Download script for downloading the source in the current folder.
#
# Execute this script from within the same directory as work directory, like this:
#   
#   sh ./download.sh


SOURCE_URL="http://www.offenedaten-koeln.de/wp-content/plugins/download-monitor/download.php?id=22"
NAME="bevoelkerung"
FINAL_FOLDER=$NAME
FILENAME=${NAME}.csv
USER_AGENT="datahub-cgn/0.1"

echo "Downloading $NAME to _source/$FILENAME"
rm -rf _source/*
mkdir -p _source
cd _source
wget -q -U $USER_AGENT -O $FILENAME $SOURCE_URL
cd ..

# standardize format, remove unnecessary columns
echo "Creating improved version in $FILENAME"
FILENAME=bevoelkerung.csv
perl -CSD -pe 'tr/\x{feff}//d' _source/$FILENAME > $FILENAME.tmp
in2csv -f csv -d ";" $FILENAME.tmp > $FILENAME.tmp2 && rm $FILENAME.tmp
csvcut -C 2,3,11,12 $FILENAME.tmp2 > $FILENAME.tmp3 && rm $FILENAME.tmp2
mv $FILENAME.tmp3 $FILENAME
