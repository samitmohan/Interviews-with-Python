# https://leetcode.com/problems/house-robber/

# either you rob this house and the house pre2 -> prev_to_prev + current
# or you rob the prev house and then get to the nest -> prev
# use dp to store state of the max robbery till now.
# Time : O(n)


class Solution:
    def rob(self, nums: List[int]) -> int:
        prev_to_prev_val, current, prev = 0, 0, 0
        for i in nums:
            # either you rob ith house and i-2th house or you rob i-1th house
            curr = max(prev, i + prev_to_prev_val)
            # do the same for all
            prev_to_prev_val = prev
            prev = curr
        return curr
