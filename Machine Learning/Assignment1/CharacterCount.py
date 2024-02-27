str1 = input("Enter a string = ")
q = ""

crr = str1[0]
count = 1

for i in range(1, len(str1)):
    if str1[i] == crr:
        count += 1
    else:
        q += crr + str(count)
        crr = str1[i]
        count = 1

q += crr + str(count)

print("String = ", q)
