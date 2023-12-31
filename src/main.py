from local import stickers_folder           # Database information, fonts, paths to local folders
from sticker_generator import *             # Generating stickers and operations on them
import os

# TITLE:        QR CODE STICKER GENERATOR
# DESCRIPTION:  THE SCRIPT GENERATES A PNG STICKER WITH A QR CODE
# AUTHOR:       MARTA SIENKIEWICZ
# LICENSE:      MIT license

def main():
    record_1 = {
        "sticker-url": "https://github.com/MartaSien",
        "sticker-label": "MartaSien",

    }
    record_2 = {
        "sticker-url": "https://github.com/MartaSien?tab=projects",
        "sticker-label": "MartaProjects",
    }
    stickers_table = [record_1, record_2]
    generate_stickers(stickers_table)
    merge_to_a4()

if __name__ == "__main__":
    main()


