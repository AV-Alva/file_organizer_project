# Python File Organizer Using Packages and Modules

## Overview

This project is a Python-based **File Organizer** that automatically organizes files in a selected folder based on their file extensions.

The project is designed to demonstrate the practical use of:

* Python functions
* Modules
* Packages
* Imports
* Custom exceptions
* Exception handling
* File and folder operations
* Logging
* `pathlib`
* `shutil`

For example:

```text
photo.jpg   -> Images/
notes.txt   -> Text/
report.pdf  -> Documents/
data.csv    -> Data/
song.mp3    -> Audio/
video.mp4   -> Videos/
```

---

## Objective

The objective of this project is to understand how a larger Python application can be divided into multiple reusable modules instead of writing the complete program inside a single Python file.

Each module has a specific responsibility, making the application easier to understand, maintain, test, and extend.

---

## Project Structure

```text
file_organizer_project/
│
├── file_organizer/
│   ├── __init__.py
│   ├── detector.py
│   ├── mover.py
│   ├── logger.py
│   └── exceptions.py
│
├── main.py
├── README.md
└── file_organizer.log
```

The `file_organizer` directory is the Python package.

---

## Module Responsibilities

### `detector.py`

This module detects the extension of a file and determines which category the file belongs to.

Examples:

```text
.jpg  -> Images
.png  -> Images
.txt  -> Text
.pdf  -> Documents
.csv  -> Data
.mp3  -> Audio
.mp4  -> Videos
```

If the file extension is not supported, the module raises the custom `UnsupportedFileError`.

---

### `mover.py`

This module is responsible for moving files into their respective destination folders.

For example:

```text
photo.jpg
```

is moved to:

```text
Images/photo.jpg
```

The module also:

* Creates the destination folder if it does not exist
* Checks for duplicate filenames
* Renames duplicate files instead of overwriting them
* Handles permission-related errors
* Handles other file-system errors

For example, if `photo.jpg` already exists inside `Images`, another file with the same name can be renamed as:

```text
photo_1.jpg
photo_2.jpg
photo_3.jpg
```

---

### `logger.py`

This module records successful and failed file operations.

The application creates a log file:

```text
file_organizer.log
```

Example log entries:

```text
2026-09-15 18:10:25 - SUCCESS: photo.jpg moved to Images/photo.jpg
2026-09-15 18:10:26 - SUCCESS: report.pdf moved to Documents/report.pdf
2026-09-15 18:10:27 - FAILED: program.exe - Unsupported file type: .exe
```

Append mode is used so that previous log records are not deleted when the application runs again.

---

### `exceptions.py`

This module contains custom exceptions used by the application.

The project defines:

```python
class UnsupportedFileError(Exception):
    """Raised when the file type is not supported."""
    pass
```

`UnsupportedFileError` is raised when the program encounters a file extension that is not configured in the supported file categories.

For example:

```text
application.xyz
```

may result in:

```text
Unsupported file type: .xyz
```

---

### `__init__.py`

The `__init__.py` file tells Python that the `file_organizer` directory should be treated as a package.

It also exposes the main functions and exceptions from the package so that they can be imported conveniently.

Example:

```python
from file_organizer import (
    detect_file_type,
    move_file,
    log_operation,
    UnsupportedFileError,
)
```

---

### `main.py`

`main.py` is the entry point of the application.

It:

1. Accepts the folder path from the user.
2. Validates that the folder exists.
3. Iterates through the files in the folder.
4. Detects each file type.
5. Determines the appropriate destination.
6. Moves supported files.
7. Handles errors.
8. Records successful and failed operations in the log file.

`main.py` is kept outside the package so that the package can be imported normally.

---

## Supported File Categories

| File Extensions | Destination |
| --------------- | ----------- |
| `               |             |
