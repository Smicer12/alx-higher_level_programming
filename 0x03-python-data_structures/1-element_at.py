#!/usr/bin/python3
def element_at(my_list, idx):
    if idx < 0:
        print("Element at index {:d} is None".format(idx))
    if idx > len(my_list) or idx == len(my_list):
        print("Element at index {:d} is None".format(idx ))
    else:
        print("Element at index {:d} is {:d}".format(idx, my_list[idx]))


element_at()
