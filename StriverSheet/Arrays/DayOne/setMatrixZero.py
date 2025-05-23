# https://takeuforward.org/data-structure/set-matrix-zero/
"""
Problem Statement:
Given a matrix if an element in the matrix is 0 then you will have to set its entire column and row to 0 and then return the matrix.

Input: matrix = [[1,1,1],[1,0,1],[1,1,1]]
Output: [[1,0,1],[0,0,0],[1,0,1]]
"""

from typing import List


def set_zeroes(matrix: List) -> List:
    row_zero, col_zero = set(), set()
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] == 0:
                row_zero.add(i)
                col_zero.add(j)

    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if i in row_zero or j in col_zero:
                # set that entire row col to zero
                matrix[i][j] = 0
    return matrix


if __name__ == "__main__":
    print(
        set_zeroes(matrix=[[1, 1, 1], [1, 0, 1], [1, 1, 1]])
    )  # [[1,0,1],[0,0,0],[1,0,1]]

"""
Time Complexity : O(2*(N*M)
Space Complexity : O(1)
"""