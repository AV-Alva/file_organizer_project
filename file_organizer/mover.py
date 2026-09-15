import shutil
from pathlib import Path

from .logger import log_operation


def move_file(file_path, category, base_folder):
    """Move a file into its category folder."""

    source = Path(file_path)
    destination_folder = Path(base_folder) / category

    try:
        # Create destination folder if it does not exist
        destination_folder.mkdir(parents=True, exist_ok=True)

        destination_file = destination_folder / source.name

        # Handle duplicate filenames
        if destination_file.exists():
            counter = 1

            while destination_file.exists():
                new_name = (
                    f"{source.stem}_{counter}{source.suffix}"
                )

                destination_file = destination_folder / new_name
                counter += 1

        shutil.move(str(source), str(destination_file))

        log_operation(
            f"SUCCESS: {source.name} moved to {destination_file}"
        )

        return destination_file

    except PermissionError as error:
        log_operation(
            f"FAILED: Permission denied for {source.name} - {error}"
        )
        raise

    except OSError as error:
        log_operation(
            f"FAILED: Could not move {source.name} - {error}"
        )
        raise
