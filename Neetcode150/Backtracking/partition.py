# https://leetcode.com/problems/palindrome-partitioning/
class Solution:
    def partition(self, s: str):
        ans = []

        def helper(s, path, ans):
            if not s:  # base case
                ans.append(path)
                return
            for i in range(1, len(s) + 1):
                if self.isPal(s[:i]):
                    helper(s[i:], path + [s[:i]], ans)

        ans = []
        helper(s, [], ans)
        return ans

    def isPal(self, s):
        return s == s[::-1]
