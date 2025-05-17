# https://leetcode.com/problems/longest-increasing-subsequence/description/
# O(n^2)


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        lis = [1] * len(nums)
        for i in range(len(nums) - 1, -1, -1):
            # start at i and iterate every subsequence
            for j in range(i + 1, len(nums)):
                # if val at i < val at j (has to be true)
                if nums[i] < nums[j]:
                    lis[i] = max(lis[i], 1 + lis[j])
        return max(lis)
