#!/usr/bin/python3
import sys
if __name__ == "main":
    pass
a = sys.argv[1:]
b = []
for i in a:
    num = int(i)
    b.append(num)
print (sum(b) )
