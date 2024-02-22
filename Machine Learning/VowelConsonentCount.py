str = input("Enter a string = ")

str.lower()

vowel = consonent = 0
for i in str:
    if i=='a'or i=='e' or i=='i' or i=='o' or i=='u':
        vowel += 1
    else:
        consonent += 1

print(f"Vowel count =  {vowel} Consonent =  {consonent}")