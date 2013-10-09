# 
# Automatic triggering of all download scripts within this folder

MYDIR=`pwd`

for f in `find . -iname "download.sh"`:
do
	cd `dirname $f`
	sh ./`basename $f`
	cd $MYDIR
done
