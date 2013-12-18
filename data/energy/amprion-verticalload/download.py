# encoding: utf-8

import requests
from datetime import datetime
import daterangestr
import csv
import os


BASE_URL = "http://preview.amprion.de/applications/applicationfiles/netzlast.php?"
BASE_URL += "mode=download&format=csv&start=%s&end=%s&lng=undefined&t=%s"


def download(start_date, end_date):
    now = datetime.now().strftime("%s")
    start = start_date.strftime("%d.%m.%Y")
    end = end_date.strftime("%d.%m.%Y")
    url = BASE_URL % (start, end, now)
    r = requests.get(url)
    if r.status_code == 200:
        return r.text


def save(data, start_date, end_date):
    yearfolder = "%d" % start_date.year
    if not os.path.exists(yearfolder):
        os.mkdir(yearfolder)
    path = '%s/verticalload_%s.csv' % (
        yearfolder, start_date.strftime("%Y%m"))
    with open(path, 'wb') as csvfile:
        writer = csv.writer(csvfile, quoting=csv.QUOTE_MINIMAL)
        writer.writerow(["date", "time_from", "time_to", "vertical_load"])
        rowcount = 0
        for line in data.split("\n"):
            if line == '':
                continue
            if rowcount > 0:
                fields = line.strip().split(";")
                dt = fields[0].split(".")
                times = fields[1].split(" - ")
                row = [
                    "%s-%s-%s" % (dt[2], dt[1], dt[0]),
                    times[0],
                    times[1],
                    fields[2]
                ]
                writer.writerow(row)
            rowcount += 1


if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser(description='Download monthly data')
    parser.add_argument('daterange',
        help='Month in the format YYYYMM, e.g. "201310"')
    args = parser.parse_args()
    (start, end) = daterangestr.to_dates(args.daterange)
    data = download(start, end)
    save(data, start, end)
