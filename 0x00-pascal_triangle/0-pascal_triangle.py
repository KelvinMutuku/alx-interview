#!/usr/bin/python3

"""
Module 0-pascal_triangle
"""


def pascal_triangle(n):
    """
    returns a list of integers
    representing Pascal's triangle
    """
    if n <= 0:
        return []

    # [1] is the initial element
    triangle = [[1]]

    # iterate to up size n - 1
    for i in range(n - 1):
        # pick the previous list
        # add zeros to both ends
        temp = [0] + triangle[-1] + [0]
        # create a new row
        row = []
        # iterate up to size of previous row + 1
        # because new row will have one more element than previous
        for j in range(len(triangle[-1]) + 1):
            # add values to next new row
            row.append(temp[j] + temp[j + 1])
        # add the row to the triangle
        triangle.append(row)

    return triangle
