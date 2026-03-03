# file_renamer.py
import os

# Folder path
folder_path = "files_to_rename"

# Counter
count = 1

# Loop through files
for filename in os.listdir(folder_path):
    if filename.endswith(".jpg"):
        new_name = f"image_{count:03}.jpg"
        os.rename(os.path.join(folder_path, filename),
                  os.path.join(folder_path, new_name))
        print(f"{filename} renamed to {new_name}")
        count += 1

print("All files renamed successfully!")