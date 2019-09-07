# FortWeather
Historical Weather Data cleaning and reformatting.

## General Information
The Midwest Regional Climate Center holds a collection of day-records for weather readings taken at U.S. Army forts around the West Coast in the 19th century.  These records are available as scans, but they were also digitized in 2010.  The format that was used is not convenient for analysis and/or presentation using python/R, or other commonly used tools.  This repository provides scripts to scan those digitized records and translate them into a more accessible format.

## Files
  * ~/Data/*.dat
     - The original data files
  *  ~/Data/DSI-3297-CDMP19thCenturyFormatDocument.doc.v2.pdf
     - The readme that came with the the data files, containing full explanations of the codes and methods used to encode the day sheets.
 * ~/FortDatParser.py  & ~/FortDatParserWide.py 
        - The python scripts that reformat the dat files into a csv file in the format of your choosing.
