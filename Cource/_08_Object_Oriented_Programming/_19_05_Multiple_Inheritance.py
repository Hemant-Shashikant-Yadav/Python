class A:

    def function(self):
        print("A")


class B:

    def function(self):
        print("B")


class C(A, B):
    pass


c = C()

c.function()
