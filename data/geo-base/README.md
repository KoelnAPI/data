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


## Source / Attribution

All data courtesy of Stadtverwaltung Köln.

Source Links:

* [Stadtbezirke/City districts](http://www.offenedaten-koeln.de/offene-daten/?did=14)
* [Stadtteile](http://www.offenedaten-koeln.de/offene-daten/?did=15)
* [Umweltzone](http://www.offenedaten-koeln.de/offene-daten/?did=31)
* [Stimmbezirke](http://www.offenedaten-koeln.de/offene-daten/?did=48)
* [Bundestagswahlkreise](http://www.offenedaten-koeln.de/offene-daten/?did=47)

## Open tasks

* Write automated conversion from shapefile to GeoJSON, KML
* Create topoligically correct simplified versions
* Check automatically for updates on source site


## Detailed folder contents

* _source: Original, unmodified data as downloaded from the City of Cologne
* stadtbezirke: Highest level city districts (Stadtbezirke)
* stadtteile: Second level city districts (Stadtbezirke)
* stimmbezirke: Election districts (smallest units)
* umweltzone: Environmental (air) protection zone
* wahlkreise_bundestag: Election districts (largest units) for the Bundestagswahl 2013
