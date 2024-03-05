#!/usr/bin/python3
""" island parameter """


def island_perimeter(grid):
    """ island parameter """
    para_len = 0
    num_cols = len(grid[0])
    num_rows = len(grid)

    def check_adjacent(row, col):
        nonlocal para_len
        if row < 0 or row >= num_rows \
           or col < 0 or col >= num_cols \
           or grid[row][col] == 0:
            para_len += 1

    for row in range(num_rows):
        for col in range(num_cols):
            if grid[row][col] == 1:
                directions = [(row, col - 1),
                              (row, col + 1),
                              (row - 1, col),
                              (row + 1, col)]
                for direction in directions:
                    check_adjacent(direction[0], direction[1])

    return para_len
