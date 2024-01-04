#!/usr/bin/python3
""" module pascal_triangle(n): """


def pascal_triangle(n):
    """ create a pascal triangl of size n """
    triangle = []
    if n <= 0:
        return triangle
    for i in range(n):
        triangle.append([1] * (i + 1))

    for row in range(2, n):
        for col in range(1, row):
            triangle[row][col] = triangle[row - 1][col - 1] + triangle[row - 1][col]

    return triangle
