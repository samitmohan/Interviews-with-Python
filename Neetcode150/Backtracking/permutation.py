# https://leetcode.com/problems/permutations/description/
"""Swap numbers : basic recursion Base case : if left == right or start == end We will use the backtracking to solve
the problem basically the intuition here is to swapping the defined position and again swapping back to the original
thing so it makes the array not changeable.."""


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def helper(left, right, ans):
            if left == right:  # base case
                ans.append(nums.copy())
                return
            # recursive case : swap
            for i in range(left, right):
                nums[left], nums[i] = nums[i], nums[left]
                helper(left + 1, right, ans)  # shift index
                # backtrack
                nums[i], nums[left] = nums[left], nums[i]
            return ans

        return helper(0, len(nums), [])
