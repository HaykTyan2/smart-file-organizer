import shutil
from pathlib import Path
from src.config_manager import load_config, update_config
from src.logger import log_action


def organize_files(folder_path):
    """
    Main function that scans the target folder, categorizes, and moves files.
    Creates 'Organized' folder inside the target directory automatically.
    """

    base_path = Path(folder_path)

    # Validate the given path
    if not base_path.exists() or not base_path.is_dir():
        print("The specified folder path is invalid.")
        return

    print(f"\nOrganizing files in: {base_path}")

    # Load the config mapping from config.json
    config = load_config()

    # Create an 'Organized' folder inside the target directory
    organized_dir = base_path / "Organized"
    # "Make a folder at this exact location"
    organized_dir.mkdir(exist_ok=True)

    # Iterate through all items in the folder
    for file in base_path.iterdir():
        # Skip the Organized folder itself and any directories
        if file.is_dir() or file.name == "Organized":
            continue

        ext = file.suffix.lower()  # e.g. '.pdf'
        category_found = None

        # Find which category this extension belongs to
        for category, extensions in config.items():
            if ext in extensions:
                category_found = category
                break

        # If known category found → move file there
        if category_found:
            move_file_to_category(file, organized_dir / category_found)
        else:
            # Unknown file type — handle interactively
            handle_unknown_extension(file, config, organized_dir)

    print("\nOrganization complete!")
    log_action(f"Finished organizing folder: {base_path}")


def move_file_to_category(file_path: Path, destination_folder: Path):
    """
    Move a single file to its destination category folder.
    """
    destination_folder.mkdir(exist_ok=True)  # Create folder if it doesn't exist

    try:
        shutil.move(str(file_path), str(destination_folder / file_path.name))
        log_action(f"Moved {file_path.name} → {destination_folder.name}")
        print(f"Moved {file_path.name} → {destination_folder.name}")
    except Exception as e:
        print(f"Could not move {file_path.name}: {e}")
        log_action(f"Error moving {file_path.name}: {e}")


def handle_unknown_extension(file_path: Path, config: dict, organized_dir: Path):
    """
    Handle files with unknown extensions by asking the user for a category.
    Updates config.json automatically with the new rule.
    """
    ext = file_path.suffix.lower()

    print(f"\nUnknown file type detected: {file_path.name} ({ext})")
    category = input("Enter category name to assign this type (e.g. Images, Documents): ").strip()

    if not category:
        print("Skipped file (no category entered).")
        log_action(f"Skipped unknown file: {file_path.name}")
        return
    
    # Update the config and save it
    update_config(ext, category)

    # Move file to the new category folder
    move_file_to_category(file_path, organized_dir / category)

    log_action(f"Learned new extension {ext} assigned to '{category}'")
    print(f"Learned and moved {file_path.name} → {category}")


# Optional direct-run mode for testing
if __name__ == "__main__":
    folder = input("Enter the path of the folder you want to organize: ").strip('"')
    organize_files(folder)
