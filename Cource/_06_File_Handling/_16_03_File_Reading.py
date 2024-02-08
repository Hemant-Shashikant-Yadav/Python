try:
    with open(file="_16_02_01_text.txt") as file:
        print(file.read())
except FileNotFoundError as e:
    print("Bruh the compiler says\n" + str(e))
# if we use `with` the file will be automatically closed
