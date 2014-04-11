# encoding: utf8

"""
Scrapes measures for one month. Call with the month
as command line argument in 'YYYYMM' format, e.g.:

    python get_values.py 201403

"""


# pollutants
measures = ("PM1", "CO", "O3", "SO2", "NO2")

# types of values available
valuetypes = ("1SMW", "1TMW", "1TMAX", "8SMW", "8TMAX")

# our bounding box of stations to look at
bbox = (6.7, 50.7, 7.2, 51.1)


import argparse
import csv
import requests
import os
import sys
import time
import json
import daterangestr


def get_data(station_id, month_string):
    """
    Load all possible meassures for all value types for a station
    """
    (start_date, end_date) = daterangestr.to_dates(month_string)
    urlmask = "http://www.umweltbundesamt.de/luftdaten/data?pollutant=%s&data_type=%s&date=%s&dateTo=%s&station=%s"
    for pollutant in measures:
        path = os.path.join(start_date.strftime("%Y%m"), station_id, pollutant)
        for t in valuetypes:
            url = urlmask % (pollutant, t, start_date.strftime("%Y%m%d"), end_date.strftime("%Y%m%d"), station_id)
            #print url
            r = requests.get(url)
            if r.status_code == 200:
                data = r.json()
                if data["count"] > 0:
                    try:
                        os.makedirs(path)
                    except:
                        pass
                    filepath = os.path.join(path, t + ".json")
                    fp = open(filepath, "wb")
                    vals = data["values"]
                    for key in vals.keys():
                        for i in range(len(vals[key])):
                            try:
                                vals[key][i] = int(vals[key][i])
                            except:
                                pass
                    fp.write(json.dumps(vals, sort_keys=True))
                    print("Wrote %s" % filepath)
                    fp.close()
            time.sleep(1)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Download UBA air quality values')
    parser.add_argument('month', metavar='MONTH',
                       help='A month in format YYYYMM')
    args = parser.parse_args()
    with open('stations_active.csv', 'rb') as csvfile:
        reader = csv.reader(csvfile)
        rowcount = 0
        for row in reader:
            rowcount += 1
            if rowcount > 1:
                station = {
                    "id": row[0],
                    "lat": float(row[5]),
                    "lon": float(row[7]),
                }
                if (station["lon"] >= bbox[0] and
                    station["lon"] <= bbox[2] and
                    station["lat"] >= bbox[1] and
                    station["lat"] <= bbox[3]):
                    print "Station: ", station
                    get_data(station["id"], args.month)
