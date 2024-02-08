# Stings are immutable which means everytime we perform a operation on the string new string is returned by the inbuilt functions and the string remains unchanged
str = "HElLO"
print(str.upper())
print(str.lower())
print(str.capitalize())
str += "a"
print(str)
print(str.count("H"))
print(str.count("x"))
print(str.count("l"))

# print(str[a:b]) //from a to b-1
print(str[0:3])
print(str[1:2])

# multi-line strings

str1 = "hello" " this is a multiline string" " nice"

str2 = """Hello
This is also a multiline string
Nice isn't it
"""

print(str1)
print(str2)
str2 = "a"
print(str2)


str = "h"
print(str+"\n")


# fstrings are same as the strings with `` in the JavaScript
a = 19
b = 16
str = f"the value of a is {a} and value of b is {b}"
print(str)
