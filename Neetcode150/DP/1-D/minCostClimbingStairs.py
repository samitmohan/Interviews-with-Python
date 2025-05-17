# http://leetcode.com/problems/min-cost-climbing-stairs/description/

# not top of the floor, it's top of the floor + 1
# can't be greedy (2nd exmaple)
# T : 2^n but using DP : O(n)


class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        # [10, 15, 20, 0]
        cost.append(0)
        for i in range(len(cost) - 3, -1, -1):  # start at 15
            cost[i] = min(
                cost[i] + cost[i + 1], cost[i] + cost[i + 2]
            )  # single and double jump
        return min(cost[0], cost[1])  # first two values
