# encoding: utf8

"""
Download script for envirocar measurements
for a specific bounding box.

It loads all measures into RAM before
writing the output. So be warned before
making the bounding box too large.
"""

import requests
import json
import csv

BBOX = (6.77, 50.82, 7.19, 51.09)


#LIMIT = 3
LIMIT = 10000


def get_measurements(page):
    """
    Downloads one page worth of measurements
    """
    url = "https://envirocar.org/api/stable/measurements"
    params = {
        "bbox": "%s,%s,%s,%s" % BBOX,
        "page": page,
        "limit": 100
    }
    r = requests.get(url, params=params)
    for feature in r.json()["features"]:
        yield feature


def get_phenomenons():
    url = "https://envirocar.org/api/stable/phenomenons"
    r = requests.get(url)
    return r.json()["phenomenons"]


if __name__ == "__main__":
    phenomenons = sorted(get_phenomenons(), key=lambda k: k["name"])
    measures = []
    for page in range(1, LIMIT):
        mlist = list(get_measurements(page))
        if len(mlist) == 0:
            break
        for m in mlist:
            measures.append(m)
    measures = sorted(measures, key=lambda k: k["properties"]["id"])
    with open("measures.csv", "wb") as csvfile:
        writer = csv.writer(csvfile)
        # header row
        headers = [
            "id",
            "datetime",
            "lon",
            "lat",
            "sensor_type",
            "sensor_id",
            "sensor_manufacturer",
            "sensor_model",
            "sensor_fueltype",
            "sensor_construction_year",
            "sensor_engine_displacement"
        ]
        for p in phenomenons:
            headers.append(p["name"])
        writer.writerow(headers)
        # data rows
        for m in measures:
            row = [
                m["properties"]["id"],
                m["properties"]["time"],
                "%.6f" % m["geometry"]["coordinates"][0],
                "%.6f" % m["geometry"]["coordinates"][1],
                m["properties"]["sensor"]["type"],
                m["properties"]["sensor"]["properties"]["id"],
                m["properties"]["sensor"]["properties"]["manufacturer"],
                m["properties"]["sensor"]["properties"]["model"],
                m["properties"]["sensor"]["properties"]["fuelType"],
                str(m["properties"]["sensor"]["properties"]["constructionYear"]),
                m["properties"]["sensor"]["properties"]["engineDisplacement"],
            ]
            for p in phenomenons:
                if p["name"] in m["properties"]["phenomenons"]:
                    row.append(str(m["properties"]["phenomenons"][p["name"]]["value"]))
                else:
                    row.append("")
            writer.writerow(row)
