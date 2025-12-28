import json
from pathlib import Path

# Define where the configuration file lives
CONFIG_PATH = Path("config.json")

def load_config():
    """
    Load and return the configuration dictionary from config.json.
    If the file doesn't exist or is broken, create a blank default config.
    """
    if not CONFIG_PATH.exists():
        print("config.json not found. Creating a new one...")
        default_config = {}
        save_config(default_config)
        return default_config

    try:
        with open(CONFIG_PATH, "r") as file:
            config = json.load(file)
            return config
    except json.JSONDecodeError:
        print("Error: config.json is corrupted or invalid JSON.")
        print("Creating a fresh empty configuration.")
        save_config({})
        return {}


def save_config(config_data):
    """
    Save the given configuration dictionary back into config.json.
    Writes in a pretty, readable format.
    """
    with open(CONFIG_PATH, "w") as file:
        json.dump(config_data, file, indent=4)


def update_config(new_ext, category):
    """
    Add a new file extension to the specified category in config.json.
    Automatically creates the category if it doesn’t exist yet.
    """
    config = load_config()

    # Ensure the extension starts with a dot (e.g. ".pdf")
    if not new_ext.startswith("."):
        new_ext = "." + new_ext

    # Add the category if missing
    if category not in config:
        config[category] = []

    # Add extension if it's not already present
    if new_ext not in config[category]:
        config[category].append(new_ext)
        save_config(config)
    else:
        print(f"Extension {new_ext} already exists in '{category}'.")


# Debug / manual test
if __name__ == "__main__":
    # Quick test to verify it's working correctly
    cfg = load_config()
    print("Loaded configuration:", cfg)

    # Example of adding a new type dynamically
    update_config(".psd", "Images")
