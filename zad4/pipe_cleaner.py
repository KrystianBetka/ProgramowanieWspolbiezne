import os

directory_path = "."
files_in_directory = os.listdir(directory_path)
client_files = [file for file in files_in_directory if file.startswith('fifo') or file.startswith('kolejka')]

for file in client_files:
    file_path = os.path.join(directory_path, file)
    os.remove(file_path)

print("Removed",len(client_files),'files')