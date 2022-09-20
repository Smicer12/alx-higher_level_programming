#!/usr/bin/python3
for i in reversed(range(66, 91, 2)):
    print("{}{}".format(chr(i).lower(), chr(i-1).upper()), end="")
