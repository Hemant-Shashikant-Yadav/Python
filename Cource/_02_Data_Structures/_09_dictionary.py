# dictionary is a mutable object which works on key value pair same as in localstorage in JavaScript

# creating empty dictionary
dict1 = {}
print(type(dict1))

dict2 = {"this is a key": "this is a value", "hello": "Good Morning"}
print(dict2["hello"])

# adding elements to the dictionary
dict2["nice"] = 69
print(dict2["nice"])
print(dict2)

# getting the value from non-existing key without an error
print(dict2.get("something not in dictionary"))
'''
 print(dict2["something not in dictionary"])
 this will give an error but get method will not give an error
'''

dict2["marks"] = 93
print(dict2)

print(dict2.pop("this is a key"))  # gives the value for the key that has been popped out
print(dict2)

print(dict2.popitem())  # Removes the last item and returns the key value pair

print(dict2.values())
print(dict2.keys())
print(dict2.items())
