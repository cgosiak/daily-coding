"""
Given a N by M matrix of numbers, print out the matrix in a clockwise spiral.

For example, given the following matrix:

[[1,  2,  3,  4,  5],
 [6,  7,  8,  9,  10],
 [11, 12, 13, 14, 15],
 [16, 17, 18, 19, 20]]
You should print out the following:

1
2
3
4
5
10
15
20
19
18
17
16
11
6
7
8
9
14
13
12
"""

def spiral_matrix(matrix):
    order = []

    row_start = 0
    row_stop = len(matrix)

    column_start = 0
    column_stop = len(matrix[0])

    while row_start < row_stop and column_start < column_stop:
        for i in range(column_start, column_stop):
            order.append(matrix[row_start][i])

        for i in range(row_start + 1, row_stop):
            order.append(matrix[i][column_stop - 1])

        for i in range(column_stop - 2, column_start - 1, -1):
            order.append(matrix[row_stop - 1][i])

        for i in range(row_stop - 2, row_start, -1):
            order.append(matrix[i][column_start])

        row_start += 1
        column_start += 1

        row_stop -= 1
        column_stop -= 1

    return order


# print the following
# - (0, 0)
# - (0, 1)
# - (1, 1)
# - (1, 0)
print(spiral_matrix([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]))
