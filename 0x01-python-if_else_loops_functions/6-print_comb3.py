#!/usr/bin/python3
for value in range(0, 9):
    for num in range(value + 1, 10):
        if value == 8:
            print("{0}{1}".format(value, num))
            break
        print("{0}{1}".format(value, num), end=", ")
