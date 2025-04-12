# https://leetcode.com/problems/longest-palindromic-substring/description/j
# length of palindrome = right - left + 1
# T : O(n^2)

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
                    ans = s[l: r + 1]
                    ans_length = r - l + 1
                l -= 1
                r += 1

            # even length palindromes
            l, r = i, i + 1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if (r - l + 1) > ans_length:
                    ans = s[l: r + 1]
                    ans_length = r - l + 1
                l -= 1
                r += 1
        return ans


# count number of palindromic strings

def count_palindromic_substrings(s):
    count = 0
    n = len(s)

    # Check for odd-length palindromic substrings
    for i in range(n):
        l = i
        r = i
        while l >= 0 and r < n and s[l] == s[r]:
            count += 1
            l -= 1
            r += 1

    # Check for even-length palindromic substrings
    for i in range(n - 1):
        l = i
        r = i + 1
        while l >= 0 and r < n and s[l] == s[r]:
            count += 1
            l -= 1
            r += 1

    return count


s = 'ABC'
print(count_palindromic_substrings(s))  # Output: 3

s = 'AAA'
print(count_palindromic_substrings(s))  # Output: 6
