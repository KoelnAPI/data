# encoding: utf8

"""
This script watches the Cologne area in
definow.org for 
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

def load_definow_aeds():
    bounds = util.get_bounds()
    out = {}
    url = "http://definow.org/de/map/node"
    print("Downloading URL '%s'..." % url)
    r = requests.post(url)
    if r.status_code != 200:
        return
    exp = r'"rmt":"([0-9]+)\\/0","latitude":"([\.0-9]+)","longitude":"([\.0-9]+)",'
    for item in re.findall(exp, r.text):
        #print item
        y = float(item[1])
        x = float(item[2])
        definow_id = int(item[0])
        position = Point([x, y])
        if not bounds.contains(position):
            continue
        out[str(definow_id)] = {
            "id": definow_id,
            "x": x,
            "y": y
        }
    # write CSV version
    with open("definow.csv", "wb") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(["id", "x", "y"])
        for aedid in out.keys():
            writer.writerow([
                str(out[aedid]["id"]),
                str(out[aedid]["x"]),
                str(out[aedid]["y"])
            ])
    return out


def find_changes(aeds, definow_aeds):
    """
    Check which definow.org nodes have been modified, added, deleted
    """
    for definow_id in definow_aeds.keys():
        found = False
        changes = []
        our_mapped_id = None
        for aed in aeds:
            if str(definow_id) == str(aed["definow_id"]):
                found = True
                our_mapped_id = aed["definow_id"]
                # check difference
                if aed["longitude"] is None:
                    continue
                if (str(definow_aeds[definow_id]["x"]) == str(aed["longitude"]) and 
                    str(definow_aeds[definow_id]["y"]) == str(aed["latitude"])):
                    # exactly same position
                    continue

                # distance from our to definow.org position
                try:
                    dist = util.distance(definow_aeds[definow_id]["x"],
                            definow_aeds[definow_id]["y"],
                            aed["longitude"], aed["latitude"])
                except TypeError:
                    print("TypeError")
                    print(json.dumps(definow_aeds[definow_id], indent=4))
                    print(json.dumps(aed, indent=4))
                if dist > 0.1:
                    sys.stderr.write("definow.org ID %s, our ID %s: position is: x=%s, y=%s, distance: %.2f m\n" % (
                        definow_id, aed["id"], definow_aeds[definow_id]["x"],
                        definow_aeds[definow_id]["y"], dist))
                    changes.append("position")
                # continue with next aed
                continue

        if not found:
            sys.stderr.write("definow.org ID %s is not in aed.csv:\n" % definow_id)
            sys.stderr.write(json.dumps(definow_aeds[definow_id], indent=4))
            sys.stderr.write("\n")

    # other way around: check which OSM nodes have been deleted
    for aed in aeds:
        if aed["definow_id"] is None:
            continue
        definow_id = str(aed["definow_id"])
        if definow_id == "":
            continue
        if definow_id not in definow_aeds:
            sys.stderr.write("definow.org ID %s, our ID %s, is no longer in AED-Kataster.net\n" % (
                definow_id, aed["id"]))


if __name__ == "__main__":
    aeds = util.load_csv_aeds()
    definow_aeds = load_definow_aeds()
    #print(json.dumps(definow_aeds, indent=4))
    print len(definow_aeds.keys()), "AEDs found in definow.org"
    find_changes(aeds, definow_aeds)
