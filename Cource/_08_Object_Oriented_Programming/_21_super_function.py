class C:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        print("Constructor of C")


class D(C):
    def __init__(self, p, q, r):
        self.r = r
        print("Constructor of D")


d = D(1, 2, 3)


# it is not mandatory to call the constructor of the base class but is not recommended
class A:

    def __init__(self, a, b):
        self.a = a
        self.b = b
        print("Constructor of A")


class B(A):
    def __init__(self, c):
        self.c = c
        print("Constructor of B")


b = B(10)
