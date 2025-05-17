# Input: heights = [2,1,5,6,2,3]
# Output: 10
# Explanation: The above is a histogram where width of each bar is 1.
# The largest rectangle is shown in the red area, which has an area = 10 units.

# https://leetcode.com/problems/largest-rectangle-in-histogram/description/

"""
Cases :
  1 -> [2,1] : can't extend it as there will be a gap since 2 > 1
  2 -> [1,2] : can extend it easily to get a area of 2 since there will be no gap 1 < 2
  3 -> [2,2] : can also extend it easily to get an area of 4

Can only compute area if heights are in increasing order. If not in increasing order (2,1) : stack = [2] pop it from stack [1]
[1,2,3,4,3] : till 4 -> area but then 3 is the next element which cannot be included, hence pop 4 from stack
  # new : [1,2,3,3] : area = 6
Similar example
  [1,2,3,4,1] till 4 -> area = 4, then 1. pop 4, 3, 2 because 1 < all, new stack : [1,1] which gives largest area of 2

Stack : hold index and height
compute and return maxArea_so_far
"""


def largestRectangleArea(heights):
    maxArea = 0
    stack = []  # pair : (index, height)
    for i, h in enumerate(heights):
        start = i
        while (
            stack and stack[-1][1] > h
        ):  # if height of top element of stack > current height [2,1] : pop
            index, height = stack.pop()
            maxArea = max(maxArea, height * (i - index))  # width
            start = index
        stack.append((start, h))

    # all the way to the end : 1,2,3,4,5 case
    for i, h in stack:
        maxArea = max(maxArea, h * (len(heights) - i))
    return maxArea


def main():
    heights = [2, 1, 5, 6, 2, 3]
    print(largestRectangleArea(heights))


main()
