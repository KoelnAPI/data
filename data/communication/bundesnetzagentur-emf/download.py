# encoding: utf8

import requests
import json
import time
from lxml import etree
import csv

# Bounding box for data scraping: Cologne plus margins
# order: west, south, east, north
BBOX = (6.77, 50.82, 7.19, 51.09)

# step with in degrees for partial worj through bounding box
# (0.05 seems to work fine)
STEP = 0.05

# Our cookie jar, as soon as session is initialized
COOKIES = None


def init_session():
    """
    Get valid session ID and store to cookie jar
    """
    global COOKIES
    url = "http://emf3.bundesnetzagentur.de/karte/default.aspx"
    r = requests.get(url)
    COOKIES = r.cookies
    time.sleep(0.2)


def get_positions(west, south, east, north):
    """
    Get antenna positions for a bounding box,
    returns list of dicts
    """
    global COOKIES
    url = "http://emf3.bundesnetzagentur.de/karte/Standortservice.asmx/GetStandorteFreigabe"
    params = {
        "Box": {
            "nord": north,
            "ost": east,
            "sued": south,
            "west": west
        }
    }
    headers = {
        "accept": "application/json",
        "content-type": "application/json; charset=UTF-8 application/json",
        "referer": "http://emf3.bundesnetzagentur.de/karte/default.aspx",
        "origin": "http://emf3.bundesnetzagentur.de"
    }
    r = requests.post(url, data=json.dumps(params),
        cookies=COOKIES, headers=headers)
    time.sleep(0.2)
    return r.json()["d"]


def get_details(fid):
    """
    Fetch details on a certain antenna position
    and return dict
    """
    global COOKIES
    url = "http://emf3.bundesnetzagentur.de/bnetzachart/Standort.vtl.aspx"
    params = {
        "fid": fid
    }
    headers = {
        "referer": "http://emf3.bundesnetzagentur.de/karte/default.aspx"
    }
    r = requests.get(url, params=params,
        cookies=COOKIES, headers=headers)
    time.sleep(0.5)
    out = {
        "fid": fid,
        "standortbescheinigung_nr": None,
        "antennas": []
    }
    html = etree.HTML(r.text)
    bnr = html.findall(".//div[@id='standortbnr']")
    if bnr == [] or bnr is None:
        return
    bnr_value = bnr[0].findall("span")[1]
    out["standortbescheinigung_nr"] = bnr_value.text
    tables = html.findall(".//table[@id='antennenTable']/tbody")
    if tables == []:
        return
    for row in tables[0].findall("tr"):
        (atype, height, direction, hdistance, vdistance) = row.findall("td")
        if direction.text.strip() == "ND":
            dirtext = None
        else:
            dirtext = direction.text.strip().replace(",", ".")
            try:
                dirtext = float(dirtext)
            except:
                pass
        if hdistance.text.strip() == "nicht angegeben":
            hdistance_text = None
        else:
            hdistance_text = float(hdistance.text.strip().replace(",", "."))
        if vdistance.text.strip() == "nicht angegeben":
            vdistance_text = None
        else:
            vdistance_text = float(vdistance.text.strip().replace(",", "."))
        out["antennas"].append({
            "type": atype.text.strip(),
            "height": float(height.text.strip().replace(",", ".")),
            "direction": dirtext,
            "hdistance": hdistance_text,
            "vdistance": vdistance_text
        })
    return out

if __name__ == "__main__":
    init_session()
    result = {}
    south = BBOX[1]
    while south <= BBOX[3]:
        north = south + STEP
        west = BBOX[0]
        while west <= BBOX[2]:
            east = west + STEP
            print (west, south, east, north)
            for position in get_positions(west, south, east, north):
                details = get_details(position["fID"])
                if details is not None:
                    details["geo_lon"] = position["Lng"]
                    details["geo_lat"] = position["Lat"]
                    print details
                    result[str(position["fID"])] = details
            west += STEP
        south += STEP

    # save JSON
    f = open("antennas.json", "wb")
    f.write(json.dumps(result.values(), indent=4, sort_keys=True))
    f.close()

    # save CSV
    result_items = sorted(result.values(), key=lambda k: k["fid"])
    with open("antennas.csv", "wb") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(["fid",
            "standortbescheinigung_nr",
            "lon",
            "lat",
            "type",
            "hdistance",
            "vdistance",
            "direction",
            "height"])
        for a in result_items:
            for i in a["antennas"]:
                dir = i["direction"]
                if dir is not None and type(dir) != float:
                    dir = dir.encode("utf8")
                row = [
                    str(a["fid"]),
                    str(a["standortbescheinigung_nr"]),
                    str(a["geo_lon"]),
                    str(a["geo_lat"]),
                    i["type"].encode("utf8"),
                    str(i["hdistance"]),
                    str(i["vdistance"]),
                    dir,
                    str(i["height"])
                ]
                writer.writerow(row)
