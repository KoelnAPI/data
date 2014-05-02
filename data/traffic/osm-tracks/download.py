#encoding: utf8


"""
Download script for all GPS tracks inside the
Cologne bounding box
"""

# minx, miny, maxx, maxy
BBOX = (6.77, 50.82, 7.19, 51.09)

CSVFILE = "trackpoints.csv"

import requests
import sys
from lxml import etree
import csv


def get_xml(url, params={}):
    r = requests.get(url, params=params, timeout=300)
    if r.status_code != 200:
        sys.stderr.write("Bad HTTP status: %s\n. Exiting." % r.status_code)
        sys.exit(1)
    #print r.url
    source = r.text
    source = source.replace('<?xml version="1.0" encoding="UTF-8"?>', '')
    source = source.replace('xmlns="http://www.topografix.com/GPX/1/0"', '')
    root = etree.fromstring(source)
    return root


def capabilities():
    """
    Get info about API/Server
    """
    url = "http://api.openstreetmap.org/api/0.6/capabilities"
    root = get_xml(url)
    status = root.find(".//status[@gpx]")
    out = {
        "database": status.get("database"),
        "api": status.get("api"),
        "gpx": status.get("gpx"),
    }
    return out


def tracklist(page=0):
    url = "http://api.openstreetmap.org/api/0.6/trackpoints"
    params = {
        "bbox": "%s,%s,%s,%s" % BBOX,
        "page": page
    }
    root = get_xml(url, params=params)
    #print(etree.tostring(root, pretty_print=True))
    for trk in root.iterfind(".//trk"):
        trkid = ""
        if trk.find("url") is not None:
            trkid = trk.find("url").text.split("/")[-1]
        #print "ID=%s" % trkid
        seg_num = -1
        for trkseg in trk.iterfind(".//trkseg"):
            seg_num += 1
            point_num = -1
            for trkpt in trkseg.iterfind(".//trkpt"):
                point_num += 1
                lon = trkpt.get("lon")
                lat = trkpt.get("lat")
                timestamp = ""
                course = ""
                speed = ""
                if trkpt.find("time") is not None:
                    timestamp = trkpt.find("time").text
                if trkpt.find("course") is not None:
                    course = trkpt.find("course").text
                if trkpt.find("speed") is not None:
                    speed = trkpt.find("speed").text
                row = [
                    trkid,
                    str(seg_num),
                    str(point_num),
                    lon,
                    lat,
                    timestamp,
                    course,
                    speed
                ]
                yield row


if __name__ == "__main__":
    cap = capabilities()
    if cap["gpx"] != "online":
        sys.stderr.write("GPX service is currently offline. Please try later or check http://api.openstreetmap.org/api/0.6/capabilities\n")
        sys.exit(2)
    with open(CSVFILE, "wb") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(["track_id", "segment_counter", "point_counter", "lon", "lat", "timestamp", "course", "speed"])
        for pagenum in range(0, 1000):
            print("Downloading list page %d" % pagenum)
            rows = list(tracklist(pagenum))
            if len(rows) == 0:
                break
            for row in rows:
                writer.writerow(row)
