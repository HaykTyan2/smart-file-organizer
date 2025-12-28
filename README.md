## smart-file-organizer

A Python-based file organization tool that automatically sorts files into folders based on file type, learns new extensions dynamically, and logs all actions to both a text log and a SQLite database.

This project was built as a learning exercise to understand filesystem automation, configuration-driven behavior, logging, and lightweight database usage in Python.

What this project does

The program scans a user-selected folder and organizes files into categorized subfolders.

It allows the user to:
```
• Automatically organize files by extension (Images, Documents, Videos, etc.)
• Learn new file types interactively when unknown extensions are found
• Store learned rules in a JSON configuration file
• Log every action to a text log and SQLite database
• Re-run safely without duplicating work
```
--------------------------------------------------------------------------------------------------------
How it works (high level)
```
• The user provides a folder path
• A configuration file defines extension-to-category mappings
• Files are scanned one by one
• Known file types are moved automatically
• Unknown file types prompt the user for a category
• New rules are saved to config.json
• All actions are logged to a file and database
• An Organized/ directory is created automatically
```
--------------------------------------------------------------------------------------------------------

## Project structure
```
smart-file-organizer/
├── src/
│   ├── organizer.py        # Core file organization logic
│   ├── config_manager.py   # Loads and updates config.json
│   ├── logger.py           # Logs actions to log.txt
│   ├── database.py         # SQLite logging backend
│
├── config.json              # File type configuration
├── main.py                  # Entry point and user interaction
├── requirements.txt
├── .gitignore
├── README.md
```
--------------------------------------------------------------------------------------------------------

##File explanations

main.py

This is the main entry point of the program.

It is responsible for:
```
• Initializing the database
• Requesting user input
• Validating folder paths
• Triggering the organization process
• Logging start and completion events
```
--------------------------------------------------------------------------------------------------------

## src/organizer.py

Handles the actual organization process.

This file:
```
• Scans the target folder
• Moves files into categorized subfolders
• Creates an Organized/ directory automatically
• Handles unknown file types interactively
```
--------------------------------------------------------------------------------------------------------

## src/config_manager.py

Manages the configuration file.

This file:
```
• Loads extension mappings from config.json
• Creates config.json if missing
• Saves newly learned file type rules
```
--------------------------------------------------------------------------------------------------------

## src/logger.py

Handles logging.

This file:
```
• Appends timestamped actions to log.txt
• Allows viewing past actions
• Supports debugging and auditing
```
--------------------------------------------------------------------------------------------------------
## src/database.py

Handles SQLite logging.

This file:
```
• Creates the SQLite database if needed
• Stores timestamped action records
• Keeps logs structured and queryable
```
--------------------------------------------------------------------------------------------------------

## Installation / Process

Clone the repository:
```
git clone https://github.com/YOUR_USERNAME/smart-file-organizer.git
```
```
cd smart-file-organizer
```
--------------------------------------------------------------------------------------------------------

## Install dependencies:
```
pip install -r requirements.txt
```
--------------------------------------------------------------------------------------------------------

## Run the program:
```
python main.py
```
--------------------------------------------------------------------------------------------------------

## Output
```
• Files are moved into Organized/ subfolders
• New categories are learned automatically
• Logs are written to log.txt
• Actions are recorded in file_organizer.db
```
--------------------------------------------------------------------------------------------------------

## Notes and limitations
```
• This project runs locally only
• It is designed for personal file organization
• The organizer skips directories by default
• Existing files are never overwritten
• SQLite database and logs are generated at runtime
```
--------------------------------------------------------------------------------------------------------

## License

This project is provided for educational and personal use.
