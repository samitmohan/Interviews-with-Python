from math import factorial
from collections import Counter

"""
Instead of going through entire range of start to end of n digit, and checking if any is palindrome
Just generate all palindrome permutations of n. Much faster since range 10 - 100 only has 11, 22, 33 as pal
So checking all might take time, but just generating all palindromes with N digits is faster.

Count all valid permutation of a palindrome: Shouldn't start with 0 (leading) and Divisible by K
Also need to count permutation of the k_palindromic number : example 515 : good number so count all arrangements
of this as well : 3!/2! = count + 3. Also if 505 : k_palindromic and permutations : 3!/2! = +3, (550 is counted)
so when we come to 550 permutation to check it shouldn't be recounted (since it was already included : TRACK)
(Make sure for valid arrangements you don't count 0 in the beginning if 0 is present in n) : example 250052, k=2
This can be checked by frequency (counter) of 0 :: so in this case (if 0 exists) :: total permutations - invalid_permutations(those that contain 0 in beginning) = answer

DFS to generate palindromes
Also a good idea to precompute factorial. Space : O(N) 
Also just store permutations in set so that they are not recounted again in re-arrangements

Final Steps -:
1) Generate all valid permutations using DFS
2) For each permutation, sort and check if permutation was already counted (set)
3) If not counted, count valid arrangements of it using precomputed factorial array

"""
"""
Factorial Precomputation:
    Precomputes factorials using a list instead of recalculating them repeatedly.

Simplified Permutation Counting:
    Uses Python's Counter to efficiently compute digit frequencies.

Palindrome Generation:
    Generates palindromes directly by mirroring digits instead of sorting repeatedly.

Compact Loops:
    Uses chr() for iterating over digits ('0' to '9').

Avoid Redundant Checks:
    Uses a set to track processed numbers (done) and avoids duplicate calculations.

# For n = 3, starting with an empty list number = [' ', ' ', ' ']:
# At pos = 0, assign '1' to both positions 0 and 2: ['1', ' ', '1'].
# At pos = 1, assign '2' to both positions 1: ['1', '2', '1'].
# At pos = 2, check divisibility by k
"""


class Solution:
    # precompute factorial
    def __init__(self) -> None:
        self.k_pal = 0
        self.done = set()
        self.factorial = [1] * 11  # precompute
        for i in range(2, 11):
            self.factorial[i] = i * self.factorial[i - 1]

    # counting all arrangements : 212 = 3!/2! (for dups)
    def count_all_permutations(self, freq, n):
        count = self.factorial[n]
        for f in freq.values():
            count //= self.factorial[f]
        return count

    def all_arrangements(self, number, n):
        sorted_num = "".join(sorted(number))
        if sorted_num in self.done:
            return 0  # already present
        self.done.add(sorted_num)
        freq = Counter(sorted_num)
        total_perm = self.count_all_permutations(freq, n)

        if (
            freq["0"] > 0
        ):  # different calc for permutations : set 0 at beginning and count for n-1
            freq["0"] -= 1
            invalid_permutations = self.count_all_permutations(freq, n - 1)
            freq["0"] += 1  # set back to normal
        else:
            invalid_permutations = 0
        return total_perm - invalid_permutations

    def is_k_pal(self, number, k):
        return int("".join(number)) % k == 0

    def ans(self, pos, n, number, k):
        # even odd palindrome generate (mirror) 0 to n+2//2 check
        if pos >= (n + 1) // 2:
            if self.is_k_pal(number, k):
                self.k_pal += self.all_arrangements(number, n)
            return
        """
        This range generates digits ('0' to '9'), but if pos == 0, it starts from '1' to avoid leading zeros in the palindrome.
        Assigns the same digit (char) to both the current position (pos) and its mirrored position (n - pos - 1) in the list number. (ensures generated string is palindromic)
        The recursion stops when pos >= (n + 1) // 2, meaning half of the palindrome has been constructed.
        Reset the current position after recursion to prepare for the next digit assignment.
        """
        start_digit = "1" if pos == 0 else "0"
        for digit in range(ord(start_digit), ord("9") + 1):
            number[pos], number[n - pos - 1] = chr(digit), chr(digit)  # mirroring
            self.ans(pos + 1, n, number, k)  # recursion
            number[pos] = " "  # reset

    def countGoodIntegers(self, n: int, k: int) -> int:
        # placeholder for palindrome construction (recursive call answers are stored here)
        number = [" "] * n
        self.ans(0, n, number, k)

        return self.k_pal
