# knapsack problem
# https://arpitbhayani.me/blogs/genetic-knapsack

memo = {}  # dp


def knapsack(maxcap, weight, value, n):
    if n == 0 or maxcap == 0:
        return 0
    # if weight of nth item is more than weight avail = skip it
    if weight[n - 1] > maxcap:
        return knapsack(maxcap, weight, value, n - 1)
    # if answer already present in memo return it
    if (maxcap, n) in memo:
        return memo[(maxcap, n)]

    # value if nth item picked
    valPicked = value[n - 1] + knapsack(maxcap - weight[n - 1], weight, value, n - 1)
    # value if nth item not picked
    valNotPicked = knapsack(maxcap, weight, value, n - 1)

    ans = max(valPicked, valNotPicked)
    memo[(maxcap, n)] = ans  # store optimal answer of subproblem

    return ans


def main():
    n = 3
    maxcap = 4
    values = [1, 2, 3]
    weight = [4, 5, 1]
    print(knapsack(maxcap, weight, values, n))


main()  # Output: 3
