from datetime import datetime


LOG_FILE = "file_organizer.log"


def log_operation(message):
    """Record a file organizer operation in the log file."""

    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    with open(LOG_FILE, "a", encoding="utf-8") as log_file:
        log_file.write(f"{timestamp} - {message}\n")