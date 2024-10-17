import os
import shutil

#Note: This is my directory file
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
