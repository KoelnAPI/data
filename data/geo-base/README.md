Geographical Base Data / Geografische Basisdaten
================================================

## Description

Basic geodata for Cologne, e.g. city districts. In addition to the original offerings,
this folder contains GeoJSON and KML versions in WGS84 coordinates with unmodified level
of detail.

Folder named "_source" contains original, unmodified data as downloaded from the source site

## Beschreibung

Geografische Basisdaten wie z.B. Stadtteile und Stadtbezirke. Zusätzlich zu den Originaldaten
werden hier GeoJSON und KML Exporte der Grenzen angeboten. Das Detail-Level ist gegenüber
den Originaldaten unverändert.

Die Unterordner mit dem Namen "_source" enthalten jeweils die unveränderten Originaldaten.


## Source / Attribution / License

All data courtesy of Stadtverwaltung Köln.

All data in this folder is licensed under CC-BY license by the Cologne city administration.


## Datensätze / data sets

### Stadtbezirke / city districts

Nine administrative districts of the city of Cologne.

([Source](http://www.offenedaten-koeln.de/offene-daten/?did=14))

### Stadtteile / sub districts

86 sub districts of the city of Cologne

([Source](http://www.offenedaten-koeln.de/offene-daten/?did=15))

### Stadtviertel / quarters

Some houring areas in Cologne are named quarters.

([Source](http://www.offenedaten-koeln.de/offene-daten/?did=58))

### Straßen / streets

All streets as line data including meta data. Each street is included
as the minimal number of lines. For example, the "Vogelsanger Straße"
is one line with length > 5000 meters.

([Source](http://www.offenedaten-koeln.de/offene-daten/?did=63))

### Straßenabschnitte / street segments

All streets as line data, without intersections. For example, the
street "Vogelsanger Straße" is split into 61 lines.

([Source](http://www.offenedaten-koeln.de/offene-daten/?did=64))

### Straßenknoten / street intersections

Every location where streets intersect, as point data. Including
meta data like, for example a attribute "TYP" containing values
like "Sackgassenendpunkt", "Einmündung" or "Kreuzung".

([Source](http://www.offenedaten-koeln.de/offene-daten/?did=65))

### Umweltzone / Low emission zone

Boundaries of the [low emission zones](https://de.wikipedia.org/wiki/Umweltzone), 
which implies limited traffic access, as polygon data.

([Source](http://www.offenedaten-koeln.de/offene-daten/?did=31))

### Stimmbezirke / voting districts (lowest level)

Boundaries of the voting districts, valid for all elections, as
polygon data.

([Source](http://www.offenedaten-koeln.de/offene-daten/?did=48))

### Bundestagswahlkreise / federal election districts

Boundaries of federal election districts.

([Source](http://www.offenedaten-koeln.de/offene-daten/?did=47))

### Wahllokale / Voting localities

Locations of the voting offices (for all elections) as point data,
including meta data, as CSV.

([Source](http://www.offenedaten-koeln.de/offene-daten/?did=74))


## Open tasks

* Write automated conversion from shapefile to GeoJSON, KML
* Create topoligically correct simplified versions for faster display on the web
* Create TopoJSON versions
* Check automatically for updates on source site
* Add [Address data](http://www.offenedaten-koeln.de/offene-daten/?did=60) in a meaningful format (point data with GeoJSON weighing more than 80 MB and KML above 150 MB)

