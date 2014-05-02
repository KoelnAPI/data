OpenStreetMap Tracks from Cologne
=================================

This is a mirror tool for OpenStreetMap GPS tracks recorded
within the bounds of Cologne, Germany. For easy direct access
and analysis.

We don't mirror the actual data here on github since it's
just too much.

## License

Open Data according to the [Open Database License](http://opendatacommons.org/licenses/odbl/) (ODBbL)
See http://www.openstreetmap.org/copyright for details.

## The download.py script

This script can be used to fetch lots and lots of track entries
from the OpenStreetMap database and write them to an easy to use
CSV file.

The file trackpoints_sample.csv file gives you an impression
how the result will look like.

Be prepared that the download can take hours and never finish.
However, you can interrupt the download at any time.

## The file trackspoints_sample.csv

This is a 1000 line sample of the data that can be collected
using the download.py script. The column schema is as follows:

* track_id: Unique OSM identifier for the track, may be empty if track is anonymous
* segment_counter: Number of the segment within the track
* point_counter: Number of the track point with the segment
* lon: X coordinate value
* lat: Y coordinate value
* timestamp: ISO timestamp in UTC timezone, may be empty
* course: always empty
* speed: always empty
