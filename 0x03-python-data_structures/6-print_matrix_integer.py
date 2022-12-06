#!/bin/usr/python3
def print_matrix_integer(matrix=[[]]):
    for items in matrix:
        for j in items:
            print("{:d}".format(j), end=" ")
        print()
