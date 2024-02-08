try:
    numerator = int(input("Enter the numerator --> "))
    denominator = int(input("Enter the denominator --> "))
    result = numerator / denominator
    print("The Division of these two numbers is {}".format(result))
except ZeroDivisionError as e:
    print(f"Error {e}")
except ValueError as e:
    print(f"Error {e}")
except Exception as e:
    print(f"Error {e}")
finally:
    # finally clause is usually used in file handling
    print("The will be executed no matter what")
