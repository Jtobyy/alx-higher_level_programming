#!/usr/bin/python3


def print_matrix_integer(matrix=[[]]):
    for mat in matrix:
        i = 0
        for el in mat:
            print("{:d}".format(el), end=" ")
        print()
