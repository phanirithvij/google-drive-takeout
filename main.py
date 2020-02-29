"""
The code was written by a me, Phani Rithvij
"""
import zipfile
from tqdm import tqdm


def extract(filename: str):
    with zipfile.ZipFile(filename) as zf:
        member = zipfile.ZipInfo()
        for member in tqdm(zf.infolist(), desc='Extracting '):
            try:
                zf.extract(member, "data")
            except FileNotFoundError as f:
                # On Windows if some path has specical characters
                # extraction will fail for that particular file
                print("FileNotFoundError occured", f)
                print(member.filename)
                # TODO print a useful error message
            except zipfile.error as e:
                print("Error occured", e)


if __name__ == "__main__":
    # Take input as a directory path
    # Filter all the zips in that dir
    # Get the most frequent pattern from all the file names
    # Or take it as an input
    # For all zips do
    # extract it
    extract("data/zip.zip")
    # place it in a folder
    # delete the zip
