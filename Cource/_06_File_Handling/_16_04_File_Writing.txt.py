# There are different modes of opening a file
# we can achieve this by giving the argument to `open`
# function for variable `mode`

with open("_16_04_01_File.txt", 'w') as file:
    file.write("This is the content that will be overwritten")

# we can write the arguments in any of this two ways,
# but this way just clarifies the arguments

with open(file="_16_04_01_File.txt", mode='a') as file:
    file.write("This is the content that will be appended")
