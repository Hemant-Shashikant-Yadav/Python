# This is same as switch case
age = int(input("Enter the age -->"))
match age:
    case 1:
        print("You are one years old")

    case 2:
        print("You are two years old")

    case 3:
        print("You are three years old")

    case 4:
        print("You are four years old")

    case _:
        print("Your age is not in the database")
