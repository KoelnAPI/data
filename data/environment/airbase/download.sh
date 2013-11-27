echo "Downloading station data"
wget http://ftp.eea.europa.eu/www/AirBase_v7/AirBase_v7_stations.zip
unzip AirBase_v7_stations.zip

echo "Downloading measurement data"
wget http://ftp.eea.europa.eu/www/AirBase_v7/AirBase_v7_statistics.zip
unzip AirBase_v7_statistics.zip

# Stations in Cologne
echo "Extracting stations in Cologne"
echo "id,name,operator,longitude,latitude" > stations.csv
in2csv -t -e "utf-8" AirBase_v7_stations.csv|csvgrep -c 3 -m "DE"|grep "Köln, Stadt"|csvcut -c 1,5,19,13,14 >> stations.csv

# short file with all measures from NRW
echo "Generating shortened measures file"
head -n 1 AirBase_v7_statistics.csv > statistics_temp.csv
grep "DENW" AirBase_v7_statistics.csv >> statistics_temp.csv
in2csv -t -e "utf-8" statistics_temp.csv > statistics_temp2.csv

for station in $(csvcut -c 1 stations.csv|tail -n +2)
do
	echo "Extracting measurements for station $station"
	csvgrep -d "," -c 1 -m $station statistics_temp2.csv > $station.csv
done

# Clean up
rm statistics_temp*
rm AirBase_v7_statistics.*
rm AirBase_v7_stations.*