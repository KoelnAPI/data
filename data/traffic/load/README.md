# Traffic load / Verkehrsauslastung

Quelle/source: Stadt Köln

http://www.offenedaten-koeln.de/offene-daten/?did=20

Lizenz/License: Creative Commons CC-BY 3.0

## Beschreibung

Daten zur Verkehrsauslastung auf ausgewählten Straßen(-abschnitten) im Kölner Stadtgebiet.

Es handelt sich um Aufzeichnungen von Daten, die von der oben genannten API der Stadt Köln ausgegeben werden. Die Aufzeichnung erfolgt regelmäßig im Abstand von 5 Minuten. Verantwortlich für die Aufzeichnung und die nachträgliche Prüfung ist Marian Steinbach.

Im Ordner _source wird je Monat ein CSV-Download zur Verfügung gestellt.

Die Spalten der CSV-Dateien haben die folgende Bedeutung:

* datetime_utc: Datum und Uhrzeit in UTC (muss für die Ermittlung der lokalen Zeit umgerechnet werden)
* identifier: Kennung des Straßenabschnitts, wie von der API ausgegeben
* auslastung: Zahlenwert für die Auslastung, wie von der API ausgegeben
* valid: Zahl 1 oder 0. Hier wird in einigen Fällen nachträglich eine 0 vergeben, wenn die Erhebung nachweislich gestört war.

Details zu den Straßenabschnitten können der Datei street_segments.geojson entnommen werden.
