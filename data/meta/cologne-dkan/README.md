Cologne DKAN Catalgue / Datenkatalog der Stadt Köln
===================================================

This is a mirror of the city of cologne Open Data catalogue's (DKAN) metadata.

Source: http://offenedaten-koeln.de/

Data is contained in the `data` subfolder. Each JSON file represents one
catalogue entry.

## Tools

### `download.py`

Scraper script for mirroring all relevant data. Call without argument:

    python download.py

The script has an internal LIMIT variable which defines which ID range
the script will check for. A limit if 800 means that IDs form 1 to 800
are scraped.
