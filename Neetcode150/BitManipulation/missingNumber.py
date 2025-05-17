# https://leetcode.com/problems/missing-number/description/
# No bit manipulation : simple math. Bit Manipulation solution : XOR (same complexity)
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        sum1 = 0
        for i in nums:
            sum1 += i
        x = len(nums)
        return x * (x + 1) // 2 - sum1


# Cyclic Sort way of doing it.

"""
0 - N for 3
0 1 2 3

In cyclic sort every index = value - 1 but that's for range 1-N, here from 0-N
    it will be index = value

# 3 is missing
0 1 2 3
4 0 2 1 

index 4 does not exist? ignore (i++)

0 1 2 3
4 0 2 1 

is 0 at correct place (index = value), no it is not. swap
0 1 2 3
0 4 2 1

is 2 at correct place? yes.

is 1 at correct place? no. swap

0 1 2 3
0 1 2 4

does 0 contain 0 yes does 1 contain 1 yes does 2 contain 2 yes does 3 contain 3 no
    return 3

Case 2 : when N is not there in array.
n = 4
arr = [1, 0, 3, 2]
0 1 2 3
0 1 2 3

answer = n : 4
"""


class Solution:
    def missingNumber(self, arr: List[int]) -> int:
        # start looking from i, swap with correct index, only move i pointer when i is at correct index.
        i = 0
        while i < len(arr):
            correct_index = arr[i]  # index = value
            if (
                arr[i] < len(arr) and arr[i] != arr[correct_index]
            ):  # edge case added (case 2)
                arr[i], arr[correct_index] = arr[correct_index], arr[i]
            else:
                i += 1
        # search for first missing number

        for i in range(len(arr)):
            if arr[i] != i:
                return i

        return len(arr)  # case 2
