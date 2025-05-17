# https://leetcode.com/problems/minimum-path-sum/description/
# https://www.youtube.com/watch?v=pGMsrvt0fp://www.youtube.com/watch?v=pGMsrvt0fpk

"""
DP Problem, recursively cache : O(n * m) complexity
Every number depends on the bottom value and right value
Bottom up > Top down.
Compute values going to the left from bottom row till top first.
    Every position computes min position from the position

2D array with one extra layer (inf all initially)
Take the value stored + min(bottom, left) = store.

Space : O(n * m)
"""


class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        ans = [[float("inf")] * (cols + 1) for r in range(rows + 1)]
        ans[rows - 1][cols] = 0  # outer posn 0 to make the math for out.

        # bottom up
        for r in range(rows - 1, -1, -1):
            for c in range(cols - 1, -1, -1):
                ans[r][c] = grid[r][c] + min(ans[r + 1][c], ans[r][c + 1])

        return ans[0][0]  # min path sum from top left column so return [0][0]
