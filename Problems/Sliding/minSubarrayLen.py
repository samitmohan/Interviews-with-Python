# https://leetcode.com/problems/minimum-size-subarray-sum/
# fun problem, easy sliding window template
"""
sum(elements of minimal_length_subarray) = target

using sliding window we can find left, right (subarray) where sum of those elements = target and then after finding every subarray we can just find the min length one by using min.
"""


class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left = 0
        min_len = float("inf")
        window_sum = 0

        for right in range(len(nums)):
            window_sum += nums[right]

            # shrink from the left while the window is valid
            while window_sum >= target:
                min_len = min(min_len, right - left + 1)
                window_sum -= nums[left]
                left += 1

        return min_len if min_len != float("inf") else 0
