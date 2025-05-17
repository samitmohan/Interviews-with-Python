# https://leetcode.com/problems/combination-sum-iii/


class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        # n -> target, k = number of elem used, 1-9 allowed, each number used atmost one
        ans = []

        def helper(num, temp, target):
            # base case : if k elements used and target reached (ans found)
            if len(temp) == k:
                if target == 0:
                    ans.append(temp)
                return

            # recursive case : if currNum <= target -
            # add to temp ans array
            # update target (target - currNum)
            # update index so can't be reused (each number used atmost one condition) -> start from currNum instead of num
            for currNum in range(num + 1, 10):
                if currNum <= target:
                    helper(currNum, temp + [currNum], target - currNum)
                else:
                    return

        helper(0, [], n)
        return ans
