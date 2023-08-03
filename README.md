# EU DEM Download

Usage:

To download DEM files covering a rectangular region of Europe (bounding box, consisting of four coordinates),
run  [./download_dem_zip.py](./download_dem_zip.py).

To extract the GeoTIFF (`.tif`) files and to create one JSON file with credits,
run [./extract_tif_and_credits.py](./extract_tif_and_credits.py).

More details can be retrieved by passing the argument `-h` or `--help` to one of the commands.

## Definitions

Digital Surface Model (DSM), Digital Terrain Model (DTM): https://www.opendem.info/definitions.html

## Arc Seconds in Meters

https://www.opendem.info/arc2meters.html

## Open DEM EU - High Resolution

https://www.opendem.info/opendemeu_background.html

High-resolution projected tiles: In a 50*50 km raster as GeoTIFFs. The spatial reference system is the ETRS89 Lambert
Azimuthal Equal-Area projection coordinate reference system (EPSG:3035) and vertical datum EVRS2000 (EPSG:5730).
Resolutions below 1 m were recalculated to a 1 m DTM with a cubic resampling method to create manageable datasets below
10 GB.

- Download link example: http://opendemdata.info/data/europe_laea/N285E445.zip
- Square of four tiles: N290E440, N290E445, N285E440, N285E445

## Open DEM EU - Medium Resolution

https://www.opendem.info/opendemeu_background.html

1-arc second European geographic tiles: The typical SRTM style 1°*1° degree tiles with 1-arc second resolution as
GeoTIFFs. The spatial reference system is geographic, lat/lon with horizontal datum ETRS89, ellipsoid GRS80 (EPSG:4258)
and vertical datum EVRS2000 with geoid EGG08 (EPSG:5730).

- Download link example: https://www.muaythaiclinch.info/opendem_europe_download/eu_4258/N49E011.zip
- Square of four tiles: N49E010, N49E011, N50E010, N50E011

### How to cite the selected Datasets:

- Produced using Copernicus data and information funded by the European Union - EU-DEM layers.
- Land NRW (2017) Data licence Germany – attribution – version 2.0 (www.govdata.de/dl-de/by-2-0)
- Agentschap voor Geografische Informatie Vlaanderen - CC0 1.0 Universal (CC0 1.0)
- Actueel Hoogtebestand Nederland (AHN) - CC0 1.0 Universal (CC0 1.0)
- Ministry of the environment and spatial planning, Slovenian environment agency (www.arso.gov.si)
- Geoland.at (2019) - CC BY 4.0 (CC BY 4.0)
- GEOPORTALE NAZIONALE - AccessConstraints: Nessuno - None

Have a look at the readme file of every tile for further information.
