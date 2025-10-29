import os


# Define the base path as a variable
base_path = r"C:\Users\Mina\Desktop\New folder (3)"

# Ensure base_path ends with a separator for consistency
if not base_path.endswith(os.sep):
    base_path += os.sep

# Walk through the directory recursively
for root, dirs, files in os.walk(base_path):
    for file in files:
        if file.lower().endswith('.jpg'):  # Check for .jpg files (case-insensitive)
            file_path = os.path.join(root, file)
            
            # Step 1: Remove spaces from the filename
            stem, ext = os.path.splitext(file)
            new_stem = stem.replace(" ", "")
            temp_name = f"{new_stem}{ext}"
            temp_file_path = os.path.join(root, temp_name)
            
            # Rename to remove spaces
            os.rename(file_path, temp_file_path)
            
            # Step 2: Get relative path from base
            relative_path = os.path.relpath(temp_file_path, base_path)
            
            # Split relative path into folders and file
            parts = relative_path.split(os.sep)
            folders = parts[:-1]  # All folders in order
            original_name = parts[-1]
            
            # Get stem and extension again after space removal
            stem, ext = os.path.splitext(original_name)
            
            # Reverse the folders and join with '_'
            reversed_folders = '_'.join(reversed(folders))
            
            # Create new name: stem + '_' + reversed_folders + ext
            new_name = f"{stem}_{reversed_folders}{ext}"
            
            # New file path
            new_file_path = os.path.join(root, new_name)
            
            # Rename the file with the new naming convention
            os.rename(temp_file_path, new_file_path)
            print(f"Renamed: {temp_file_path} -> {new_file_path}")


print('done')