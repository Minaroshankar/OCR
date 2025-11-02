import os
import pandas as pd


def rename_images_in_directory(base_path: str) -> None:
    """
    Removes spaces from .jpg filenames and renames them to include reversed folder structure.

    Parameters:
        base_path (str): Base directory to search for .jpg files recursively.
    """
    # Ensure base_path ends with a separator
    if not base_path.endswith(os.sep):
        base_path += os.sep

    # Walk through all subdirectories
    for root, dirs, files in os.walk(base_path):
        for file in files:
            if file.lower().endswith('.jpg'):
                file_path = os.path.join(root, file)

                # Step 1: Remove spaces
                stem, ext = os.path.splitext(file)
                new_stem = stem.replace(" ", "")
                temp_name = f"{new_stem}{ext}"
                temp_file_path = os.path.join(root, temp_name)
                os.rename(file_path, temp_file_path)

                # Step 2: Create relative path (for folder structure)
                relative_path = os.path.relpath(temp_file_path, base_path)
                parts = relative_path.split(os.sep)
                folders = parts[:-1]
                original_name = parts[-1]
                stem, ext = os.path.splitext(original_name)

                # Step 3: Reverse folder names and join with '_'
                reversed_folders = '_'.join(reversed(folders))
                new_name = f"{stem}_{reversed_folders}{ext}"
                new_file_path = os.path.join(root, new_name)

                # Step 4: Rename to final name
                os.rename(temp_file_path, new_file_path)
                print(f"Renamed: {temp_file_path} -> {new_file_path}")

    print("Image renaming done.")


def process_excel_and_save_labels(file_path: str, base_path: str, output_file: str = "output.txt") -> None:
    """
    Reads an Excel file with folder info and labels,
    searches for images in the given folders,
    and writes image names and labels to a text file.

    Parameters:
        file_path (str): Path to Excel file.
        base_path (str): Base directory containing image folders.
        output_file (str): Path to output .txt file.
    """
    xls = pd.ExcelFile(file_path)

    with open(output_file, "w", encoding="utf-8") as f:
        for sheet_name in xls.sheet_names:
            df = pd.read_excel(file_path, sheet_name=sheet_name, header=None)
            print(f"Processing sheet: {sheet_name}")

            for idx, row in df.iterrows():
                folder_names = row.iloc[1:5]
                label = row.iloc[0]

                # Clean folder names (skip empty / NaN)
                folder_names = [
                    name if isinstance(name, str) and name.strip() != ""
                    else str(int(name))
                    for name in folder_names
                    if (
                        (isinstance(name, str) and name.strip() != "") or
                        (isinstance(name, (int, float)) and not (isinstance(name, float) and str(name) == "nan"))
                    )
                ]

                # Join folder names into a path
                full_path = os.path.join(base_path, '\\'.join(folder_names))

                # Search for image files
                if os.path.exists(full_path):
                    for file_name in os.listdir(full_path):
                        if file_name.lower().endswith((".jpg", ".jpeg", ".png")):
                            f.write(f"{file_name} {label}\n")
                else:
                    print(f"No path found: {full_path}")

    print("label dict done.")
