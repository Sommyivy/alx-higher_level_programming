#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for items in matrix:
        for j in items:
            if j != 0:
                print(" ", end='')
            print("{:d}".format(j), end=" ")
     print()
