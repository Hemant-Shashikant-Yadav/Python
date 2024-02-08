from functools import reduce

list_1 = [1, 4, 5, 7, 5, 7, 56, 26, 26, 2, 6, 5, 256]
# first remove the even elements and later add them into single entity
odd_sum_list_1 = reduce(lambda x, y: x + y, list_1)
print(odd_sum_list_1)
