# OCR
Image Processing and Label Generation Scripts

This repository contains two Python scripts designed to automate image file management and dataset preparation.
They are particularly useful for organizing large collections of images and generating text-based label files for machine learning workflows.

Table of Contents

Overview

Scripts

1. rename_images.py

2. generate_labels.py

Requirements

Usage

Examples

Notes

License

Author

Overview

The repository includes:

A batch image renaming script that recursively cleans and standardizes .jpg filenames.

A dataset label generator that reads folder structures and labels from an Excel file and exports a .txt file for training pipelines.

Scripts
1. rename_images.py

Purpose:
Automatically renames all .jpg files in a base directory by removing spaces and appending folder names (in reverse order) to the filenames.

Key Features:

Recursively processes subfolders

Removes spaces from filenames

Appends folder hierarchy (reversed) to filenames

Prints all rename operations for tracking

Example:

Before:

C:\Users\Mina\Desktop\New folder (3)
│
├── Cats\Cute Cats\fluffy cat.jpg
└── Dogs\happy dog.jpg


After:

C:\Users\Mina\Desktop\New folder (3)
│
├── Cats\Cute Cats\fluffycat_Cute Cats_Cats.jpg
└── Dogs\happydog_Dogs.jpg


How to Run:

Update the path in the script:

base_path = r"C:\Users\Mina\Desktop\New folder (3)"


Execute the script:

python rename_images.py

2. generate_labels.py

Purpose:
Reads folder paths and labels from an Excel sheet, scans each folder for image files, and writes their filenames with corresponding labels to a text file.

Key Features:

Reads Excel file (.xlsx) using pandas

Builds folder paths dynamically

Checks for .jpg, .jpeg, and .png files

Outputs a output.txt file containing:

filename label


Excel Format Example:

Label	Folder 1	Folder 2	Folder 3	Folder 4
cat	A	B	C	D
dog	E	F		

Example Output (output.txt):

fluffycat_Cute Cats_Cats.jpg cat
happydog_Dogs.jpg dog


How to Run:

Update the paths in the script:

df = pd.read_excel(r"C:\Users\Mina\Desktop\excel khayamm.xlsx", header=None)
base_path = r"C:\Users\Mina\Desktop\Khayamm\Khayamm"


Execute:

python generate_labels.py


The script will create output.txt in the same directory.

Requirements

Python 3.7 or higher

Libraries:

pandas

os (built-in)

Install dependencies:

pip install pandas

Usage

Clone the repository:

git clone https://github.com/<your-username>/<repo-name>.git
cd <repo-name>


Modify the base_path and file locations as needed.

Run the scripts independently as shown above.

Examples

rename_images.py

Renamed: C:\...\fluffy cat.jpg -> C:\...\fluffycat_Cute Cats_Cats.jpg
Renamed: C:\...\wild cat.jpg -> C:\...\wildcat_Cats.jpg
done


generate_labels.py

no path C:\Users\Mina\Desktop\Khayamm\Khayamm\A\B\C\D
done

Notes

Always back up your files before running bulk rename scripts.

The label generator assumes your Excel file structure follows the described format.

Works best with consistent folder hierarchies.
