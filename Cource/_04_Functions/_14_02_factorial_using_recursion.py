def fact(a):
    if a == 1 or a == 0:
        return 1
    else:
        return fact(a - 1) * a


n = int(input("Enter the number whose factorial has to be found --> "))
print("The factorial of the number is", fact(n))
