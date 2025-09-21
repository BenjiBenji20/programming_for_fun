# CLI File Organizer

A simple CLI tool to organize files in a directory by their extensions, moving them into dedicated folders. Built to demonstrate file handling and automation without frameworks.

## Features
- Navigate to a directory and organize files with specific extensions: `.jpg`, `.txt`, `.html`, `.mp4`.
- Files are sorted into folders: `.jpg` → `images`, `.txt` → `notes`, `.html` → `webs`, `.mp4` → `videos`.
- Supports undo functionality to revert the last organization.

## Commands
- `go <path>`: Navigate to the specified directory (like `cd`).
- `org`: Organize files in the current directory based on predefined rules.
- `undo`: Revert the last organization (if applicable).

## File Organization Rules
- `.jpg` → `images` folder
- `.txt` → `notes` folder
- `.html` → `webs` folder
- `.mp4` → `videos` folder

## Usage
1. Clone the repo and navigate to this folder.
2. Run the CLI app (e.g., `python main.py` or equivalent, depending on the language).
3. Use `go <path>` to navigate to a directory with unorganized files.
4. Run `org` to sort files into their respective folders.
5. Run `undo` to revert the last organization if needed.

*Note*: Currently supports `.jpg`, `.txt`, `.html`, and `.mp4` files. Future updates may allow custom folder names.
