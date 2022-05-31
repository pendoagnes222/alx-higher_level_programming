#!/usr/bin/python3
import random
number = random.randint(-10, 10)
for i in range(-10,10):
    if i > 0:
        print("is positive")
    elif i == 0:
        print("is zero")
    elif i<0:
        print("is negative")
