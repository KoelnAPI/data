# encoding: utf-8

"""
Converts some shapefiles with very specific format
to GeoJSON files with WGS84 (longitude/latitude) coordinates

Requirements:
- shapefile (pip install pyshp)
- pyproj
- GDAL

"""

import shapefile
import json
import argparse
import pyproj
import osr


out_projection = pyproj.Proj("+proj=latlong +datum=WGS84")


def convert(path, output_name_prefix):
    """
    The main conversion method
    """
    # get projection information
    prj_file = path + '.prj'
    prj_text = open(prj_file, 'r').read()
    srs = osr.SpatialReference()
    if srs.ImportFromWkt(prj_text):
        raise ValueError("Error importing PRJ information from: %s" % prj_file)
    in_projection = pyproj.Proj(srs.ExportToProj4())
    # process shapes
    geojson = {
        'type': 'FeatureCollection',
        'features': []
    }
    # read attribute table records
    sf = shapefile.Reader(path)
    fields = {}
    num = 0
    for field in sf.fields:
        if field[0] == 'DeletionFlag':
            continue
        fields[field[0]] = {
            'name': field[0],
            'type': field[1],
            'sequence_number': num
        }
        num += 1
    # convert shapes
    #print fields.keys()
    for r in sf.shapeRecords():
        shape = r.shape
        record = r.record
        rec_id = None
        if 'NUMMER' in fields:
            rec_id = record[fields['NUMMER']['sequence_number']]
        elif 'OBJECTID' in fields:
            rec_id = record[fields['OBJECTID']['sequence_number']]
        elif 'ID' in fields:
            rec_id = record[fields['ID']['sequence_number']]
        feature = shape.__geo_interface__
        projected_feature = {
            'type': 'Feature',
            'geometry': {
                'coordinates': [],
                'type': 'Polygon'  # hard coded...
            },
            'id': rec_id,
            'properties': {}
        }
        # add properties from records
        for key in fields:
            fieldname = fields[key]['name']
            val = record[fields[key]['sequence_number']]
            if type(val) == str:
                val = val.decode('latin-1')
            projected_feature['properties'][fieldname] = val
        for ring in feature['coordinates']:
            projected_ring = []
            for c in ring:
                p = pyproj.transform(in_projection, out_projection, c[0], c[1])
                projected_ring.append(p)
            projected_feature['geometry']['coordinates'].append(projected_ring)
        geojson['features'].append(projected_feature)
    write_geojson(geojson, output_name_prefix + '.geojson')
    write_kml(geojson, output_name_prefix, output_name_prefix + '.kml')


def write_geojson(data, path):
    f = open(path, 'wb')
    f.write(json.dumps(data, sort_keys=True, indent=4))
    f.close()


def write_kml(data, name, path):
    placemarks = ''
    for feature in data['features']:
        properties = ''
        coordinates = ''
        for prop in feature['properties']:
            val = feature['properties'][prop]
            if type(val) == unicode:
                val = val.encode('utf-8')
            properties += '<SimpleData name="%s">%s</SimpleData>\n' % (prop, val)
        for point in feature['geometry']['coordinates'][0]:
            coordinates += "%s,%s\n" % (point[0], point[1])
        placemarks += '''<Placemark>
            <Style>
                <LineStyle>
                    <color>ff0000ff</color>
                </LineStyle>
                <PolyStyle>
                    <fill>0</fill>
                </PolyStyle>
            </Style>
            <ExtendedData>
                <SchemaData schemaUrl="#%s">
                    %s
                </SchemaData>
            </ExtendedData>
            <Polygon>
                <outerBoundaryIs>
                    <LinearRing>
                        <coordinates>
                            %s
                        </coordinates>
                    </LinearRing>
                </outerBoundaryIs>
            </Polygon>
        </Placemark>''' % (name, properties, coordinates)
    # TODO: Make the schema declaration dynamic
    kml = '''<?xml version="1.0" encoding="utf-8" ?>
        <kml xmlns="http://www.opengis.net/kml/2.2">
            <Document>
                <Folder>
                    <name>%s</name>
                    <Schema id="%s" name="%s">
                        <SimpleField name="Name" type="string"/>
                        <SimpleField name="Description" type="string"/>
                        <SimpleField name="NUMMER" type="string"/>
                        <SimpleField name="SHAPE_AREA" type="float"/>
                        <SimpleField name="SHAPE_LEN" type="float"/>
                    </Schema>
                    %s
                </Folder>
            </Document>
        </kml>''' % (name, name, name, placemarks)
    f = open(path, 'wb')
    f.write(kml)
    f.close()


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Process some integers.')
    parser.add_argument('path', metavar='INPUT_PATH',
        help='Path to the input shapefile (without .shp suffix)')
    parser.add_argument('output_prefix', metavar='OUTPUT_NAME',
        help='Name prefix to be used for output files')
    args = parser.parse_args()
    convert(args.path, args.output_prefix)
