import sqlite3
from pathlib import Path

DB_PATH = Path("file_organizer.db")

def init_db():
    """Initialize SQLite database with a logs table."""
    conn = sqlite3.connect(DB_PATH) #connects to it if it exists OR creates one if it doesn't exist
    cursor = conn.cursor()
    # the id is hidden by default with name "rowid"
    # So defining id INTEGER PRIMARY KEY just makes that visible and controlled by you rather than hidden and internal.
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS actions (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            timestamp TEXT NOT NULL,
            action TEXT NOT NULL
        )
    """)
    conn.commit()
    conn.close()


def log_to_db(action: str):
    """Insert a log record into the database."""
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute(
        #INSERT INTO actions (we're inserting into only these columns) VALUES (these values)
        "INSERT INTO actions (timestamp, action) VALUES (datetime('now', 'localtime'), ?)",
        (action,)
    )
    
    conn.commit()
    conn.close()

#why 2nd arguement has to be a tuple or list?
#The cursor.execute() function expects its second argument to be a sequence (an iterable) of parameters — because it’s designed to handle any number of placeholders (?).

#if we have any placeholders in the first arguement then we're required to have a 2nd arguement that is used to fill in those placeholders

#if we specify a 2nd arguement even though our first arguement doesn't have a placeholder there'll be an error, same vise versa

#each ? is mappe to one value from your provided sequence, in order. (in order of how the 2nd argument is)



#Tiny analogy for why we use 2 arguements and "?" placeholders
# Unsafe = handing someone a paper with text pasted into the middle of a sentence. If the pasted text says “burn this house,” they might follow it.
# Safe = you hand them the sentence with a blank and a sealed envelope with the text. They open the envelope and put the content into the blank as plain text. The content can’t change the sentence’s rules.