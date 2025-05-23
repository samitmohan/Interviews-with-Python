# https://takeuforward.org/data-structure/kadanes-algorithm-maximum-subarray-sum-in-an-array/
# kadane.py has all the approaches

"""
Problem Statement: Given an integer array arr, find the contiguous subarray (containing at least one number) which
has the largest sum and returns its sum and prints the subarray.

Another one of those problems if you don't know the answer to -> you just don't. It's an Algorithm.
O(N)
"""


def maxSumArr(arr):
    curr_sum = 0
    max_sum = arr[0]
    for i in arr:
        if curr_sum < 0:
            curr_sum = 0  # reset
        curr_sum += i
        max_sum = max(curr_sum, max_sum)
    return max_sum


def main():
    print(maxSumArr(arr=[-2, 1, -3, 4, -1, 2, 1, -5, 4]))  # 6 ([4,-1,2,1])


main()
