#!/usr/bin/python3
""" rotate a matrix """


def rotate_2d_matrix(matrix):
    """ rotate a matrix """

    n = len(matrix)
    # transpose matrix
    for row in range(n):
        for col in range(row + 1, n):
            matrix[row][col], matrix[col][row] = matrix[col][row], \
                    matrix[row][col]

    # reverse matrix
    for row in range(n):
        i = 0
        j = n - 1
        while i < j:
            matrix[row][i], matrix[row][j] = matrix[row][j], matrix[row][i]
            i += 1
            j -= 1
