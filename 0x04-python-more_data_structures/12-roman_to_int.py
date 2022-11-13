#!/usr/bin/python3
def roman_to_int(roman_string):
    if roman_string == None:
        return 0
    num_str = []
    for i in roman_string:
        if i == "I":
            num_str.append(1)
        elif i == "V":
            num_str.append(5)
        elif i  == "X":
            num_str.append(10)
        elif i == "L":
            num_str.append(50)
        elif i == "C":
            num_str.append(100)
        elif i == "D":
            num_str.append(500)
        elif i == "M":
            num_str.append(1000)
    
    return (sum(num_str))
