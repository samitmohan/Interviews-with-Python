# https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/

# Input: numbers = [2,7,11,15], target = 9
# Output: [1,2]


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # two pointer approach (just need to return index instead of numbers [use binary search])
        # TC -> O(logN), SC -> O(1)
        left = 0
        right = len(nums) - 1
        while left < right:
            val = nums[left] + nums[right]
            if val == target:
                return [left + 1, right + 1]
            elif val < target:
                left += 1
            else:
                right -= 1
