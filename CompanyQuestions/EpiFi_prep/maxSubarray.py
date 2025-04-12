# https://leetcode.com/problems/maximum-subarray/description/

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        curr_sum = 0
        max_sum = float("-inf")
        for i in nums:
            if curr_sum < 0:  # if -ve : make it 0
                curr_sum = 0
            curr_sum += i
            max_sum = max(max_sum, curr_sum)
        return max_sum
