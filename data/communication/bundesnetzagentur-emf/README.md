Antenna positions according to Bundesnetzagentur EMF database
=============================================================

**Antennenstandorte entsprechend der EMF-Datenbank der Bundesnetzagentur**

An extract from the Bundesnetzagentur EMF database with antenna positions
from cell phone providers and other operators, bound to the Cologne, Germany
area.

Each antenna position (mast) usually has multiple antennas pointing into
different directions and serving various purposes.

For cell phone antennas, unfortunately no information on the cell phone
provider is given.

## Source

http://emf3.bundesnetzagentur.de/karte/default.aspx

## License

unknown

## The file `antennas.csv`

CSV file with all antenna positions, sorted by field `fid`.

* `fid`: Unique identifier of the position from the source database
* `standortbescheinigung_nr`: Unique identifier of the [Standortbescheinigung](http://de.wikipedia.org/wiki/Standortbescheinigung), an official license.
* `lon`: Geographic longitude (WGS84)
* `lat`: Geographic latitude (WGS84)
* `type`: An antenna type string like "Mobilfunk" (cell phone) or "Sonstige Funkanlage" (other)
* `hdistance`: Safety distance in horizontal direction in meters
* `vdistance`: Safety distance in vertical direction in meters
* `direction`: direction the antenna is sending to
* `height`: height above ground in meters

## The file `antennas.json`

JSON version of the data, indented and sorted by key for version control.

The attribute names and meanings are the same as in `antennas.csv`.

## The script `download.py`

Python script for download of up-to-date data, stores into `antennas.csv` and `antennas.json`.
