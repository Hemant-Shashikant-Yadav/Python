import os

import shutil

filepath = "text.txt"
empty_folder_path = "16_07_02_empty_folder"
non_empty_folder_path = "16_07_03_non_empty_folder"
try:
    os.remove(filepath)
    print("file was removed :)")
except FileNotFoundError:
    print("file not found :(")

try:
    os.rmdir(empty_folder_path)
    print("empty folder was removed :)")
except OSError:
    print("The folder you want to remove is not empty:( or the folder is not present")

try:
    os.rmdir(non_empty_folder_path)
except:
    print("cannot remove non-empty folder")

try:
    shutil.rmtree(non_empty_folder_path)
except Exception as e:
    print(f"Bruh {e}" )


# os.remove --> needs file
# os.rmdir  --> needs empty folder
# shutil.rmtree --> needs a folder no matter the contents
