# https://leetcode.com/problems/reverse-integer/solutions/
# REVISIT BIT QUESTIONS
class Solution:
    def reverse(self, x: int) -> int:
        rev = 0
        sign = 1 if x >= 0 else -1
        x *= sign
        while x > 0:
            rev = rev * 10 + x % 10
            x //= 10
        rev *= sign
        return rev if -(2**31) <= rev <= (2**31 - 1) else 0
