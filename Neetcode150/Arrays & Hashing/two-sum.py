# https://leetcode.com/problems/two-sum/

# Input: nums = [2,7,11,15], target = 9
# Output: [0,1]

# approach -> keep a hashmap, go through elements (a + b = c, so c - b = a)
# if present in hashmap -> answer found, else keep adding elements to hashmap.

from collections import Counter


class Solution:
    def twoSum(self, nums, target):
        hm = {}  # arr = [3,5,6,4]
        for i, num in enumerate(nums):  # index, value mapping in hashmap
            diff = target - nums[i]
            if diff in hm:
                return [hm[diff], i]
            hm[num] = i  # hm = {3: 0, 5: 1, 6: 2, 4: 3}


s = Solution()
print(s.twoSum(nums=[3, 4, 5, 6], target=7))
print(s.twoSum(nums=[4, 5, 6], target=10))
print(s.twoSum(nums=[5, 5], target=10))
# [1,3,4,2], target = 6
# {1 : 0, 3: 1, 4:2, 2:3}
# diff = 6 - 1 = 5, 6-3 = 3, 6-4
