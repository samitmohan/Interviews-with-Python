# https://leetcode.com/problems/climbing-stairs/
# recursive soln doesn't work for large numbers -> use DP.
# observation -> 1 1 2 3 5 8 13 -> fib numbers.

# What if instead of recomputing each value of climbStairs, we made sure to save that somewhere, trading space for time? That's what a top-down dynamic programming approach called memoization is. We make use of a dictionary memo in which we store the values of climbStairs that we have computed, and if we ever have to compute that value again we just check memo in (average) O(1) time instead of doing the work all over again


class Solution:
    def climbStairs(self, n: int) -> int:
        # defination and base cases
        memo = {}
        memo[1] = 1
        memo[2] = 2

        def climb(n):
            if n in memo:  # if recursion already done -> return saved state
                return memo[n]
            else:  # store recursion in look up table and return ans
                memo[n] = climb(n - 1) + climb(n - 2)
                return memo[n]

        return climb(n)
