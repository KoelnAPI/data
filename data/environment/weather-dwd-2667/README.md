Daily Weather data from Cologne/Bonn airport / Tägliche Wetterdaten vom Flughafen Köln/Bonn
===========================================================================================

## Description

Historic weather records from Cologne/Bonn airport (EDDK), acquired from [DWD](http://www.dwd.de/).

The records have a daily interval, starting in September 1957.

CSV files in this folder contain the following columns:

* Stations_ID
* Mess_Datum: Date in the format "YYYYMMDD"
* Qualitaets_Niveau: An integer (1, 3, 5, 7, 10) indicating the data quality level
* BEDECKUNGSGRAD: Cloud coverage level as a float between 0.0 and 8.0
* REL_FEUCHTE: Relative humidity as percentage float
* DAMPFDRUCK: Unknown ("steam pressure"), float between 1.3 and ~23.2
* LUFTTEMPERATUR: Air temperature in degrees Celsius, float
* LUFTDRUCK_STATIONSHOEHE: Air pressure, float
* WINDGESCHWINDIGKEIT: Wind speed, probably in meters/second
* LUFTTEMP_AM_ERDB_MINIMUM: Ground temperature minimum
* LUFTTEMPERATUR_MINIMUM: Air temperature minimum
* LUFTTEMPERATUR_MAXIMUM: Air temperature maximum
* WINDSPITZE_MAXIMUM: Wind speed maximum
* NIEDERSCHLAGSHOEHE_IND: Unknown indicator, values 0, 1, 6, 7, 8
* NIEDERSCHLAGSHOEHE: Percitipation level, probably in millimeters
* SONNENSCHEINDAUER: Sunshine duration in hours
* SCHNEEHOEHE: Snow level

## Beschreibung

Wetterdaten vom Flughafen Köln/Bonn (EDDK), bezogen vom Deutschen Wetterdienst (DWD)

Es handelt sich um tägliche Mittelwerte. Die Zeitreihe beginnt im September 1959.

Quelle: http://www.dwd.de/bvbw/appmanager/bvbw/dwdwwwDesktop?_nfpb=true&_pageLabel=_dwdwww_klima_umwelt_klimadaten_deutschland&T82002gsbDocumentPath=Navigation%2FOeffentlichkeit%2FKlima__Umwelt%2FKlimadaten%2Fkldaten__kostenfrei%2Fausgabe__tageswerte__node.html%3F__nnn%3Dtrue

## License

Unknown

## Tools

The script download.sh can be used to acquire the latest source data.

## Updates

Data updates will be committed on an irregular basis.
