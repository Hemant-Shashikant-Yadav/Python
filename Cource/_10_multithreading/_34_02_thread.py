import threading

def print_even(numbers):
    for number in numbers:
        if number % 2 == 0:
            print(f"Even number: {number}")

def print_odd(numbers):
    for number in numbers:
        if number % 2 != 0:
            print(f"Odd number: {number}")

numbers_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

thread1 = threading.Thread(target=print_even, args=(numbers_list,))
thread2 = threading.Thread(target=print_odd, args=(numbers_list,))

thread1.start()
thread2.start()

thread1.join()
thread2.join()
