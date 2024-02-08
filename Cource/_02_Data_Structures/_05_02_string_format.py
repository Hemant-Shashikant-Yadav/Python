animal = "cow"
item = "moon"
beverage = "redbull"
print("The {} jumped over the {} after drinking {}".format(animal, item, beverage))
# positional argument
print("The {0} jumped over the {2} after drinking {1}".format(animal, beverage, item))
# keyword argument
print("The {company} creates the {car} and {car} is {type}".format(company="Toyota", car="Supra", type="JDM"))

print("Hello there {name:>10}. How are you".format(name="boi"))
print("Hello there {name:<10}. How are you".format(name="boi"))
# rounding of floating points
print("The number is {num:.3f}".format(num=12.42424))
# formatting with commas for higher values
print("The number is {num:,}".format(num=1452.42424))
# converting into different number system
print("The number is {num:b}".format(num=12))  # binary
print("The number is {num:o}".format(num=12))  # octal
print("The number is {num:x}".format(num=12))  # lowercase hexadecimal
print("The number is {num:X}".format(num=12))  # uppercase hexadecimal
print("The number is {num:e}".format(num=12))  # lowercase scientific format
print("The number is {num:E}".format(num=12))  # uppercase scientific format
