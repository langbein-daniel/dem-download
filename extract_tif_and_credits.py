import argparse
import json
from io import TextIOWrapper
from pathlib import Path
import zipfile
from typing import IO


def main():
    parser = argparse.ArgumentParser(
        description='Extract .tif files from .zip files of source directory into target directory and'
                    ' create one JSON file with credits of the open data sources.')
    parser.add_argument('--src-dir',
                        dest='src_dir',
                        help='Source directory with .zip files',
                        type=Path,
                        metavar='SOURCE_DIR',
                        default=Path('zip'))
    parser.add_argument('--dst_dir',
                        dest='dst_dir',
                        help='Target directory for extracted .tif files and credits.json',
                        type=Path,
                        metavar='TARGET_DIR',
                        default=Path('dem'))

    # Parse and get arguments.
    args = parser.parse_args()
    src_dir: Path = args.src_dir
    dst_dir: Path = args.dst_dir

    extract_tif_and_credits(src_dir, dst_dir)


def extract_tif_and_credits(src_dir: Path, dst_dir: Path):
    dst_dir.mkdir(parents=True, exist_ok=True)
    unique_credits = set()

    src_files = [file for file in src_dir.iterdir()
                 if file.is_file()]
    for src_file in src_files:
        with zipfile.ZipFile(src_file, 'r') as source_zf:
            # We expect the zip file to contain exactly one .tif and one readme.txt file.
            tifs = [x for x in source_zf.infolist()
                    if x.filename.endswith('.tif')]
            assert len(tifs) == 1
            tif = tifs[0]
            readmes = [x for x in source_zf.infolist()
                       if x.filename.endswith('/readme.txt')]
            assert len(readmes) == 1
            readme = readmes[0]

            # Extract the .tif file.
            source_zf.extract(member=tif, path=dst_dir)

            # Parse the readme.txt file.
            readme_io: IO[bytes]
            with source_zf.open(readme) as readme_io:
                readme_str: str = TextIOWrapper(readme_io, 'utf-8').read()

                # Remove start of readme before quoted credits.
                credits_header = 'The following credit must be displayed when using these data:\n'
                assert credits_header in readme_str
                quoted_credits = readme_str.split(credits_header, maxsplit=1)[1]

                # Extract credits from double quotes.
                assert quoted_credits.startswith('"')
                _, credits_str, _ = quoted_credits.split('"', 2)

                # Add credits to set.
                unique_credits.add(credits_str)

    # Create JSON file containing all credits.
    credits_json = json.dumps(list(unique_credits))
    (dst_dir / 'credits.json').write_text(credits_json)


if __name__ == '__main__':
    main()
