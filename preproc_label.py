import pandas as pd
import os

file_path = r"C:\Users\Mina\Desktop\excel khayamm.xlsx"

xls = pd.ExcelFile(file_path)

base_path = r"C:\Users\Mina\Desktop\work\ocr\Khayamm\Khayamm"


output_file = "output.txt"

with open(output_file, "w", encoding="utf-8") as f:
    for sheet_name in xls.sheet_names:
        df = pd.read_excel(file_path, sheet_name=sheet_name, header=None)
        print(f"Processing sheet: {sheet_name}")
        for idx, row in df.iterrows():
                folder_names = row.iloc[1:5]
                label = row.iloc[0]
                # Remove excel unnecessary tag and parameters and parse to string
                # folder_names = [str(name) for name in folder_names]
                folder_names = [
                    name if isinstance(name, str) and name.strip() != ""
                    else str(int(name))
                    for name in folder_names
                    if (
                        (isinstance(name, str) and name.strip() != "") or
                        (isinstance(name, (int, float)) and not (isinstance(name, float) and str(name) == "nan"))
                    )
                ]

                # Concat column 1 to 5 with \ together
                full_path = os.path.join(base_path, '\\'.join(folder_names))

                # Check folder exist
                if os.path.exists(full_path):
                    # Get the name of files of current folder (full path) (list of file names)
                    for file_name in os.listdir(full_path):
                        # Check file extension is jpg, jpeg or png
                        if file_name.lower().endswith((".jpg", ".jpeg", ".png")):
                            # Save into text file with column 0 as label
                            f.write(f"{file_name} {label}\n")
                else:
                    print(f"no path {full_path}")

print("done")

