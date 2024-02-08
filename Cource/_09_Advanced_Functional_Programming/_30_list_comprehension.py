# list = [item_value for i in iterable]

list_1 = [1, 2, 3, 4, 5]

list_1_square = [i * i for i in list_1]
print(list_1_square)

# list = [item_value for i in iterable if (condition)]
list_2 = [1, 3, 5, 6, 8, 9]

list_2_even_square = [i * i for i in list_2 if i % 2]
print(list_2_even_square)

# list = [item_value if (condition) else diff_item_value  for i in iterable ]
list_3 = [1, 2, 3, 4, 5]

list_3_even_square = [i * i if i % 2 else 0 for i in list_3]

print(list_3_even_square)
