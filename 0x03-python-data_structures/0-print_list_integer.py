#!/usr/bin/python3
def print_list_integer(my_list=[]):
    result = [val for val in my_list if isinstance(val, (int))]
    for i in result:
        print("{:d}".format(i))


print_list_integer()
