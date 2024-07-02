from local import stickers_folder           # Database information, fonts, paths to local folders
from sticker_generator import *             # Generating stickers and operations on them
import csv
import os

# TITLE:        QR CODE STICKER GENERATOR
# DESCRIPTION:  THE SCRIPT GENERATES A PNG STICKER WITH A QR CODE
# AUTHOR:       MARTA SIENKIEWICZ
# LICENSE:      MIT license

STICKERS_TABLE = []

def main():
    with open("stickers.csv", 'r') as csv_file:
        csv_reader = csv.reader(csv_file)
        for row in csv_reader:
            STICKERS_TABLE.append(row)
    generate_stickers(STICKERS_TABLE)
    merge_to_a4()

if __name__ == "__main__":
    main()
