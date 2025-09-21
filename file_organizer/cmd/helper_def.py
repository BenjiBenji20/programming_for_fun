from pathlib import Path
import os
from navigator import ROOT_DIR

# available commands as of the starting creation 09/21/2025.
CMD = {
    "go" # <- nav to a parameter. Similar to cd
    "org" # <- organize known files in a paramter
    "undo" # <- only if existing command has been done, it undo the previous file org
}

# in the future we can pass a preferred folder name than these static folder names
RULES = {
    ".jpg": "images", # <- .jpg stores in images folder
    ".mp4": "videos", # <- .mp4 stores in videos folder
    ".html": "webs", # <- .html stores in webs folder
    ".txt": "notes" # <- .txt stores in notes folder
}


def check_file_in_dir(path: Path) -> bool:
    """Checks if the dir has known files that does not inside a sub folder"""
    path = ROOT_DIR / path
    files = os.listdir(str(path))
    
    for f in files:
        return os.path.splitext(f)[1] in list(RULES.keys()) # immediate return True if found known files
    
    
def org_file_in_dir(path: Path) -> dict:
    """Organize the known files in dir that does not inside a sub folder"""
    if not check_file_in_dir(path): # check if known files exist
        return {}
    
    path = ROOT_DIR / path
    files = os.listdir(str(path))
    
    res = {}
    for f in files:
        ext = os.path.splitext(f)[1] # hanldes extension
        if ext in RULES.keys():
            folder_category = RULES[ext]
            # ensure folder category not already in res
            if folder_category not in res:
                res[folder_category] = set()
            res[folder_category].add(f) # add file to correct folder category
            
    return res
    
#print(org_file_in_dir("Users\\imper\\Downloads\\test_folder"))
