# new_dict = {key: new_value for (key,value) in original_dict.items()}
dict_1 = {1: "one", 2: "two", 3: "three", 4: "four"}

new_dict = {key: value.join(("student_", "")) for (key, value) in dict_1.items()}
print(new_dict)

# new_dict = {key: new_value for (key,value) in original_dict.items() if (condition)}
new_dict_2 = {key: value for key, value in dict_1.items() if key > 2}  # only the true elements will be appended
print(new_dict_2)


# new_dict = {key: function(new_value) for (key,value) in original_dict.items()}
def alter_value(value):
    # perform operation on the
    if value == "three":
        return "Three"
    if value == "four":
        return "FOUR"
    return value


new_dict_3 = {key: alter_value(value) for (key, value) in dict_1.items()}
print(new_dict_3)

# new_dict = {key: new_value_1 if(condition) else new_value_2  for (key,value) in original_dict.items()}

new_dict_4 = {key: value if key > 2 else "less than two" for (key, value) in dict_1.items()}
print(new_dict_4)
