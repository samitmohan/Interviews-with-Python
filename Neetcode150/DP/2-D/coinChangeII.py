# https://leetcode.com/problems/coin-change-ii/description/
"""
DP solution : https://www.youtube.com/watch?v=qMky6D6YtXU&t=73s
Time : O(n * m)
"""


class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        cache = {}  # key : index, val : amount

        def dfs(i, a):
            if a == amount:
                return 1
            if a > amount:
                return 0
            if i == len(coins):
                return 0
            if (i, a) in cache:
                return cache[(i, a)]

            cache[(i, a)] = dfs(i, a + coins[i]) + dfs(i + 1, a)  # buy and skip
            return cache[(i, a)]

        return dfs(0, 0)
