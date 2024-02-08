class A:
    alive = True

    def eat(self):
        print("A")


class B(A):
    def eat(self):
        print("B")


class C(B):
    pass


c = C()

c.eat()
