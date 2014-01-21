Flächennutzungsplan / Zoning Plan
=================================

## Beschreibung

Dieser Ordner enthält Daten des offiziellen Flächennutzungsplans der Stadt Köln.

Der [Flächennutzungsplan](http://de.wikipedia.org/wiki/Fl%C3%A4chennutzungsplan) ist ein Planungsinstrument, mit dem die städtebauliche Entwicklung gesteuert werden soll. Neben dem Bebauungsplan ist der Flächennutzungsplan Teil der Bauleitplanung. Inhalte sowie Verfahren sind in §§ 5, 6 und 7 des [Baugesetzbuches](https://github.com/bundestag/gesetze/blob/master/b/bbaug/index.md) geregelt.

Die Stadt Köln über den Flächennutzungsplan:

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

Die Auszeichnung der verschiedenen Inhalte wird in der [Planzeichenverordnung](http://www.dr-frank-schroeter.de/planzv.htm#Anlage) (PlanZV) geregelt.

Im Ordner `_source` befinden sich die Original-Dateien. Hier im selben Ordner sind zudem einige davon abgeleitete Dateien wie GeoJSON, KML (mit WGS84-Koordinaten) und CSV zu finden.

Die Geodaten umfassen diverse Layer, deren Bedeutung nur zum Teil ersichtlich ist.

### abgrabungszone

### fnp_agl

### fnp_aktuell

In diesem Layer ist das gesamte Stadtgebiet nahtlos in Polygone aufgeteilt, die Informationen über die Flächennutzung geben. Ein Auszug der darin enthaltenen Attribute:

* `TYP`: Nutzungskategorien wie z.B. "Grün", "GBFL", "W", "GE" und "Wasser".
* `subtype`: numerische Nutzungskategorien
* `Langname`: Offenbar die ausführliche Bezeichnung des Typs, z.B. "Gemeinbedarfsfläche" für "GBFL"
* `ZWECK`: Optionale Freitext-Beschreibung der Nutzung, z.B. "Hafen", "Messe" etc.
* `LABEL1`: Planzeichen, 12 verschiedene Werte wie z.B. "W", "GE", "M", "SO", "GI", nicht für jede Fläche vergeben
* `TYPspezial`: Offenbar Unterkategorien für bestimmte Flächen. Es gibt aktuell die Werte "Veranstaltungen", "Golf" und "Stellplätze"

Die Kategorisierung nach TYP > subtype > Langname ergibt die folgende Hierarchie:

    bahn
      12
        Fläche für Bahnanlagen
    flug
      15
        Fläche für die Luftfahrt
    GBFL
      11
        Gemeinbedarfsfläche
    GE
      3
        Gewerbefläche
    GI
      4
        Industriefläche
    Grün
      5
        Grünfläche mit tw. landwirtschatl. Nutzung
      12
        Fläche für Bahnanlagen
    GrünSpezial
      22
        Grünfläche mit besonderer Nutzung
    Landwi
      6
        Fläche für Landwirtschaft
    M
      2
        Gemischte Baufläche
        Mischfläche
    MI
      16
        Mischbaufläche
        Mischgebiet
    MK
      15
        Kerngebiet
    NS
      13
        Fläche für Hauptverkehrszüge
    S
      10
        Sonderbaufläche
    san
      21
        Sanierungsgebiet
    SO
      17
        Sonderbaufläche
    verkehr
      13
        Fläche für Hauptverkehrszüge
    Versor
      9
        Fläche für Ver- und Entsorgung
    Versorg
      9
        Fläche für Ver- und Entsorgung
    W
      0
        Wohnbaufläche
      19
        Wohnbaufläche(zurückgestellt)
    Wald
      7
        Fläche für die Forstwirtschaft (Erholungswald)
    Wasser
      8
        Wasserfläche
    WB
      1
        Besonderes Wohngebiet
    WEA
      20
        Fläche für Windenergieanlagen


Die Attribute der Original-Shapedatei sind im Zeichensatz ISO-8859-1 gepspeichert.

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