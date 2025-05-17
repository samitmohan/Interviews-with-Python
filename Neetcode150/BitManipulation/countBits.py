# https://leetcode.com/problems/counting-bits/
"""
0 - 0000
1 - 0001
2 - 0010
3 - 0011
4 - 0100
5 - 0101
6 - 0110
7 - 0111
8 - 1000

4-7 is same as 1-3 just 1 difference in MSB
Changes again at 8.
Pattern changes at every power change of 2.
1,2,4,8,16 etc...

Computing same thing again : dp. (2 and 4 will have same answer but 1 +)
0 - 0000 = 0
1 - 0001 = 1
2 - 0010 = 1
3 - 0011 = 2
4 - 0100 = 1 + dp[0] = 1 + dp[n - 4]
5 - 0101 =
6 - 0110
7 - 0111
8 - 1000 = 1 + dp[n - 8]
1 + dp[n - offset] (offset : MSB we've reached so far)
MSB : 1, 2, 4, 8, 16 (powers of two)

Time & Space : O(n)
"""


class Solution:
    def countBits(self, n: int) -> List[int]:
        dp = [0] * (n + 1)
        offset = 1  # highest power of 2
        for i in range(1, n + 1):
            # can we double our offset (4 * 2 == 8 : change offset to 8)
            if offset * 2 == i:
                offset = i
            dp[i] = 1 + dp[i - offset]
        return dp
