# encoding: utf-8

"""
Track message status to database
for later evaluation
"""

import json
import MySQLdb
import warnings
from datetime import datetime


def init_db():
    warnings.filterwarnings('ignore')
    sql = """
    CREATE TABLE IF NOT EXISTS kvbstatus_bahn (
        datetime_local DATETIME UNIQUE,
        num_messages SMALLINT,
        num_stations MEDIUMINT
    )
    ENGINE = MyISAM
    """
    cursor.execute(sql)
    sql = """
    CREATE TABLE IF NOT EXISTS kvbstatus_bus (
        datetime_local DATETIME UNIQUE,
        num_messages SMALLINT,
        num_stations MEDIUMINT
    )
    ENGINE = MyISAM
    """
    cursor.execute(sql)


def track(path_bahn, path_bus):
    bahn = json.load(open(path_bahn, "rb"))
    bus = json.load(open(path_bus, "rb"))
    lastmod_bahn = datetime.strptime(bahn["last_modified"], "%Y-%m-%dT%H:%M:%S")
    lastmod_bus = datetime.strptime(bus["last_modified"], "%Y-%m-%dT%H:%M:%S")
    num_messages_bahn = 0
    num_messages_bus = 0
    num_stations_bahn = 0
    num_stations_bus = 0

    for msg in bahn["messages"]:
        num_messages_bahn += 1
        for station in msg["station_info"]:
            num_stations_bahn += 1
    cursor.execute("INSERT IGNORE INTO kvbstatus_bahn VALUES (%s, %s, %s)",
        (lastmod_bahn.strftime("%Y-%m-%d %H:%M:%S"), num_messages_bahn, num_stations_bahn))
    for msg in bus["messages"]:
        num_messages_bus += 1
        for station in msg["station_info"]:
            num_stations_bus += 1
    cursor.execute("INSERT IGNORE INTO kvbstatus_bus VALUES (%s, %s, %s)",
        (lastmod_bus.strftime("%Y-%m-%d %H:%M:%S"), num_messages_bus, num_stations_bus))

    print("Bahn: %d Meldungen, %d Stationen - %s" % (num_messages_bahn, num_stations_bahn, lastmod_bahn))
    print("Bus: %d Meldungen, %d Stationen - %s" % (num_messages_bus, num_stations_bus, lastmod_bus))

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument('--host', dest="dbhost",
        help='DB host name. Default: localhost', default="localhost")
    parser.add_argument('-u', dest="dbuser",
        help='DB user name. Default: koelnapi', default="koelnapi")
    parser.add_argument('-p', dest="dbpass",
        help='DB password. Default: empty', default="")
    parser.add_argument('-n', dest="dbname",
        help='DB name. Default: koelnapi', default="koelnapi")
    args = parser.parse_args()
    conn = MySQLdb.connect(host=args.dbhost,
        user=args.dbuser, passwd=args.dbpass, db=args.dbname)
    conn.autocommit()
    cursor = conn.cursor(MySQLdb.cursors.DictCursor)
    init_db()
    track("messages_bahn.json", "messages_bus.json")
