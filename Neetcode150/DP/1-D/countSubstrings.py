# https://leetcode.com/problems/palindromic-substrings/description/

"""
There are two types of palindromic substrings : strings of odd length and even length
# odd
a : palindrome
b a b : also a palindrome

# even
aa : palindrome
b aa b : palindrome
b aa c : inside is a palindrome but expanding outwards : not a palindrome.

Each character is a subtring also, 'abc' : a, b, c

Optimised : O(n^2)
    a a a
    l   r

Two pointer solution and then move inward. -> <-

n^2 substrings and checking for every paldinrome : n = n^3

Optimisation : Treat every character as the middle element and expand towards left and right and check
This way we're cutting down on repeated work of checking every char for palindrome.
"aaab"
L and R both at a.
    ans += 1 # L == R
L is out of bounds

a a a b
  LR

a a a b
L   R

    ans = 3

This way we'll only get palindromes of odd length
For even length : start at every even position. (Righter pointer = L + 1)
a a a b
L R

a a a b
  L R

so on...
"""


# Start from the middle and expand, every step : check for palindrome and out of bounds.
# T : O(n^2) for odd and O(n^2) for even : O(n^2)


class Solution:
    def countSubstrings(self, s: str) -> int:
        ans = 0
        for i in range(len(s)):
            # odd
            left = right = i
            while left >= 0 and right < len(s) and s[left] == s[right]:
                ans += 1
                left -= 1
                right += 1

            # even
            left, right = i, i + 1
            while left >= 0 and right < len(s) and s[left] == s[right]:
                ans += 1
                left -= 1
                right += 1
        return ans
