from pathlib import Path

from file_organizer import (
    detect_file_type,
    move_file,
    log_operation,
    UnsupportedFileError,
)


def organize_folder(folder_path):
    """Organize all supported files inside the given folder."""

    folder = Path(folder_path)

    if not folder.exists():
        print("Folder does not exist.")
        log_operation(
            f"FAILED: Folder does not exist - {folder_path}"
        )
        return

    if not folder.is_dir():
        print("The provided path is not a folder.")
        log_operation(
            f"FAILED: Not a folder - {folder_path}"
        )
        return

    for file_path in folder.iterdir():

        # Ignore folders
        if not file_path.is_file():
            continue

        try:
            category = detect_file_type(file_path)

            destination = move_file(
                file_path,
                category,
                folder
            )

            print(
                f"Moved: {file_path.name} "
                f"-> {destination.parent.name}/"
            )

        except UnsupportedFileError as error:
            print(f"Skipped: {file_path.name} - {error}")
            log_operation(
                f"FAILED: {file_path.name} - {error}"
            )

        except FileNotFoundError as error:
            print(f"File not found: {error}")
            log_operation(f"FAILED: {error}")

        except PermissionError as error:
            print(f"Permission denied: {error}")

        except OSError as error:
            print(f"File operation failed: {error}")


def main():
    """Run the File Organizer application."""

    print("=" * 40)
    print("       PYTHON FILE ORGANIZER")
    print("=" * 40)

    folder_path = input(
        "Enter the folder path to organize: "
    )

    organize_folder(folder_path)

    print("\nFile organization completed.")
    print("Check file_organizer.log for operation history.")


if __name__ == "__main__":
    main()