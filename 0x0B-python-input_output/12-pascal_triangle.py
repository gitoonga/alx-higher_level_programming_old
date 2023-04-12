#!/usr/bin/python3
"""
Returns a list of lists of integers representing the Pascal’s triangle of n
"""

def pascal_triangle(n):

    """
    Generates the first 'n' rows of Pascal's Triangle and returns them as a list of lists.

    Parameters:
    n (int): The number of rows of Pascal's Triangle to generate.

    Returns:
    List[List[int]]: A list of 'n' lists, each containing the corresponding row of Pascal's Triangle.
    """
    if not isinstance(n, int) or n <= 0:
        return []
        
    triangle = [[1]]

    for i in range(1, n):
        previous_row = triangle[-1]
        new_row = [1] + [previous_row[j] + previous_row[j+1] for j in range(i-1)] + [1]
        triangle.append(new_row)

    return triangle
