# Used to solve maximum subarray (contiguous) sum
"""
[1, -3, 2, 1, -1]

2 + 1 = 3 (max)
"""


# Bruteforce O(N^3)


def bruteforce(arr):
    max_sum = arr[0]
    for i in range(len(arr)):
        for j in range(i, len(arr)):
            curr_sum = 0
            for k in range(i, j):
                curr_sum += arr[k]

            max_sum = max(max_sum, curr_sum)

    return max_sum


# Optimised bruteforce O(N^2)


def optimised_bruteforce(arr):
    max_sum = arr[0]
    for i in range(len(arr)):
        curr_sum = 0
        for j in range(i, len(arr)):
            curr_sum += arr[j]
            max_sum = max(max_sum, curr_sum)
    return max_sum


# Kadane's Algorithm O(N) : Ignore the negative numbers.
"""
[-2, 1, -3, 4, -1, 2, 1, -5, 4]
-2 + 1 = -1 : ignore negative (i += 1)
1 + -3 : -2 (store)

next number : 4 (greater than -2 so no point in storing this : discard)
current sum = 4
4 + -1 = 3

next number = 2 (positive : add) : 3 + 2 = 5 [4, -1, 2]
next number = 1 (add : 5 + 1 = 6)
next = -5 = 6-5 = 1 (not max) = max(6, 1) = 6
next number = 4 = 4 + 1 = 5 = max(6, 5) = 6. [4,-1,2,1]

Sliding Window technique.
"""


def kadane(arr):
    max_sum = arr[0]
    curr_sum = 0
    for num in arr:
        if curr_sum < 0:
            curr_sum = 0  # ignore negatives
        curr_sum += num
        max_sum = max(max_sum, curr_sum)
    return max_sum
