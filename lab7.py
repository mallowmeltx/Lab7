"""
UTM: CSC108, Fall 2021

Practical Lab 7

Instructors: Michael Liut, Andrew Petersen, Andi Bergen,
             Tingting Zhu, Pooja Vashisth, and Sonya Allin

This code is provided solely for the personal and private use of
students taking the CSC108 course at the University of Toronto.
Copying for purposes other than this use is expressly prohibited.
All forms of distribution of this code, whether as given or with
any changes, are expressly prohibited.

All of the files in this directory and all subdirectories are:
Copyright (c) 2021 Michael Liut, Haocheng Hu

LAB RESTRICTIONS, PLEASE READ:
Do not add any imports, the ones that you need will be given to you.
You may not use any dictionaries or dictionary methods.
Do not use try-except statements, you should be able to anticipate
or prevent any errors from happening at all!
"""


def longest_chain(lst: list[int]) -> int:
    """
    Your longest_chain function from last week, make sure this works properly
    before proceeding with the rest of the lab!
    """
    iteration_count = 0
    counter = 0
    counter_compare = []

    while iteration_count < len(lst):
        if 1 == lst[iteration_count]:
            counter += 1
        # this only happens when the program iterate over 0
        else:
            # add the counter to a list to compare all counters later
            counter_compare.append(counter)
            # reset counter for the next chain
            counter = 0

        iteration_count += 1
    # add the last counter if the list ends in 1
    # since counter is only appended if it iterates into 0
    counter_compare.append(counter)

    return max(counter_compare)


def largest_at_position(matrix: list[list[int]], row: int, col: int) -> int:
    """
    Returns the area of the largest rectangle whose top left corner is at
    position <row>, <col> in <matrix>.

    You MUST make use of the helper <longest_chain> here as you loop through
    each row of the matrix. Do not modify (i.e., mutate) the input matrix.

    >>> case1 = [[1, 0, 1, 0, 0],
    ...          [1, 0, 1, 1, 1],
    ...          [1, 1, 1, 1, 1],
    ...          [1, 0, 0, 1, 0]]
    >>> largest_at_position(case1, 0, 0)
    4
    >>> largest_at_position(case1, 2, 0)
    5
    >>> largest_at_position(case1, 1, 2)
    6
    """
    pass


def largest_in_matrix(matrix: list[list[int]]) -> int:
    """
    Returns the area of the largest rectangle in <matrix>.

    The area of a rectangle is defined by number of 1's that it contains.

    Again, you MUST make use of the helper <largest_at_position> here. If you
    managed to code <largest_at_position> correctly, this function should be
    simple to implement.

    Similarly, do not modify (i.e., mutate) the input matrix.

    Precondition:
        <matrix> will only contain the integers 1 and 0.

    >>> case1 = [[1, 0, 1, 0, 0],
    ...          [1, 0, 1, 1, 1],
    ...          [1, 1, 1, 1, 1],
    ...          [1, 0, 0, 1, 0]]
    >>> largest_in_matrix(case1)
    6
    """
    pass


if __name__ == '__main__':
    import doctest

    doctest.testmod()
