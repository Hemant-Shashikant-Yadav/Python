# This is same concepts as in mathematics sets
# every elements is only considered only at once and the duplicates are automatically removed and all of the elements are automatically sorted after assigment of the tuple
a1 = {10, 1, 2, 3, 4, 19, 5, 6, 5, 5, 5, 3, 6, 6, 8, 6, 4, 4, 4}
print(a1)

# removes first element from the set
print(a1.pop())
print(a1)

# adds the element to end of the tuple in sorted order
a1.add(7)
print(a1)

# the empty set is created as follows
set2 = set()
print(type(set2))

# discard and remove methods are used to remove a specific value from the set while discard will not raise error if the element is not present in the set but the remove method will do
a1.remove(3)
print(a1)
a1.discard("str")
print(a1)
