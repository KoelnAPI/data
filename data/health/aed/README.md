Defibrillatoren / AED
=====================

*(Information in English below)*

In diesem Bereich werden Standort-Daten zu Defibrillatoren, auch AED ("Automatisierter Externer Defibrillator) genannt, aus verschiedenen Quellen gesammelt und gemeinsam zur Verfügung gestellt.

Weitere Informationen: http://wiki.koelnapi.de/w/Defibrillatoren

## Lizenz

Public Domain: Die Daten sind frei von Urheberrechten und können ohne Einschränkung verwendet werden.

## Die Datei `aed.csv`

Die Datei aed.csv ist das Herzstück unserer konsolidierten Datensammlung. Hier sollen alle neue Standorte eingetragen werden und nach und nach mit weiteren Details versehen werden.

Zur Bedeutung der Spalten:

* `id`: Eindeutige ID zur Kennzeichnung des Defi(-standorts), vergeben von Köln API
* `city_district`: Name des Stadtbezirks
* `city_subdistrict`: Name des Stadtteils
* `name`: Name des Standorts/Gebäudes. Dieser soll möglichst knapp und so beschrieben sein, dass jemand im direkten Umfeld das Gebäude identifizieren kann.
* `location_details`: Beschreibung des Standorts innerhalb des Gebäudes
* `address`: Straße und Hausnummer des Gebäudes
* `postalcode`: Postleitzahl
* `opening_hours`: Öffnungszeiten
* `longitude`: Geografischer Längengrad (WGS84-Koordinatensystem)
* `latitude`: Geografischer Breitengrad (WGS84-Koordinatensystem)
* `osm_node_id`: Falls dieser Standort bereits in der OpenStreetMap eingetragen ist, wird hier die ID des Knotens erfasst
* `aedkatasternet_id`: ID dieses Standaorts bei aed-kataster.net
* `definow_id`: ID dieses Standaorts bei definow.org
* `aed4eu_id`: ID dieses Standorts bei AED4.EU
* `crowdsav_id`: ID dieses Standorts bei CrowdSav
* `source`: Quelle, aus der der Eintrag stammt
* `last_edited`: Datum und ggf. Uhrzeit der letzten Bearbeitung
* `last_edited_by`: Name des letzten Bearbeiters
* `comment`: Bearbeitungskommentar (nur angeben falls nötig)

Zu aed-kataster.net: http://aed-kataster.net/
Zu AED4EU: http://aed4.eu/
Zu CrowdSav: https://www.crowdsav.com/aeds
Zu Defi Now!: https://www.definow.org/

## Derivate `aed.geojson` und `aed.min.geojson`

Diese beiden Dateien werden mit dem Script `csv_to_geojson.py` aus aed.csv abgeleitet. Sie enthalten alle Standorte, die bereits mit Geoinformationen (Spalten longitude und latitude) versehen sind, im GeoJSON-Format.

Die Datei `aed.min.geojson` ist inhaltlich identisch mit `aed.geojson`, jedoch kompakter weil ohne Einrückung.

## Der Ordner `_source`

In diesem Ordner werden unveränderte Kopien von Dateien abglegt, die wir aus verschiedenen Quellen zusammen tragen.

* `_source/aed_crowdsav.json`: Standortdaten von [CrowdSav](https://www.crowdsav.com/aeds) im Original
* `_source/aed_crowdsav.csv`: Standortdaten von [CrowdSav](https://www.crowdsav.com/aeds) in CSV konvertiert
* `_source/aed_defikoeln.html`: Standortdaten von [defiköln](http://www.defikoeln.de/defi-in-koeln/standorte-nach-stadtbezirken/)
* `_source/aed_stadt_koeln.csv`: Standortdaten der [Stadt Köln](http://www.offenedaten-koeln.de/dataset/defibrillatoren-stadt-k%C3%B6ln). Lizenz: Creative Commons Namensnennung ([CC-BY 3.0](http://creativecommons.org/licenses/by/3.0/de/))

## Der Ordner `todo`

Hier werden Listen mit noch ungeprüften, möglichen Standortdaten hinterlegt.

Hinweis für Bearbeiter: Bitte Einträge darin löschen, sobald sie in aed.csv übernommen wurden.

## Die Datei [aed_not_existent.md](aed_not_existent.md)

Diese Liste enthält von uns geprüfte Standorte, an denen möglicherweise
früher einmal ein AED zu finden war, nun aber nicht mehr. Wir sammeln diese
Information, um die Entfernung solcher Einträge aus anderen Datenbanken
zu erleichtern und eine aufwändige, mehrfache Prüfung zu vermeiden.


## Haftungsausschluss

Die Daten werden ohne jegliche Garantie der Richtigkeit oder Vollständigkeit veröffentlicht.


## FAQ

### Ich kenne einen Defibrillator-Standort. Was soll ich tun?

1. Bitte sieh in der Datei `aed.csv` nach, ob der Standort in der Datei schon erfasst ist. Wenn ja, brauchst Du nichts weiter zu tun.
2. Ist der Standort noch nicht erfasst, dann teile uns bitte den Standort mit. Siehe dazu die nächste Frage "Wie kann ich einen Defibrillator-Standort melden?"

### Wie kann ich einen Defibrillator-Standort melden?

Dazu gibt es mehrere Möglichkeiten. Der für uns einfachste:

1. Forke dieses Repository hier auf GitHub.
2. Füge am Ende von `aed.csv` einen neuen Eintrag hinzu. Fülle dabei alle Felder aus, die Du ausfüllen kannst.
3. Speichere die Datei und "committe" die Änderung ins Repository.
4. Sende die Änderung als Pull Request an uns.

Falls Dir das zu kompliziert vorkommt, kannst Du uns auch eine E-Mail schreiben.

1. Bitte nenne mindestens die Adresse des Standorts.
2. Maile das ganze an `marian AT sendung PUNKT de`.

### Wie kann ich Änderungen an einem Defibrillator-Standort melden?

Dies ist die bevorzugte Methode:

1. Forke dieses Repository hier auf Github.
2. Bearbeite den entsprechenden Eintrag in der Dtaei `aed.csv`.
3. Speichere die Datei und "committe" die Änderung ins Repository.
4. Sende die Änderung als Pull Request an uns.

Oder Du schreibst eine E-Mail.

1. Bitte nenne unbedingt die ID des Eintrags (erste Spalte in `aed.csv`).
2. Sag uns genau, was sich ändern muss.
3. Maile das ganze an `marian AT sendung PUNKT de`.

### Ich möchte einen Defibrillator-Standort in die OpenStreetMap eintragen. Was muss ich tun?

1. Du benötigst ein Benutzerkonteo auf http://www.openstreetmap.org/.
2. Sobald Du eingeloggt bist, kannst Du auf http://www.openstreetmap.org/ an der richtigen Position auf den Button "Bearbeiten" klicken. Damit aktivierst Du die Bearbeitungsfunktionen von OSM.
3. Sieh nach, ob es schon einen geigneten Punkt (node) für den Defibrillator-Standort gibt. Bei einer kleinen Sparkassen-Filiale beispielsweise könnte es reichen, diesen mit einem zusätzlichen Tag zu versehen.
4. Sollte es keinen geeigneten Punkt geben, lege einen neuen Punkt mit der richtigen Position an.
5. Versieh den entsprechenden Punkt mit dem Tag `emergency=defibrillator`.
6. Merke Dir die ID des Punkts, den Du bearbeitest. Diese kannst Du herausfinden, wenn Du im Web-Editor den Punkt markierst und dann unten links auf den Link "Auf openstreetmap.org ansehen" klickts.
7. Sende die Änderung an OSM. Im Änderungskommentar kannst Du als Quelle diese Seite angeben.
8. Forke dieses Repository hier auf Github.
9. Bearbeite den Eintrag des Defibrillators in der Dtaei `aed.csv` und trage in der Spalte `osm_node_id` die ID des Punkts ein, die Du in Schritt 6 herausgefunden hast.
10. Speichere die Datei und "committe" die Änderung ins Repository.
11. Sende die Änderung als Pull Request an uns.

Die Schritte 8 bis 11 dienen als Rückmeldung an uns. Wenn Dir die Schritte 8 bis 11 zu kompliziert vorkommen, kannst Du uns auch eine Nachricht schicken. Siehe dazu weiter oben "Wie kann ich Änderungen an einem Defibrillator-Standort melden?".


# Information in English


## Description

Here we collect location data on AEDs. Additional information in German:

http://wiki.koelnapi.de/w/Defibrillatoren


## License

Public Domain, no rights reserved.


## The file `aed.csv`

This is the centerpiece of this data collection. It contains consolidated AED location information. Every location we know about shall have an entry in this file. More details an be acquired per entry over time.

The column schema:

* `id`: Unique identifier we (Köln API) assign to each entry
* `city_district`: Name of the city district
* `city_subdistrict`: Name des city sub district
* `name`: Descriptive name of the AED location, e.g. building name
* `location_details`: Optional description of the AED location, e.g. inside the building
* `address`: street and house number of the position
* `opening_hours`: Opening hours (if applicable)
* `longitude`: geographic longitude (WGS84 coordinate referene system)
* `latitude`: geographic latitude (WGS84 coordinate referene system)
* `osm_node_id`: ID of the OSM node of this location, in case the AED is already mapped in OSM
* `aed4eu_id`: ID of this AED location in the AED4EU database
* `crowdsav_id`: ID of this AED location at CrowdSav
* `source`: Origin of this entry
* `last_edited`: Date if last edit
* `last_edited_by`: Name of the last editor
* `comment`: Optional editors comment

More about AED4EU: http://aed4.eu/
More about CrowdSav: https://www.crowdsav.com/aeds

## The folder `_source`

In this folder we hold and track copies of the data we download from different sources.

* `_source/aed_crowdsav.json`: Location data from [CrowdSav](https://www.crowdsav.com/aeds)
* `_source/aed_crowdsav.csv`: Location data from CrowdSav converted to CSV
* `_source/aed_defikoeln.html`: Location data from [defiköln](http://www.defikoeln.de/defi-in-koeln/standorte-nach-stadtbezirken/)
* `_source/aed_stadt_koeln.csv`: Location data from the [City of Cologne](http://www.offenedaten-koeln.de/dataset/defibrillatoren-stadt-k%C3%B6ln). License: Creative Commons Attribution ([CC-BY 3.0](http://creativecommons.org/licenses/by/3.0/de/))


## Die Datei [aed_not_existent.md](aed_not_existent.md)

This is a list of places where **no AED** can be found. They
might have been announced in the past, but the AED has meanwhile
been removed etc. We maintain this list for future reference,
since outdated records are still spread out over variaous data
stores.


## Disclaimer

The data is provided without warranty of any kind, express or implied, including but not limited to the warranties of completeness or correctness.
