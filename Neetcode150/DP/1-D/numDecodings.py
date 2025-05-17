# https://leetcode.com/problems/decode-ways/description/
"""
Edge Case : 06 -> 6 is different from 06 and this grouping is invalid and the integers have to be [1-26]
121 

Values : 1-26 
Decision/Recursive Tree : 1 or 12
     121
     /  \
    1   12
   / \   \
  2   21  1
 / 
1   

Can only take double digit values only when first digit starts from 1, second digit = 0-9
    but if starting digit = 2, then second digit = 0-6

Time : 2^n

Optimising using DP.

dp[i] = dp[i + 1] + dp[i + 2]

Time : O(n) 
Space : O(1)
"""


class Solution:
    def numDecodings(self, s: str):
        dp = {len(s): 1}  # empty string returns 1

        def dfs(i):
            if i in dp:
                return dp[i]
            if s[i] == "0":  # starts with 0 : invalid
                return 0

            # 1 - 9
            ans = dfs(i + 1)
            # check for second character and limit of 26
            if i + 1 < len(s) and (
                s[i] == "1" or s[i] == "2" and s[i + 1] in "0123456"
            ):
                ans += dfs(i + 2)
            dp[i] = ans  # store cache
            return ans

        return dfs(0)
