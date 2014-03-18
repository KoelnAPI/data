LANUV Air Quality Data
======================

This folder shall contain air quality data from the environment agency of Northrhine-Westphalia (LANUV).

Currently it only holds metadata on measurement stations.

## Contents:

* `stations.csv` - Station list with it's LANUV id and very rough geo position. This list is generated (scraped) from the LANUV website using the script get_stations.py
* `stations_mapping.csv` - A mapping table from LANUV station identifiers to identifiers used by both the federal environment agency (Umweltbundesamt, UBA) and the European Environment Agency (EEA).

## A note on geo positions in `stations.csv`

The geo locations in `stations.csv` are derived from the LANUV website where they are given in degrees, minutes and seconds, with one second as the resolution. Tests have shown that they derive from the actual position by several 100 meters.

For geo positions that seem to be more accurate, use the mapping table (stations_mappings.csv) to find the according UBA entry for each station and then look up the station position in `../uba-arquality/stations.csv`.

## License

Should be free for any use by the terms of the german federal law on environmental information (Umweltinformationsgesetz, UIG).
