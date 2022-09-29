#!/usr/bin/python3
import sys
if __name__ == "main":
    pass
a = sys.argv
if len(sys.argv) - 1 == 1:
    print("{} argument:".format(len(sys.argv) - 1))
    print("{}: {}".format(len(sys.argv) - 1, a[1]))
else:
    print("{} arguments:".format(len(sys.argv) - 1))

    for arg in range(1, len(sys.argv)):
        print("{}: {}".format(arg, a[arg]))
