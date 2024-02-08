class A:

    color = None


class B:
    pass


def global_function(object_of_any_class, color="White"):
    
    # if the object do not have color attribute
    # this function will create a color attribute for the passed object
    object_of_any_class.color = color


a1 = A()
global_function(a1, "black")
print(a1.color)

b1 = B()
global_function(b1, "red")
print(b1.color)

b2 = B()
global_function(b2)
print(b2.color)
