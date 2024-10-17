# File Management Scripts

This repository contains two Python scripts to perform basic file operations:

1. **Listing Files with Specific Extension**  
2. **Renaming and Moving Files**

---

## Scripts Overview

### 1. List Files with Specific Extension  
This script lists all files with a given extension in a specified directory and saves the filenames (without extensions) to a text file.

**Code:**  
```python
import os

def list_files_with_extension(directory, extension, output_file='file_names.txt'):
    with open(output_file, 'w') as f:
        for file in os.listdir(directory):
            if file.endswith(extension) and file != os.path.basename(output_file):
                f.write(file[:-len(extension)] + '\n')

    print(f"File names with extension '{extension}' have been saved to '{output_file}'.")

# Example usage
directory = r"C:\Users\amitv\Videos\example" 
extension = ".txt"

list_files_with_extension(directory, extension)
```

**How it works:**  
- Lists all `.txt` files (or any specified extension) in the `directory`.
- Saves the filenames (without extensions) into `file_names.txt`.
  
---

### 2. Rename and Move Files  
This script renames files following a specific pattern and moves them to a new directory.

**Code:**  
```python
import os
import shutil

# Directories
source_folder = r'C:\Users\amitv\Videos\example'
destination_folder = r'C:\Users\amitv\Videos\example\edited_files'

os.makedirs(destination_folder, exist_ok=True)

for i in range(1, 11):
    old_name = f'example{i}.txt'
    new_name = f'edit_example{i}.txt'

    old_file_path = os.path.join(source_folder, old_name)
    new_file_path = os.path.join(destination_folder, new_name)

    if os.path.isfile(old_file_path):
        shutil.move(old_file_path, new_file_path)
        print(f'Renamed and moved: {old_file_path} -> {new_file_path}')
    else:
        print(f'File {old_file_path} does not exist.')
```

**How it works:**  
- Checks for files named `example1.txt` to `example10.txt` in the `source_folder`.
- Renames them to `edit_example1.txt` to `edit_example10.txt`.
- Moves the renamed files to the `edited_files` folder.

---

## Requirements

- Python 3.x  
- No external libraries required (only uses `os` and `shutil` from the standard library).

---

## Usage

1. Update the `directory`, `source_folder`, and `destination_folder` variables to match your desired paths.
2. Run each script as needed to manage your files.

---

## Acknowledgment  

This code was generated under the guidance of **ChatGPT**.

---
