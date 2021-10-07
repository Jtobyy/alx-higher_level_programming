#!/usr/bin/python3
'''divides all elements of a matrix'''


def matrix_divided(matrix, div):
    '''
    divides all elements of matrix by div
    '''
    if type(matrix) != list:
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    new_matrix = []
    mat_len = len(matrix)
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    elif div == 0:
        raise ZeroDivisionError("division by zero")
    elif type(matrix[0]) != list:
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    
    row_len = len(matrix[0])
    for ls in matrix:
        if len(ls) != row_len:
            raise TypeError("Each row of the matrix must have the same size")
        for val in ls:
            if not isinstance(val, (int, float)):
                raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
        sub_matrix = [round(i / div, 2) for i in ls]
        new_matrix.append(sub_matrix)

    return new_matrix
