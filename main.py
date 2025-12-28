import os
from pathlib import Path
from src.organizer import organize_files
from src.logger import log_action
from src.database import init_db, log_to_db   # ← added this line


def main():
    """
    Entry point for the Smart File Organizer.
    Handles user input and triggers the organization process.
    """
    print("\nSmart File Organizer")
    print("───────────────────────────────")

    # Initialize the database here
    init_db()   # ← this ensures the database and table are ready before anything else

    # Ask user for the target folder
    folder_input = input("Enter the full path of the folder you want to organize: ").strip('"').strip("'")

    if not folder_input:
        print("No folder entered. Exiting.")
        return

    folder_path = Path(folder_input)

    # Validate the folder path
    if not folder_path.exists() or not folder_path.is_dir():
        print("Invalid folder path. Please check and try again.")
        return

    print(f"\nFolder found: {folder_path}")

    # Log to file and database
    log_action(f"Started organizing: {folder_path}")
    log_to_db(f"Started organizing: {folder_path}")

    # Run the organizer
    organize_files(folder_path)

    print("\nAll done! Your files have been organized.")

    log_action(f"Completed organizing: {folder_path}")
    log_to_db(f"Completed organizing: {folder_path}")

    # Optional: ask if the user wants to open the organized folder
    choice = input("Would you like to open the folder now? (y/n): ").lower()
    if choice == "y":
        try:
            os.startfile(folder_path)  # works on Windows
        except AttributeError:
            # macOS/Linux fallback
            os.system(f"open '{folder_path}'" if os.name == "posix" else f"xdg-open '{folder_path}'")


if __name__ == "__main__":
    main()
