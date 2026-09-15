from pathlib import Path

from .exceptions import UnsupportedFileError


FILE_CATEGORIES = {
    ".jpg": "Images",
    ".jpeg": "Images",
    ".png": "Images",
    ".gif": "Images",

    ".txt": "Text",

    ".pdf": "Documents",
    ".doc": "Documents",
    ".docx": "Documents",

    ".csv": "Data",
    ".xlsx": "Data",

    ".mp3": "Audio",
    ".wav": "Audio",

    ".mp4": "Videos",
    ".mkv": "Videos",
}


def detect_file_type(file_path):
    """Return the destination category based on the file extension."""

    path = Path(file_path)

    if not path.exists():
        raise FileNotFoundError(f"File does not exist: {file_path}")

    if not path.is_file():
        raise ValueError(f"Path is not a file: {file_path}")

    extension = path.suffix.lower()

    if extension not in FILE_CATEGORIES:
        raise UnsupportedFileError(
            f"Unsupported file type: {extension or 'No extension'}"
        )

    return FILE_CATEGORIES[extension]
