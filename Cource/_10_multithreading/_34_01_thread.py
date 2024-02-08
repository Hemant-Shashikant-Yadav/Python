import threading

def print_square(numbers):
    for number in numbers:
        print(f"Square of {number}: {number**2}")

def print_cube(numbers):
    for number in numbers:
        print(f"Cube of {number}: {number**3}")

numbers_list = [1, 2, 3, 4, 5]

thread1 = threading.Thread(target=print_square, args=(numbers_list,))
thread2 = threading.Thread(target=print_cube, args=(numbers_list,))

thread1.start()
thread2.start()

thread1.join()
thread2.join()
