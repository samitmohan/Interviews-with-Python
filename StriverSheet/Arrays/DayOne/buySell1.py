# https://takeuforward.org/data-structure/stock-buy-and-sell/

"""
Problem Statement: You are given an array of prices where prices[i] is the price of a given stock on an ith day.
You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.
Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

Example 1:
Input: prices = [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.

Example 2:

Input: prices = [7,6,4,3,1]
Output: 0
Explanation: In this case, no transactions are done and the max profit = 0.

O(N) pass means kadane's algorithm again
We want the profit to increase so just calculate difference / profit by curr_day - min_buy_price_seen and calculate maxProfit
Understand the Goal: Maximize sell_price - buy_price where sell_day > buy_day.

As I iterate through the prices array, let's say I'm at prices[i].
If I decide to sell at prices[i], what's the best I could have done? I should have bought at the minimum price seen on any day before day i.
This means, as I iterate, I need to keep track of two things:

The minimum price encountered so far (min_buy_price_so_far).
The maximum profit found so far (maxProfit).

Decision 1: Is this price a better selling opportunity?
    Calculate profit if I sell today: current_profit = price - min_buy_price_so_far.
    Update maxProfit = max(maxProfit, current_profit).

Decision 2: Is this price a new record low for buying?
    Update min_buy_price_so_far = min(min_buy_price_so_far, price)

Ask yourself-:
"If I sell today, what's the best profit I could have made (by buying at the lowest price seen so far)?"
"Is today's price a new record low that I should remember for future selling opportunities?"
"""


def maxProfit(prices):
    maxProfit = 0
    min_buy_price_so_far = prices[0]
    for num in prices:
        if num < min_buy_price_so_far:
            min_buy_price_so_far = num
        profit = num - min_buy_price_so_far
        maxProfit = max(maxProfit, profit)

    return maxProfit


def main():
    print(maxProfit(prices=[7, 1, 5, 3, 6, 4]))  # 5


main()
