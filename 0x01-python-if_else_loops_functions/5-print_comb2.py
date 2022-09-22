#! /usr/bin/env python
for num in range(0, 100):
    if num != 99:
        print("{:02}".format(num), end=", ")

print("{}".format(num))
