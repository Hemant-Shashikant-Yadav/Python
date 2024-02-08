import os

source_path = "_16_05_02_duplicate.txt"
destination_path = "F:\\study material\\codes\\PYTHON\\MovedFile.txt"
try:
    if os.path.exists(destination_path):
        print("The file is already present at the destination")
    else :
        os.replace(src=source_path,dst=destination_path)
        print("File was moved");
except FileNotFoundError as e:
    print("File not found")
