import os

# ------------------------ LOCAL FOLDERS ------------------------ #
script_folder = os.path.dirname(__file__)
main_folder = os.path.dirname(script_folder)
stickers_folder = os.path.join(main_folder, "stickers")
assets_folder = os.path.join(main_folder, "assets")
source_sans_pro = os.path.join(
    assets_folder, "Source_Sans_Pro", "SourceSansPro-Regular.ttf"
)
