# 
# Automatic triggering of all download scripts within this folder

MYDIR=`pwd`

for f in `find . -name "download_live*"`:
do
	cd `dirname $f`
	sh `basename $f`
	cd $MYDIR
done
