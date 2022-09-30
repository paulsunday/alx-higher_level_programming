#!/usr/bin/python3
def roman_to_int(roman_string):
    if roman_string is None:
        return 0
    num_list = []
    for i in roman_string:
        if i == 'I':
            num_list.append(1)
        elif i == 'V':
            num_list.append(5)
        elif i == 'X':
            num_list.append(10)
        elif i == 'L':
            num_list.append(50)
        elif i == 'C':
            num_list.append(100)
        elif i == 'D':
            num_list.append(500)
        elif i == 'M':
            num_list.append(1000)
    return (sum(num_list))
