#!/usr/bin/python3
#6-print_matrix_integer.py

def print_matrix_integer(matrix=[[]]):
    """ prints a matrix of integers."""

    for i in len(matrix):
       for j in len(matrix[i]):
          print("{:d}".format(matrix[i][j]), end="")
          if j != (len(matrix[i]) - 1):
             print(" ", end="")
              
       print("")
