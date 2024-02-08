# Abstract class can't be initialized
# we need at least an abstract method in the class to avoid initialization

from abc import ABC, abstractmethod


class A(ABC):

    @abstractmethod  # it is mandatory to add this decorator
    def function(self):
        pass


class B(A):
    def function(self):
        print("B")


class C(A):

    def function(self):
        print("C")


b = B()
b.function()

c = C()
c.function()
