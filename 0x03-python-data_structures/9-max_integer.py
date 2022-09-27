#!/usr/bin/python3
def max_integer(my_list=[]):
    if len(my_list) < 1:
        return None
    else:
        maxi = my_list[0]
        for i in range(1, len(my_list)):
            if my_list[i] > maxi:
                maxi = my_list[i]
        return maxi
