# calculator functions
def addition(a, b):
    print("The addition of these two numbers is", a + b)


def subtraction(a, b):
    print("The subtraction of these two numbers is", a - b)


def multiplication(a, b):
    print("The multiplication of these two numbers is", a * b)


def division(a, b):
    print("The division of these two numbers is", a % b)


# driver function
def driverfunc():
    a = int(input("Enter the two numbers --> "))
    b = int(input())
    choice = int(input("1.Addition\t2.Subtraction\t3.Multiplication\t4.Division\n"))
    match choice:
        case 1:
            addition(a, b)
        case 2:
            subtraction(a, b)
        case 3:
            multiplication(a, b)
        case 4:
            division(a, b)
        case _:
            print("Invalid choice")
            driverfunc()


# Driver function call
driverfunc()
