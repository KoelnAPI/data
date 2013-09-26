# encoding: utf-8

"""
Tool to parse a (Geo)JSON file
and reduce the precision of the floating point
coordinate values in order to save some bytes.

More information:

https://github.com/marians/datahub-cgn/tree/master/tools/lessprecise

"""

import sys
import argparse
import json


def parse_file(input_path):
    rawdata = open(input_path, 'rb').read()
    data = json.loads(rawdata)
    # recurse through the data dict and modify floats
    data = recurse_modify(data)
    return data


def recurse_modify(matter):
    if type(matter) == dict:
        for k in matter.keys():
            matter[k] = recurse_modify(matter[k])
    elif type(matter) == list:
        for n in range(len(matter)):
            matter[n] = recurse_modify(matter[n])
    elif type(matter) == float:
        # reduce precision
        a, b = str(matter).split('.')
        if len(b) > args.digits:
            matter = float(float_format % matter)
    elif type(matter) in [str, unicode, int, bool] or matter is None:
        pass
    else:
        sys.stderr.write(
            "Unknown dict member type '%s' found.\n" % type(matter))
    return matter


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description='Reduce floating point precision of a (Geo)JSON file.')
    parser.add_argument('input_path', help="Path of the JSON file to read.")
    parser.add_argument('--digits', '-d', default=7, type=int, dest="digits",
        help="Number of floating point digits to write to output")
    parser.add_argument('--indent', default=None, type=int, dest="indent",
        help="Indentation of JSON putput code (default: no" +
            "line breaks, no indentation)")
    parser.add_argument('--sort', default="1", dest="sort",
        help="Sort keys in output JSON (1=Yes, 0=No)")
    parser.add_argument('-o', '--output', default=None, dest="output_path",
        help="Output file path. Default: write to STDOUT")
    args = parser.parse_args()
    if args.sort == "1":
        args.sort = True
    else:
        args.sort = False
    float_format = '%.' + str(args.digits) + "f"
    data = parse_file(args.input_path)
    if args.output_path is None:
        print json.dumps(data, indent=args.indent, sort_keys=args.sort)
    else:
        f = open(args.output_path, 'wb')
        f.write(json.dumps(data, indent=args.indent, sort_keys=args.sort))
        f.close()
