import argparse
import math
from pathlib import Path
from urllib import request


def main():
    # Example:
    #   ./download.py 10.011636032586688,48.70792025947608,12.223993889052613,50.25793688217101

    parser = argparse.ArgumentParser(
        description='Download DEM tiles'
                    ' covering a bounding box from OpenDemEU with 1 arc second resolution.'
                    ' For details, see "1-arc second European geographic tiles" at'
                    ' https://www.opendem.info/opendemeu_background.html')
    parser.add_argument('bbox',
                        help='Bounding Box',
                        type=str,
                        metavar='BOUNDING_BOX')
    parser.add_argument('--target-dir',
                        dest='dst_dir',
                        help='Target directory',
                        type=Path,
                        metavar='TARGET_DIRECTORY',
                        default=Path('zip'))

    # Parse and get arguments.
    args = parser.parse_args()
    bbox: str = args.bbox
    dst_dir: Path = args.dst_dir

    # Parse bounding box.
    min_lon, min_lat, max_lon, max_lat = [float(x) for x in bbox.split(',', maxsplit=3)]

    download(min_lon, min_lat, max_lon, max_lat, dst_dir)


def download(min_lon: float, min_lat: float, max_lon: float, max_lat: float,
             dst_dir: Path):
    """
    How to get the filename:
    - Four tiles cover the point with coordinate (50.0, 11.0): N49-50, E010-E011
    - Four tiles cover the point with coordinate (28.0, -18.0): N27-28, W18-19
    - -> Round coordinates to floor.
    - -> N/S, W/E depending on sign of coordinates.
    """

    dst_dir.mkdir(parents=True, exist_ok=True)
    for url, filename in tile_urls(min_lon, min_lat, max_lon, max_lat):
        target = dst_dir / filename

        if target.is_file():
            print(f'Skipping {filename} (does already exist)')
            continue
        print(f'Downloading {filename} ...')

        try:
            _, http_message = request.urlretrieve(url, target)
        except Exception as e:
            raise Exception(f'Error during download of {filename} from {url}\n'
                            f'Please delete an incomplete file and try to download it again.') from e


def tile_urls(min_lon: float, min_lat: float, max_lon: float, max_lat: float):
    for lat, lon in tile_coordinates(min_lon, min_lat, max_lon, max_lat):
        lon_str = 'E' if lon > 0 else 'W'
        lat_str = 'N' if lat > 0 else 'S'

        # Absolute values.
        lat, lon = [abs(x) for x in [lat, lon]]

        filename = f'{lat_str}{lat:02d}{lon_str}{lon:03d}.zip'
        yield f'https://www.muaythaiclinch.info/opendem_europe_download/eu_4258/{filename}', filename


def tile_coordinates(min_lon: float, min_lat: float, max_lon: float, max_lat: float):
    # Round floor.
    min_lon, min_lat, max_lon, max_lat = [math.floor(x) for x in [min_lon, min_lat, max_lon, max_lat]]

    for lon in range(min_lon, max_lon + 1):
        for lat in range(min_lat, max_lat + 1):
            yield lat, lon


if __name__ == '__main__':
    main()
