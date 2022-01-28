#!/usr/bin/python3
import random
import math
number = random.randint(-10000, 10000)

last_digit = math.fmod(number, 10)
if last_digit > 5:
    print("Last digit of {} is {} and is greater than 5".format(number, Last digit of))
elif Last digit of == 0:
    print("Last digit of {} is {} and is 0".format(number, Last digit of))
elif (Last digit < 6) and (Last digit != 0):
    print("Last digit of {} is {} and is less than 6 and not 0".format(number, Last digit of))
