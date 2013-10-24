Weather data from Cologne/Bonn airport / Wetterdaten vom Flughafen Köln/Bonn
============================================================================

## Description

Historic weather records from Cologne/Bonn airport (EDDK), acquired from [OpenWeatherMap](http://openweathermap.org/).

The records should have an hourly interval, however some intervals are empty.

The data collection has been started in October 2013 and dates back until some day in June 2012.

CSV files in this fodler contain the following columns:

* timestamp: Unix timestamp for the hour interval
* hum_count: Number of humidity measures within the interval
* hum_min: Minimum relative humidity (percent) within interval
* hum_max: Maximum relative humidity (percent) within interval
* hum_mean: Average relative humidity (percent) within interval
* press_count: Number of pressure measures within the interval
* press_min: Minimum pressure (hpa) within interval
* press_max: Maximum pressure (hpa) within interval
* press_mean: Average pressure (hpa) within interval
* temp_count: Number of temperature measures within interval
* temp_min: Minimum temperature (degrees Kelvin) within interval
* temp_max: Maximum temperature (degrees Kelvin) within interval
* temp_mean: Average temperature (degrees Kelvin) within interval
* windspeed_count: Number of wind speed measures within interval
* windspeed_min: Minimum Wind speed (m/s) within interval
* windspeed_max: Maximum Wind speed (m/s) within interval
* windspeed_mean: Average Wind speed (m/s) within interval
* winddir: Wind direction (degrees)

## Beschreibung

Wetterdaten vom Flughafen Köln/Bonn (EDDK), bezogen über die API von [OpenWeatherMap](http://openweathermap.org/).

Die Daten sollten stündliche Intervalle repräsentieren, einige Intervalle fehlen jedoch.

Die Datensammlung wurde im Oktober 2013 gestartet und reicht zurück bis in den Juni 2012. Weiter zurück liegende Zeiträume sind über OpenWeatherMap aktuell leider nicht abrufbar.

## License

Data is licensed under CC-BY-SA 2.0 by [OpenWeatherMap](http://openweathermap.org/).

## Tools

The script get_data.py can be used to acquire more recent data or specific time spans. Examples:

    # get all available records for October 2013
    python get_data.py 201310

    # get records for October 8, 2013
    python get_data.py 20131008

    # get records for October 8 to 13, 2013
    python get_data.py 20131008-20131013

## Updates

Data updates will be committed on an irregular basis.
