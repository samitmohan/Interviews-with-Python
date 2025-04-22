# https://leetcode.com/problems/count-the-hidden-sequences/description/
"""
Need to build hidden array of n + 1 numbers
Numbers of hidden array are in range low to high (inclusive)
And hidden has difference of differences between consec elements
# differences[i] = hidden[i + 1] - hidden[i]
[1, -3, 4] : [3, 4, 1, 5] , [4, 5, 2, 6] : 2
Return the number of possible hidden sequences there are.
If there are no possible sequences, return 0.

Instead of checking all arrays (constraints are big) -> fix the first elem of hidden
and rest of hidden array is based on diffferences array.
    can calculate the range of possible starting values that keep the whole sequence within bounds.


1) build hidden array :: [0] * (n+1) where n = len(differences)
2) go from lower to upper and find all combinations of arrays
     check if hidden[i+1] = differences[i] + hidden[i]: answer += 1
     else return 0


"""


class Solution:
    def numberOfArrays(self, differences, lower, upper):
        """
        We want to count how many valid hidden arrays can be formed.

        Observation:
        - The first number of the hidden array can vary.
        - Once the first number is fixed, the rest of the array is fully determined by 'differences'.

        Approach:
        1. Build prefix sums based on differences, assuming start = 0.
        2. Determine the min and max values in this prefix array.
        3. Figure out which start values would keep the entire hidden array within [lower, upper].
        4. Return the count of such valid starting values.
        """
        prefix = [0]
        for d in differences:
            prefix.append(prefix[-1] + d)

        min_prefix = min(prefix)
        max_prefix = max(prefix)
        # range of start = lower - min_prefix and upper - max_prefix
        min_start = lower - min_prefix
        max_start = upper - max_prefix
        if min_start > max_start:  # no values in hidden
            return 0
        # else return what number of valid numbers in that range
        return max_start - min_start + 1


s = Solution()
print(s.numberOfArrays(differences=[1, -3, 4], lower=1, upper=6))

# O(N) space and time, can do it in O(1) space : no need to keep prefix array just count curr as we go
"""
min_prefix = max_prefix = current = 0
for d in differences:
    current += d
    min_prefix = min(current, min_prefix)
    max_prefix = min(current, max_prefix)
"""
