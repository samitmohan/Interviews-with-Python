class Solution:
    def numTilings(self, n: int) -> int:
        dp = [0] * (n + 1)
        # to reduce small val errors
        if n >= 0:
            dp[0] = 1
        if n >= 1:
            dp[1] = 1
        if n >= 2:
            dp[2] = 2
        if n >= 3:
            dp[3] = 5
        mod = 1000000007

        if n <= 3:
            return dp[n]
        for i in range(4, n + 1):
            dp[i] = (2 * dp[i - 1] + dp[i - 3]) % mod
        return dp[n]
