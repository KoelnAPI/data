# Download script for downloading the source in the current folder.
#
# Execute this script from within the same directory as work directory, like this:
#   
#   sh ./download.sh


SOURCE_URL="http://www.offenedaten-koeln.de/node/303/download"
NAME="bevoelkerung"
FINAL_FOLDER=$NAME
FILENAME=${NAME}.csv
USER_AGENT="datahub-cgn/0.1"

# creating SHA1 hash to compare before/after download
if [ -a _source/$FILENAME ]; then
    HASH=shasum.before
    shasum _source/$FILENAME > $HASH
fi

echo "Downloading $NAME to _source/$FILENAME"
rm -rf _source/*
mkdir -p _source
cd _source
wget -q -U $USER_AGENT -O $FILENAME $SOURCE_URL
cd ..

# Check SHA1 of new download
if [ -a $HASH ]; then
    shasum -c --status $HASH
    if [ $? -eq 0 ]; then
        echo "Source file hasn't changed"
        rm $HASH
        exit
    else
        echo "Source file has been updated"
        rm $HASH
    fi
fi

# standardize format, remove unnecessary columns
echo "Creating improved version in $FILENAME"
perl -CSD -pe 'tr/\x{feff}//d' _source/$FILENAME > $FILENAME.tmp
in2csv -f csv -d ";" -y 100000 $FILENAME.tmp > $FILENAME.tmp2 && rm $FILENAME.tmp
csvcut -C 2,3,11,12 $FILENAME.tmp2 > $FILENAME.tmp3 && rm $FILENAME.tmp2
mv $FILENAME.tmp3 $FILENAME
