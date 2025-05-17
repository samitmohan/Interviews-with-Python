# https://leetcode.com/problems/maximum-product-subarray/submissions/
# https://www.youtube.com/watch?v=_i4Yxeh5ceQ&t=3s
"""
Bruteforce : O(n^2)
How to improve?
[1, 2, 3] all positive
1 * 2 * 3

If we have positive numbers -> Product increasing (Easy)

All negative
[-1, -2, -3]
-1 * -2 = 2
-1 * 2 * -3 = -6
-1, 2, -6, 24, -120... (Negatives consecutively : signs alternating)

Keep track of min prod subarray also...
    [-1, -2, -3]
    2 (max) and -2 (min)
    [2,-2] similarily :: -3 * 2 = 6, -3 * 2 = 6 [6, -6]
Another element = 4 = 4 * max_pos = 4 * 6 = 24.

Edge case -> 0 value. (Kills streak.) Just reset max and min to 1 (way to ignore 0)
"""


class Solution:
    def maxProduct(self, nums):
        ans = max(nums)
        curr_min, curr_max = 1, 1
        for n in nums:
            if n == 0:
                curr_max, curr_min = 1, 1
                continue

            temp = curr_max * n
            curr_max = max(n * curr_max, n * curr_min, n)
            curr_min = min(temp, n * curr_min, n)  # [-1,-8] : 8 but we need -8
            ans = max(ans, curr_max, curr_min)
        return ans
