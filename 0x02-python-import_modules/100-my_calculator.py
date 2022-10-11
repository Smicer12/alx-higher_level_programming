#!/usr/bin/python3
if __name__ == "__main__":
    from calculator_1 import add, sub, mul, div
    import sys
element = sys.argv[1:]
a = int(element[1])
b = int(element[3])
operator = element[2]

if len(lis) < 3:
    print("Usage: ./100-my_calculator.py <a> <operator> <b>")
    exit(1)

if operator != '+' or '-' or '*' or '/':
    print("Unknown operator. Available operators: +, -, * and /")
    exit(1)
if operator == '+':
    print(add(a, b))
    exit(0)
if operator == '-':
    print(sub(a,b))
    exit(0)
if operator == '*':
    print(mul(a, b))
    exit(0)
if operator == '/':
    print(div(a, b))
    exit(0)