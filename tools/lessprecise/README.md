lessprecise
===========

## Description

A little python tool to reduce the floating point precision
of a JSON or GeoJSON file. In GeoJSON, this sometimes enables
huge space savings, since coordinate values are normally
given as floating point values with an unnecessary high
precision.

Additionally, lessprecise allows you to influence JSON 
indentation and key sorting of the output file. This can
be used to further reduce the file size or make the
file content more predictable, which can be benefitial in
version control systems.

## Beschreibung

Ein kleines Python-Werkzeug zur Reduktion der Genauigkeit von
Fließkommawerten in JSON- und GeoJSON-Dateien. Gerade bei
GeoJSON kommt es häufig vor, dass viele Fließkommawerte mit
unnötig hoher Anzahl von Nachkommastellen in den Daten enthalten
sind. Hier lassen sich Dateigroßen oft merklich reduzieren.

Außerdem erlaub lessprecise die Kontrolle des Zeilenumbruchs und
Einrückung der ausgegebenen JSON-Datei. Auch damit kann die Dateigröße
optimiert oder die Lesbarkeit bzw. Vorhersagbarkeit des Dateiaufbaus,
was z.B. bei Versionskontrollsystemen von Bedeutung ist, beeinflusst
werden.

## Use

Simplest form. Reduces floats to max. 7 digits behind the dot, creates
no line breaks nor indentation.

    python lessprecise.py bloated.json > compact.json

or

    python lessprecise.py bloated.json -o compact.json

Lets you define the precision (here: 4 digits).

    python lessprecise.py bloated.json -d 4 > more_compact.json

Enables indentation (2 spaces):

	python lessprecise.py bloated.json --indent 2 > nicely_indented.json

Enables key sorting:

    python lessprecise.py bloated.json --sort > sorted.json

Now controlling it all:

    python lessprecise.py bloated.json -d 5 --indent 2 --sort > nice.json
