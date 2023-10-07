# Empty list
l = []

# Create a simple list
List1 = list((1,2,"apple", "banana", "cherry"))
print(List1)

#Get the length of list using len funtion
print(len(List1))

# Access the elements inside the list with index position
list2 = ["abc", 34, True, 40, "male"]
print(list2)
print(list2[1])
print(list2[-1]) #Access from end

#You can check wheter certain element is present in list or not in list using if
if 34 in list2:
    print("Yes")
else:
    print("No")

#You can split the scentence into the list items
string = input("Enter elements (Space-Separated): ")
lst = string.split()
print('The list is:', lst)

#Appending new elements into the end of list
List = []
print("Initial blank List: ")
print(List)
List.append(1)
List.append(2)
List.append(4)
print(List)

#You can append one list into another list just like extend
List2 = ['For', 'Geeks']
List.append(List2)
print("\nList after Addition of a List: ")
print(List)
print(len(List))

List.extend(List2)
print(List)
#In append the other list is appended as a single list element and in extend the elements in other list added individually

#Insert element at specific location
List.insert(3, 12)

#Sort the list (Note: all elements in list should be of same type)
mylist = [1, 2, 3, 4, 5]
mylist.sort()
print(mylist)
#You can sort the list in reverse order also
mylist.reverse()
print(mylist)

my_list = [1, 2, 3, 4, 5]
reversed_list = list(reversed(my_list))
print(reversed_list)

# Pop the last element in list
List = [1, 2, 3, 4, 5]
List.pop()
print("\nList after popping an element: ")
print(List)

#Pop specific element in list
# You can also use remove also for that
List.pop(2)
print("\nList after popping a specific element: ")
print(List)
List.remove(4)
print(List)

List = [1, 2, 3, 4, 5,6,7,8,9,10]
Sliced_List = List[3:8]
print("\nSlicing elements in a range 3-8: ")
print(Sliced_List)


Sliced_List = List[:-6]
print("\nElements sliced till 6th element from last: ")
print(Sliced_List)
