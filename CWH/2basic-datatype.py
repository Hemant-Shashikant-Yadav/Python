# Variables
a = "Hello World"
b = 5
c = 15.17

print(a)
print(b)
print(c)

print("\n")

# Datatypes
print(type(a))
print(type(b))
print(type(c))

print("\n")

d = "Hello"
e = "World"

h="55"
i="10"

f=15
g=20

print(d+e)
print(h+i)#Addition is not performed because it is a string is concatnated
print(int(h)+int(i))#typecast
print(g+f)

#Global variable
# x = "awesome"
#
# def myfunc():
#   x = "fantastic"
#   print("Python is " + x)
#
# myfunc()
#
# print("Python is " + x)
#


x = "awesome"

def myfunc():
    global x
    x = "fantastic"

myfunc()

print("Python is " + x)

# Text Type:	    str
# Numeric Types:	int, float, complex
# Sequence Types:	list, tuple, range
# Mapping Type:	    dict
# Set Types:	    set, frozenset
# Boolean Type: 	bool
# Binary Types:	    bytes, bytearray, memoryview
# None Type:	    NoneType

x = "Hello World"	                                #str
print(x)
print(type(x))
x = 20	                                            #int
print(x)
print(type(x))
x = 20.5	                                        #float
print(x)
print(type(x))
x = 1j	                                            #complex
print(x)
print(type(x))
x = ["apple", "banana", "cherry"]	                #list
print(x)
print(type(x))
x = ("apple", "banana", "cherry")	                #tuple
print(x)
print(type(x))
x = range(6)	                                    #range
print(x)
print(type(x))
x = {"name" : "John", "age" : 36}	                #dict
print(x)
print(type(x))
x = {"apple", "banana", "cherry"}	                #set
print(x)
print(type(x))
x = frozenset({"apple", "banana", "cherry"})	    #frozenset
print(x)
print(type(x))
x = True	                                        #bool
print(x)
print(type(x))
x = b"Hello"	                                    #bytes
print(x)
print(type(x))
x = bytearray(5)	                                #bytearray
print(x)
print(type(x))
x = memoryview(bytes(5))	                        #memoryview
print(x)
print(type(x))
x = None                                            #NoneType
print(x)
print(type(x))




