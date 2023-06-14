#!/usr/bin/python3
#6-print_matrix_integer.py

def print_matrix_integer(matrix=[[]]):
    """ prints a matrix of integers."""

    for i in matrix:
       for j in i:
          print("{:d}".format(j), end=" ")

       print("")
