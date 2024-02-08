# accepting function as argument
def loud(text):
    return text.upper()


def quiet(text):
    return text.lower()


def hello(func, text):
    print(func(text))


hello(loud, "Hello")
hello(quiet, "Hello")


# returning function from a function
def outer_function(x):
    def inner_function(y):
        return x*y
    return inner_function


# the `variable_1` will store the address of `inner_function` as a object with having access to a variable `x` with assinged value as 5 at non-local scope
variable_1 = outer_function(5)


variable_2 = variable_1(1)
variable_3 = variable_1(2)
variable_4 = variable_1(3)

print(variable_2)
print(variable_3)
print(variable_4)
