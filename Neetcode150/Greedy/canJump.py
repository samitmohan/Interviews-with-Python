# https://leetcode.com/problems/jump-game/description/

"""
DP / Greedy
O(n)
Reverse order
[2,3,1,1,4] (start from end and see if you can reach first)

[2,3,1,1,4]
Start position : 2
Goal : to reach 4
from 1 -> 4 :: easy (given)
So shift goal to 1 now
[2,3,1,1] : 1 (i) can reach 1 (goal)
Shift again : goal = 1
[2,3,1]
3 can reach new goal (1) easily
Shift goal : 3
2 can make a jump of 1 to get to 3 (goal)
    return True
"""


# print(goal) # 4
# print(i) # 4 3 2 1 0
# print(nums[i]) # [4, 1, 1, 3, 2]
# i + nums[i] (jump length) >= goal


class Solution:
    def canJump(nums):
        goal = len(nums) - 1  # last
        for i in range(len(nums) - 1, -1, -1):
            # we can reach the goal (i = position we're jumping from)
            if i + nums[i] >= goal:
                goal = i
        return True if goal == 0 else False


if __name__ == "__main__":
    nums = [2, 3, 1, 1, 4]
    print(Solution.canJump(nums))
