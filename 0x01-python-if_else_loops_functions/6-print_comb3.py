#!/usr/bin/python3

for i in range(0, 10):
    for n in range(0, 10):
        if i == n:
            continue
        elif i, n = n, i:
            continue
        else:
            print(i, n)
