def string_to_float(num_as_string):
    return float(num_as_string)


def negative_to_positive(num):
    return abs(num)


def round_num(num):
    return round(num)


num = round_num(negative_to_positive(string_to_float(input("Enter the number --> "))))

print(num)
