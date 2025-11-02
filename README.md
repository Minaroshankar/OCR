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

    EXAMPLE(rename_images_in_directory):
    base_path = directory path(input)
    rename_images_in_directory(base_path)


    EXAMPLE(process_excel_and_save_labels):

    file_path = excel path(test)
    base_path = directory path(input)
    output_file = text file

    process_excel_and_save_labels(file_path, base_path, output_file)


## Requirements

- Python 3.7 or higher  
- Required library:
  - `pandas`  
- Uses only built-in and lightweight dependencies.

Install dependencies:
```bash
pip install pandas

## Requirements

- Python 3.7 or higher  
- Required library:
  - `pandas`  
- Uses only built-in and lightweight dependencies.

Install dependencies:
```bash
pip install pandas



