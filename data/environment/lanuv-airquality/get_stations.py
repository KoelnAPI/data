# encoding: utf8

"""
Scraper für die Stationsliste vom LANUV
mit Geo-Koordinaten
"""

import sys
import requests
from bs4 import BeautifulSoup
import time
import csv


def get_list():
    url = "http://www.lanuv.nrw.de/luft/immissionen/aktluftqual/eu_luft_akt.htm"
    r = requests.get(url)
    if r.status_code == 200:
        soup = BeautifulSoup(r.text)
        for table in soup.find_all("table", id='akt_luft'):
            for row in table.find_all("tr"):
                tds = row.find_all("td")
                if len(tds) < 5:
                    continue
                a = tds[0].find_all("a")
                if len(a) < 1:
                    continue
                record = {
                    "url": "http://www.lanuv.nrw.de" + a[0]["href"],
                    "id": tds[1].text,
                    "name": tds[0].text
                }
                yield record


def get_details(url):
    r = requests.get(url)
    if r.status_code != 200:
        sys.stderr.write("ERROR in HTTP request for %s\n" % url)
        return
    soup = BeautifulSoup(r.text)
    record = {}
    for table in soup.find_all("table", id='station'):
        for row in table.find_all("tr"):
            tds = row.find_all("td")
            #print [tds[0].text, tds[1].get_text()]
            if tds[0].text == u'L\xe4ngengrad:':
                record["longitude"] = parse_latlong(tds[1].text)
            elif tds[0].text == u'Breitengrad:':
                record["latitude"] = parse_latlong(tds[1].text)
    return record


def parse_latlong(s):
    """convert string like u'6\xb0 5min 40sec' to float"""
    #print "String:", (s)
    deg, rest = s.split(u"\xb0 ", 1)
    minutes, rest = rest.split(u"min ", 1)
    rest = rest.split(u"sec")
    deg = int(deg.strip())
    minutes = int(minutes.strip())
    sec = int(rest[0].strip())
    decimal = float(deg) + (float(minutes) / 60.0) + (float(sec) / 3600.0)
    #print s, [deg, minutes, sec], decimal
    return decimal


if __name__ == "__main__":
    with open("stations.csv", "wb") as csvfile:
        writer = csv.writer(csvfile, quoting=csv.QUOTE_MINIMAL)
        writer.writerow(["id", "name", "longitude", "latitude"])
        for item in get_list():
            print item
            details = get_details(item["url"])
            print details
            writer.writerow([
                item["id"],
                item["name"].encode("utf8"),
                details["longitude"],
                details["latitude"]
            ])
            #time.sleep(1)
