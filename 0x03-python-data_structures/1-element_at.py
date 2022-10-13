#!/usr/bin/python3
from main_1 import my_list, idx
from main_2 import my_list, idx
def element_at(my_list, idx):
    if idx < 0:
        print("Element at index {:d} is None".format(idx))
    if idx > len(my_list) or idx == len(my_list):
        print("Element at index {:d} is None".format(idx ))
    else:
        print("Element at index {:d} is {:d}".format(idx, my_list[idx]))


element_at(my_list, idx)
