# https://leetcode.com/problems/coin-change/description/
"""
Fewest number of coins needed.
Infinite number of each kind of coin given.
coins = [1,2,5] amount = 1
5 + 5 + 1 = 11 : answer = 3

Top Down Approach
[1,3,4,5] Amount = 7

5 and 3 = -1 amount left : negative : skip. (Save so it can be used later)

Save states and ignore negatives and update minimum

Bottom Up Aproach
Min coins to sum to 0
dp[0] = 0
dp[1] = 1
dp[2] = 1 + dp[1]

and so on...

"""


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [float("inf")] * (amount + 1)  # 0 -> amount and default value = max
        dp[0] = 0

        for amt in range(1, amount + 1):
            for coin in coins:
                if amt - coin >= 0:  # non negative : soln
                    dp[amt] = min(
                        dp[amt], 1 + dp[amt - coin]
                    )  # coin = 4, amt = 7. dp[7] = 1 + dp[3]
        return (
            dp[amount] if dp[amount] != float("inf") else -1
        )  # return only when != default value
