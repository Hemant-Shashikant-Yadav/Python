# The list is changed everytime we perform the operations on it, it is same as array
# The lists are mutable and inbuilt methods changes the list on every operations
list1 = [1, 2, 3, 4, 5, 6, 685]
print(list1)

# deletes the last element present at the list and returns the popped elements
print(list1.pop())
print(list1)

# adds the argument to the end of the list and returns `None`
list1.append(2)
print(list1)

# removes the first instance of the given argument from the list and returns `None`
list1.remove(2)
print(list1)

# sorts the list and returns `None`
list1.sort()
print(list1)

# adding a list to existing list and returns `None`
list2 = [41, 42, 43, 44, 45, 46, 47]
list1.extend(list2)
print(list1)


# deletes all of the elements from the list and returns `None`
"""
list1.clear()
print(list1)
"""

# list[a:b] returns the list with elements from index position a to b-1
print(list1[0:4])
print(list1)

list1[0] = 1234567
print(list1)

# Negative indexing will refer to the elements from the end
print(list2[-2], list2[-1])



