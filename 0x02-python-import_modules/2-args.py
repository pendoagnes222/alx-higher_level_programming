#!/usr/bin/python3
from sys import argv

n = len(argv)
index = 1
if n == 1:
    print(f"{n-1} argument.")
elif n == 2:
    print(f"{n-1} argument:")
    print(f"{index}: {argv[index]}")
elif n > 2:
    print(f"{n-1} arguments:")
    for j in range(1, n):
        print(f"{index}: {argv[index]}")
        index += 1
