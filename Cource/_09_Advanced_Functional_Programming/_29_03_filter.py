# filter will return a new collection by removing the elements having `True` value for the function that has given as
# argument to `filter`

list_1 = [1, 4, 6, 8, 13, 24, 26, 54, 44, 767, 7767, 678]
filtered_list_1 = list(filter(lambda x: x % 3, list_1))  # the elements divisible by 3 will not be present
print(filtered_list_1)
print(list_1)
