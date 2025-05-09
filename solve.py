# https://leetcode.com/problems/count-number-of-balanced-permutations/description/?envType=daily-question&envId=2025-05-09

from itertools import permutations
class Solution:
    # for unique permutations use set
    def countBalancedPermutations(self, num: str) -> int:
        seen = set()
        ans = 0
        for perm in permutations(num):
            if perm in seen: continue
            seen.add(perm)
            even_sum = sum(int(perm[i]) for i in range(0, len(perm), 2))
            odd_sum = sum(int(perm[i]) for i in range(1, len(perm), 2))
            if even_sum == odd_sum:
                ans += 1
        mod = 10**7
        return ans % mod

# Does not work -> Time Constraint Error

# Gotta use DP to store??


# Smarter way
'''
Total sum way -> sum_even = sum_odd = k then S(total sum) = 2K {if S is even then target sum for both odd and even posns are S/2}

Need to split digits into 2 groups -> even posn and odd posn
Both groups must sum to target_sum = S/2. Num(even posn) = N+1//2 and Num(odd posn) == N//2

How to use DP? For each type of digit (0s, 1s, 2s .. ) we need to figure out how many go to even posns and how many go to odd posns
solve(digit_type, count_evens, sum_evens)
    - digit_type: current digit we are distributing
    - count_evens: how many digits we've alr placed in even slots 
    - sum_evens: sum of all digits in the even spot

this for odd numbers/posns can be figured out from this

idx = current digit value (0 to 9) being considered.
cnt1 = num of digits placed in even posns from 0 to idx - 1
sum1 = sum of those cnt1 digits

Base case: idx == 10 (all digits checked)
    - cnt1 == L_even, sum1 == Target_sum
    - verify cn2 == L_odd, sum2 = Target_sum
    - if all good return 1 else return 0

Recursive case: for current digit_val == idx:
    - freq[idx] = how many of this digit val we have
    - iterate i from 0 to freq[idx] (num of dig_values to place in even slots)
    - j = freq[idx] - i (number of dig_values to place in odd slots)
    - calc cnt_odd_so_far and cnt_even_so_far (from idx-1 and cnt1, sum1)

Precompute Prefix: s_cnt_prefix[k]: total count of digits 0 .. k
                   s_val_prefix[k]: total sum of d * freq[d] for digits 0 ... k
                   

'''
from collections import Counter
def solve(num):
    @cache  
    def dp(odd, even, odd_remaining):
        if odd == even == 0: return odd_remaining == 0
        ret, a = 0, A[n - (odd + even)]
        if odd and odd_remaining - a >= 0:
            ret += dp(odd - 1, even, odd_remaining-a) * odd
        if even:
            ret += dp(odd, even - 1, odd_remaining) * even
    MOD = 1_000_000_007
    A = list(map(int, num))
    ss = sum(A)
    if ss % 2 != 0: return 0

    target = ss/2
    n = len(A)
    even, odd = n//2, (n+1)//2
    A.sort(reverse=True)
    fac, freq = 1, Counter(A)
    for v in freq.values():
        fac *= factorial(v)
    return (dp(odd, even, target) // fac) % MOD


def main():
    solve(num=[])
main()


# fuck this. i dont know how to solve this. i never will.