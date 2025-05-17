# https://leetcode.com/problems/longest-increasing-path-in-a-matrix/description/
"""
No starting point :: check all? bruteforce.
LIP : Empty grid of same size (m * n answer matrix) : Store length
Simple DFS starting from 0,0 (up left right down) -> Compare values from previous val
    If yes : run dfs on new number (but if already visited : don't)
    If no : change direction. If still not : put 1 in empty grid (default val)
Always go up down right left but if going up to down (4 -> 8) then don't go up for 8 (it'll be 4)

Caching work in matrix : DP [Return max of answer grid]
Time : O(n * m)
"""


class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        rows, cols = len(matrix), len(matrix[0])
        dp = {}  # (r, c) -> LIP

        def dfs(r, c, prev_val):
            # out of bounds
            if r < 0 or r == rows or c < 0 or c == cols or matrix[r][c] <= prev_val:
                return 0

            if (r, c) in dp:
                return dp[(r, c)]

            ans = 1  # at least 1
            # position, previous val : curr val rn, run for all directions
            ans = max(ans, 1 + dfs(r + 1, c, matrix[r][c]))
            ans = max(ans, 1 + dfs(r - 1, c, matrix[r][c]))
            ans = max(ans, 1 + dfs(r, c + 1, matrix[r][c]))
            ans = max(ans, 1 + dfs(r, c - 1, matrix[r][c]))
            # store
            dp[(r, c)] = ans
            return ans

        for r in range(rows):
            for c in range(cols):
                dfs(
                    r, c, -1
                )  # default val : -1 [never eval true : none of the values in matrix will be < -1]
        return max(dp.values())
