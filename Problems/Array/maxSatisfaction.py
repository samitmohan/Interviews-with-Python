# https://leetcode.com/problems/reducing-dishes/description/
"""
Input: satisfaction = [-1,-8,0,5,-9]
Output: 14
Explanation: After Removing the second and last dish, the maximum total like-time coefficient will be equal to (-1*1 + 0*2 + 5*3 = 14).
Each dish is prepared in one unit of time.

Max sum : sort input array in decreasing order (ensures max satisfaction level value at front)
[5,0,-1,-8,-9]
ans = 0
prefix_sum = 0

pick 5
pick first val, add to prefix_sum, before adding prefix_sum to ans check if it's positive. ans += prefix_sum
    [prefix_sum shouldn't be negative]

now 0
prefix_sum = 5 + 0 = 5, ans += prefix_sum = 5 + 5 = 10

-1
prefix_sum = 4, prefix_sum is still pos, ans = 10 + 4 = 14

-8
prefix_sum = 4 +(-8) = -4, prefix_sum is negative : ignore, similarly ignore -9

return ans
Time : O(n*log(n))
"""


class Solution:
    def maxSatisfaction(self, satisfaction: List[int]) -> int:
        satisfaction.sort(reverse=True)
        ans, prefix_sum = 0, 0
        for i in range(len(satisfaction)):
            prefix_sum += satisfaction[i]
            if prefix_sum < 0:
                break
            ans += prefix_sum
        return ans
