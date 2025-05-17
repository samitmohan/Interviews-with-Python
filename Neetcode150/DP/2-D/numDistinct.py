# https://leetcode.com/problems/distinct-subsequences/
# Time : O(n ^ 2)
class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        cache = {}

        def dfs(i, j):
            # base cases
            if j == len(t):
                return 1
            if i == len(s):
                return 0
            if (i, j) in cache:
                return cache[(i, j)]

            if s[i] == t[j]:  # look at remainder of s and t
                cache[(i, j)] = dfs(i + 1, j + 1) + dfs(i + 1, j)
            else:  # don't match : only shift i pointer
                cache[(i, j)] = dfs(i + 1, j)
            return cache[(i, j)]

        return dfs(0, 0)
