# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/submissions/
# find minimum price : pick that for day 1
# find max(maxprofit, price_on_each_day - minimum_price)


def maxProfit(prices):
    max_profit = 0
    minimum = prices[0]
    for price in prices:
        if price < minimum:  # lowest found
            minimum = price
        max_profit = max(max_profit, price - minimum)
    return max_profit


def main():
    prices = [7, 1, 5, 3, 6, 4]
    print(maxProfit(prices))


main()
