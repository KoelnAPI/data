# encoding: utf8

"""
Converts aed.csv to aed.json
"""

import json
import csv


def convert(input_path):
    records = []
    with open(input_path, "rb") as csvfile:
        reader = csv.reader(csvfile)
        rowcount = -1
        headers = []
        for row in reader:
            rowcount += 1
            if rowcount == 0:
                headers = row
            else:
                record = {}
                for n in range(len(headers)):
                    val = row[n]
                    if val == "":
                        val = None
                    elif headers[n] in ["id", "osm_node_id", "crowdsav_id"]:
                        val = int(val)
                    elif headers[n] in ["latitude", "longitude"]:
                        val = float(val)
                    else:
                        val = val.decode("utf8")
                    record[headers[n]] = val
                records.append(record)
    geojson = {
        "type": "FeatureCollection",
        "features": []
    }
    for record in records:
        # skip nodes without position
        if record["latitude"] is None or record["longitude"] is None:
            continue
        feature = {
            "id": record["id"],
            "type": "Feature",
            "geometry": {
                "type": "Point",
                "coordinates": [
                    record["longitude"],
                    record["latitude"]
                ]
            },
            "properties": {}
        }
        for key in record.keys():
            if key not in ["id", "latitude", "longitude"]:
                feature["properties"][key] = record[key]
        geojson["features"].append(feature)
    fp = open("aed.json", "wb")
    fp.write(json.dumps(geojson, indent=4, sort_keys=True))
    fp.close()
    fp = open("aed.min.json", "wb")
    fp.write(json.dumps(geojson))
    fp.close()

if __name__ == "__main__":
    convert("aed.csv")
