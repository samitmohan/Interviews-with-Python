# https://leetcode.com/problems/house-robber-ii/description/
# Time : O(n)


class Solution:
    def rob(self, nums: List[int]) -> int:
        # edge cases : skip first and last house
        # what if inp array with only 1 val? : empty array?? nums[0]
        return max(nums[0], self.helper(nums[1:]), self.helper(nums[:-1]))

    # house robber I solution
    def helper(self, nums):
        rob1, rob2 = 0, 0
        for i in nums:
            # either you rob ith house and i-2th house or you rob i-1th house
            curr = max(rob1 + i, rob2)
            # do the same for all
            rob1 = rob2
            rob2 = curr
        return rob2
