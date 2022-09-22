#!/usr/bin/python3
def remove_char_at(str, n):
    str_copy = []
    for ch in str:
        if n > len(str) or n < 0:
            return str
        elif ch != str[n]:
            str_copy.append(ch)
    return ''.join(str_copy)
