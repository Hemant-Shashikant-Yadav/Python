from numpy import floor


str = input("Enter a string = ")

j=len(str)-1
for i in range(int(len(str)/2)):
    if str[i] != str[j]:
        print("String is not palindrome")
        exit(1)
    j-=1

print("String is palindrome")