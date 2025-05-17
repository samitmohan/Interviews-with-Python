# https://leetcode.com/problems/minimum-equal-sum-of-two-arrays-after-replacing-zeros/submissions/1629843895/?envType=daily-question&envId=2025-05-10
"""
sum can only be incremented if number of zeroes are present.
as long as it has one zero its sum can be greater than curr sum

You have to increment at least 1 if there exists to be one 0.

iterate over both arrays
count number of zeroes
for every number of zero in particular nums -> incremenet sum of that particular nums
check if sum1 == sum2
The minimum possible sum of each array can be computed by assuming each zero is replaced with 1.

# both nums should have the same minimum possible sum

For each array:
    Minimum sum = all 0s replaced by 1.
    Maximum sum = all 0s replaced by some large value (but keep in mind: we only care about equality, not how big).

You Only Need to Adjust the Smaller Sum
    Say sum1 < sum2. That means you need to see if you can increase sum1 enough (by replacing 0s with values > 1).
    The maximum increase you can get is zeroes * (X - 1) if you replace 0s with value X instead of 1.

Edge case: If either array has no zeroes -> sum are not equal
"""


class Solution:
    def minSum(self, nums1: List[int], nums2: List[int]) -> int:
        zero1, zero2 = 0, 0
        sum1, sum2 = 0, 0
        for i in nums1:
            sum1 += i
            if i == 0:
                sum1 += 1
                zero1 += 1
            # sum1 add zero1
        for i in nums2:
            sum2 += i
            if i == 0:
                sum2 += 1
                zero2 += 1
            # sum2 add zero2

        if (zero1 == 0 and sum2 > sum1) or (zero2 == 0 and sum1 > sum2):
            return -1  # no ans
        return max(sum1, sum2)
