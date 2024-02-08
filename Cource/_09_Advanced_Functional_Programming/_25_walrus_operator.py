# walrus operator `:=` is used for assingment of variables in the larger expressions

while True:
    choice = int(input("Enter the choice --> "))
    if choice == 0:
        break
    print("do something")

while choice := int(input("Enter the choice --> ")) != 0:
    print("do something")
