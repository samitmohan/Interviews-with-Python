# https://leetcode.com/problems/target-sum/description/
# using DP (Caching)
# base case : index reaches the len(nums)
# Choice : either + or - :: backtrack(index, total) : if add : backtrack(index + 1, total + nums[i]) else : backtrack(index + 1, total - nums[i])
# adding both of them together = number of ways we can reach the answer


class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        dp = {}  # (index, total) = number of ways

        def backtrack(index, total):
            if index == len(nums):
                return 1 if total == target else 0
            if (index, total) in dp:
                return dp[(index, total)]  # caching result
            # recursion
            dp[(index, total)] = backtrack(index + 1, total + nums[index]) + backtrack(
                index + 1, total - nums[index]
            )
            return dp[(index, total)]

        return backtrack(0, 0)
