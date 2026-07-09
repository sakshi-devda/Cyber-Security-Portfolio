import os
import shutil

# --------------------------------------------------
# File Organizer
# Author: Sakshi Devda
# Description: Organize files into folders based on
#              their file extensions.
# --------------------------------------------------

print("=" * 40)
print("        FILE ORGANIZER")
print("=" * 40)

# Current working directory
source_folder = os.getcwd()

# File type categories
file_types = {
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".bmp"],
    "Documents": [".pdf", ".doc", ".docx", ".txt", ".ppt", ".pptx", ".xls", ".xlsx"],
    "Videos": [".mp4", ".mkv", ".avi", ".mov"],
    "Audio": [".mp3", ".wav", ".aac"],
    "Archives": [".zip", ".rar", ".7z"],
    "Python": [".py"],
}

# Organize files
for file in os.listdir(source_folder):

    file_path = os.path.join(source_folder, file)

    # Skip folders
    if os.path.isdir(file_path):
        continue

    # Get file extension
    extension = os.path.splitext(file)[1].lower()

    # Move file to matching folder
    for folder, extensions in file_types.items():

        if extension in extensions:

            destination_folder = os.path.join(source_folder, folder)

            # Create folder if it doesn't exist
            os.makedirs(destination_folder, exist_ok=True)

            # Move file
            shutil.move(file_path, os.path.join(destination_folder, file))

            print(f"Moved: {file} → {folder}")

            break

print("\nFiles organized successfully!")
