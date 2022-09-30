#!/usr/bin/python3
import sys
if __name__ == "main":
    import sys
a = sys.argv
if len(sys.argv) - 1 == 1:
    print("{:d} argument:".format(len(sys.argv) - 1))
    print("{:d}: {:s}".format(len(sys.argv) - 1, a[1]))

else:
    print("{:d} arguments:".format(len(sys.argv) - 1))

    for arg in range(1, len(sys.argv)):
        print("{:d}: {:s}".format(arg, a[arg]))
