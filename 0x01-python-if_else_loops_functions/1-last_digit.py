#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number > 0:
    mod = number % 10
    if number % 10 > 5:
        print(f"Last digit of {number} is {mod} and is greater than 5")
    elif number % 10 == 0:
        print(f"Last digit of {number} is {mod} and is 0")
    elif number % 10 < 6 and number % 10 != 0:
        print(f"Last digit of {number} is {mod} and is less than 6 and not 0")
elif number < 0:
    mod = -number % 10
    if mod == 0:
        print(f"Last digit of {number} is {mod} and is 0")
    else:
        print(f"Last digit of {number} is {-mod} and is less than 6 and not 0")
else:
    print(f"Last digit of {number} is {number} and is 0")
