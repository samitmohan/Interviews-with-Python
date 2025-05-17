# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-cooldown/description/
"""
State : Buying or Selling? Recursive Tree (Buy/Sell or Cooldown)
If buy -> i + 1
if sell -> i + 2 (need to wait for cooldown)
Cache result and return max
"""


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        dp = {}  # key : (i, buying) val : max_profit [buying : boolean]

        def dfs(i, buying):
            if i >= len(prices):
                return 0
            if (i, buying) in dp:
                return dp[(i, buying)]

            # main
            if buying:
                buy = (
                    dfs(i + 1, not buying) - prices[i]
                )  # profit = price to buy - og price
                cooldown = dfs(i + 1, buying)
                dp[(i, buying)] = max(buy, cooldown)
            else:
                # selling
                sell = dfs(i + 2, not buying) + prices[i]
                cooldown = dfs(i + 1, buying)
                dp[(i, buying)] = max(sell, cooldown)
            return dp[(i, buying)]

        return dfs(0, True)  # initially we are buying
