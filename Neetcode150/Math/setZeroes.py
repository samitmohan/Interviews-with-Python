# https://leetcode.com/problems/set-matrix-zeroes/
# great video for intuition: https://www.youtube.com/watch?v=T41rL0L3Pnw

# more obvious soln, keep track of which rows, col you want to zero and just do that at the end.


def setZeroes_opt(matrix):
    row_set = set()
    col_set = set()
    rows, cols = len(matrix), len(matrix[0])
    for i in range(rows):
        for j in range(cols):
            if matrix[i][j] == 0:
                row_set.add(i)
                col_set.add(j)
    for r in range(rows):
        for c in range(cols):
            if r in row_set or c in col_set:
                matrix[r][c] = 0

    return matrix

# Time Complexity: (O(m * n)
# Space Complexity: O(m + n)

"""
Neetcode soln : O(1) space
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


# space: O(1), time: O(m*n)
"""
The key idea here is to use the first row and first column as "markers." If a cell at matrix[i][j] is 0, we mark the i-th row by setting matrix[i][0] to 0 and the j-th column by setting matrix[0][j] to 0.
However, we have a special case: matrix[0][0] is used to mark both the first row and the first column. This is where the col0 flag comes in. We'll use matrix[0][0] to indicate if the first row should be zeroed, and the separate col0 flag to indicate if the first column should be zeroed.
"""

def setZeroes_intuitive_opt(matrix):
    """
    Sets all elements of a matrix row or column to 0 if any element
    in that row or column is 0, using O(1) extra space.

    The first row and first column are used as markers to indicate
    whether a row or column should be zeroed. A separate flag is used
    to handle the first column's special case.

    Args:
        matrix: A list of lists representing the matrix.

    Returns:
        The modified matrix with rows and columns zeroed out as required.
    """
    rows = len(matrix)
    cols = len(matrix[0])

    # We need a separate flag to track if the first column should be zeroed.
    # We can't use matrix[0][0] for this because matrix[0][0] will be used
    # to indicate if the first *row* should be zeroed.
    is_col0_zero = False

    # --- First Pass: Mark rows and columns that need to be zeroed ---
    # We iterate through the matrix. If we find a 0 at matrix[i][j]:
    # 1. We mark the i-th row by setting matrix[i][0] to 0.
    # 2. We mark the j-th column by setting matrix[0][j] to 0.
    # We handle the first column separately using the 'is_col0_zero' flag.

    for i in range(rows):
        # Check if any element in the first column is 0.
        # If yes, the entire first column needs to be zeroed later.
        if matrix[i][0] == 0:
            is_col0_zero = True

        # Iterate through the rest of the columns (starting from the second column).
        for j in range(1, cols):
            # If we find a 0 in the current cell, mark the corresponding
            # first row cell and first column cell.
            if matrix[i][j] == 0:
                matrix[i][0] = 0  # Mark the i-th row
                matrix[0][j] = 0  # Mark the j-th column

    # --- Second Pass: Zero out rows and columns based on the markers ---
    # Now that we have the markers in the first row and first column,
    # we iterate through the matrix again (this time in reverse order
    # to avoid clobbering the markers prematurely).

    # We iterate from bottom-right to top-left. This is important!
    # If we iterate from top-left, setting a cell in the first row or
    # first column to 0 might incorrectly cause entire rows/columns
    # to be zeroed out in subsequent steps.
    for i in range(rows - 1, -1, -1):
        # Iterate through columns from right to left.
        # We start from the second column (cols - 1 down to 1) because
        # we handle the first column (index 0) separately at the end of the row loop.
        for j in range(cols - 1, 0, -1):
            # Check if the first cell in the current row (matrix[i][0])
            # or the first cell in the current column (matrix[0][j]) is 0.
            # If either is 0, it means this cell's row or column needs to be zeroed.
            if matrix[i][0] == 0 or matrix[0][j] == 0:
                matrix[i][j] = 0

        # After processing columns 1 to cols-1 in the current row,
        # we handle the first column (index 0) for this row.
        # We only set matrix[i][0] to 0 if the 'is_col0_zero' flag is True.
        # This is because matrix[i][0] was potentially used as a marker
        # for the i-th row to be zeroed out, but it *itself* only gets
        # zeroed if the original first column had a 0.
        if is_col0_zero:
            matrix[i][0] = 0

    # No explicit return needed, as we modified the matrix in-place.
    # However, the function signature implies a return, so we can return it
    # for clarity, although the LeetCode problem often expects in-place modification.
    # return matrix # If you were to return the modified matrix explicitly

# Example usage:
# matrix = [[1, 1, 1], [1, 0, 1], [1, 1, 1]]
# setZeroes_intuitive_opt(matrix)
# print(matrix) # Output: [[1, 0, 1], [0, 0, 0], [1, 0, 1]]

# matrix2 = [[0, 1, 2, 0], [3, 4, 5, 2], [1, 3, 1, 5]]
# setZeroes_intuitive_opt(matrix2)
# print(matrix2) # Output: [[0, 0, 0, 0], [0, 4, 5, 0], [0, 3, 1, 0]]

