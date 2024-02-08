# zip function converts multiple iterables elements into a tuple of single iterable entity

list_1 = [1, 2, 3, 4, 5]
tuple_1 = ("one", "two", "three", "four", "five")
set_1 = {"ek", "don", "teen", "char", "pach"}

new_iterable = zip(list_1, tuple_1, set_1)

print(new_iterable)

new_iterable = list(new_iterable)

print(new_iterable)

new_dict = dict(zip(list_1,tuple_1))

print(new_dict)
