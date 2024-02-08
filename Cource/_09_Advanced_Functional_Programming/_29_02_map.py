# map function will execute the function on each element by giving that as argument and assigning the returned value for that index


def function(x):
    return x * 2


list_1 = [1, 2, 3, 4, 5, 6]
list_1 = list(map(function, list_1))
print(list_1)

list_2 = [1, 3, 4]
list_2 = list(map(lambda x: x + 1, list_2))
print(list_2)

list_3 = [("one", 1),
          ("two", 2),
          ("three", 3),
          ("four", 4),
          ("five", 5)
          ]

list_3 = list(map(lambda temp_tuple: (temp_tuple[0].join(("student_", "")), temp_tuple[1]), list_3))

for i in list_3:
    print(i)
