# CLI File Organizer

A simple CLI tool to organize files in a directory by their extensions, moving them into user-customized folders. Built to demonstrate file handling and automation without frameworks.

## Features
- Navigate to a directory and organize files interactively in real-time, detecting changes during runtime.
- Supports custom folder names via user input for detected file extensions (e.g., `.jpg`, `.txt`, `.html`, `.mp4`).
- Automatically identifies available file types and only applies rules to existing extensions, ignoring irrelevant ones.
- Example: If directory has `.jpg` (e.g., "cat.jpg") and `.txt` (e.g., "notes.txt", "todo.txt"), you can pair them to custom folders like `.jpg` → `images`, `.txt` → `notes`.
- Supports undo to revert the last organization.

## Commands
- `goin <path>`: Navigate to the specified directory (like `cd`).
- `org`: Organize files in the current directory—prompts for custom folder names based on detected extensions.
- `undo`: Revert the last organization (if applicable).
- `exit`: Exit the application

## Usage
1. Clone the repo and navigate to this folder.
2. Run the CLI app (e.g., `python main.py` or equivalent, depending on the language).
3. Use `go <path>` to navigate to a directory with unorganized files.
4. Run `org` to detect files, input custom folder names for each extension, and sort accordingly.
5. Run `undo` to revert if needed.

*Note*: Focuses on real-time file detection and user-defined organization.