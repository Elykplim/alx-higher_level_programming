#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    # Create a new matrix to store the squared values
    squared_matrix = []

    # Iterate over each row in the input matrix
    for row in matrix:
        # Create a new row for the squared_matrix
        squared_row = []

        # Iterate over each element in the row and square it
        for value in row:
            squared_row.append(value ** 2)

        # Add the squared row to the squared_matrix
        squared_matrix.append(squared_row)

    return squared_matrix

