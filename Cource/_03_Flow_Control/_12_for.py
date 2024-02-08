# num = int(input("Enter the number whose table you want to print"))
num = 12
for i in range(10):
    print((i + 1) * num)
print("")

# starts from 2 ends at 3
for j in range(2, 4):
    print(j)
print("")

# iterates over each element of the list
list1 = [1, 2, 3, 4, 5, 6]
for item in list1:
    print(item)

# iterates over each character of the string
str = "This is a string"
for char in str:
    print(char)
print("")

# for-else --> else statement is executed after the for block of for is completely executed.
for i in range(5):
    print(i)
else:
    print("The for loop has finished")
print("")

# Else block will not be executed if the break is used to stop the flow of the `for loop`
for i in range(15):
    if i == 5:
        break
    print(i)
else:
    print("This else block will not be executed since the break is used")
print("")

# for loop on sets will not give out the elements in the order that it is initialized
set1 = {1, 22, 23, 14, 5, 6}
for item in set1:
    print(item)
print("")

# for loop on dictionary
dict1 = {"key1": 1, "key2": 2, "key3": 3, "key4": 4, "key5": 5, "key6": 6}
for item in dict1:
    print(item, dict1[item])  # item is the key element and dict1[item] is value element
print("")
