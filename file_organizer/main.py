import sys
import json

from file_organizer.cmd.cmd import CMD
from file_organizer.cmd.navigator import ROOT_DIR
from file_organizer.cmd.helper_def import *
from file_organizer.application.file_organizer import FileOrganizerApp


def file_organizer_app_command(cmd: str):
    organizer_app = None
    
    if is_chain_cmd(cmd):
        cmd = cmd.split(" ")
        for i, c in enumerate(cmd):
            match c:
                case "goin":
                    if i + 1 < len(cmd): # check for index boundary
                        path = rf"{cmd[i + 1]}"
                        organizer_app = FileOrganizerApp(path)



def main():
    print("ORGANIZE YOUR FILE IN ONE COMMAND")
    print("Available Commands:")
    prompt = """
    - `goin <path>`: Navigate to the specified directory (like `cd`).
    - `org`: Organize files in the current directory—prompts for custom folder names based on detected extensions.
    - `undo`: Revert the last organization (if applicable).
    - `redo`: To redo the undid organization of files (if applicable).
    - `exit`: Exit the application (type anywhere to exit).
    \n'Separate by space for chain of commands'
    """
    print(prompt)
    print()
    
    current_dir = ROOT_DIR
    
    while True:
        cmd = input(str(f"Navigate first in the directory using goin command.\n\n{current_dir} >")).strip().lower()
        
        if cmd == "exit":
            sys.exit()
            
    
if __name__ == "__main__":
    main()    
        
    