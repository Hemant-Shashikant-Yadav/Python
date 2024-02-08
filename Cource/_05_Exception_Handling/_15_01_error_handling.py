def fact(a):
    if a == 1 or a == 0:
        return 1
    else:
        return fact(a - 1) * a


try:
    a = int(input("Enter the number: "))
    print(fact(a))
except Exception as e:
    print(e, "is an error")
    print(type(e))
