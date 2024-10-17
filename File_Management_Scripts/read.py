import os

def list_files_with_extension(directory, extension, output_file='file_names.txt'):
    with open(output_file, 'w') as f:
        for file in os.listdir(directory):
            if file.endswith(extension) and file != os.path.basename(output_file):
                f.write(file[:-len(extension)] + '\n')

    print(f"File names with extension '{extension}' have been saved to '{output_file}'.")

#Note: This is my directory file
directory = r"C:\Users\amitv\Videos\example" 
extension = ".txt"

list_files_with_extension(directory, extension)
