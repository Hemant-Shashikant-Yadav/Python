
# variable_name `lambda` arguments: return_statment


def multiply(a, b):
    return a*b



multiply_lambda = lambda  a, b: a*b

print(multiply_lambda(2,3))

check_age = lambda age: True if age > 17 else False


print(check_age(10))
print(check_age(19))

