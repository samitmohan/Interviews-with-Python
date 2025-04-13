from math import ceil

'''
https://leetcode.com/problems/count-good-numbers/
n = 0 : 0
n = 1 : 5 numbers (0,2,4,6,8)
n = 2 : 22,23,25,27,42,43,45,47,62,63,65,67,82,83,85,87 : 16 numbers
n = 3 : 220, 222, 224, 226, 228, 230, 232, 234, 236, 238, 250, 252, 254, 256, 258, 270, 272, 274, 276, 278, 420 ... 
# Pattern : 0, 5, 16, 80, 400

even_indexes = [0,2,4,6,8]
odd_index = [1,3,5,7,9]
prime = [2,3,5,7]
nums = str(n)
for i in range(nums) (2 = 100 to 999)
    if nums[even_indexes] % 2 == 0 and nums[odd_index_value] == any(prime):
        ans += 1
    return ans mod 109 + 7


I dont want to go through all numbers of digits (if n = 3 :: range = 100 to 999)
because constraints are 1 <= n <= 10^15.
Need to return count of good digit strings (even indices are even and odd are prime)

Looking at the pattern

Each posn has limited choices
Even index: 5 choices → {0, 2, 4, 6, 8}
Odd index: 4 choices → {2, 3, 5, 7}

Even choices = 5, Odd Choices = 4, Answer = 5^even_indices * 4^odd_indices : pnc.

Number of even indices = n+1 // 2, Number of odd indices = n//2
n = 1, even indices = 1, odd inidices = 0 answer = 5 (5^1 * 4^0)
n = 2, even indices = 1, odd indices = 1 answer = 16 (5^1 * 4^1 )
n = 3, even indices = 2, odd indices = 1 answer = 5^2 * 4^1 = 100
Example n = 4, even indices = 5//2 = 2, odd indices = 4//2 = 2, answer = 5^2 * 4^2 = 400
n = 5, even indices = 3, odd indices = 2, 5^3 * 4^2 = 2000


# MOD = 10**9 + 7
# even_digits = 5
# prime_digits = 4 #(prime)
# evenPosn, oddPosn = (n + 1) // 2, n // 2
# return pow(even_digits, evenPosn, MOD) * pow(prime_digits, oddPosn, MOD) % MOD
'''
class Solution:
    def countGoodNumbers(self, n: int) -> int:
        # one liner (walrus operator ftw)
        return pow(5, ceil(n/2), mod:=10**9 + 7) * pow(4, n//2, mod) % mod

ans = Solution()
print(ans.countGoodNumbers(3))