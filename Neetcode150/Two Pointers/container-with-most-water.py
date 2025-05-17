# https://leetcode.com/problems/container-with-most-water/s

# Given array of heights, find max water container can store
# Input : height = [1,8,6,2,5,4,8,3,7]
# Output : 49, (8 - 1) x min(8, 7)

# TC -> O(N)

"""
Documentation : Two Pointer
  ans = Total water contained in an interval = width * height
  distance = high - low (width)
  height =  min(arr[low], arr[high])
"""


class Solution:
    def maxArea(self, height: List[int]) -> int:
        low = 0
        high = len(height) - 1
        ans = 0
        while low < high:
            ans = max(ans, min(height[low], height[high]) * (high - low))
            if height[low] < height[high]:
                low += 1
            else:
                high -= 1

        return ans
