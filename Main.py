import os
import shutil

print("File Organizer developed by Monty")
folder_path = input("Enter folder path to organize: ")

files = os.listdir(folder_path)

for file in files:
    if os.path.isfile(os.path.join(folder_path, file)):
        extension = file.split(".")[-1]

        new_folder = os.path.join(folder_path, extension + "_files")

        if not os.path.exists(new_folder):
            os.makedirs(new_folder)

        shutil.move(os.path.join(folder_path, file), os.path.join(new_folder, file))

print("Files organized successfully")
