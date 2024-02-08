list_1 = [1, 5, 3, 62, 6, 2, 27]

list_1.sort()

print(list_1)

tuple_1 = (5, 2, 9, 7)

# sorted method will return new dataset of type which it has recieved
sorted_tuple = sorted(tuple_1)
print(sorted_tuple)


list_2 = [(1, 4, 2),
          (2, 5, 7),
          (7, 2, 9),
          (9, 6, 1),
          (6, 1, 6)]


# will sort the list_2 on the basis of first index of the inner tuple
list_2.sort()

for i in list_2:
    print(i)
print()

# takes tuple and returns the second element


def second_index(temp_tuple): return temp_tuple[1]


# the second_index function will be given element of `list_2` as argument
list_2.sort(key=second_index)

for i in list_2:
    print(i)


list_3 = [[1, 2, 3],
          [2, 1, 6],
          [4, 3, 2],
          [6, -1, 4]
          ]

# the lambda function will return the second item from each list and `sort` function will sort on the basis of that
list_3.sort(key=lambda x: x[1])

for i in list_3:
    print(i)


tuple_2 = ((1, 4, 2),
           (2, 5, 7),
           (7, 2, 9),
           (9, 6, 1),
           (6, 1, 6))

sorted_tuple_2 = sorted(tuple_2, key=lambda x: x[1])

for i in sorted_tuple_2:
    print(i)
