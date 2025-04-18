# https://leetcode.com/problems/valid-sudoku/

# Determine if a 9 x 9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:

# Each row must contain the digits 1-9 without repetition.
# Each column must contain the digits 1-9 without repetition.
# Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition.

"""
Documentation
  -> Keep a hashmap (set) and put all values of box in it, then check if it repeats for every row/column -> if it does -> not valid
  -> Check for every row (9) for every col (9) and also for every square,
  Defining Square
    instead of 0 1 2 .. 9 -> label them as 0 1 2 (col and rows), and to calc just // -> 4 row 4 col -> 4 // 3, 4 // 3 -> [1, 1] -> check at 1, 1

Time Complexity -> Hashsets for columns, rows, and each 3x3 square, O(1) time to check, iterating through the entire board (9*9) -> O(81)
"""

import collections

from collections import defaultdict


class Solution:
    """
    set to store rows, col and 3 grid boxes (r//3, c//3)
    if already present in either of these three ^ return False, else add to the hashmap
    if all cases passed -> return True
    """

    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = defaultdict(set)
        col = defaultdict(set)
        squares = defaultdict(set)
        for r in range(9):
            for c in range(9):
                val = board[r][c]
                if val == ".":
                    continue
                if (
                    val in rows[r]
                    or val in col[c]
                    or val in squares[(r // 3), (c // 3)]
                ):
                    return False
                # otherwise add in set
                col[c].add(val)
                rows[r].add(val)
                squares[(r // 3), (c // 3)].add(val)
        return True


def main():
    board = [
        ["5", "3", ".", ".", "7", ".", ".", ".", "."],
        ["6", ".", ".", "1", "9", "5", ".", ".", "."],
        [".", "9", "8", ".", ".", ".", ".", "6", "."],
        ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
        ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
        ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
        [".", "6", ".", ".", ".", ".", "2", "8", "."],
        [".", ".", ".", "4", "1", "9", ".", ".", "5"],
        [".", ".", ".", ".", "8", ".", ".", "7", "9"],
    ]
    solution = Solution()
    print(solution.isValidSudoku(board))


main()


# Same but a little better way to write


class Solution:
    def isValidSudoku(self, board):
        rows, cols = len(board), len(board[0])
        row_set = [set() for _ in range(9)]
        col_set = [set() for _ in range(9)]
        box_set = [set() for _ in range(9)]
        for r in range(rows):
            for c in range(cols):
                num = board[r][c]
                if num == ".":
                    continue
                k = (r // 3) * 3 + c // 3
                if num in row_set[r] or num in col_set[c] or num in box_set[k]:
                    return False
                row_set[r].add(num)
                col_set[c].add(num)
                box_set[k].add(num)
        return True
