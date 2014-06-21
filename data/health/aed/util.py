# encoding: utf8

import csv
import json
from shapely.geometry import Polygon, Point
from pyproj import Proj, transform

wgs84_projection = Proj(init="epsg:4326")
metric_projection = Proj(init="epsg:25832")

def distance(x1, y1, x2, y2):
    """
    Get distance in meters between to lon, lat points
    """
    x1, y1 = transform(wgs84_projection,
        metric_projection, float(x1), float(y1), radians=False)
    x2, y2 = transform(wgs84_projection,
        metric_projection, float(x2), float(y2), radians=False)
    #print x1, y1, x2, y2
    return Point(x1, y1).distance(Point(x2, y2))

def get_bounds():
    """
    Importiere Grenze von Köln
    als Shapely-Polygon
    """
    f = open("../../geo-base/city-boundary/cityboundary.geojson")
    data = json.loads(f.read())
    f.close()
    coords = data["coordinates"][0]
    return Polygon(coords)


def load_csv_aeds():
    out = []
    headers = []
    with open("aed.csv", "rb") as csvfile:
        reader = csv.reader(csvfile)
        rowcount = -1
        for row in reader:
            rowcount += 1
            if rowcount == 0:
                headers = row
            else:
                record = {}
                for n in range(len(row)):
                    if row[n] == "":
                        row[n] = None
                    if row[n] is not None:
                        if headers[n] in ["latitude", "longitude"]:
                            row[n] = float(row[n])
                    record[headers[n]] = row[n]
                out.append(record)
    return out
