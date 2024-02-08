try:
    file = open(file="_16_02_01_text.txt")
    print(file.read())
    file.close()
except FileNotFoundError:
    print("File not found :(")

