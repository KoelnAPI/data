# encoding: utf-8

"""
Download script for DKAN metadata records
"""

import time
import requests
import json


# URLs look like this:
URL_SCHEMA = "http://offenedaten-koeln.de/node/%d/json"

# we test IDs up to this number:
LIMIT = 1000


if __name__ == '__main__':
    for n in range(0, LIMIT):
        time.sleep(0.5)
        url = URL_SCHEMA % n
        print url
        r = requests.get(url)
        if r.status_code != 200:
            continue
        data = r.json()
        if data["id"] == "":
            continue
        path = "data/%d.json" % n
        f = open(path, 'wb')
        f.write(json.dumps(data, indent=4, sort_keys=True))
        f.close()
