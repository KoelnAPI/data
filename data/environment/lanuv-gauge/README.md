Water gauge data from LANUV / Wasserpegeldaten vom LANUV
========================================================

This folder contains daily unverified water gauge values from various streams in Northrhine-Westfalia. Historic data collections starts on Jan 1, 2013.

Station information is contained in the files "gauge_stations.csv" and "gauge_stations.geojson". Station coordinates in the source appear to be coded in UTM32N format. They are converted to WGS84 (latitude/longitude) coordinates for the CSV and GeoJSON export.

Source data is not contained in the repository due to file size restrictions. The Original files can be downloaded and derivatives updated using the script "download.sh".

## Source

Landesamt für Natur, Umwelt und Verbraucherschutz (LANUV)

http://www.lanuv.nrw.de/wasser/pegeldaten.htm

## License

Unknown

## Beschreibung

Dieser Ordner enthält ungeprüfte Pegeldaten des LANUV mit täglichen Werten ab Januar 2013.

Stationsdaten sind in den Dateien "gauge_stations.csv" und "gauge_stations.geojson" enthalten. Die Stationskoordinaten in den Quelldaten sind im UTM32N-Format angegeben. Für die CSV- und Geo-JSON-Exporte werden sie in WGS84-Koordinaten (Längen- und Breitengrad) konvertiert.

Aufgrund der Dateigrößen sind die Originaldateien nicht im Repository enthalten. Diese können jedoch temporär mit dem Script "download.sh" herunter geladen werden, um die Derivate zu aktualisieren.
