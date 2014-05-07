enviroCar Measurements
======================

[enviroCar](https://envirocar.org/) allows car owners to track engine sensor data
using mobile devices like smartphones. This data is collected, anonymized and
provided for analysis.

The sensor data contains values like driving speed, fuel consumption, rounds per minute, 
throttle percentage, CO2 emissions etc.

## Source

enviroCar (<https://envirocar.org/>)

## License

Data is provided under the terms of the [ODbL](http://opendatacommons.org/licenses/odbl/1.0/).

## The file measures.csv

This file contains measures as point data, one measure per line.

The last columns represent individual sensor measures. A current list of measures and
units of measures can be accessed via <https://envirocar.org/api/stable/phenomenons>.

## The script download.py

This script is used to create the file measures.csv by downloading data from the enviroCar API.
