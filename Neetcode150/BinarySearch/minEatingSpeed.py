# https://leetcode.com/problems/koko-eating-bananas/
# Time : O(n * log(m)) : n is number of piles and m is range of k (left to right) | Space : O(1)
# Simple binary search problem : k -> speed at which he will eat the bananas
"""
piles : [3,6,7,11] and h = 8
k can be anywhere from 1 -> max in our arr (11) : [1,2,3,4,5,6,7,8,9,10,11]
  Perform binary search on k.
  First iteration : mid val : 6 so koko eats bananas at rate of 6.
    3/6 = 1, total_hours = 0 + 1 = 1
    6/6 = 1, total_hours = 1 + 1 = 2
    7/6 = 2, total_hours = 2 + 2 = 4
    11/6 = 2, total_hours = 4 + 2 = 6
  Can finish all bannas in 6 hours and h = 8, so it works (* before the guards come *) but we need to return min k
    # value smaller than k = 6 : decrement high pointer to mid - 1
    new_mid : 3, doesn't work so value > 3 needed : increment low pointer to mid + 1
"""

import math


def can_eat_in_time(piles, k, h):
    total_hours = 0
    for pile in piles:
        # k = 6, pile = 11 : pile / k -> 11/6 -> 2 (take ceil)
        hrs = math.ceil(pile / k)
        total_hours += hrs
    return total_hours <= h


def minEatingSpeed(piles, h):
    low, high = 1, max(piles)
    while low <= high:
        mid = (low + high) // 2
        # if koko can eat mid bananas per hour in less than or equal to h : possible answer found
        if can_eat_in_time(
            piles, mid, h
        ):  # -> decrement our right pointer to find a better solution
            high = mid - 1
        else:
            low = mid + 1
    return low  # at the end when low > high : low points to the min rate of bananas that koko can eat+finish in h time


def main():
    piles = [3, 6, 7, 11]
    h = 8
    print(minEatingSpeed(piles, h))


main()
