# *argument_name --> the astrick (*) symbol will pack the all arguments
#                    that the function has received into the tuple named
#                    as `argument_name`. It is used so that the function can get
#                    the variable amount of arguments

def add_the_numbers(*args):  # args will be the name of the tuple
    sum = 0
    for item in args:
        sum += item
    print(f"The sum of these {len(args)} numbers is {sum}")


add_the_numbers(1, 2, 4, 4, 444)
add_the_numbers(1, 2, 41, 3, 2, 5, 74, 26, 2)
