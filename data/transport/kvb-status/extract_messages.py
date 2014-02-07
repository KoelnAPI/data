# encoding: utf-8

"""
Extracts messages from _source/mofis_bahn.html,
which is a copy of http://www.kvb-koeln.de/german/home/mofis_bahn.html
"""

import os
from lxml import etree
import json
from datetime import datetime

#from bs4 import BeautifulSoup


def extract(path):
    lastmod = datetime.fromtimestamp(int(os.stat(path).st_mtime))
    out = {
        "last_modified": lastmod.isoformat(),
        "messages": []
    }
    fp = open(path, "rb")
    parser = etree.HTMLParser()
    tree = etree.parse(fp, parser)
    fp.close()

    """
    Erst mal die Container (table) finden, in denen die einzelnen Nachrichten
    enthalten sind.
    """
    for table in tree.findall("//div[@id='content']/div[@class='fliesstext']/div/table"):
        message = {
            "type": None,
            "text": None,
            "station_info": []
        }
        #print table
        for row in table.findall("tr"):
            for td in row.findall("td"):
                if td.text is not None:
                    message["text"] = td.text
                span = td.find("span[@class='top_head_rot_small']")
                if span is not None:
                    message["type"] = span.text

                """
                Die Haltestelleninformation befindet sich in einer
                weiteren Tabelle in einem div.
                """
                subtable = td.find("div/table")
                if subtable is not None:
                    for subfield in subtable.findall("tr/td"):
                        fieldtext = subfield.text.strip()

                        """
                        Die Textinformation, welche Haltestelle betroffen ist,
                        kann einen Pfeil als Symbol für die Fahrtrichtung
                        enthalten, muss aber nicht.
                        """
                        if fieldtext != "":
                            if u" \u2192 " in fieldtext:
                                station, direction = fieldtext.split(u" \u2192 ", 1)
                                message["station_info"].append({
                                    "station": station,
                                    "direction": direction
                                })
                            else:
                                message["station_info"].append({
                                    "station": fieldtext,
                                    "direction": None
                                })

        out["messages"].append(message)
    return out


if __name__ == "__main__":
    data = extract("_source/mofis_bahn.html")
    out = open("messages.json", "wb")
    out_min = open("messages.min.json", "wb")
    out.write(json.dumps(data, indent=4, sort_keys=True))
    out_min.write(json.dumps(data))
    out.close()
    out_min.close()
