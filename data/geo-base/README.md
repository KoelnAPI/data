Geographical Base Data / Geografische Basisdaten
================================================

## Description

Basic geodata for Cologne, e.g. city districts. In addition to the original offerings,
this folder contains GeoJSON and KML versions in WGS84 coordinates with unmodified level
of detail.


## Beschreibung

Geografische Basisdaten wie z.B. Stadtteile und Stadtbezirke. Zusätzlich zu den Originaldaten
werden hier GeoJSON und KML Exporte der Grenzen angeboten. Das Detail-Level ist gegenüber
den Originaldaten unverändert.


## Source / Attribution / License

All data courtesy of Stadtverwaltung Köln.

Source Links:

* [Stadtbezirke/City districts](http://www.offenedaten-koeln.de/offene-daten/?did=14)
* [Stadtteile](http://www.offenedaten-koeln.de/offene-daten/?did=15)
* [Stadtviertel](http://www.offenedaten-koeln.de/offene-daten/?did=58)
* [Straßen](http://www.offenedaten-koeln.de/offene-daten/?did=63)
* [Straßenabschnitte](http://www.offenedaten-koeln.de/offene-daten/?did=64)
* [Straßenknoten](http://www.offenedaten-koeln.de/offene-daten/?did=65)
* [Umweltzone](http://www.offenedaten-koeln.de/offene-daten/?did=31)
* [Stimmbezirke](http://www.offenedaten-koeln.de/offene-daten/?did=48)
* [Bundestagswahlkreise](http://www.offenedaten-koeln.de/offene-daten/?did=47)

All data in this folder is licensed under CC-BY license by the Cologne city administration.

## Open tasks

* Write automated conversion from shapefile to GeoJSON, KML
* Create topoligically correct simplified versions for faster display on the web
* Create TopoJSON versions
* Check automatically for updates on source site
* Add [Address data](http://www.offenedaten-koeln.de/offene-daten/?did=60) in a meaningful format (point data with GeoJSON weighing more than 80 MB and KML above 150 MB)


## Detailed folder contents

* stadtbezirke: Highest level city districts as polygons
* stadtteile: Second level city districts as polygons
* stadtviertel: Neighbourhoods as polygons
* strassen: Streets as paths (lines)
* strassenabschnitte: Street segments as paths (lines)
* strassenknoten: Street nodes, e.g. crossings (point data)
* stimmbezirke: Election districts (smallest units) as polygons
* umweltzone: Environmental (air) protection zone boundaries as polygons
* wahlkreise_bundestag: Election districts (largest units) for the Bundestagswahl 2013 as polygons

Folder named "_source" contains original, unmodified data as downloaded from the source site
