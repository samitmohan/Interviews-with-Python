# https://leetcode.com/problems/3sum/

# Input: nums = [-1,0,1,2,-1,-4]
# Output: [[-1,-1,2],[-1,0,1]]
# Explanation:
# nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
# nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
# nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
# The distinct triplets are [-1,0,1] and [-1,-1,2].

"""
Documentation
  Pick first number (make sure it's not duplicate)
  Apply twosum for other 2 numbers.
  Skip duplicates. (for both 2nd and 3rd number)

We then enter 2 more loops. These loops are used to bypass duplicates.
The first one continues while low < high and also while the element at the current pointer position equals the element at the next pointer position.
We move the left pointer forwards until a unique element is found.

Notes : Look how to skip duplicates || work on it on paper.
"""


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        for i, a in enumerate(nums):
            if i > 0 and a == nums[i - 1]:
                continue  # avoid duplicates
            low, high = i + 1, len(nums) - 1
            # play 2sum
            while low < high:
                curr_sum = a + nums[low] + nums[high]
                if curr_sum > 0:
                    high -= 1
                elif curr_sum < 0:
                    low += 1
                else:
                    res.append([a, nums[low], nums[high]])
                    # avoid duplicates for 2nd and 3rd number
                    low += 1
                    while nums[low] == nums[low - 1] and low < high:
                        low += 1  # skip duplicates
        return res
