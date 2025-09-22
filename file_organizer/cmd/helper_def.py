from pathlib import Path
import os

# Functions designed to always call files_in_dir, which then navigate to pass param path directory.
# files_in_dir organizes the files in key, value pair {extension: filename}.
# It was designed this way to handle real-time changes of files in the pass param path directory during code runtime.


# start the navigation from root directory
# and define according to os type
# windows == nt, linux == /
ROOT_DIR = Path("C:\\") if os.name == "nt" else Path("/")

def files_in_dir(path: Path) -> dict:
    """Collects existing files in dir"""
    path = ROOT_DIR / path
    files = [f for f in path.iterdir() if f.is_file()]

    res = {}
    for file in files:
        file_extension = file.suffix.lower()
        if file_extension not in res:
            res[file_extension] = set() 
        res[file_extension].add(file.name)
        
    return res


def choose_file_ext_to_org(path: Path, chosen_files: list) -> set:
    """Choose and collects which files are only allowed to organize"""
    available_files = files_in_dir(path)
    
    res = set()
    for k in available_files.keys():
        if k in chosen_files:
            res.add(k)
    return res


def file_folder_pair_rules(path: Path, pair_rules: dict) -> dict:
    """
        Create a key value pair for the chosem files and the available files
        ex:
            available files:
                ".txt": {"notes.txt", "todo.txt"},
                ".jpg": {"cat.jpg"}
            pair_rules passed param:
                {".jpg": "images", ".txt": "notes", ".py": "programs", ".png": "sugar"}
            directory name for each file extension [output]:
                {
                    ".jpg": "images", # <- .jpg stores in images folder
                    ".txt": "notes" # <- .txt stores in notes folder,
                    ... # .py and .png key, value were ignored since these files are not existing
                }
    """
    available_files = files_in_dir(path)
    res = {
        ext: folder_name for ext, folder_name in pair_rules.items() if ext in available_files.keys()
    }
    return res


def check_file_in_dir(path: Path, rules: dict) -> bool:
    """Checks if the dir has known files that does not inside a sub folder"""
    path = ROOT_DIR / path
    files = os.listdir(str(path))
    
    for f in files:
        return os.path.splitext(f)[1] in rules.keys() # immediate return True if found known files
    
    
def org_file_in_dir(path: Path, rules: dict) -> dict:
    """Organize files in directory according to rules"""
    organized = {}
    path = ROOT_DIR / path
    
    if not path.exists():
        return {}
    
    # Get all files in the directory not included the subdirectories
    files = [f for f in path.iterdir() if f.is_file()]
    
    for file in files:
        file_extension = file.suffix.lower()

        # Check if this extension has a rule
        for ext, folder in rules.items():
            if file_extension == ext.lower():
                if folder not in organized:
                    organized[folder] = []
                organized[folder].append(file.name)
                break
    
    return organized
    
    
def is_chain_cmd(cmd: str) -> bool:
    import re
    return re.search(r"\s", cmd) or cmd != cmd.strip()
    
avf = files_in_dir(r"Users\imper\Downloads\test_folder")
print(avf)
print("Files to organizd: ",choose_file_ext_to_org("Users\\imper\\Downloads\\test_folder", ['.py', '.txt']))
rules = file_folder_pair_rules("Users\\imper\\Downloads\\test_folder", {".jpg": "images", ".txt": "notes", ".py": "gagi", ".png": "sugar"})

print("Rules: ", rules)
print(org_file_in_dir("Users\\imper\\Downloads\\test_folder", rules))
