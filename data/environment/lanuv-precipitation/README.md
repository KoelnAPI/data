Precipitation data from LANUV / Niederschlagsdaten vom LANUV
============================================================

Hourly precipitation sum values (rain, snow) measured at stations
throughout NRW.

`stations.csv` and `stations.geojson` contain information on
measurement stations.

`values.csv` contains hourly sum values.

## Source

Landesamt für Natur, Umwelt und Verbraucherschutz (LANUV)

http://www.lanuv.nrw.de/wasser/niederschlag/nieder.htm

## License

Unknown

## Beschreibung

Stündliche Niederschlagsdaten von Messstationen in NRW.

`stations.csv` und `stations.geojson` enthalten Daten zu den Stationen.

`values.csv` enthält die stündlichen Summenwerte.

## Tools

### Download script `download.sh`

Downloads all data and merges new values into `values.csv`.
Call without arguments like this:

    sh download.sh
