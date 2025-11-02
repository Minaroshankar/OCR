# Image Processing and Label Generation Scripts

This repository contains two Python scripts for automating image file organization and dataset preparation.  
The scripts are designed to help manage large image datasets and create label text files for machine learning workflows.

---

## Overview

The repository includes two automation scripts:

- **rename_images.py**: Cleans and standardizes `.jpg` filenames recursively based on their folder hierarchy.  
- **generate_labels.py**: Reads folder structures and labels from an Excel file and generates a `.txt` file mapping filenames to their labels.

These tools are useful for preprocessing image datasets before training or organizing large photo collections systematically.

---

## Scripts

### 1. rename_images.py

**Purpose:**  
Renames all `.jpg` files in a directory and its subfolders by removing spaces and appending folder names (in reverse order) to the filenames.

**Main Features:**
- Recursively processes nested folders  
- Removes spaces from filenames  
- Builds filenames using reversed folder hierarchy  
- Prints all rename operations for verification  

---

### 2. generate_labels.py

**Purpose:**  
Generates a label text file from an Excel sheet containing folder hierarchy and corresponding labels.  
Each image file found in the specified folders is written to the output text file alongside its label.

**Main Features:**
- Reads Excel files with `pandas`  
- Constructs folder paths dynamically based on Excel columns  
- Checks for `.jpg`, `.jpeg`, and `.png` files  
- Saves results in a single `.txt` output file with filenames and their associated labels  

---

## Requirements

- Python 3.7 or higher  
- Required library:
  - `pandas`  
- Uses only built-in and lightweight dependencies.

Install dependencies:
```bash
pip install pandas

## Example Usage

# ==========================
# Example 1: Rename Images
# ==========================

rename_images_in_directory(
    base_path=r"path"
)

"""
this function is for renaming image files

Steps:
1. Walk through all subdirectories of the given base_path.
2. Remove any spaces from .jpg file names.
3. Rename each image by appending its parent folder names in reverse order, joined by '_'.

Parameters:
- base_path: path to the base directory that contains image subfolders

Example:
If you have:
    C:\Data\A\B\sample 1.jpg
it becomes:
    C:\Data\A\B\sample1_B_A.jpg
"""



# ==========================
# Example 2: Process Excel and Create Label File
# ==========================

process_excel_and_save_labels(
    file_path=r"file_path",
    base_path=r"Excel_path",
    output_file=r"text_file"
)

"""
this function is for reading Excel data and generating a label text file

Steps:
1. Reads an Excel file containing folder names and labels.
2. Traverses through folders (columns 1–4 of each row) under base_path.
3. Finds image files (.jpg, .jpeg, .png) in each corresponding directory.
4. Writes their filenames and labels into a text file (output.txt).

Parameters:
- file_path: path to the Excel file that contains folder names and labels
- base_path: path to the main folder that contains all subdirectories
- output_file: path where the generated label text file will be saved

Example:
If the Excel has:
    Row:  Label | Folder1 | Folder2 | Folder3 | Folder4
The program will search:
    base_path\Folder1\Folder2\Folder3\Folder4\
and write each image name with its label, like:
    image1.jpg Label1
    image2.jpg Label1
"""



# ==========================
# Example 3: Combined Main Run
# ==========================

def main():
    """
    This function runs both processes sequentially:
    1. Renames all images inside a directory.
    2. Processes the Excel file to generate label mappings.
    """

    # Step 1: Rename images
    rename_images_in_directory(
        base_path=r"base_path"
    )

    # Step 2: Process Excel and save labels
    process_excel_and_save_labels(
        file_path=r"path",
        base_path=r"path",
        output_file=r"path"
    )

    print("All tasks completed successfully.")


# Run main
if __name__ == "__main__":
    main()
