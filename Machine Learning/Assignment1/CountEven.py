import sys


num=[]

while True:
    a=input("Enter number in list = ")
    a.lower()
    if a == 'exit':
        break
    elif int(a) >=0 and int(a) <= sys.maxsize:
        num.append(int(a))
    else:
        print("Invalid input")

evencount = 0
for i in num:
    if i %2 == 0:
        evencount+=1

print(f"Even number count = {evencount}")