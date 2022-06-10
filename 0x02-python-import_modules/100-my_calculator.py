#!/usr/bin/python3
import calculator_1 as cal
import sys

n = len(sys.argv)
if n != 4:
    print(f"Usage: ./100-my_calculator.py <a> <operator> <b>")
    sys.exit(1)
if n == 4:
    x = int(sys.argv[1])
    y = int(sys.argv[3])
    operator = sys.argv[2]
    if operator not in ['+', '-', '*', '/']:
        print(f"Unknown operator. Available operators: +, -, * and /")
        sys.exit(1)
    if operator == '+':
        print(f"{x} {operator} {y} = {cal.add(x, y)}")
        sys.exit(0)
    if operator == '-':
        print(f"{x} {operator} {y} = {cal.sub(x, y)}")
        sys.exit(0)
    if operator == '*':
        print(f"{x} {operator} {y} = {cal.sub(x, y)}")
        sys.exit(0)
    if operator == '/':
        print(f"{x} {operator} {y} = {cal.div(x, y)}")
        sys.exit(0)
