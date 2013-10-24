# encoding: utf-8

import openweather
import daterangestr
import csv
import argparse
import sys


STATION_ID = 4885  # EDDK / Cologne/Bonn airport


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description='Download openweather data for EDDK for given date range')
    parser.add_argument('daterange',
        help='Date range in the format YYYYMM or YYYYMMDD-YYYYMMDD')
    args = parser.parse_args()
    if args.daterange is None:
        sys.stderr.write("You have to give a date range.")
        sys.exit()
    (start_date, end_date) = daterangestr.to_dates(args.daterange)
    ow = openweather.OpenWeather()
    print "Getting hourly values for %s to %s" % (start_date, end_date)
    hw = ow.get_historic_weather(STATION_ID, start_date, end_date)

    headers = [
        'timestamp',
        'hum_count',
        'hum_min',
        'hum_max',
        'hum_mean',
        'press_count',
        'press_min',
        'press_max',
        'press_mean',
        'temp_count',
        'temp_min',
        'temp_max',
        'temp_mean',
        'windspeed_count',
        'windspeed_min',
        'windspeed_max',
        'windspeed_mean',
        'winddir'
    ]
    filename = '%s.csv' % args.daterange
    print "Writing to %s" % filename
    with open(filename, 'wb') as csvfile:
        writer = csv.writer(csvfile, quoting=csv.QUOTE_MINIMAL)
        writer.writerow(headers)
        for item in hw:
            row = [str(item['dt'])]
            try:
                row.append(str(item['humidity']['c']))
                row.append(str(item['humidity']['mi']))
                row.append(str(item['humidity']['ma']))
                row.append(str(item['humidity']['v']))
            except KeyError:
                row.append('')
                row.append('')
                row.append('')
                row.append('')
            try:
                row.append(str(item['pressure']['c']))
                row.append(str(item['pressure']['mi']))
                row.append(str(item['pressure']['ma']))
                row.append(str(item['pressure']['v']))
            except KeyError:
                row.append('')
                row.append('')
                row.append('')
                row.append('')
            try:
                row.append(str(item['temp']['c']))
                row.append(str(item['temp']['mi']))
                row.append(str(item['temp']['ma']))
                row.append(str(item['temp']['v']))
            except:
                row.append('')
                row.append('')
                row.append('')
                row.append('')
            try:
                row.append(str(item['wind']['speed']['c']))
                row.append(str(item['wind']['speed']['mi']))
                row.append(str(item['wind']['speed']['ma']))
                row.append(str(item['wind']['speed']['v']))
                if 'deg' in item['wind']:
                    row.append(str(item['wind']['deg']['v']))
                else:
                    row.append('')
            except:
                row.append('')
                row.append('')
                row.append('')
                row.append('')
                row.append('')
            writer.writerow(row)
        csvfile.close()
