# encoding: utf-8

"""
Save street segment data from traffic load API
to GeoJSON file
"""

import requests
import json


def get():
    url = "http://geoportal1.stadt-koeln.de/ArcGIS/rest/"
    url += "services/WebVerkehr_Data/MapServer/3/query?"
    url += "text=&geometry=&geometryType=esriGeometryPolyline"
    url += "&inSR=&spatialRel=esriSpatialRelIntersects"
    url += "&relationParam=&objectIds="
    url += "&where=IDENTIFIER+IS+NOT+NULL&time="
    url += "&returnCountOnly=false&returnIdsOnly=false"
    url += "&returnGeometry=true&maxAllowableOffset="
    url += "&outSR=4326&outFields=OBJECTID,IDENTIFIER,NAME,&f=json"
    r = requests.get(url)
    if r.status_code == 200:
        return r.json()


def save_to_geojson(data, path):
    g = {
        "type": "FeatureCollection",
        "features": []
    }
    for f in data['features']:
        gf = {
            'type': 'Feature',
            'geometry': {
                'type': 'MultiLineString',
                'coordinates': f['geometry']['paths']
            },
            'properties': f['attributes']
        }
        g['features'].append(gf)
    with open(path, 'wb') as gfile:
        json.dump(g, gfile, indent=4, sort_keys=True)

if __name__ == '__main__':
    data = get()
    save_to_geojson(data, 'street_segments.geojson')
