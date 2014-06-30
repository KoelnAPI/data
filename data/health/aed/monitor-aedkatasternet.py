# encoding: utf8

"""
This script watches the Cologne area in
aed-kataster.net for 
AED entries and looks for matches in our
aed.csv source

"""

import sys
import json
import csv
import requests
from bs4 import BeautifulSoup
from shapely.geometry import Polygon, Point
import util
import re

def load_aedkataster_aeds():
    bounds = util.get_bounds()
    out = {}
    url = "http://aed-kataster.net/nw.html"
    print("Downloading URL '%s'..." % url)
    r = requests.post(url)
    if r.status_code != 200:
        return
    exp = r'GLatLng\(([\.0-9]+),([\.0-9]+)\);\s+SobiCatOverMap\.addOverlay\(\s+createSobiMarker\(\s+MarkerPoint,\s+\'<div><a href="[^\?]+\?sobi2Task=sobi2Details&amp;sobi2Id=([0-9]+)">'
    for item in re.findall(exp, r.text):
        #print item
        y = float(item[0])
        x = float(item[1])
        aedk_id = int(item[2])
        position = Point([x, y])
        if bounds.contains(position):
            out[str(aedk_id)] = {
                "id": aedk_id,
                "x": x,
                "y": y
            }
    return out


def find_changes(aeds, aedk_aeds):
    """
    Check which aed-kataster.net nodes have been modified
    """
    for aedk_id in aedk_aeds.keys():
        found = False
        changes = []
        our_mapped_id = None
        for aed in aeds:
            if str(aedk_id) == str(aed["aedkatasternet_id"]):
                found = True
                our_mapped_id = aed["aedkatasternet_id"]
                # check difference
                if aed["longitude"] is None:
                    continue
                if (str(aedk_aeds[aedk_id]["x"]) != str(aed["longitude"]) or 
                    str(aedk_aeds[aedk_id]["y"]) != str(aed["latitude"])):

                    # distance form our to AEDK position
                    try:
                        dist = util.distance(aedk_aeds[aedk_id]["x"],
                                aedk_aeds[aedk_id]["y"],
                                aed["longitude"], aed["latitude"])
                    except TypeError:
                        print("TypeError")
                        print(json.dumps(aedk_aeds[aedk_id], indent=4))
                        print(json.dumps(aed, indent=4))
                    if dist > 0.1:
                        print("Position offset: AED-Kataster.net ID %s, our ID %s, distance: %.1f m" % (
                            aedk_id, aed["id"], dist))
                        changes.append("position")
                continue

        if not found:
            print("Not in aed.csv: http://aed-kataster.net/component/sobi2/?sobi2Task=sobi2Details&sobi2Id=%s, x=%s, y=%s" % (
                aedk_id, aedk_aeds[aedk_id]["x"], aedk_aeds[aedk_id]["y"]))

    # other way around: check which OSM nodes have been deleted
    for aed in aeds:
        if aed["aedkatasternet_id"] is None:
            continue
        aedk_id = str(aed["aedkatasternet_id"])
        if aedk_id == "":
            continue
        if aedk_id not in aedk_aeds:
            print("AED-Kataster.net ID %s, our ID %s, is no longer in AED-Kataster.net\n" % (
                aedk_id, aed["id"]))


if __name__ == "__main__":
    aeds = util.load_csv_aeds()
    aedkataster_aeds = load_aedkataster_aeds()
    #print(json.dumps(aedkataster_aeds, indent=4))
    print len(aedkataster_aeds.keys()), "AEDs found in AED-Kataster.net"
    find_changes(aeds, aedkataster_aeds)
