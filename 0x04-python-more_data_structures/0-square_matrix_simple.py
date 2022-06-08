#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    squares = [[i**2 for i in sublist] for sublist in matrix]
    return squares
