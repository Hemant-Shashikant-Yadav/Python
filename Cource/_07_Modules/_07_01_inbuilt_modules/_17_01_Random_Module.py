import random

x = random.randint(1, 5)
print(x)
y = random.random()
print(y)

my_list = ['rock', 'paper', 'scissors']

z = random.choice(my_list)
print(z)

my_list_2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
random.shuffle(my_list_2)  # only works on mutable datasets like list and not on tuples
print(my_list_2)
