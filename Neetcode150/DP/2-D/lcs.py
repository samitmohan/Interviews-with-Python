# https://leetcode.com/problems/longest-common-subsequence/description/
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        # 2d grid of len(text2+1) and (text1+1) with 0
        dp = [[0 for j in range(len(text2) + 1)] for i in range(len(text1) + 1)]
        # nested loop -> iterate through 2d grid in reverse order
        for i in range(len(text1) - 1, -1, -1):
            for j in range(len(text2) - 1, -1, -1):
                # if the char match
                if text1[i] == text2[j]:
                    # 1 + diag
                    dp[i][j] = 1 + dp[i + 1][j + 1]
                else:
                    # 2 cases -> Max(go right or go down)
                    dp[i][j] = max(dp[i][j + 1], dp[i + 1][j])

        # matrix is filled at the end -> ans is at dp[0][0] (first number) -> 3
        return dp[0][0]


# Time and Space -> O(n * m) where n = len(text1) and m = len(text2) and O(n * m) for 2d matrix
