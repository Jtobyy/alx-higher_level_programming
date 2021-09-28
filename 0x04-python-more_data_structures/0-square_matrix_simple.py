#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    new_matrix = []
    for i in matrix:
        sub_matrix = list(map(lambda x: x**2, i))
        new_matrix.append(sub_matrix)
    return new_matrix
