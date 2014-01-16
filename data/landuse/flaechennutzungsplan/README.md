Flächennutzungsplan / Zoning Plan
=================================

## Beschreibung

Dieser Ordner enthält Daten des offiziellen Flächennutzungsplans der Stadt Köln.

Über den Flächennutzungsplan:

	"Der Flächennutzungsplan (FNP) umfasst das gesamte Stadtgebiet und stellt
	auf der Ebene der vorbereitenden Bauleitplanung dessen vorhandene und
	geplante Nutzung dar. Die Aussagen dieses Plans beziehen sich auf die
	beabsichtigte städtebauliche Entwicklung für einen längeren Zeitraum
	(i.d.R. zwischen 10 und 15 Jahre). Der Flächennutzungsplan entwickelt
	keine unmittelbaren Rechtswirkungen gegenüber den Bürgern, insbesondere
	schafft er kein Baurecht. Er ist verwaltungsinterne Vorgabe für
	nachfolgende Bebauungspläne sowie für Planungen anderer Planungsträger
	und Fachbehörden. Darüber hinaus ist er behördenverbindliche Vorgabe
	zur Steuerung des Baugeschehens im Außenbereich. Zum Flächennutzungsplan
	und seinen Änderungen gehören Anlagepläne und Erläuterungstexte, in dem
	die Plandarstellungen ausführlich dargestellt werden. Die Aktualisierung
	des FNP erfolgt auf Ratsbeschluss."

Im Ordner `_source` befinden sich die Original-Dateien. Hier im selben Ordner sind zudem einige davon abgeleitete Dateien wie GeoJSON, KML (mit WGS84-Koordinaten) und CSV zu finden.

Die Geodaten umfassen diverse Layer:

### abgrabungszone

### fnp_agl

### fnp_aktuell

In diesem Layer ist das gesamte Stadtgebiet nahtlos in Polygone aufgeteilt, die Informationen über die Flächennutzung geben. Ein Auszug der darin enthaltenen Attribute:

* `TYP`: 23 verschiedene Kategorien wie z.B. "Grün", "GBFL", "W", "GE" und "Wasser".
* `ZWECK`: 44 verschiedene Kategorien wie z.B. "Hafen", "großfl. E.H.+z.S.", "Messe", "Camping", "Soz. Einricht."
* `LABEL1`: 12 verschiedene Werte wie z.B. "W", "GE", "M", "SO", "GI".
* `subtype`: 22 verschiedene numerische Werte
* `TYPspezial`: Die Kategorien "Veranstaltungen", "Golf" und "Stellplätze"


### naturschutz

### sanierungsgebiete

### signet_aktuell

### tunnel

### VerkehrNachricht


## Quelle / Lizenz

Quelle: Stadt Köln, http://www.offenedaten-koeln.de/dataset/fl%C3%A4chennutzungsplan

Lizenz: Creative Commons Namensnennung 3.0 Deutschland Lizenz

## Description

This folder contains official zone planning data for the City of Cologne.

The subfolder `_source` contains the original data source. This folder here holds derivates such as GeoJSON, KML (using WGS84 coordinates) and CSV.

## Source / License

Source: Stadt Köln, http://www.offenedaten-koeln.de/dataset/fl%C3%A4chennutzungsplan

License: Creative Commons Namensnennung 3.0 Deutschland Lizenz