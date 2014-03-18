UBA Air Quality Data
====================

This folder shall contain air quality data from the federal environmental agency of Germany, the "Umweltbundesamt" (UBA).

Only data from stations in the Cologne region is mirrored here.

## Contents:

* Measurement values are contained in directory structure `<YYYYMM>/<station_id>/<pollutant>/<type>.json`. See below for details.
* `stations_complete.csv` - A complete list of all stations, including historic stations, including geo position
* `stations_active.csv` - Same schema as above, only containing active stations

Example JSON file (201402/DENW053/NO2/1SMW):

```json
{
    "20140201": [
        49,
        42,
        39,
        36,
        33,
        26,
        29,
        32,
        26,
        17,
        19,
        -999,
        22,
        22,
        22,
        19,
        32,
        53,
        53,
        42,
        51,
        35,
        25,
        20
    ],
 	...
}
```

Values of `-999` indicate missing values.

The pollutant codes are:

* PM1 - particle matter
* CO - carbon monoxyde
* O3 - ozone
* SO2 - 
* NO2 - 

The type codes are:

* 1SMW - one hour mean
* 8SMW - eight hour mean (moving average)
* 8TMAX - eight hour maximum
* 1TMW - one day mean
* 1TMAX - one day max

The unit of all measures is: µg/m³

## License

Should be free for any use by the terms of the german federal law on environmental information (Umweltinformationsgesetz, UIG).

## Fetching data

In order to acquire data for a month not yet contained in the repository, call the script get_values.py with the month as a parameter in YYYYMM format, for example:

    python get_values.py 201406

