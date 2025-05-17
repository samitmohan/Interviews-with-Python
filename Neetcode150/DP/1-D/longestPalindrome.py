# https://leetcode.com/problems/longest-palindromic-substring/description/j
# length of palindrome = right - left + 1
# T : O(n)


class Solution:
    def longestPalindrome(self, s: str) -> str:
        ans = ""
        ans_length = 0
        for i in range(len(s)):
            # odd length palindromes
            l, r = i, i
            # palindrome and in bounds
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if (r - l + 1) > ans_length:
                    ans = s[l : r + 1]
                    ans_length = r - l + 1
                l -= 1
                r += 1

            # even length palindromes
            l, r = i, i + 1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if (r - l + 1) > ans_length:
                    ans = s[l : r + 1]
                    ans_length = r - l + 1
                l -= 1
                r += 1
        return ans
