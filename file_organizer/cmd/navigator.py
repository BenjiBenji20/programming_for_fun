from pathlib import Path
import os

# start the navigation from root directory
# and define according to os type
# windows == nt, linux == /
ROOT_DIR = Path("C:\\") if os.name == "nt" else Path("/")


# test
# os.chdir(ROOT_DIR)
# print("Current dir: ", Path.cwd())
