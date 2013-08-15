# 
# Automatic triggering of all download scripts within this folder

MYDIR=`pwd`

for f in `find . -name "download.sh"`:
do
	cd `dirname $f`
	sh download.sh
	cd $MYDIR
done
