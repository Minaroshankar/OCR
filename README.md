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

## Example Usage

    This functions run two processes:
    1. Renames all images inside a directory.
    2. Processes the Excel file to generate label mappings.
    """
    Example function 1:
        If you have:
            C:\Data\A\B\sample 1.jpg
        it becomes:
            C:\Data\A\B\sample1_B_A.jpg
    Example function 2:
        If the Excel has:
            Row:  Label | Folder1 | Folder2 | Folder3 | Folder4
        The program will search:
            base_path\Folder1\Folder2\Folder3\Folder4\
        and write each image name with its label, like:
            image1.jpg Label1
            image2.jpg Label1


## Requirements

- Python 3.7 or higher  
- Required library:
  - `pandas`  
- Uses only built-in and lightweight dependencies.

Install dependencies:
```bash
pip install pandas



