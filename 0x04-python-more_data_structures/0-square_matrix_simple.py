#!/usr/python3
def square_matrix_simple(matrix=[]):
    return [list(map((lambda x: x * x), els)) for elm in matrix]
