#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    # Create a new empty matrix with the same size as the input matrix
    squared_matrix = []
    for i in range(len(matrix)):
        squared_matrix.append([])
        for j in range(len(matrix[i])):
            squared_matrix[i].append(0)

    # Calculates the square value of each element in the matrix and
    # stores it in the element of the new squared matrix
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            squared_matrix[i][j] = matrix[i][j] ** 2

    # Return the new squared matrix
    return squared_matrix

