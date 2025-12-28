from datetime import datetime
from pathlib import Path

# Define where the log file will be created or updated
LOG_PATH = Path("log.txt")

def log_action(message: str):
    """
    Append a log entry to log.txt with a timestamp.

    Args:
        message (str): The text to log (e.g. "Moved file.txt → Documents")
    """
    # Ensure the log file exists — open() with "a" will create it if missing
    with open(LOG_PATH, "a", encoding="utf-8") as f:
        # Format: YYYY-MM-DD HH:MM:SS - message
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        f.write(f"{timestamp} - {message}\n")

def read_logs():
    """
    Read and print all log entries.
    Useful for debugging or checking what the program did previously.
    """
    if not LOG_PATH.exists():
        print("No log file found yet.")
        return

    print("\n📜 Log History:\n" + "-" * 40)
    with open(LOG_PATH, "r", encoding="utf-8") as f:
        print(f.read())

# Optional test section — lets you test it by running this file directly
if __name__ == "__main__":
    log_action("Test log entry created successfully.")
    print("Wrote a test log entry to log.txt")
    read_logs()
