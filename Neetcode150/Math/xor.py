# https://leetcode.com/problems/sum-of-all-subset-xor-totals/description/
from itertools import combinations


class Solution:
    def subsetXORSum(self, nums):
        def xor(subset):
            ans = 0
            for i in range(len(subset)):
                ans ^= subset[i]
            return ans

        result = 0
        for r in range(len(nums) + 1):
            for subset in combinations(nums, r):
                result += xor(subset)
        return result


# How to do it without combinations? Recursion backtrack and calculate XOR on the fly.
# better solution
def subsetXORSum(nums):
    # generate all subsets
    def dfs(idx, curr_xor):
        if idx == len(nums):
            return curr_xor
        # include curr element
        include = dfs(idx + 1, curr_xor ^ nums[idx])
        # exclude curr element
        exclude = dfs(idx + 1, curr_xor)
        return include + exclude

    return dfs(0, 0)


def main():
    print(subsetXORSum(nums=[1, 3]))
    print(subsetXORSum(nums=[5, 1, 6]))


main()
