#!/usr/bin/python3
import sys
if __name__ == "main":
    pass
argv = sys.argv[1:]
count = len(argv)
index = 1
result = 0

while index <= count:
    result += int(sys.argv[index])
    index += 1

print("{:d}".format(result))
