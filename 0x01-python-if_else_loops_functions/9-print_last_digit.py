#!/usr/bin/python3


def print_last_digit(number):
    if number < 0:
        l = number % 10
        print(-abs(l))
    else:
        s = number % 10
        print(abs(s))

