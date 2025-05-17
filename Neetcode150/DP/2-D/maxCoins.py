# https://leetcode.com/problems/burst-balloons/
# This the type of question you skip in an interview.
"""
Which number to pop first? Once you do : continue on that (backtrack) : T = n^n
[3, 1, 5, 8] sub problem?
Pop 5
[3, 1, 8]
2 sub-arrays [3, 1] and 8
For array size of n : there are at-most n^2 sub-arrays
[3, 1] and [8]
We can't look at it independently as we'll get 6 and 8 = 14
But it is actually [3,1,8] : 3 * 1 * 8 after popping 1 = 24.

Clever trick.
Reverse thinking : Instead of popping 5 first, pop it at the last
[5] and popped_elements = [3,1,8]
1,[5],1 : 5
Remaining amount [3,1] : pop = [3,1,5] :
 pop 1 = 3 * 1 * 5 and
 pop 3 = 1 * 3 * 5

Array hasn't changed but pop all elements except 5 before.
How to? We know there is an explicit 1 on L and R
    Similarly = 1, [3, 1], 5 # implicit values : 1 and 5 now
                     L  R


For every value we will check if we can pop it last to get optimum answer and store in cache
2D cache : DP = [L][R]

Time : O(n^3)
cache is a decorator that helps in reducing function execution for the same inputs using the memoization technique
"""

from functools import cache


class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        nums = [1] + nums + [1]
        dp = {}

        @cache  # only works when passing the cache decorator, why?
        def dfs(left, right):
            if left > right:
                return 0  # nothing left to pop
            if (left, right) in dp:
                return dp[(left, right)]

            # compute
            dp[(left, right)] = 0
            # max number of points we can get for this pair
            for i in range(left, right + 1):
                coins = nums[left - 1] * nums[i] * nums[right + 1]
                # call for both left and right sub-array
                coins += dfs(left, i - 1) + dfs(i + 1, right)
                dp[(left, right)] = max(dp[(left, right)], coins)
            return dp[(left, right)]

        return dfs(1, len(nums) - 2)  # ignore the "1s"
