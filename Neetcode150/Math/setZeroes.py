# https://leetcode.com/problems/set-matrix-zeroes/
"""
O(1) memory.
Put the extra row and column array (_) and put it in the matrix.
Just one extra block
_ 1,0,1
  1,0,1
  0,1,1

0 spotted at [0][1]: mark 0 as 0 (column needs to be zeroed out) and _ as 0 (row needs to be zeroed out)

0 1,0,1
  1,0,1   (set 0 to 0 for column (already zeroed from before) and set [1][0] to also 0 indicating row is zeroed out
  0,1,1

In the end :
  0,0,0
  0,0,0
  0,0,0

Trick to O(1) : use extra space : col0 :: initially false and if found (matrix[i][0] == 0) = set to true
"""


# Steps:
# determine which rows/cols need to be zero
# zero out most of them
# zero out 1st col if we need to
# zero out 1st row if we need to


def setZeroes(matrix):
    rows, cols = len(matrix), len(matrix[0])
    col0 = False
    for i in range(rows):
        # checking if 0 present of not in the 0th column
        if matrix[i][0] == 0:
            col0 = True
        # setting all others to 0 (starting from 1)
        for j in range(1, cols):
            if matrix[i][j] == 0:
                # set that row and col to 0
                matrix[i][0] = 0
                matrix[0][j] = 0

    # traversing in reverse order and checking if row/col has 0 or not
    # if yes set matrix values accoringly
    for i in range(rows - 1, -1, -1):
        for j in range(cols - 1, 0, -1):
            if matrix[i][0] == 0 or matrix[0][j] == 0:
                matrix[i][j] = 0
        # for col0 val -> if yes then fill that row with 0s
        if col0:
            matrix[i][0] = 0


def main():
    matrix = [[1, 1, 1], [1, 0, 1], [1, 1, 1]]
    setZeroes(matrix)
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            print(matrix[i][j], end=" ")
        print()


main()
