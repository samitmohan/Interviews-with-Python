# https://leetcode.com/problems/daily-temperatures/
"""
Monotonic Decr Stack -> put elements in stack
73 next number -> 74 -> 74 - 73 > 0 so next number is warmer temperature.
pop 73 and print 1 (i - stackInd) and put 74 in it.
next number -> 75 (69-75) (71-75) (72-75) all negative -> push in stack and find i - stackInd
76-75 > 0 -> pop all and find i - stackInd
Calculating difference using the index.
"""


class Solution(object):
    def dailyTemperatures(self, temperatures):
        ans = [0] * len(temperatures)
        stack = []  # pair : temp, index
        for i, t in enumerate(temperatures):
            while (
                stack and t > temperatures[stack[-1]]
            ):  # curr element greater than top element : pop
                stackIndex = stack.pop()
                ans[stackIndex] = i - stackIndex
            stack.append(i)
        return ans
