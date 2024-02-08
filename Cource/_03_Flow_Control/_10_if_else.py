age = int(input("Enter your age --> "))
if age > 17:
    print("The individual can vote")
# elif age < 10 and age > 0:
elif 10 > age > 0:
    print("The individual is smol child")
elif age <= 0:
    print("What the hell man are you kidding me")
else:
    print("The individual cannot vote")
