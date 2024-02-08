# **kwargs --> kwargs will be treated as a dictionary

'''
def student_info(**kwargs):
    print(
        f"The name of the student is {kwargs.get('first_name')} {kwargs.get('middle_name')} {kwargs.get('last_name')}")
    print(f"The roll number of the student is {kwargs.get('roll_no')} and the URN is {kwargs.get('urn')}")


student_info(first_name="Atharv", last_name="Sankpal", urn=21031040, middle_name="Santosh")
'''


def say_hello(**dict):
    print("Hello", end=" ")

    for value in dict.values():
        print(value, end=" ")


# any of the following method will do the same task
'''
    for key in dict:
        print(dict[key], end=" ")

    for key in dict.keys():
        print(dict[key], end=" ")

    for key, value in dict.items():
        # print(dict[key], end="")
        print(value, end="")
'''

say_hello(title="Mr", first_name="Atharv", middle_name="Santosh", last_name="Sankpal")
