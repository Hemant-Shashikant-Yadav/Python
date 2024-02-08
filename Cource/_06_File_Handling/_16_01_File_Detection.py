import os

path = "F:\\study material\\codes\\java"

if os.path.exists(path):
    print("This path exists in the OS")
    if os.path.isfile(path):
        print("The path is file")
    elif os.path.isdir(path):
        print("The path is directory(folder)")
else:
    print("This path doesn't exist")
